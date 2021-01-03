# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(821, 516)
        icon = QIcon()
        icon.addFile(u"logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionWindow_Settings = QAction(MainWindow)
        self.actionWindow_Settings.setObjectName(u"actionWindow_Settings")
        self.actionLogout = QAction(MainWindow)
        self.actionLogout.setObjectName(u"actionLogout")
        self.actionExport_Wallet = QAction(MainWindow)
        self.actionExport_Wallet.setObjectName(u"actionExport_Wallet")
        self.actionImport_Wallet = QAction(MainWindow)
        self.actionImport_Wallet.setObjectName(u"actionImport_Wallet")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.feed_tab_widget = QTabWidget(self.centralwidget)
        self.feed_tab_widget.setObjectName(u"feed_tab_widget")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feed_tab_widget.sizePolicy().hasHeightForWidth())
        self.feed_tab_widget.setSizePolicy(sizePolicy)
        self.feed_tab_widget.setTabsClosable(False)
        self.feed_tab_widget.setMovable(False)
        self.feed_tab = QWidget()
        self.feed_tab.setObjectName(u"feed_tab")
        self.verticalLayout = QVBoxLayout(self.feed_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.results_scroll_area_2 = QScrollArea(self.feed_tab)
        self.results_scroll_area_2.setObjectName(u"results_scroll_area_2")
        self.results_scroll_area_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.results_scroll_area_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 577, 382))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.feed_vertical_layout = QVBoxLayout()
        self.feed_vertical_layout.setObjectName(u"feed_vertical_layout")
        self.feed_greeting_notification = QLabel(self.scrollAreaWidgetContents_4)
        self.feed_greeting_notification.setObjectName(u"feed_greeting_notification")

        self.feed_vertical_layout.addWidget(self.feed_greeting_notification)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.feed_vertical_layout.addItem(self.verticalSpacer_6)


        self.verticalLayout_14.addLayout(self.feed_vertical_layout)

        self.results_scroll_area_2.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout.addWidget(self.results_scroll_area_2)

        self.feed_tab_widget.addTab(self.feed_tab, "")
        self.search_tab = QWidget()
        self.search_tab.setObjectName(u"search_tab")
        self.verticalLayout_11 = QVBoxLayout(self.search_tab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.search_tab)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.search_username = QLineEdit(self.search_tab)
        self.search_username.setObjectName(u"search_username")

        self.horizontalLayout_2.addWidget(self.search_username)

        self.search_button = QPushButton(self.search_tab)
        self.search_button.setObjectName(u"search_button")

        self.horizontalLayout_2.addWidget(self.search_button)


        self.verticalLayout_11.addLayout(self.horizontalLayout_2)

        self.groupBox_3 = QGroupBox(self.search_tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy2)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.results_scroll_area = QScrollArea(self.groupBox_3)
        self.results_scroll_area.setObjectName(u"results_scroll_area")
        self.results_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.results_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 84, 28))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.results_vertical_layout = QVBoxLayout()
        self.results_vertical_layout.setObjectName(u"results_vertical_layout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.results_vertical_layout.addItem(self.verticalSpacer_2)


        self.verticalLayout_12.addLayout(self.results_vertical_layout)

        self.results_scroll_area.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_3.addWidget(self.results_scroll_area)


        self.verticalLayout_11.addWidget(self.groupBox_3)

        self.feed_tab_widget.addTab(self.search_tab, "")
        self.tab_account = QWidget()
        self.tab_account.setObjectName(u"tab_account")
        self.verticalLayout_2 = QVBoxLayout(self.tab_account)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(self.tab_account)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.label_9)

        self.account_username_label = QLabel(self.tab_account)
        self.account_username_label.setObjectName(u"account_username_label")

        self.horizontalLayout_3.addWidget(self.account_username_label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.groupBox = QGroupBox(self.tab_account)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy4)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_13.addWidget(self.label_10)

        self.address_label = QLabel(self.groupBox)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_13.addWidget(self.address_label)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_13.addWidget(self.label_11)

        self.balance_label = QLabel(self.groupBox)
        self.balance_label.setObjectName(u"balance_label")
        self.balance_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_13.addWidget(self.balance_label)

        self.private_key_button = QPushButton(self.groupBox)
        self.private_key_button.setObjectName(u"private_key_button")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.private_key_button.sizePolicy().hasHeightForWidth())
        self.private_key_button.setSizePolicy(sizePolicy5)

        self.verticalLayout_13.addWidget(self.private_key_button)

        self.private_key_label = QLabel(self.groupBox)
        self.private_key_label.setObjectName(u"private_key_label")
        self.private_key_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_13.addWidget(self.private_key_label)


        self.verticalLayout_5.addLayout(self.verticalLayout_13)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.activation_group_box = QGroupBox(self.tab_account)
        self.activation_group_box.setObjectName(u"activation_group_box")
        self.verticalLayout_6 = QVBoxLayout(self.activation_group_box)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.activation_label = QLabel(self.activation_group_box)
        self.activation_label.setObjectName(u"activation_label")
        sizePolicy3.setHeightForWidth(self.activation_label.sizePolicy().hasHeightForWidth())
        self.activation_label.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.activation_label)

        self.activate_account_button = QPushButton(self.activation_group_box)
        self.activate_account_button.setObjectName(u"activate_account_button")
        sizePolicy5.setHeightForWidth(self.activate_account_button.sizePolicy().hasHeightForWidth())
        self.activate_account_button.setSizePolicy(sizePolicy5)

        self.horizontalLayout_4.addWidget(self.activate_account_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addWidget(self.activation_group_box)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.feed_tab_widget.addTab(self.tab_account, "")
        self.profile_tab = QWidget()
        self.profile_tab.setObjectName(u"profile_tab")
        self.verticalLayout_8 = QVBoxLayout(self.profile_tab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.profile_username = QLabel(self.profile_tab)
        self.profile_username.setObjectName(u"profile_username")

        self.verticalLayout_8.addWidget(self.profile_username)

        self.profile_address = QLabel(self.profile_tab)
        self.profile_address.setObjectName(u"profile_address")

        self.verticalLayout_8.addWidget(self.profile_address)

        self.profile_currency = QLabel(self.profile_tab)
        self.profile_currency.setObjectName(u"profile_currency")

        self.verticalLayout_8.addWidget(self.profile_currency)

        self.profile_date_created = QLabel(self.profile_tab)
        self.profile_date_created.setObjectName(u"profile_date_created")

        self.verticalLayout_8.addWidget(self.profile_date_created)

        self.line = QFrame(self.profile_tab)
        self.line.setObjectName(u"line")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy6)
        self.line.setMinimumSize(QSize(0, 0))
        self.line.setFrameShadow(QFrame.Raised)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout_8.addWidget(self.line)

        self.groupBox_2 = QGroupBox(self.profile_tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_16.addWidget(self.label_14)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.payments_amount = QDoubleSpinBox(self.groupBox_2)
        self.payments_amount.setObjectName(u"payments_amount")
        sizePolicy5.setHeightForWidth(self.payments_amount.sizePolicy().hasHeightForWidth())
        self.payments_amount.setSizePolicy(sizePolicy5)
        self.payments_amount.setMinimumSize(QSize(200, 0))
        self.payments_amount.setDecimals(18)
        self.payments_amount.setSingleStep(0.000001000000000)

        self.horizontalLayout_7.addWidget(self.payments_amount)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)


        self.verticalLayout_16.addLayout(self.horizontalLayout_7)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetMinimumSize)
        self.profiile_pay_button = QPushButton(self.groupBox_2)
        self.profiile_pay_button.setObjectName(u"profiile_pay_button")
        sizePolicy5.setHeightForWidth(self.profiile_pay_button.sizePolicy().hasHeightForWidth())
        self.profiile_pay_button.setSizePolicy(sizePolicy5)

        self.horizontalLayout_5.addWidget(self.profiile_pay_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.profile_request_button = QPushButton(self.groupBox_2)
        self.profile_request_button.setObjectName(u"profile_request_button")
        sizePolicy5.setHeightForWidth(self.profile_request_button.sizePolicy().hasHeightForWidth())
        self.profile_request_button.setSizePolicy(sizePolicy5)

        self.horizontalLayout_5.addWidget(self.profile_request_button)


        self.verticalLayout_16.addLayout(self.horizontalLayout_5)


        self.verticalLayout_8.addWidget(self.groupBox_2)

        self.feed_tab_widget.addTab(self.profile_tab, "")

        self.horizontalLayout.addWidget(self.feed_tab_widget)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.login_tab_widget = QTabWidget(self.centralwidget)
        self.login_tab_widget.setObjectName(u"login_tab_widget")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.login_tab_widget.sizePolicy().hasHeightForWidth())
        self.login_tab_widget.setSizePolicy(sizePolicy7)
        self.login_tab = QWidget()
        self.login_tab.setObjectName(u"login_tab")
        self.verticalLayout_9 = QVBoxLayout(self.login_tab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label = QLabel(self.login_tab)
        self.label.setObjectName(u"label")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy8)

        self.verticalLayout_9.addWidget(self.label)

        self.login_username = QLineEdit(self.login_tab)
        self.login_username.setObjectName(u"login_username")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.login_username.sizePolicy().hasHeightForWidth())
        self.login_username.setSizePolicy(sizePolicy9)

        self.verticalLayout_9.addWidget(self.login_username)

        self.label_2 = QLabel(self.login_tab)
        self.label_2.setObjectName(u"label_2")
        sizePolicy8.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy8)

        self.verticalLayout_9.addWidget(self.label_2)

        self.login_password = QLineEdit(self.login_tab)
        self.login_password.setObjectName(u"login_password")
        sizePolicy10 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.login_password.sizePolicy().hasHeightForWidth())
        self.login_password.setSizePolicy(sizePolicy10)
        self.login_password.setEchoMode(QLineEdit.Password)

        self.verticalLayout_9.addWidget(self.login_password)

        self.label_5 = QLabel(self.login_tab)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_9.addWidget(self.label_5)

        self.wallet_line_Edit = QLineEdit(self.login_tab)
        self.wallet_line_Edit.setObjectName(u"wallet_line_Edit")

        self.verticalLayout_9.addWidget(self.wallet_line_Edit)

        self.login_button = QPushButton(self.login_tab)
        self.login_button.setObjectName(u"login_button")
        sizePolicy5.setHeightForWidth(self.login_button.sizePolicy().hasHeightForWidth())
        self.login_button.setSizePolicy(sizePolicy5)

        self.verticalLayout_9.addWidget(self.login_button)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.login_tab_widget.addTab(self.login_tab, "")
        self.create_account_tab = QWidget()
        self.create_account_tab.setObjectName(u"create_account_tab")
        self.verticalLayout_10 = QVBoxLayout(self.create_account_tab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_3 = QLabel(self.create_account_tab)
        self.label_3.setObjectName(u"label_3")
        sizePolicy8.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy8)

        self.verticalLayout_10.addWidget(self.label_3)

        self.create_account_username = QLineEdit(self.create_account_tab)
        self.create_account_username.setObjectName(u"create_account_username")
        sizePolicy10.setHeightForWidth(self.create_account_username.sizePolicy().hasHeightForWidth())
        self.create_account_username.setSizePolicy(sizePolicy10)

        self.verticalLayout_10.addWidget(self.create_account_username)

        self.label_4 = QLabel(self.create_account_tab)
        self.label_4.setObjectName(u"label_4")
        sizePolicy8.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy8)

        self.verticalLayout_10.addWidget(self.label_4)

        self.create_account_password = QLineEdit(self.create_account_tab)
        self.create_account_password.setObjectName(u"create_account_password")
        sizePolicy10.setHeightForWidth(self.create_account_password.sizePolicy().hasHeightForWidth())
        self.create_account_password.setSizePolicy(sizePolicy10)
        self.create_account_password.setEchoMode(QLineEdit.Password)

        self.verticalLayout_10.addWidget(self.create_account_password)

        self.label_7 = QLabel(self.create_account_tab)
        self.label_7.setObjectName(u"label_7")
        sizePolicy8.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy8)

        self.verticalLayout_10.addWidget(self.label_7)

        self.create_account_confirm_password = QLineEdit(self.create_account_tab)
        self.create_account_confirm_password.setObjectName(u"create_account_confirm_password")
        sizePolicy10.setHeightForWidth(self.create_account_confirm_password.sizePolicy().hasHeightForWidth())
        self.create_account_confirm_password.setSizePolicy(sizePolicy10)
        self.create_account_confirm_password.setEchoMode(QLineEdit.Password)

        self.verticalLayout_10.addWidget(self.create_account_confirm_password)

        self.create_button = QPushButton(self.create_account_tab)
        self.create_button.setObjectName(u"create_button")
        sizePolicy5.setHeightForWidth(self.create_button.sizePolicy().hasHeightForWidth())
        self.create_button.setSizePolicy(sizePolicy5)

        self.verticalLayout_10.addWidget(self.create_button)

        self.create_account_error_message = QLabel(self.create_account_tab)
        self.create_account_error_message.setObjectName(u"create_account_error_message")
        self.create_account_error_message.setStyleSheet(u"color: red;")

        self.verticalLayout_10.addWidget(self.create_account_error_message)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_5)

        self.login_tab_widget.addTab(self.create_account_tab, "")

        self.verticalLayout_4.addWidget(self.login_tab_widget)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.status = QLabel(self.centralwidget)
        self.status.setObjectName(u"status")

        self.horizontalLayout_6.addWidget(self.status)

        self.status_balance_label = QLabel(self.centralwidget)
        self.status_balance_label.setObjectName(u"status_balance_label")
        sizePolicy3.setHeightForWidth(self.status_balance_label.sizePolicy().hasHeightForWidth())
        self.status_balance_label.setSizePolicy(sizePolicy3)

        self.horizontalLayout_6.addWidget(self.status_balance_label)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 821, 20))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.addAction(self.actionLogout)
        self.menuFile.addAction(self.actionExport_Wallet)
        self.menuFile.addAction(self.actionImport_Wallet)
        self.menuSettings.addAction(self.actionWindow_Settings)

        self.retranslateUi(MainWindow)

        self.feed_tab_widget.setCurrentIndex(2)
        self.login_tab_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Metallic", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionWindow_Settings.setText(QCoreApplication.translate("MainWindow", u"Window Settings", None))
        self.actionLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.actionExport_Wallet.setText(QCoreApplication.translate("MainWindow", u"Export Wallet", None))
        self.actionImport_Wallet.setText(QCoreApplication.translate("MainWindow", u"Import Wallet", None))
        self.feed_greeting_notification.setText(QCoreApplication.translate("MainWindow", u"You have not received or made any payments yet!", None))
        self.feed_tab_widget.setTabText(self.feed_tab_widget.indexOf(self.feed_tab), QCoreApplication.translate("MainWindow", u"Feed", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Results", None))
        self.feed_tab_widget.setTabText(self.feed_tab_widget.indexOf(self.search_tab), QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.account_username_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Wallet", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.address_label.setText(QCoreApplication.translate("MainWindow", u"0x0", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Balance", None))
        self.balance_label.setText(QCoreApplication.translate("MainWindow", u"0.00 Ethereum", None))
        self.private_key_button.setText(QCoreApplication.translate("MainWindow", u"Show Private Key", None))
        self.private_key_label.setText(QCoreApplication.translate("MainWindow", u"0x0", None))
        self.activation_group_box.setTitle(QCoreApplication.translate("MainWindow", u"Activation", None))
        self.activation_label.setText(QCoreApplication.translate("MainWindow", u"This account is unactivated. Use account balance to activate account", None))
        self.activate_account_button.setText(QCoreApplication.translate("MainWindow", u"Activate", None))
        self.feed_tab_widget.setTabText(self.feed_tab_widget.indexOf(self.tab_account), QCoreApplication.translate("MainWindow", u"Account", None))
        self.profile_username.setText(QCoreApplication.translate("MainWindow", u"profile_username", None))
        self.profile_address.setText(QCoreApplication.translate("MainWindow", u"profile_address", None))
        self.profile_currency.setText(QCoreApplication.translate("MainWindow", u"profile_currency", None))
        self.profile_date_created.setText(QCoreApplication.translate("MainWindow", u"profile_date_created", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Payments", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Ethereum", None))
        self.profiile_pay_button.setText(QCoreApplication.translate("MainWindow", u"Pay", None))
        self.profile_request_button.setText(QCoreApplication.translate("MainWindow", u"Request", None))
        self.feed_tab_widget.setTabText(self.feed_tab_widget.indexOf(self.profile_tab), QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Wallet", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.login_tab_widget.setTabText(self.login_tab_widget.indexOf(self.login_tab), QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.create_button.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.create_account_error_message.setText("")
        self.login_tab_widget.setTabText(self.login_tab_widget.indexOf(self.create_account_tab), QCoreApplication.translate("MainWindow", u"Create Account", None))
        self.status.setText(QCoreApplication.translate("MainWindow", u"Logged out", None))
        self.status_balance_label.setText(QCoreApplication.translate("MainWindow", u"Balance: 0 Ethereum", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

