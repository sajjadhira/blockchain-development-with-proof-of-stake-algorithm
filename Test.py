from ProofOfStake import ProofOfStake

if __name__ == '__main__':
    pos = ProofOfStake()
    pos.update('Bob', 10)
    pos.update('Alice', 100)

    print(pos.get('Bob'))
    print(pos.get('Alice'))

    print(pos.get('Jack'))
