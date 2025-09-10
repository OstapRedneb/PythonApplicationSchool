from turtle import*
from itertools import*
from ipaddress import*

##Задание 2
#for x in range(0, 2):
#    for y in range(0, 2):
#        for z in range(0, 2):
#            for w in range(0, 2):
#                if (x or y) and not(y == x) and not(w):
#                    print(f"{x} {y} {z} {w}")


## Задание 6
#
#k = 15
#tracer(0)
#left(90)
#down()
#
#for i in range(2):
#    forward(14 * k)
#    left(270)
#    back(12 * k)
#    right(90)
#up()
#
#forward(9 * k)
#right(90)
#back(7 * k)
#right(90)
#down()
#
#for i in range(2):
#    forward(13 * k)
#    right(90)
#    forward(6 * k)
#    right(90)
#up()
#
#for x in range(-50, 50):
#    for y in range(-50, 50):
#        goto(x*k, y*k)
#        dot()
#
#done()



##Задание 8
#
#n = 0
#for x in product('akorst', repeat=5):
#    x = ''.join(x)
#    n += 1
#
#    if x[0] != 'a' and x[0] != 's' and x[0] != 't' and x.count('o') == 2 and n % 2 == 0:
#        print(n)



##Задание 13 (Сумма октетов(чисел через .) максимально-возможного ip, исключая широковещательны и общий)
#
#n = ip_network("102.162.200.51/255.255.255.0", 0)
#print(sum(map(int, str(n[-2]).split('.'))))



##Задание 13 (Минимальный IP)
#n = ip_network("158.214.121.40/255.255.255.224", 0)
#print(str(n[1]))



##Задание 13 (маска неизвестна, перебором ищем минмаьное число едениц в разряде маски с условием)
#for x in range(0, 32):
#    n = ip_network(f'84.32.84.32/{x}', 0)
#    b = bin(int(n[-2]))[2:].zfill(32) #f'{n[-2]:b}'
#    if b.count('1') == 19:
#        print(x, n.num_addresses)



##Задание 13 (Ищем подключённые устройства, -2(широковещательный и база) - 1(то устройство, что задало сеть))
#n = ip_network('95.24.20.25/255.255.252.0', 0)
#print(n.num_addresses - 2 - 4 - 3 - 2 - 1 - 1)



##Задание 13 (сравнение 2 одинаковых бита)
#n = ip_network('222.121.128.0/255.255.224.0', 0)
#k = 0
#for ip in n:
#    b = f"{ip:b}"
#    if b[-2] == b[-1]:
#        k += 1
#print(k)



##Задание 13 (нахождение устройств перебором А)
#max = 1000000
#for a in range(0, 256):
#    n = ip_network(f"192.214.{a}.184/255.255.255.224", 0)
#    k = 0
#    adreses = 0
#    for ip in n:
#        adreses += 1
#        b = f"{ip:b}"
#        if b.count('1') > 15:
#            k += 1
#    if k == adreses:
#        print(a)



##Задание 9
#fileData = open("File1.txt")
#k = 0
#for s in fileData:
#    num = [int(x) for x in s.split()]
#    n4 = [x for x in num if num.count(x) == 4]
#    n2 = [x for x in num if num.count(x) == 2]
#    n1 = [x for x in num if num.count(x) == 1]
#    if len(n1) == 3 and len(n2) == 2 and len(n4) == 4\
#        and sum(n1) / len(n1) >= max(n2 + n4):
#        k+=1
#print(k)



##Задание 9
#fileData = open("File1.txt")
#k = 0
#for s in fileData:
#    num = [int(x) for x in s.split()]
#    n3 = [x for x in num if num.count(x) == 3]
#    n2 = [x for x in num if num.count(x) == 2]
#    num.sort()
#    nch = [x for x in num[:4] if x % 2 != 0]
#    ch = [x for x in num[:4] if x % 2 == 0]
#    if len(n3) == 1 and len(n2) == 4\
#        and len(ch) == 2 and len(nch) == 2:
#        k += sum(num)
#print(k)



##Вариант 20
#for x in range(0, 2):
#    for y in range(0, 2):
#        for z in range(0, 2):
#            for w in range(0, 2):
#                if ((not(x)) <= (not(y))) and z and not(w == z):
#                    print(f'{w} {z} {y} {x}')

#def Bild(n):
#    n -= n % 2
#    x = bin(n)[2:]
#    if x.count('0') % 2 == 0:
#        x += '1'
#        x = '10' + x[2:]
#    else:
#        x += '0'
#        x = '11' + x[2:]
#    return int(x, 2)
#
#for n in range(1, 10000):
#    r = Bild(n)
#    if r > 50:
#        print(n)
#        break


#file = open("File1.txt")
#k = 0
#for s in file:
#    nums = [int(x) for x in s.split()]
#    nums.sort()
#    if nums[-1] <= (nums[0] + nums[1] + nums[2]) / 3 or str(nums[0])[-1] == str(nums[1])[-1] == str(nums[2])[-1] == str(nums[3])[-1]:
#        k += 1
#print(k)


#def Bild(s):
#    while '98' in s or '888' in s or '7788' in s:
#        if '98' in s:
#            s = s.replace('98', '7', 1)
#        if '888' in s:
#            s = s.replace('888', '78', 1)
#        if '7788' in s:
#            s = s.replace('7788', '897', 1)
#    return s
#
#k = 0
#for n in range(4, 1000):
#    x = '9' + n * '8'
#    s = Bild(x)
#    if sum(map(int, s)) <= 399:
#        k += 1
#print(k)


#k = 0
#n = ip_network('108.35.239.240/255.255.255.248', 0)
#for ip in n:
#    b = f'{ip:b}'
#    if b.count('0') % 3 == 0:
#        k += 1
#print(k)

#c = 12
#nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C']
#
#for x in nums:
#    k = 0
#    for y in nums:
#        p = int(f'CC68{x}{y}', 13) + int(f'2{y}343{x}7', 13)
#        if p % 7 == 0:
#            k += 1
#    if k == 13:
#        print(x)
#        break
#print ((int(f'CC6833', 13) + int(f'2334337', 13)) / 7)

#def Del(n, m):
#    return n % m == 0
#
#list = []
#for a in range(1, 1500):
#    k = 0
#    for x in range(1, 1500):
#        if (Del(x, 20) <= (not(Del(x, 11)))) or (a < 3*x + 600):
#            k += 1
#    if k == 1499:
#        list.append(a)
#print(list[-1])



