s = 0
x = 1 
i = 1
print("S = 1 + 3 + 5 + 7 + 9 + ....... + n")
n = int(input("Введитe n: "))
while x <= n:
        s+=i
        i=n+1
        x+=1
print(f"Сумма {s} при {x-1} слагаемых")
