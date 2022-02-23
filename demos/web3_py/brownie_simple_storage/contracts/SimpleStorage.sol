pragma solidity ^0.6.0;

contract SimpleStorage {
    // external, public, internal, private
    // this will get initialized to 0!
    uint256 favoriteNumber;
    bool favoriteBool;

    struct People {
        uint256 favoriteNumber;
        string Name;
    }

    // array
    People[] public people;

    mapping(string => uint256) public nameToFavoriteNumber;

    People public person = People({favoriteNumber: 2, Name: "Andrew"});

    function store(uint256 _favoriteNumber) public {
        favoriteNumber = _favoriteNumber;
    }

    function retrieve() public view returns (uint256) {
        return favoriteNumber;
    }

    // memory = only be stored during execution of the contract call
    // storage = data will persist even after execution

    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People(_favoriteNumber, _name));
    }
}
