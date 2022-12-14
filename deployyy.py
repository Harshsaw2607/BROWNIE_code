from brownie import accounts, config,SimpleStorage
def deploy_simple_storage():
    account=accounts.load("freecodecamp-account")
    # print(account)
    simple_storage=SimpleStorage.deploy({"from":account})
    stored_value=simple_storage.retrieve()
    print(stored_value)
    transaction=simple_storage.store(15,{"from":account})
    transaction.wait(1)
    updated_storage_value=simple_storage.retrieve()
    print(updated_storage_value)

def get_account():
 if network.show_active=="development":
    return accounts[0]
 else:
    return accounts.add(config["wallets"]["from_key"])



def main():
    deploy_simple_storage()

        