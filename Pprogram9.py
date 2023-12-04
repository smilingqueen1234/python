def calculate_stock_span(arr):
    stack=[]
    span=[1]*len(arr)
    for i  in range(len(arr)):
        while stack and arr[i]>=arr[stack[-1]]:
            stack.pop()
        if stack:
            span[i]=i-stack[-1]
        else:
            span[i]=i+1
        stack.append(i)
    return span
T=int(input())
for _ in range(T):
    N=int(input())
    prices=list(map(int,input().split()))
    span_result=calculate_stock_span(prices)
    print(*span_result)


        
        