# def degreeAB(a, b):
#     if b == 0:
#         return 1
#     return a * degreeAB(a, b - 1)
#
# a = int(input('Введите число: '))
# b = int(input('Введите степень: '))
# print(degreeAB(a, b))

a = int(input("Введите первое неотрицительное число "))
b = int(input("Введите второе неотрицательно число "))


def recursive_sum(a, b):
    if a == 0:
        return b
    else:
        return recursive_sum(a - 1, b + 1)


print(recursive_sum(a, b))