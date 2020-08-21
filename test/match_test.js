const EnergyTrading = artifacts.require("EnergyTrading");

contract("EnergyTrading", async accounts => {
    it("Case 1 | Single user sell/buy test.", async () => {
        let instance = await EnergyTrading.deployed();
        await instance.bid(accounts[0], "now", "sell", [20, 5, 10, 15, 20], [20, 25, 40, 60, 60]);
        await instance.bid(accounts[1], "now", "buy", [10, 30, 20, 15, 10], [70, 55, 30, 25, 10]);
        let result = await instance.match_bids([accounts[0], accounts[1]], "now");
        assert.equal(
            result.logs[0].args[0],
            true,
            "Match result should be true."
        );
        assert.equal(
            result.logs[0].args[1].toString(),
            '40',
            "Matched volume should be 40."
        );
        assert.equal(
            result.logs[0].args[2].toString(),
            '40',
            "Matched price should be 40."
        );
        assert.equal(
            result.logs[0].args[3].toString(),
            accounts[0],
            "Matched buy users is not as expected."
        );
        assert.equal(
            result.logs[0].args[4].toString(),
            '100',
            "Matched buy ratio should be 100."
        );
        assert.equal(
            result.logs[0].args[5].toString(),
            accounts[0],
        );
        assert.equal(
            result.logs[0].args[6].toString(),
            '100',
            "Matched buy ratio should be 100."
        );
    });

    it("Case 2 | Multiple users with multiple buy/sell ratio", async () => {
        let instance = await EnergyTrading.deployed();
        await instance.bid(accounts[0], "now", "sell", [20, 5, 10, 15, 20], [20, 25, 40, 60, 60]);
        await instance.bid(accounts[0], "now", "buy", [10, 30, 20, 15, 10], [70, 55, 30, 25, 10]);
        let result = await instance.match_bids([accounts[0]], "now");
        assert.equal(
            result.logs[0].args[0],
            true,
            "Match result should be true."
        );
        assert.equal(
            result.logs[0].args[1].toString(),
            '40',
            "Matched volume should be 40."
        );
        assert.equal(
            result.logs[0].args[2].toString(),
            '40',
            "Matched price should be 40."
        );
        // assert.equal(
        //     result.logs[0].args[3].toString(),
        //     accounts[0],
        //     "Matched buy users is not as expected."
        // );
        assert.equal(
            result.logs[0].args[4].toString(),
            '100',
            "Matched buy ratio should be 100."
        );
        assert.equal(
            result.logs[0].args[5].toString(),
            accounts[0],
        );
        assert.equal(
            result.logs[0].args[6].toString(),
            '100',
            "Matched buy ratio should be 100."
        );
    });
});
