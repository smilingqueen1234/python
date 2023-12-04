def compress_string(s):
    compressed_string=" "
    count=1
    for i in range(1,len(s)):
        if s[i] == s[i - 1]:
            count+=1
    else:
        compressed_string += s[i-1] + str(count)
        count = 1
    compressed_string += s[-1] + str(count)
    return compressed_string
input_string =input("Enter a string:")
str1=sorted(input_string)
result = compress_string(str1)
print("compressed string:",result)

