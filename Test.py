from ProofOfStake import ProofOfStake
from Lot import Lot
import random
import string


def getRandomString(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


if __name__ == '__main__':
    pos = ProofOfStake()
    pos.update("bob", 10)
    pos.update("alice", 100)

    bobWins = 0
    aliceWins = 0

    for i in range(100):
        forger = pos.forger(getRandomString(i))
        if forger == "bob":
            bobWins += 1
        elif forger == "alice":
            aliceWins += 1
    print("Bob wins: " + str(bobWins) + " times \n\n")
    print("Alice wins: " + str(aliceWins) + " times \n\n")
