from flask import Flask, render_template, url_for, flash, redirect
import forms
from metallic import Metallic


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
                    {
                        'author': 'Corey Schafer',
                        'title': 'Blog Post 1',
                        'content': 'First post content',
                        'date_posted': 'April 20, 2018'
                    },
                    {
                        'author': 'Jane Doe',
                        'title': 'Blog Post 2',
                        'content': 'Second post content',
                        'date_posted': 'April 21, 2018'
                    }
                ]

def run_website(_metallic: Metallic):
    global metallic
    metallic = _metallic
    app.run(debug=True)


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
        print(allUsernames)
        print(len(matchingAccounts))
        return render_template('search.html', title="Create Account", form=form, matchingAccounts=matchingAccounts)

    return render_template('search.html', title="Create Account", form=form, matchingAccounts=None)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/create-account", methods=['GET', 'POST'])
def createAccount():
    account_form = forms.CreateAccountForm()

    # set payment address
    account_form.payment_address.text = "0x1234abcd"

    # handle button presses
    if account_form.validate_on_submit():

        #create account
        metallic.addAccount(account_form.username.data,
                            account_form.public_address.data,
                            "Ethereum")

        # verify the username was added
        print(metallic.username_exists(account_form.username.data))
        print(metallic.getAddress(account_form.username.data))

        # tell the user what happened
        flash("Account Created.", 'success')

        # payment verified, reroute to home
        return redirect(url_for('home'))

    return render_template('createAccount.html', title="Create Account", account_form=account_form)


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
