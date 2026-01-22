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



#for m in range(32):
#    n = ip_network(f'215.181.200.27/{m}', 0)
#    print(n, n.netmask)


#n = ip_network(f'112.208.0.0/255.255.128.0', 0)
#print(n, n.netmask)
#
#k = 0
#for ip in n:
#    b = f'{ip:b}'
#    if b.count('1') % 11 == 0:
#        k += 1
#print(k)


#for m in range(32):
#    n = ip_network(f'20.24.110.42/{m}', 0)
#    print(n, n.netmask)


#n = ip_network(f'172.16.160.0/255.255.240.0', 0)
#print(n, n.netmask)
#
#k = 0
#for ip in n:
#    b = f'{ip:b}'
#    if b.count('1') % 3 != 0:
#        k += 1
#print(k)


#for m in range(32):
#    n1 = ip_network(f'118.187.59.255/{m}', 0)
#    n2 = ip_network(f'118.187.65.115/{m}', 0)
#    if n1 != n2:
#        print(m)
#        print(1, n1[0], n1[-1])
#        print(1, n2[0], n2[-1])
#        print('---------------------------')


#n = ip_network(f'195.102.65.64/255.255.255.192', 0)
#
#k = 0
#for ip in n:
#    b = f'{ip:b}'
#    if b[-8:].count('1') == b[-8:].count('0'):
#        k += 1
#print(k)






#for m in range(32):
#    n = ip_network(f'215.181.200.27/{m}', 0)
#    print(n, n.netmask)



#n = ip_network(f'98.81.154.195/255.252.0.0', 0)
#
#k = 0
#for ip in n:
#    print(ip)


#n = ip_network(f'235.86.56.0/255.255.248.0', 0)
#
#k = 0
#for ip in n:
#    b = f'{ip:b}'
#    if b[-2:] == '11':
#        k += 1
#print(k)



#n = ip_network(f'122.159.136.144/255.255.255.248', 0)
#print(n, n.netmask)
#
#k = 0
#for ip in n:
#    b = f'{ip:b}'
#    if b.count('1') % 4 != 0:
#        k += 1
#print(k)



#n = ip_network(f'123.222.111.192/255.255.255.248', 0)
#print(n, n.netmask)
#
#k = 0
#for ip in n:
#    b = f'{ip:b}'
#    if b[-8:].count('1') % 3 != 0:
#        k += 1
#print(k)



#n = ip_network(f'87.226.26.72/255.255.255.252', 0)
#print(n, n.netmask)
#
#k = 0
#for ip in n:
#    b = f'{ip:b}'
#    if b.count('0') % 2 == 0:
#        k += 1
#print(k)



#for m in range(32):
#    n1 = ip_network(f'61.58.73.42/{m}', 0)
#    n2 = ip_network(f'61.58.75.136/{m}', 0)
#    if n1 == n2:
#        print(m)
#        print(1, n1[0], n1[-1])
#        print(1, n2[0], n2[-1])
#        print('---------------------------')


#for m in range(32):
#    n1 = ip_network(f'151.172.115.121/{m}', 0)
#    n2 = ip_network(f'151.172.115.156/{m}', 0)
#    if n1 != n2:
#        print(m)
#        print(1, n1[0], n1[-1])
#        print(1, n2[0], n2[-1])
#        print('---------------------------')


#n = ip_network(f'192.168.160.0/255.255.224.0', 0)
#
#k = 0
#for ip in n.hosts():
#    b = f'{ip:b}'
#    if b.count('1') == 19:
#        k += 1
#print(k)



#n = ip_network(f'192.168.76.160/255.255.255.240', 0)
#
#k = 0
#i = 0
#for ip in n.hosts():
#    i += 1
#    b = f'{ip:b}'
#    if b[-8:].count('1') % 2 == 0 and i % 2 == 0:
#        k += 1
#print(k)


def SumOct(s):
    nums = [int(x) for x in s.split('.')]
    return sum(nums)

#n = ip_network(f'172.95.116.174/255.255.192.0', 0)
#print(n[0])
#k = 0
#for ip in n.hosts():
#    print(SumOct(str(ip)))
#    break


#k = 0
#for m in range(32):
#    n = ip_network(f'192.214.116.184/{m}', 0)
#    b = f'{n[0]:b}'
#    if b.count('1') % 5 == 0 and b.count('1') > 0:
#        if '192.214.116.184' not in str(n[0]):
#            k += 1
#print(k)


#i = ""
#n = ip_network(f'192.168.12.207/255.192.0.0', 0)
# 
#for ip in list(n.hosts())[::-1]:
#    b = f'{ip:b}'
#    if b.count('0') == b.count('1'):
#       print(ip)
#       break


#i = ""
#n = ip_network(f'111.222.0.124/255.255.224.0', 0)
# 
#for ip in list(n.hosts())[::-1]:
#    b = f'{ip:b}'
#    if b.count('0') * b.count('1') % 2 != 0:
#       print(SumOct(str(ip)))
#       break