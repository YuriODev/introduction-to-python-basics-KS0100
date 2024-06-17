a= int(input())
b= int(input())
max_val = (a+b+(a-b))//2
max_val = a*(a>b)+b*(b>=a)
print(max_val)
