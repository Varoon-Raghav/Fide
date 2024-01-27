
# pip install requests


#----------------------------------- The basics

import requests
from requests.auth import HTTPBasicAuth

# Replace 'YOUR_INFURA_API_KEY' with your Infura API key
infura_url = "https://mainnet.infura.io/v3/51d7beff73ea4e538da40926ae2df5cb"

# Replace 'YOUR_ADDRESS' with your Ethereum address
address = "0x4b6b892b6878e61f421066a01fc03d0648228f82"

def send_ethereum_request(method, params):
    headers = {"Content-Type": "application/json"}
    data = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params,
    }

    response = requests.post(infura_url, headers=headers, json=data, auth=HTTPBasicAuth('', ''))
    return response.json()



#----------------------------------- Account Balance



# Example: Check Account Balance
balance_params = [address, "latest"]
balance_response = send_ethereum_request("eth_getBalance", balance_params)
balance_wei = int(balance_response["result"], 16)
balance_eth = balance_wei / 1e18

print(f"Balance of {address}: {balance_eth} ETH")




#----------------------------------- # of Transactions




# Get the number of transactions sent from the address
transaction_count_params = [address, "latest"]
transaction_count_response = send_ethereum_request("eth_getTransactionCount", transaction_count_params)

if "result" in transaction_count_response:
    total_transactions = int(transaction_count_response["result"], 16)
    print(f"Total transactions for {address}: {total_transactions}")
else:
    print("Error retrieving transaction count.")
