# -*- coding:utf-8 -*-
#1-100所有数的和
'''
x = 0
for i in range(1,101):
    x += i
    print(x)
'''
#整数加法计算器 如 content = input(">>> ")   # 5+9 , 6+4
'''
qwe = input(">>>")
a, b = qwe.split("+")
a = int(a)
b = int(b)
print(a + b)
'''

# 将集合[11,22,33,44,55,66,77,88,99,90]分类，大于66的放到另外一个
'''
li = [11,99,66,22,55,90,77,33,88,44]
li.sort() # 使用sort进行对集合排序 sort(cmp=None, key=None, reverse=False)
print(li)
z = li.index(66) # 获取集合对应值的下标
print("z=", z)
dic = {"key1":li[0:z], "key2":li[z:-1]} # 将集合切片
print(dic)
'''

#将一个集合中数字进行组合。组合成为两位数且不重复 抄袭实现方式
'''
li = [1,2,3,4,5,6,7,8,8]
li2 = []
li3 = []
for i in li:
    for x in li:
        if i != x:
            a = "%d%d" %(i, x)
            li2.append(a)
for y in li2:
    if y not in li3:
        li3.append(y)
print(li3)
print(len(li3))

#实现方式2
li = [1,2,3,2,4,6,5,6,7,8,8]
li2 = []
for i in li:
    for j in li:
        if i != j :
            a = "%s%s" %(i, j)
            if a not in li2:
                li2.append(a)
print(li2)
print(len(li2))
'''

'''
r = (72 / 85) * 100
print('%.1f%%'%r)
'''

def power(x, n = 2): # n = 2 默认参数。不传值则默认等于2
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5))
print(5**3)

def cnss(*number): # 可变参数
    for num in number:
        print(num)

cnss([1,66,44])