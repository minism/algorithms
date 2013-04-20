# Given a string, find the longest substring such that 
# the substring contains only K unique characters

# http://www.careercup.com/question?id=17221689


def find_substring(S, k=1):
    if len(S) < 2:
        return S

    charmap = {}        # Track counts for each char
    unique = 0          # Track the number of unique characters
    longest = ''        # Track the longest word
    start, end = 0, 0   # Iteration pointers
    while end < len(S):
        if unique <= k:
            end += 1
            newchar = S[end - 1]
            charmap[newchar] = charmap.get(newchar, 0) + 1
            if charmap[newchar] == 1:
                unique += 1
        else:
            start += 1
            remchar = S[start - 1]
            charmap[remchar] = charmap[remchar] - 1
            if charmap[remchar] == 0:
                unique -= 1
        if len(S[start:end]) > len(longest) and unique <= k:
            longest = S[start:end]
    return longest



input = 'aabbcbbbadef'

print find_substring(input, k=2)
