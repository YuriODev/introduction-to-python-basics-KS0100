n = int(input())
A1 = n // 1000
A2 = (n%1000)//100
A3 = (n % 100)//10
A4 = n%10
diff = abs((A1-A4)+(A2-A3))
print(max(1-diff,0))
