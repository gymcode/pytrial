blockchain = [1]

def get_last_blockchain_value():
    return blockchain[-1]


def add_value_to_transaction(transaction_amount):
    blockchain.append([get_last_blockchain_value(), transaction_amount])

add_value_to_transaction(2)
add_value_to_transaction(3)
add_value_to_transaction(4)

print(blockchain)