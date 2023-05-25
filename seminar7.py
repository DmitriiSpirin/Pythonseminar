# def poems(str):
#     str = str.split()
#     list_1 = []
#     for word in str:
#         sum = 0
#         for i in word:
#             if i in 'аеёиоуыэюя':
#                 sum += 1
#         list_1.append(sum)
#     return len(list_1) == list_1.count(list_1[0])
#
# text = input("Введите фразу: ")
# if poems(text):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')

# def print_operation_table(operation, num_rows, num_сolumns):
#     arr=[[operation(i,j) for i in range(1,num_rows+1)] for j in range(1, num_сolumns+1)]
#     for i in arr:
#         print(*[f"{x:>3}"for x in i])
# line = int(input("Введите количество строк: "))
# columns = int(input("Введите количество столбцов: "))
# print_operation_table(lambda x,y: x*y,line,columns)

lst_in = input().strip().split()
tp = {}
tp.update(list(map(lambda x: tuple(x.split('=')), lst_in)))
print(*sorted(tp.items()))
