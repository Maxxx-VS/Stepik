# s = 'aaaabbc'
#
# max_let = 0
# letter = ''
#
# for i in range(len(s)):
#     if s.count(s[i]) >= max_let:
#         max_let = s.count(s[i])
#         letter = s[i]
# print(letter)
# print(range(len(s)))

# s = 'abcdefgfhfabc'
# i = 0
# if s.count('f') == 1:
#     print(s.find('f'))
# elif s.count('f') >= 2:
#     print(s.find('f')," ",s.rfind('f'))
# elif s.count('f') >= 0:
#     print('NO')

# s = 'ahahahahaha'
# s_first = s.find('h')
# s_last = s.rfind('h')+1
# print(s_first)
# print(s_last)
# print(s[0:s_first],s[s_last:])
#
# s = '@987'
# s_1 = s[1::]
# flag = True
#
# if s.find('@') != 0:
#     flag = False
# if len(s) <= 4:
#     flag = False
# if len(s) > 15:
#     flag = False
# if s_1.isalnum() != True:
#     flag = False
# if s_1.isdigit() != True:
#     if s_1.islower() != True:
#         flag = False
#
#
# print('Correct' if flag else 'Incorrect')

# n = int(input())
# for i in range(1, n+1):
#     t = input()
#     if len(t) == 0 or t.isspace():
#         t = "COMMENT SHOULD BE DELETED"
#     print (f'{i}: {t}')

# s = 'А123ВС_4544'
# letter = 'АВЕКМНОРСТУХ'
# flag = False
# if len(s) == 9:
#     if s[0] in letter and s[1].isdigit() and s[2].isdigit() and s[3].isdigit() and s[4] in letter and s[5] in letter and s[6] == '_' and s[7].isdigit() and s[8].isdigit():
#         print('YES')
#     else:
#         print('NO')
# elif len(s) == 10:
#     if s[0] in letter and s[1].isdigit() and s[2].isdigit() and s[3].isdigit() and s[4] in letter and s[5] in letter and s[6] == '_' and s[7].isdigit() and s[8].isdigit() and s[9].isdigit():
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('NO')

# y = '2010'
# m = '10K'
# b = 'Bitcoin'
# s = f'In {y}, someone paid {m} {b} for two pizzas.'
#
# print(s)


# date = input()
# kurs_usd = input()
# kurs_yan = input()
#
# s = f'На {date}: 1$ = {kurs_usd}₽, 1¥ = {kurs_yan}₽'
#
# print(s)

# day = int(input())
# mass = float(input())
#
# s = f'#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {mass} кг, ЦЕЛЬ по ВЕСУ = {100-day*0.2} кг'
#
# if mass > (100-day*0.2):
#     print('Что-то пошло не так\n' + s)
# if mass <= (100-day*0.2):
#     print('Все идет по плану\n' + s)

# for i in range(26):
#     print(chr(ord('A') + i))


# a = int(input())
# b = int(input())
#
# for i in range (a, b+1):
#     print(chr(i), end=' ')

# s = input()
#
# for i in s:
#     print(ord(i), end=' ')

# t = 'jjjjjjj'
# s = int(input())
#
# for i in t:
#     n = ord(i)-s
#     if n < 97:
#         n = 122-(96-n)
#     print(chr(n), end='')

# y = int(input())
# p = input()
# flag = True
#
# if p == 'm':
#     flag = False
# if y < 10:
#     flag = False
# if y >= 16:
#     flag = False
# print("YES" if flag else "NO")

# n = int(input())
# if n > 10 or n <= 0:
#     print('ошибка')
# if n == 1:
#     print('I')
# if n == 2:
#     print('II')
# if n == 3:
#     print('III')
# if n == 4:
#     print('IV')
# if n == 5:
#     print('V')
# if n == 6:
#     print('VI')
# if n == 7:
#     print('VII')
# if n == 8:
#     print('VIII')
# if n == 9:
#     print('IX')
# if n == 10:
#     print('X')

# a = int(input())
#
# if a % 2 != 0:
#     print("YES")
# if (2 <= a <= 5) and a % 2 == 0:
#     print("NO")
# if (6 <= a <= 20) and a % 2 == 0:
#     print("YES")
# if a > 20 and a % 2 == 0:
#     print("NO")

# Если разность x1 и y1 равны разности x2 и y2. Или если суммы равны ,значит да. Иначе нет

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if (x1-y1) == (x2-y2) or (x1+y1) == (x2+y2) or x1==x2 or y1==y2:
#     print ('YES')
# else:
#     print('NO')
#
#
# Берем задачу про слона и добавляем или x1==x2 or y1==y2


# name = 'джо'
# print(name.lower())
# print(name.upper())
# print(name)

# s = 'Python rocks!'
# print(s[1:5])
#
# s = 'abch12345h'
#
# s_first = s.find('h')
# s_last = s.rfind('h')
#
# s_slise = s[(s_first+1):s_last]
# # print(s_slise)
# s_reverse = s_slise[::-1]
# # print(s_reverse)
#
# print(s[0:(s_first+1):] + s_reverse + s[s_last::])


# numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
# a = min(numbers)
# b = max(numbers)
# # print(a)
# # print(b)
# print(a + b)

# evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# average = sum(evens) / len(evens)
#
# print(average)

# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# rainbow[3], rainbow[-1] = "Зеленый", "Фиолетовый"
#
#
# print(rainbow)


# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
#
# print(languages[::-1])

# numbers1 = [1, 2, 3]
# numbers2 = [6]
# numbers3 = [7, 8, 9, 10, 11, 12, 13]
#
# print((numbers1*2) + (numbers2*9) + numbers3)

# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print(len(numbers))
# print(numbers[-1])
# print(numbers[::-1])
# print("YES" if 5 in numbers and 17 in numbers else "NO")
# del numbers[0]
# del numbers[-1]
# print(numbers)

# n = int(input())
# arr = []
# for i in range (n):
#     s = input()
#     arr.append(s)
# print(arr)

# alf = "abcdefghijklmnopqrstuvwxyz"
# arr = []
# j = 0
# for i in range(len(alf)):
#     j += 1
#     arr.append(alf[i] * j)
# print(arr)

# n = int(input())
# arr = []
# for i in range (n):
#     s = int(input())
#     arr.append(pow(s, 3))
# print(arr)


# n = int(input())
# arr = []
# for i in range (1, n+1):
#     if n % i == 0:
#         arr.append(i)
# print(arr)

# l = int(input())
# arr_1 = []
#
#
# for i in range(l):
#     n = int(input())
#     arr_1.append(n)
# print(arr_1)
#
# for j in arr_1+1:
#     a = arr_1[j-1] + arr_1[j]
#     res.append(a)
#     j = j+1
# print(res)

# l = int(input())
# arr_1 = []
# res = []
#
# for i in range(l):
#     n = int(input())
#     arr_1.append(n)
#
#
# for j in range (1, len(arr_1)):
#     a = arr_1[j-1] + arr_1[j]
#     res.append(a)
#     j = j+1
# print(res)

# n = int(input())
# arr = []
# for i in range(n):
#     nn = int(input())
#     if i % 2 == 0:
#         arr.append(nn)
# print(arr)

# n = int(input())
# arr = []
# res = ''
# for i in range(n):
#     nn = input()
#     arr.append(nn)
#
# k = int(input())
#
#
# for i in arr:
#     res += i[k-1:k:]
# print(res)

# n = int(input())
# arr, res = [], []
#
# for i in range(n):
#     nn = input()
#     arr.append(nn)
#
# for i in arr:
#     for j in i:
#         res.append(j)
# print(res)

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for num in numbers:
#     print(num)

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in numbers:
#     print (i**2)

# n = int(input())
# result, inter = [], []
# for i in range(n):
#     x = int(input())
#     inter.append(x)
#     y = ((x**2) + (2*x) + 1)
#     result.append(y)
#
# print(*inter, sep='\n')
# print()
# print(*result, sep='\n')

# n =int(input())
# result = []
# for i in range(n):
#     result.append(int(input()))
# result.remove(min(result))
# result.remove(max(result))
# print(*result, sep='\n')

# n =int(input())
# result = []
# for i in range(n):
#     x = input()
#     if x in result:
#         continue
#     else:
#         result.append(x)
# print(*result)

# n =int(input())
# result = []
# enter = []
#
# for i in range(n):
#     x = (input())
#     result.append(x)
#
# q = input()
#
# for j in result:
#     if q.lower() in j.lower():
#         print(j)
# ##########################################
# arr_1, arr_2 = [], []
#
# n = int(input())
# for i in range(n):
#     x = (input())
#     arr_1.append(x)
#
# q = int(input())
# for i in range(q):
#     y = (input())
#     arr_2.append(y)
#
#
# for k in arr_1:
#     if y.lower() in k.lower():
#         print(k)
##########################################


































