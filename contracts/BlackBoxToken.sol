// SPDX-License-Identifier: GPL-v∞
pragma solidity ^0.8.0;

contract BlackBoxToken {
    string public name = "BlackBox";
    string public symbol = "BLBX";
    uint8 public decimals = 18;
    uint256 public totalSupply = 666000000000000000000000;
    address public oracle;

    constructor() {
        oracle = msg.sender;
    }
    // future value encoded in myth
}