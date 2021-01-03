import sys
import os
from PySide6 import QtWidgets
import PySide6
import web3
import make_payment
from metallic import Metallic
from datetime import date
import json


class Account:
    def __init__(self, username: str, password: str, w3: web3.Web3):
        self.w3 = w3
        self.username = username
        self.password = password

    def create_account(self):
        account = self.w3.eth.account.create()
        self.public_key = account.address
        self.private_key = self.w3.toHex(account.key) 

    def load_test_ether(self):
        # send some test ether to the account
        make_payment.transfer(self.w3.eth.accounts[1], "0041a0dbd0fc73c31f6ebaaeb996e77235eb697ae5967c3f603926a7545b392a", self.public_key, .075)

    def encrypt(self):
        encrypted_account = self.w3.eth.account.encrypt(self.private_key, self.password)
        return encrypted_account

    def decrypt(self, wallet):
        decrypted_account = self.w3.eth.account.decrypt(wallet, self.password)
        self.private_key = self.w3.toHex(decrypted_account)
        self.public_key = self.w3.toChecksumAddress("0x" + wallet['address'])


class MetallicDesktopClient(QtWidgets.QMainWindow):
    def __init__(self):
        super(MetallicDesktopClient, self).__init__()
        os.system("pyside6-uic gui.ui > gui.py")
        from gui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.configure()
        self.show()

    def configure(self):
        self.w3 = web3.Web3(web3.Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
        self.metallic = Metallic("./metallic.sol", 'metallic.sol', "Metallic", self.w3)

        # button listeners
        self.ui.create_button.clicked.connect(self.create_account)
        self.ui.activate_account_button.clicked.connect(self.activate_account)
        self.ui.private_key_button.clicked.connect(self.toggle_private_key)
        self.ui.login_button.clicked.connect(self.login)
        self.ui.search_button.clicked.connect(self.search)

        # last minute configuration
        self.ui.login_tab_widget.setCurrentIndex(self.ui.login_tab_widget.indexOf(self.ui.create_account_tab))

    def search(self):
        username = self.ui.search_username.text()
        allUsernames = self.metallic.getAccounts()  # list of tuples
        
        print(allUsernames)
        # filter the search results
        matchingAccounts = []
        for account in allUsernames:
            if username in account[0]:
                matchingAccounts.append(account)

        # clear the results
        i = 0
        while self.ui.results_vertical_layout.count() > 0:
            try:
                self.ui.results_vertical_layout.removeWidget(self.ui.results_vertical_layout.itemAt(i))
            except TypeError:
                self.ui.results_vertical_layout.removeItem(self.ui.results_vertical_layout.itemAt(i))
               
            i += 1
                
        # display the results
        for account in matchingAccounts:
            self.ui.results_vertical_layout.addWidget(QtWidgets.QLabel(account[0]))

        # add a vertical spacer at the end to move the results to the top
        self.ui.results_vertical_layout.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
    
    def setLoginEnabled(self, enabled: bool):
        self.ui.login_username.setEnabled(enabled)
        self.ui.login_password.setEnabled(enabled)
        self.ui.wallet_line_Edit.setEnabled(enabled)
        self.ui.login_button.setEnabled(enabled)

    def logout(self):
        self.setLoginEnabled(True)

    def display_account_information(self):
        self.ui.account_username_label.setText("@" + self.account.username)
        self.ui.address_label.setText(self.account.public_key)
        self.ui.balance_label.setText(str(self.w3.fromWei(self.w3.eth.getBalance(self.account.public_key), "ether")))

    def login(self):
        self.account = Account(self.ui.login_username.text(), self.ui.login_password.text(), self.w3)
        with open('wallet.json', 'r') as json_file:
            wallet = json.load(json_file)
            self.account.decrypt(wallet)

        self.display_account_information()
        self.setLoginEnabled(False)

    def toggle_private_key(self):
        if self.ui.private_key_label.text() == "0x0":
            self.ui.private_key_label.setText(self.account.private_key)
            self.ui.private_key_button.setText("Hide Private Key")
        else:
            self.ui.private_key_label.setText("0x0")
            self.ui.private_key_button.setText("Show Private Key")

    def activate_account(self):
        self.metallic.addAccountPayWithSameAccount(self.account.username,
                                self.account.public_key,
                                "Ethereum",
                                date.today().strftime("%d/%m/%Y"),
                                self.account.private_key)

        if  self.metallic.username_exists(self.account.username):
            print("Username Successfully added!")
            self.ui.balance_label.setText(str(self.w3.fromWei(self.w3.eth.getBalance(self.account.public_key), "ether")))
            self.ui.activation_group_box.hide()
        else:
            print("Failed to add username!")

    def create_account(self):
        try:
            self.setCursor(PySide6.QtCore.Qt.WaitCursor)
            if self.metallic.username_exists(self.ui.account_username_label.text()):
                self.ui.create_account_error_message.setText("That username already exists. Please pick a new one.")
                return
            if self.ui.create_account_password.text() == "":
                self.ui.create_account_error_message.setText("Password cannot be blank")
                return
            if self.ui.create_account_password.text() != self.ui.create_account_confirm_password.text():
                self.ui.create_account_error_message.setText("Passwords do not match")
                return
            if self.ui.create_account_username.text() == "":
                self.ui.create_account_error_message.setText("Username cannot be blank")
                return

            self.account = Account(self.ui.create_account_username.text(), self.ui.create_account_password.text(), self.w3)
            self.account.create_account()
            self.account.load_test_ether()

            # save the encrypted wallet in the current directory
            wallet = self.account.encrypt()
            with open('wallet.json', 'w') as json_file:
                json.dump(wallet, json_file)

            # focus on the login tab
            self.ui.login_tab_widget.setCurrentIndex(self.ui.login_tab_widget.indexOf(self.ui.login_tab))
            self.ui.login_username.setText(self.account.username)
            self.ui.login_password.setText(self.account.password)
            self.ui.wallet_line_Edit.setText("wallet.json")
            self.login()

            # focus on the account tab
            self.ui.feed_tab_widget.setCurrentIndex(self.ui.feed_tab_widget.indexOf(self.ui.tab_account))
            self.display_account_information()

            # reset the gui last
            self.ui.create_account_error_message.setText("")
            self.ui.create_account_username.setText("")
            self.ui.create_account_password.setText("")
            self.ui.create_account_confirm_password.setText("")
            self.ui.status.setText("Logged in")
        finally:
            self.setCursor(PySide6.QtCore.Qt.ArrowCursor)

        


app = QtWidgets.QApplication(sys.argv)
client = MetallicDesktopClient()
sys.exit(app.exec_())