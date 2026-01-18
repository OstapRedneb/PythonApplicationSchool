from turtle import*
from itertools import*
from ipaddress import*

##������� 2
#for x in range(0, 2):
#    for y in range(0, 2):
#        for z in range(0, 2):
#            for w in range(0, 2):
#                if (x or y) and not(y == x) and not(w):
#                    print(f"{x} {y} {z} {w}")


## ������� 6
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



##������� 8
#
#n = 0
#for x in product('akorst', repeat=5):
#    x = ''.join(x)
#    n += 1
#
#    if x[0] != 'a' and x[0] != 's' and x[0] != 't' and x.count('o') == 2 and n % 2 == 0:
#        print(n)



##������� 13 (����� �������(����� ����� .) �����������-���������� ip, �������� ���������������� � �����)
#
#n = ip_network("102.162.200.51/255.255.255.0", 0)
#print(sum(map(int, str(n[-2]).split('.'))))



##������� 13 (����������� IP)
#n = ip_network("158.214.121.40/255.255.255.224", 0)
#print(str(n[1]))



##������� 13 (����� ����������, ��������� ���� ��������� ����� ������ � ������� ����� � ��������)
#for x in range(0, 32):
#    n = ip_network(f'84.32.84.32/{x}', 0)
#    b = bin(int(n[-2]))[2:].zfill(32) #f'{n[-2]:b}'
#    if b.count('1') == 19:
#        print(x, n.num_addresses)



##������� 13 (���� ������������ ����������, -2(����������������� � ����) - 1(�� ����������, ��� ������ ����))
#n = ip_network('95.24.20.25/255.255.252.0', 0)
#print(n.num_addresses - 2 - 4 - 3 - 2 - 1 - 1)



##������� 13 (��������� 2 ���������� ����)
#n = ip_network('222.121.128.0/255.255.224.0', 0)
#k = 0
#for ip in n:
#    b = f"{ip:b}"
#    if b[-2] == b[-1]:
#        k += 1
#print(k)



##������� 13 (���������� ��������� ��������� �)
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



##������� 9
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



##������� 9
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



##������� 20
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



#for x in range(0, 2):
#    for y in range(0, 2):
#        for z in range(0, 2):
#            for w in range(0, 2):
#                if (x <= (y and w)) and z:
#                    print(x, y, z, w)
#
#
#def ConvertToZ(n):
#    n = str(n)  #Ну хоть какие-то плюсы динамической типизации
#    s = sum(map(int, n))
#    m = min(map(int, n)) + max(map(int, n))
#    l = list(map(int, n))[0]
#    r = list(map(int, n))[-1]
#    p1 = s - l
#    p2 = m - r
#    preZ = sorted([p1, p2])
#    z = preZ[1] + preZ[0]
#    return z
#
#answer = 0
#for n in range(10000, 100000):
#    z = ConvertToZ(n)
#    if z == 222:
#        answer = n
#print(answer)
#
#
#k = 20
#screensize(1000, 1000)
#tracer(0)
#speed(2000)
#
#for i in range(101):
#    forward(10*k)
#    left(90)
#    forward(4*k)
#up()
#forward(5*k)
#right(90)
#for i in range(201):
#    back(12*k)
#    right(90)
#for i in range(301):
#    forward(11*k)
#    left(90)
#    forward(4*k)
#
#for x in range(-50, 50):
#    for y in range(-50, 50):
#        goto(x*k, y*k)
#        dot()
#done()


#print((2560*1440*20*10 - 1920*1080*15*10) / 8 / 1024)

#k = 0
#i = 0
#for s in product('агдейсэ', repeat=6):
#    i += 1
#    s = ''.join(s)
#    if 'егэ' in s:
#        k += i
#print(k)

#def inc(l):
#    k = 1
#    for x in l:
#        k *= x
#    return k
#
#ls = []
#file = open('File1.txt')
#for s in file:
#    nums = [int(x) for x in s.split()] #да я Linq зависимвй
#    n3 = [x for x in nums if nums.count(x) == 3]
#    n1 = [x for x in nums if nums.count(x) == 1]
#    if len(n3) == 3 and len(n1) == 4:
#        if sum(n1) <= 3 * n3[0]:
#            ls.append(nums)
#
#
#nummax = -100000
#for nums in ls:
#    n1 = [x for x in nums if nums.count(x) == 1]
#    if inc(n1) > nummax:
#        nummax = sum(nums)
#
#print(nummax)


#У меня проблема с 10, т.к. официальной лицензии нет, а на сайтах функционала поиска нет

#print(bin(32786)[2:])
#print(287 * 2 + 1 + 13)

#def HasEqualySum(ip):
#    s = ip.split('.')
#    if int(s[0]) == int(s[1]) + int(s[2]) + int(s[3]):
#        return True
#    if int(s[1]) == int(s[0]) + int(s[2]) + int(s[3]):
#        return True
#    if int(s[2]) == int(s[1]) + int(s[0]) + int(s[3]):
#        return True
#    if int(s[3]) == int(s[1]) + int(s[2]) + int(s[0]):
#        return True
#    return False
#
#ips = ip_network('46.29.170.214/255.255.128.0', 0)
#i = 0
#for ip in ips:
#    i += 1
#    if i != 32 and HasEqualySum(str(ip)):
#        print(ip)

#for sys in range(11, 33):
#    for x in range(1, 500_000):
#        if int('29A1', sys) + int('47771', sys) == 1_000_000 + x:
#            print(sys)

#print(125 - 32)


