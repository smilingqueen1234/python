#wapp to recursion of digit 
def recursive_digit_sum(n,k):
    def digit_sum(num):
        if num < 10:
            return num 
        else:
            return num % 10 + digit_sum(num//10)
    initial_sum=digit_sum(n)*k
    if initial_sum>9 and k>=1:
        return recursive_digit_sum(initial_sum,1)
    else:
        return initial_sum
n=9875
k=3
result=recursive_digit_sum(n,k)
print(result)
