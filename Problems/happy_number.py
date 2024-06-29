def isHappy(n: int) -> bool:
    # If the current number n is already in the set,
    # then we are in a loop
    hset = set()

    while n != 1:
        if n in hset: 
            print(hset, n)
            return False
        hset.add(n)
        n = sum(int(i) ** 2 for i in str(n))
    else:
        print(hset)
        return True


if __name__ == '__main__':
    # n = 19
    n = 2
    print(isHappy(n))