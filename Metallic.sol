// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.8.0;

contract UsernameDatabase {

    mapping (address => string) addressToUsername;
    mapping (string => address) usernameToAddress;

    constructor() public {

    }

    // underscore because this function needs to be internal, and
    // the derived classes addUsername must be public. If they share the
    // same name, then it is an override, but overrides cannot have
    // different visibility.
    function _addUsername(string memory username) internal virtual {
        require (!usernameExists(username), "Username already exists.");

        // if the username is unused, add it to the database
        usernameToAddress[username] = msg.sender;
        addressToUsername[msg.sender] = username;
    }

    function usernameExists(string memory username) public view returns (bool) {
        return usernameToAddress[username] != address(0);
    }

    function getAddressFromUsername(string memory username) public view returns (address) {
        return usernameToAddress[username];
    }

    function getUsernameFromAddress(address currAddress) public view returns (string memory) {
        return addressToUsername[currAddress];
    }

    function getCurrentUsersUsername() public view returns (string memory) {
        return addressToUsername[msg.sender];
    }
}

contract Metallic is UsernameDatabase{

    function substring(string memory str, uint startIndex, uint endIndex) internal returns (string memory) {
        bytes memory strBytes = bytes(str);
        bytes memory result = new bytes(endIndex-startIndex);
        for(uint i = startIndex; i < endIndex; i++) {
            result[i-startIndex] = strBytes[i];
        }
        return string(result);
    }

    function isValidChar(bytes1 c) private pure returns (bool) {
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
    function addUsername(string memory username) public {
        require(bytes(username).length <= 32, "Usernames must be 32 characters or less.");
        require(bytes(username).length >= 1, "Usernames must be at least one character");

        for (uint i = 0; i < bytes(username).length; i++ ){
            bytes1 char = bytes(substring(username, i, i+1))[0];
            require(isValidChar(char), "Characters must be 0-9, a-z, A-Z.");
        }

        super._addUsername(username);
    }
}
