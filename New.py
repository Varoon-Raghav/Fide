# from web3 import Web3

# infura_url = "https://mainnet.infura.io/v3/51d7beff73ea4e538da40926ae2df5cb"

# web3 = Web3(Web3.HTTPProvider(infura_url))

# # print(web3.is_connected())

# account = "0x4b6b892b6878e61f421066a01fc03d0648228f82"

# print(Web3.is_address(account))

# print(Web3.is_checksum_address(account))

# balance = (web3.eth.get_balance(account))

# print(web3.from_wei(balance, "ether"))



from web3 import Web3

# Connect to an Ethereum node (you can use Infura or run your own node)
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/51d7beff73ea4e538da40926ae2df5cb'))

# Replace 'YOUR_ETH_ADDRESS' with the Ethereum wallet address you want to check
wallet_address = '0x4b6b892b6878e61f421066a01fc03d0648228f82'

# Convert the address to checksum address
checksum_address = w3.to_checksum_address(wallet_address)

# Check the balance
try:
    balance_wei = w3.eth.get_balance(checksum_address)
    balance_eth = w3.from_wei(balance_wei, 'ether')
    print(f"Balance of {checksum_address}: {balance_eth} ETH")
except Exception as e:
    print(f"Error: {e}")





# Get the latest block number
latest_block_number = w3.eth.block_number

# Initialize variables to store the latest mined transaction
latest_mined_transaction = None

# Iterate through the latest blocks to find the latest mined transaction involving the specified address
try:
    for i in range(latest_block_number, max(0, latest_block_number - 100), -1):
        block = w3.eth.get_block(i, full_transactions=True)

        for tx in block['transactions']:
            if tx['to'].lower() == wallet_address.lower() or tx['from'].lower() == wallet_address.lower():
                if not latest_mined_transaction or tx['blockNumber'] > latest_mined_transaction['blockNumber']:
                    latest_mined_transaction = tx

except Exception as e:
    print(f"Error: {e}")

# Print information about the latest mined transaction
if latest_mined_transaction:
    value_eth = w3.from_wei(latest_mined_transaction['value'], 'ether')
    direction = "Received" if latest_mined_transaction['to'].lower() == wallet_address.lower() else "Sent"
    print(f"{direction} Transaction:")
    print(f"  Hash: {latest_mined_transaction['hash']}")
    print(f"  From: {latest_mined_transaction['from']}")
    print(f"  To: {latest_mined_transaction['to']}")
    print(f"  Value: {value_eth} ETH")
    print(f"  Block Number: {latest_mined_transaction['blockNumber']}")
    print("---------------")
else:
    print("No mined transactions found.")