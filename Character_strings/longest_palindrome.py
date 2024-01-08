# Input: babcbabcbaccba
# Output: abcbabcba

def longestPalindrome(s: str) -> int:
    S = set()
    for char in s:
        if char not in S:
            S.add(char)
        else:
            S.remove(char)

    if len(S) != 0:
        return len(s) - len(S) + 1
    else:
        return len(s)

if __name__ == '__main__':
    input_text = 'abcbaad'
    res = longestPalindrome(input_text)
    print(res)