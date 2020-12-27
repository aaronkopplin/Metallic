from flask import Flask, render_template, url_for, flash, redirect
import forms
from metallic import Metallic
from make_payment import transfer
from datetime import date


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

def run_website(_metallic: Metallic):
    global metallic
    metallic = _metallic
    app.run(debug=False)


@app.route('/search', methods=["GET","POST"])
def search():
    form = forms.SearchForm()
    if form.validate_on_submit():
        username = form.search.data
        allUsernames = metallic.getAccounts()  # list of tuples
        
        # filter the search results
        matchingAccounts = []
        for account in allUsernames:
            if username in account[0]:
                matchingAccounts.append(account)

        if len(matchingAccounts) == 0:
            flash("No matching usernames were found.", 'danger')

        # render the page again, but this time with the search results
        return render_template('search.html', title="Search", form=form, matchingAccounts=matchingAccounts)

    return render_template('search.html', title="Search", form=form, matchingAccounts=None)


@app.route("/")
@app.route("/home")
def home():
    accounts = metallic.getStructuredAccounts()
    return render_template('home.html', accounts=accounts)


@app.route("/create-account", methods=['GET', 'POST'])
def createAccount():
    account_form = forms.CreateAccountForm()
        
    # set payment address
    account_form.payment_address.text = metallic.getReceiveAddress()

    # handle button presses
    if account_form.validate_on_submit():

        # for testing purposes, pay for the account manually
        # use any address from your test blockchain that has a balance of at least a few Eth.
        public_key = "0xB753e2f771BF4C1C92eE4143e8cbe2F6aE2E4024"
        private_key = "a751fc02ac56ad329589b24778ef57173dc1a2d58d008693f43dd5e2b97db94f"
        transfer(public_key, private_key,metallic.getReceiveAddress(), 0.02)

        #create account
        metallic.addAccount(account_form.username.data,
                            account_form.public_address.data,
                            account_form.currency.data,
                            date.today().strftime("%d/%m/%Y"))

        # verify the username was added
        print("Username Successfully added!" if  metallic.username_exists(account_form.username.data) else "Failed to add username!")

        # tell the user what happened
        flash("Account Created.", 'success')

        # payment verified, reroute to home
        return redirect(url_for('home'))

    # 1 gwei = 1 / 1,000,000,000 ETH or 0.000000001 ETH
    estimated_gas = metallic.estimateGasToAddAccount("test", "test", "test", "test")
    gas_price = 47
    total_eth = int(estimated_gas) * gas_price * 0.000000001
    print(str(total_eth))

    # render the page
    return render_template('createAccount.html', 
                            title="Create Account", 
                            account_form=account_form,
                            estimated_gas=str(total_eth))


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = forms.RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
