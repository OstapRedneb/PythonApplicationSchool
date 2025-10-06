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



##Lesson 15.09
#for x in range(0, 2):
#    for y in range(0, 2):
#        for z in range(0, 2):
#            for w in range(0, 2):
#                if (x or y) and not(y == x) and not(w):
#                    print(f"{x} {y} {z} {w}")


#def Build(n):
#    x = bin(n - n%2)[2:]
#    if x.count('0') % 2 == 0:
#        x += '1'
#        x = '10' + x[2:]
#    else:
#        x += '0'
#        x = '11' + x[2:]
#    return int(x, 2)
#
#for n in range(1, 10000):
#    r = Build(n)
#    if r > 50:
#        print(n)
#        break


#list = ['0', '2', '4', '6', '8','A', 'C', 'E']
#k = 0
#for s in product('0123456789ABCDE', repeat=6):
#    s = "".join(s)
#    newlist = [s.index(x) for x in s if x in list]
#    if len(newlist) == 1 and (newlist[0] == 0 and s[newlist[0] + 1] != '3' or newlist[0] == 5 and s[newlist[0] - 1] != '3' or s[newlist[0] + 1] != '3' and s[newlist[0] - 1] != '3'):
#        k += 1
#print(k)



#n = ip_network("74.3.123.17/255.255.248.0", 0)
#print(str(n[-1]))

#def s4(a):
#    s = ''
#    while a > 0:
#        s = str(a % 4) + s
#        a //= 4
#    return s
#
#maxx = -100000000
#for x in range(3200, 0, -1):
#    a = 4**190 + 4**100 - 4**20 - x
#    if s4(a).count('0') % 2 == 0:
#       maxx = max(maxx, s4(a).count('0'))
#       if s4(a).count('0') == maxx:
#           print(x)

#print(((1121 * 1122 * 1123 * 1124 * 1125 * 1126 * 1127 * 1128) / 4 + (1121 * 1122) / 2) % 10000000000)


#for x in range(0, 2):
#    for y in range(0, 2):
#        for z in range(0, 2):
#            for w in range(0, 2):
#                if ((w <= (x==z)) or (not(y <= z))) == 0:
#                    print(z ,x, w, y)


#def Build(n):
#    x = oct(n)[2:]
#    if n % 8 == 0:
#        x += '1'
#        x = '2' + x
#    else:
#        x += str(n % 8)
#    return int(x, 8)
#
#for n in range(1, 10000):
#    r = Build(n)
#    if r <= 345:
#        print(n)

#file = open("File1.txt")
#k = 0
#for s in file:
#    nums = [int(x) for x in s.split()]
#    n2 = [x for x in nums if nums.count(x) == 2]
#    n1 = [x for x in nums if nums.count(x) == 1]
#    if len(n2) == 2 and len(n1) == 4:
#        if n2[0] >= (sum(n1) / 4):
#            k += sum(nums)
#print(k)

#list =[]
#for n in range(5, 4000):
#    s = '4' + n * '5'
#    while '45' in s or '155' in s or '1555' in s:
#        if '45' in s:
#            s = s.replace('45', '5', 1)
#        if '155' in s:
#            s = s.replace('155', '515', 1)
#        if '1555' in s:
#            s = s.replace('1555', '141', 1)
#    x = sum(map(int, s))
#    list.append(x)
#print(min(list))


#list =[]
#n = ip_newtwork('223.184.69.7/223.184.0.0', 0)
#for ip in n:
#    list.append(int(ip.split()[2]))
#print(max(list))

#def f5(a):
#    s = ''
#    while a != 0:
#        s = str(a % 5) + s
#        a //= 5
#    return s
#
#a = 4 * 625**1820 + 4 * 125**1830 - 4*25**1840 - 3 * 5 ** 1850 - 1860
#s = f5(a)
#print(sum(map(int, s)))


#file = open('14_17.txt')
#nums = [int(x) for x in file]
#minn = min([x for x in nums if abs(x) % 100 == 43])
#t = [nums[i] + nums[i + 1] for i in range(len(nums) - 1) if (nums[i] % 10000 != 0) + (nums[i+1] % 10000 != 0) > 0 and (nums[i] + nums[i+1])**2 >= minn**2]
#print(len(t), abs(min(t)))


#def Build(e, x, k):
#    if (e + x) >= 333: return k % 2 == 0
#    if k % 2 == 0: return 0
#
#    h = [Build(e, x+2, k-1), Build(e+2, x, k-1), Build(e*2, x, k-1), Build(e, x*2, k-1)]
#    return sum(h) if k % 2 == 0 else any(h)
#
#print('19', *(x for x in range(1, 322) if Build(11, x, 2)))
#print('20', *(x for x in range(1, 322) if Build(11, x, 3) and not Build(11, x, 1)))
#print('21', *(x for x in range(1, 322) if Build(11, x, 4) and not Build(11, x, 2)))








##VAR-1

#for x in range(0, 2):
#    for y in range(0, 2):
#        for z in range(0, 2):
#            for w in range(0, 2):
#                if (z or (x == (y <= w))) == 0:
#                    print(y, z, w, x)

def ToSystem(number, system, convertation='str'):
    s = ''
    systemList = []
    while number != 0:
        s = str(number % system) + s
        systemList.append(number % system)
        number //= system
    if convertation == 'list':
        systemList.reverse()
        return systemList
    return s


#def Bild(n):
#    x = ToSystem(n, 3)
#    if n % 5 == 0:
#        x += x[-2:]
#    else:
#        u = 7 * (n % 5)
#        x += ToSystem(u, 3)
#    return int(x, 3)
#
#for n in range(1, 10000):
#    r = Bild(n)
#    if r <= 273:
#        print(n)


#tracer(0)
#speed(10000)
#k = 20
#down()
#screensize(3000, 3000)
#
#for i in range(5):
#    forward(k*42)
#    right(270)
#    forward(k*55)
#    left(90)
#up()
#forward(k*17)
#right(90)
#forward(k*12)
#left(90)
#down()
#for i in range(14):
#    forward(k*14)
#    left(90)
#    forward(k*200)
#    left(90)
#up()
#
#for x in range(-75, 75):
#    for y in range(-75, 75):
#        goto(x*k, y*k)
#        dot()
#done()


#print(16 / 5)

#k = 0
#for s in product('абинорту', repeat=5):
#    k += 1
#    x = ''.join(s)
#    if k % 2 != 0 and x[0] != 'а' and x[0] != 'и' and x[0] != 'о' and x[0] != 'у' and x.count('б') <= 1 and x.count('у') <= 1 and x.count('р') <= 1 and x.count('а') <= 1 and x.count('т') <= 1 and x.count('и') <= 1 and x.count('н') <= 1 and x.count('о') <= 1:
#        print(k)


#k=0
#file = open('File1.txt')
#for s in file:
#    nums = [int(x) for x in s.split()]
#    n1 = [x for x in nums if nums.count(x) == 1]
#    nums.sort()
#    if len(n1) == 5 and (nums[0] + nums[4]) <= (nums[1] + nums[2] + nums[3]):
#        k += 1
#print(k)


#print(2 * 8 * 1024**3 / 10 / 31922)


#n = ip_network('150.122.11.21/255.255.254.0', 0)
#b = f'{n[1]:b}'
#print(b.count('1'))


#a = 5*729**2024 + 3*243**1413 - 7*81**169 - 2*9**107 + 3017
#systemList = ToSystem(a, 27, 'list')
#print(sum([systemList[i] for i in range(0, len(systemList)) if systemList[i] <= 25]))


#def Bild(x, y, a):
#    f = (2 * x * y > a) or (y < x) or (x < 15)
#    return f
#
#
#for a in range(500, 1, -1):
#    if all([Bild(x, y, a) for x in range(1, 500) for y in range(1, 500)]):
#        print(a)


#def Build(x, k):
#    if x >= 444: return k % 2 == 0
#    if k == 0: return 0
#
#    h = [Build(x+2, k-1), Build(x+5, k-1), Build(x*3, k-1)]
#    return all(h) if k % 2 == 0 else any(h)
#
#print('19', [x for x in range(1, 401) if Build(x, 2)])
#print('20', [x for x in range(1, 401) if Build(x, 3) and not Build(x, 1)])
#print('21', [x for x in range(1, 401) if Build(x, 4) and not Build(x, 2)])


#s = open(f"24 (12).txt").read()
#reultList = []
#news = ''
#
#
#for i in range(0, len(s) - 1):
#    if s[i] < s[i+1]:
#        news += s[i]
#    else:
#        news += s[i]
#        reultList.append(news)
#        news = ''
#
#print(len([string for string in reultList if len(string) == 5]))


#for x in range(0, 2):
#    for y in range(0, 2):
#        for z in range(0, 2):
#            for w in range(0, 2):
#                if ((not(x <= z)) or (w <= (y == z))) == 0:
#                    print(w, z, y, x)


def Build(x, k):
    if x <= 26: return k % 2 == 0
    if k == 0: return 0

    newx = x // 3
    if x % 3 != 0:
        newx += 1

    h = [Build(x-1, k-1), Build(x-4, k-1), Build(newx, k-1)]
    return all(h) if k % 2 == 0 else any(h)

print('19', [x for x in range(27, 401) if Build(x, 2)])
print('20', [x for x in range(27, 401) if Build(x, 3) and not Build(x, 1)])
print('21', [x for x in range(27, 401) if Build(x, 4) and not Build(x, 2)])