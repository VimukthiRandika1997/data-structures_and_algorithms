def isAnagram(s: str, t: str) -> bool:
    # base case: lenght should be same for two strings
    if len(s) != len(t):
        return False

    # word count for two strings should be same
    # 'anagram' , 'nagaram'
    # 'a' = 3, 'n' = 1, ...
    # using hash-map to store

    def get_vocab(string: str):
        vocab = {}
        for ch in string:
            if ch not in vocab:
                vocab[ch] = 1
            else:
                vocab[ch] += 1
        return vocab

    vocab1 = get_vocab(s)
    vocab2 = get_vocab(t)

    # loop through each ch
    for ch in list(vocab1.keys()):
        if ch not in list(vocab2.keys()):
            return False
        if vocab1[ch] != vocab2[ch]:
            return False

    return True

# s = "anagram"; t = "nagaram"
s = "rat"; t = "car"
print(isAnagram(s, t))
