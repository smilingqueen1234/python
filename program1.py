def count_pretty_numbers(l,r):
    pretty_count=0
    for num in range(l,r+1):
        last_digit=num%10
        if last_digit==5:
            pretty_count+=1
    return pretty_count
t=int(input())
for _ in range(t):
    l,r = map(int,input().split())
    result = count_pretty_numbers(l,r)
    print(result)
