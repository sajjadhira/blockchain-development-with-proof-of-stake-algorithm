from Transaction import Transaction
from Wallet import Wallet

if __name__ == '__main__':
    sender = 'sender'
    recipient = 'recipient'
    amount = 100
    type = 'TRANSFER'
    transaction = Transaction(sender, recipient, amount, type)
    transaction_json = transaction.toJson()
    wallet = Wallet()
    signature = wallet.sign(transaction_json)
    transaction.sign(signature)
    print(transaction.toJson())
