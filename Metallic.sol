// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.8.0;

contract UsernameDatabase {

    mapping (address => bytes32) addressToUsername;
    mapping (bytes32 => address) usernameToAddress;

    constructor() public {

    }

    function addUsername(bytes32 username) public virtual {
        require (!usernameExists(username), "Username already exists.");

        // if the username is unused, add it to the database
        usernameToAddress[username] = msg.sender;
        addressToUsername[msg.sender] = username;
    }

    function usernameExists(bytes32 username) public view returns (bool) {
        return usernameToAddress[username] != address(0);
    }

    function getAddressFromUsername(bytes32 username) public view returns (address) {
        return usernameToAddress[username];
    }

    function getUsernameFromAddress(address currAddress) public view returns (bytes32) {
        return addressToUsername[currAddress];
    }

    function getCurrentUsersUsername() public view returns (bytes32) {
        return addressToUsername[msg.sender];
    }
}

contract Metallic is UsernameDatabase{

    function isValidChar(bytes1 c) public pure returns (bool) {
        //utf-8
        return ((c >= 0x30 && c <= 0x39)     // 0-9
                || (c >= 0x41 && c <= 0x5A)  // capital letters
                || (c >= 0x61 && c <= 0x7A)  // lowercase letters
                || (c == 0x5F));              // underscore
    }

    function helloWorld() public pure returns (string memory) {
        return "Hello World";
    }

    //add a username for an address
    function addUsername(bytes32 username) public override {
        for (uint i = 0; i < 32; i++ ){
            require(isValidChar(username[i]), "Characters must be 0-9, a-z, A-Z");
        }

        super.addUsername(username);
    }
}
