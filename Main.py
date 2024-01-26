from Transaction import Transaction

if __name__ == '__main__':
    sender = 'sender'
    recipient = 'recipient'
    amount = 100
    type = 'TRANSFER'
    transaction = Transaction(sender, recipient, amount, type)
    print(transaction.toJson())
