def anagrams(S):
    """Detect all anagrams for a given text snippet
    
    time complexity: n**2klogk(worst-case)
    """
    d = {}
    for word in S: # O(n)
        s = ''.join(sorted(word)) # calculate the signature: sort words according to the lexigraphical order: O(klogk)
        if s in d and s != '':
            if word not in d[s]: # Remove duplicates
                d[s].append(word)
        else:
            d[s] = [word]
    # get all anagrams
    return [d[s] for s in d if len(d[s]) > 1] # O(k): no of keys: k


if __name__ == '__main__':
    input_text = 'below the car is a rat drinking cider and bending its elbow while this thing is an arc  \
                that can act like a cat which cried during the night caused by pain in its bowel'

    res = anagrams(S=input_text.split(' '))
    print(res)