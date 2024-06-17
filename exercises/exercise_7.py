x = int(input())
n1 = x//1000
n2 = (x % 1000)//100
n3 = (x % 100)//10
n4 = x % 10
sum_of_digits =n1+n2+n3+n4
print(sum_of_digits)
