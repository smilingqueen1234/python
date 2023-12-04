def longest_prefix_suffix_length(s):
    n = len(s)
    lps = [0]*n
    j=0
    for i in range(1,n):
        while j > 0 and s[i] != s[j]:
            j = lps[j -1]
        if s[i] == s[j]:
            j+=1
        lps[i] = j
    length = lps[-1]
    return length
input_string = input("enter a string:")
result = longest_prefix_suffix_length(input_string)
print("lengthof longestproper prefix same as suffix:",result)