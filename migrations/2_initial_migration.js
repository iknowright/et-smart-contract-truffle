const EnergyTradingLite = artifacts.require("EnergyTradingLite");

module.exports = function(deployer) {
  deployer.deploy(EnergyTradingLite);
};
