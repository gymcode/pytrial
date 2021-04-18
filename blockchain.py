blockchain = [1]

def get_last_blockchain_value():
    return blockchain[-1]


def add_value_to_transaction(transaction_amount, last_transaction=get_last_blockchain_value()):
    blockchain.append([last_transaction, transaction_amount])

add_value_to_transaction(2)



print(blockchain)