# Metallic

Metallic is an open source Ethereum Smart Contract that allows usernames to be mapped to ethereum addresses. 

Metallic makes making ethereum payments easy by allowing payments to be made between easily recognizeable usernames like @bob or @alice, rather than traditional, difficult to read ethereum addresses.

# Dependencies

pip3 install Flask
pip3 install py-solc-x
pip3 install -U web3[tester]
pip3 install flask-wtf
pip3 install email_validator

# Development  

To launch metallic: "python3 app.py HTTP://127.0.0.1:7545", where the ip and port number are your test blockchain provider ip and port #. This will serve the website, and compile and deploy the smart contract to your test blockchain. 

If you dont have a test blockchain environment, ganache is recommended. 

To get a feel for how the website works follow these steps:

1. Launch Metallic.
2. In your browser, search for "http://127.0.0.1:5000/", this will take you to the Metallic website.
3. Go to the "Create Account" link on the top right of the website.
4. Fill out the three fields, and then hit "Create Account". You will be redirected to the homepage if your account creation was successful. The homepage is a feed of all of the accounts that have been created on your current instance of the smart contract, sorted by date created. 
5. Go to the "Search" link and search for the username you just created. Any username that contains the search term will be returned. 

Currently, all accounts are paid for automatically by one of the addresses from your test blockchain. The public key and private key for this address can be set in website.py > createAccount().

# Open Issues

1. Adding accounts to Metallic is very expensive. Somewhere around $5 usd at the current gas and Eth price (arounc 47 gwei and $650 USD at the time of writing). To reduce the cost, the smart contract should stop using "string memory" and start using bytes 32 instead. 

2. Error checking.

3. Smart contract gas efficiency is low in general. Any improvemements are welcome.
