pragma solidity ^0.8.18;

contract Lottery {
    address public manager;
    address payable [] public players;
    address payable [] winStack;

    constructor() {
        manager = msg.sender;
    }
    
    modifier restricted() {
        require(msg.sender == manager);
        _;
    }

    function addressStartsWith0xD(address account) private pure returns (bool) {
        bytes memory addrBytes = abi.encodePacked(account);
        bytes1 prefix1 = 0x0D;
        bytes1 prefix11 = 0x0F;
        bytes1 prefix2 = addrBytes[1];
        return (prefix1 == prefix2 || prefix11 == prefix2);
    }

    
    function enter() public payable {
        require(msg.value > .01 ether);
        bool addr_of_sender = addressStartsWith0xD(msg.sender);
        if (addr_of_sender) {
            winStack.push(payable(msg.sender));
        } 
        players.push(payable(msg.sender));
    }
    
    // Recognized security concern: for sake of tutorial only
    function random() private view returns (uint) {
        return uint(keccak256(abi.encodePacked(block.difficulty, block.timestamp, winStack)));
    }
    
    function pickWinner() public restricted {
        uint index = random() % winStack.length;
        winStack[index].transfer(address(this).balance);
        winStack = new address payable[](0);
    }
    
    function getPlayers() public view returns (address payable[] memory) {
        return players;
    }
    
}