from ProofOfStake import ProofOfStake
from Lot import Lot
import random
import string


def getRandomString(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


if __name__ == '__main__':
    pos = ProofOfStake()
    pos.update("bob", 75)
    pos.update("alice", 100)
    pos.update("jack", 50)

    bobWins = 0
    aliceWins = 0
    jackWins = 0

    for i in range(100):
        forger = pos.forger(getRandomString(i))
        if forger == "bob":
            bobWins += 1
        elif forger == "alice":
            aliceWins += 1
        elif forger == "jack":
            jackWins += 1
    print("Bob wins: " + str(bobWins) + " times \n\n")
    print("Alice wins: " + str(aliceWins) + " times \n\n")
    print("Jack wins: " + str(jackWins) + " times \n\n")
