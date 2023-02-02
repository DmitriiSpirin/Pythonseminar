"""
a = int(input("Введите трехзначное число: "))
a1 = a % 10
a2 = a % 100//10
a3 = a // 100
print("Сумма цифр числа: ", a1+a2+a3)
"""
"""
s = int(input("Введите количество журавликов: "))
kat = int((s/3)*2)
pet = int((kat/2)/2)
ser = int((kat/2)/2)
print(kat, pet, ser)
"""
"""
n = input()
s1 = int(n[0]) + int(n[1]) + int(n[2])
s2 = int(n[3]) + int(n[4]) + int(n[5])
if s1 == s2:
  print("YES")
else:
  print("NO")
"""

n = int(input())
m = int(input())
k = int(input())
if k < n*m and k % n == 0 or k % m == 0:
    print("YES")
else:
    print("NO")
