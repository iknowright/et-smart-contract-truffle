const EnergyTrading = artifacts.require("EnergyTrading");

module.exports = function(deployer) {
  deployer.deploy(EnergyTrading);
};
