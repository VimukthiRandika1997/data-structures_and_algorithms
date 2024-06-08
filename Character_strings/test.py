def licenseKeyFormatting(s: str, k: int) -> str:
    # split the text 
    split_list = s.split('-')

    final = []
    # loop through each split
    for i, split in enumerate(split_list):
        if i == 0:
            if len(split) < 1: # should have at-least one-character
                return
            final.append(split)
        
        else:
            res = split
            j = i + 1
            while len(res) != k and j < len(split_list):
                res = res + split_list[j]
                j = j + 1
            final.append(res)

            if j >= len(split_list): # all the split are used!
                break

    print(final)
    return '-'.join(final)



def licenseKeyFormatting2(s: str, k: int) -> str:
    st = ""
    s = s.replace("-", "").upper()
    s = s[::-1] # reverse the string

    for i in range(0, len(s), k):
        st += s[i : i + k]
        st += "-"
    sts = st[::-1]

    sts = sts.replace("-", "", 1)
    return sts
    

def strStr(haystack: str, needle: str) -> int:
    res, i, j = 0, 0, 0

    while i < len(haystack) and j < len(needle):
        print(i, j, res)
        if haystack[i] == needle[j]: # check the equality
            i = i + 1
            j = j + 1
        else:
            res = i
            j = 0

        if j >= len(needle) - 1:
            return res
 
    return -1



if __name__ == '__main__':
    # input_text, k = '5F3Z-2e-9-w', 4
    # res = licenseKeyFormatting(input_text, k)
    # res = licenseKeyFormatting2(input_text, k)
    res = strStr('leetcode', 'leeto')
    print(res)