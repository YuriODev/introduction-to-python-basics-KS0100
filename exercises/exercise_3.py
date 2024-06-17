n =int(input("Enter a number?"))
hr =(n//3600)%24
min =(n//60)%60
sec =n%60
print(f"{hr}:{min:02d}:{sec:02d}")
