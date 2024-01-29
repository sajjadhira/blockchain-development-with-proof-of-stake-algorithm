from ProofOfStake import ProofOfStake
from Lot import Lot

if __name__ == '__main__':
    # pos = ProofOfStake()
    # pos.update('Bob', 10)
    # pos.update('Alice', 100)

    # print(pos.get('Bob'))
    # print(pos.get('Alice'))

    # print(pos.get('Jack'))

    lot = Lot('bob', 1, '00000000')
    print(lot.lotHash())
