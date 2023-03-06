# a1= int(input("Введите значение 1-го элемента:"))
# d=int(input("Введите разность элементов:"))
# n=int(input("Введите количество элементов:"))
# res = [a1 + (i - 1) * d for i in range(1, n + 1)]
# print(*res)

list=[-5,9,0,3,-1,-2,1,4,-2,10,2,0,-9,8,10,-9,0,-5,-5,7]
min_number = int(input())
max_number = int(input())
for i in range(len(list)):
    if min_number <= list[i] <= max_number:
        print(i)