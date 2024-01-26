from Transaction import Transaction
from Wallet import Wallet

if __name__ == '__main__':
    sender = 'sender'
    recipient = 'recipient'
    amount = 100
    type = 'TRANSFER'

    wallet = Wallet()

    fruadulentWallet = Wallet()

    transaction = wallet.createTransaction(recipient, amount, type)

    signatureInValid = Wallet.signatureValid(
        transaction.payload(), transaction.signature, fruadulentWallet.publicKeyString())

    signatureValid = Wallet.signatureValid(
        transaction.payload(), transaction.signature, wallet.publicKeyString())

    print('Signature Valid: ', signatureValid)
    print('Signature InValid: ', signatureInValid)
