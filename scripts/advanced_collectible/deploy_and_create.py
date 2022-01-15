from brownie import AdvancedCollectible, network, config
from scripts.helpful_scripts import (
    get_account,
    OPENSEA_URL,
    get_contract,
    fund_with_link,
)


def deploy_and_create():
    # We want to be able to use the deployed contract if we are on a testnet
    # Otherwise, we weant to deploy some mocks and use those
    # Rinkeby
    account = get_account()
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
    )
    fund_with_link(advanced_collectible.address)
    creating_tx = advanced_collectible.createCollectible({"from": account})
    creating_tx.wait(1)
    print("New token has been created!")


def main():
    deploy_and_create()
