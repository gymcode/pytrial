blockchain = [11]

def get_last_blockchain_value():
    return blockchain[-1]


def add_value_to_transaction(transaction_amount, last_transaction=get_last_blockchain_value()):
    blockchain.append([last_transaction, transaction_amount])


tx_amount = float(input("add transaction amount"))
add_value_to_transaction(tx_amount)
add_value_to_transaction(10.892)
add_value_to_transaction(23)

print(blockchain)