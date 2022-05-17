// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";


contract TokenFarm is Ownable {
    // mapping token addrress -> staker address -> amount
    mapping(address => mapping(address => uint256)) public stakingBalance;
    mapping(address => uint256) public uniqueTokensStaked;
    mapping(address => address) public tokenPriceFeedMapping;
    address[] public stakers;
    address[] public allowedTokens;
    IERC20 public dappToken;

    // stateTokens
    // unStakeTokens
    // issueTokens
    // addAllowedTokens
    // getEthValue

    constructor(address _dappTokenAddress) public {
        dappToken = IERC20(_dappTokenAddress);
    }

    function setPriceFeedContract(address _token, address _priceFeed) public onlyOwner {
        tokenPriceFeedMapping[_token] = _priceFeed;
    }


    function issueTokens() public onlyOwner {
        // issue tokens to all stakers
        for (uint256 stakersIndex = 0; stakersIndex < stakers.length; stakersIndex++){
            address recipient = stakers[stakersIndex];
            uint256 userTotalValue = getUserTotalValue(recipient);
            // send them a token reward
            // dappToken.transfer(recipient, )
            // baded on their total value locked
        }
    }

    function getUserTotalValue(address _user) public view returns (uint256){
        uint256 totalValue = 0;
        require(uniqueTokensStakes[_user] > 0,"No tokens staked!");
        for (
            uint256 allowedTokensIndex = 0;
            allowedTokensIndex < allowedTokens.length;
            allowedTokensIndex++
            ){
                totalValue = totalValue + getUserSingleTokenValue(_user, allowedTokens[allowedTokenIndex]);
            }
    }

    function getUserSingleTokenValue(address _user, addressc _token) public view returns (uint256) {
        if (uniqueTokensStaked[_user]<= 0){
            return 0;
        }
        // price of the token * stakingBalance[_token][_user]
        getTokenValue(_token);
    }
    
    function getTokenValue(address _token) public view turns (uint256) {
        // priceFeedAddress
        address priceFeedAddress = tokenPriceFeedMapping[_token];
    }

    function stakeTokens(uint256 _amount, address _token) public {
        // what tokens can they stake?...
        // how much can they stake?...
        require(_amount > 0, "Amount must be more than 0");
        require(tokenIsAllowed(_token), "Token is currently not allowed");
        IERC20(_token).transferFrom(msg.sender, address(this), _amount);
        updateUniqueTokensStaked(msg.sender, _token);
        stakingBalance[_token][msg.sender] =
            stakingBalance[_token][msg.sender] +
            _amount;
        if (uniqueTokensStakes[msg.sender] == 1){
            stakers.push(msg.sender);
        }
    }

    functions updateUniqueTokensStaked(address _user,address _token) internal {
        if (stakingBalance[_token][_user]<= 0){
            uniqueTokensStaked[_user] = uniqueTokensStaked[_user] + 1;
        }
    }

    function addAllowedTokens(address _token) public onlyOwner {
        allowedTokens.push(_token);
    }

    function tokenIsAllowed(address _token) public returns (bool) {
        for (
            uint256 allowedTokensIndex = 0;
            allowedTokensIndex < allowedTokens.length;
            allowedTokensIndex++
        )
            if (allowedTokens[allowedTokensIndex] == _token) {
                return true;
            }
        return false;
    }
}
