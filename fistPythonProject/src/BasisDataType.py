#coding=utf-8
#运算符-基础数据类型整理 与实际应用效果

#运算符
anumber = 20
bnumber = 40
cnumber = 31
enumber = 2
fnumber = 0
gnumber = 3
hnumber = 31

astr = "str1Zsan"
bstr = "-bstrCza"
cstr = "str1Zsan"
dstr = "31"

afloat = 1.23
bfloat = 4.556
cfloat = 0.5
dfloat = 1.7
efloat = 1.23
ffloat = 31.0

#算术运算符

#加号 + 两个对象相加
print(anumber + bnumber)# 40
print(anumber + afloat)# 21.23
print(astr + bstr)# str1Zsan-bstrCza
#print(anumber + astr) # 错误 TypeError: unsupported operand type(s) for +: 'int' and 'str'
print("-------------")

#减号 -
print(anumber - enumber)# 18
print(anumber - bnumber)# -20
#print(anumber - astr) # 错误TypeError: unsupported operand type(s) for -: 'int' and 'str'
#print(astr - bstr)# 错误TypeError: unsupported operand type(s) for -: 'str' and 'str'
#print(astr - anumber)# TypeError: unsupported operand type(s) for -: 'str' and 'int'
print(afloat - bfloat)# -3.326
print(bfloat - afloat)# 3.326
print(anumber - afloat)# 18.77
print("-------------")

#乘号 *
print(anumber * bnumber)# 800
print(anumber * afloat)# 24.26
print(enumber * astr)# str1Zsanstr1Zsan  字符串str1Zsan输出两遍，字符串*多少则输出多少
print(anumber * fnumber)# 0
#print(astr * bstr)# 错误 TypeError: can't multiply sequence by non-int of type 'str'
print("-------------")

#除号 /
print(bnumber / anumber)# 2.0
print(anumber / bnumber)# 0.5
#print(anumber / fnumber)# 错误 ZeroDivisionError: division by zero
print(fnumber / anumber)# 0.0
print(anumber / afloat)# 16.260162601626018
print(8 / 6) # 1.3333333333333333 除不尽不知道内部如何处理的~~~
#print(anumber / astr)# 错误 TypeError: unsupported operand type(s) for /: 'int' and 'str'
#print(astr / anumber)# 错误 TypeError: unsupported operand type(s) for /: 'str' and 'int'
#print(astr / bstr)# 错误 TypeError: unsupported operand type(s) for /: 'str' and 'str'
print("-------------")

#取模 % 反会除法的余数,与浮点类型取模将反会浮点类型
print(bnumber % anumber) # 0
print(cnumber % enumber) # 1
print(anumber % bnumber) # 20
print(anumber % afloat) # 0.3200000000000003
print(anumber % cfloat) # 0.0
#print(anumber % astr) # 错误 TypeError: unsupported operand type(s) for %: 'int' and 'str'
#print(astr % anumber) # 错误 TypeError: not all arguments converted during string formatting
#print(astr % bstr) # 错误 TypeError: not all arguments converted during string formatting
print("-------------")

#幂 ** 返回x的y次方
print(anumber ** gnumber) # 8000
print(anumber ** afloat) # 39.83519015836661
#print(anumber ** astr) # 错误 TypeError: unsupported operand type(s) for ** or pow(): 'int' and 'str'
#print(astr ** bstr) # 错误 TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'str'
print(afloat ** bfloat) # 2.568074909363066
print("-------------")

#取整除 // 反会商的整数---与float类型取整除会返回float类型,int与int则反会int
print(anumber // afloat) # 16.0
print(anumber // dfloat) # 11.0 11.7....直接舍却了7
#print(anumber // astr) # 错误 TypeError: unsupported operand type(s) for //: 'int' and 'str'
#print(astr // bstr) # 错误 TypeError: unsupported operand type(s) for //: 'str' and 'str'
print(cnumber // bnumber) # 0
print("-------------")


#比较运算符

#等于 == 比较对象是否相等 ---- int类型与float类型值相等则返回True, int与float类型与str类型值相等也不会返回True
print(anumber == bnumber) # False
print(cnumber == hnumber) # True
print(cnumber == ffloat) # True
print(cnumber == dstr) # False
print(ffloat == dstr) # False
print(astr == bstr) # False
print(astr == cstr) # True
print("-------------")

#不等于 != 比较两个对象是否不相等 ---- int类型与float类型值不相等则返回True, int与float类型与str类型值相等也不会返回False
print(anumber != bnumber) # True
print(cnumber != hnumber) # False
print(cnumber != ffloat) # False
print(cnumber != dstr) # True
print(ffloat != dstr) # True
print(astr != bstr) # True
print(astr != cstr) # False
print("-------------")

#不等于 <> 比较两个对象是否不相等 python 3以上版本不可用

#大于 > 返回x是否大于y ---- 不能int、float类型不能与str类型进行比较。str可以与str进行比较，根据第一位字符的ascii
print(anumber > bnumber) # False
print(cnumber > hnumber) # False
print(cnumber > ffloat) # False
#print(cnumber > dstr) # 错误 TypeError: '>' not supported between instances of 'int' and 'str'
#print(ffloat > dstr) # 错误 TypeError: '>' not supported between instances of 'float' and 'str'
print(astr > bstr) # True
print(astr > cstr) # False
print("-------------")

#小于 < 返回x是否小于y ---- 不能int、float类型不能与str类型进行比较。str可以与str进行比较，根据第一位字符的ascii
print(anumber < bnumber) # True
print(cnumber < hnumber) # False
print(cnumber < ffloat) # False
#print(cnumber < dstr) # 错误 TypeError: '<' not supported between instances of 'int' and 'str'
#print(ffloat < dstr) # 错误 TypeError: '<' not supported between instances of 'float' and 'str'
print(astr < bstr) # False
print(astr < cstr) # False
print("-------------")

#小于 >= 返回x是否大于等于y ---- 不能int、float类型不能与str类型进行比较。str可以与str进行比较，根据第一位字符的ascii
print(anumber >= bnumber) # False
print(cnumber >= hnumber) # True
print(cnumber >= ffloat) # True
#print(cnumber >= dstr) # 错误 TypeError: '>=' not supported between instances of 'int' and 'str'
#print(ffloat >= dstr) # 错误 TypeError: '>=' not supported between instances of 'float' and 'str'
print(astr >= bstr) # True
print(astr >= cstr) # True
print("-------------")

#小于 <= 返回x是否小于等于y ---- 不能int、float类型不能与str类型进行比较。str可以与str进行比较，根据第一位字符的ascii
print(anumber <= bnumber) # True
print(cnumber <= hnumber) # True
print(cnumber <= ffloat) # True
#print(cnumber <= dstr) # 错误 TypeError: '<=' not supported between instances of 'int' and 'str'
#print(ffloat <= dstr) # 错误 TypeError: '<=' not supported between instances of 'float' and 'str'
print(astr <= bstr) # False
print(astr <= cstr) # True
print("-------------")

#赋值运算符

#简单赋值运算符 =
inumber = anumber + bnumber
print("将anumber赋值给inumber=",inumber)
inumber = 44
strtes = 'aassss'
print("普通赋值=",inumber,strtes)
print("-------------")

#加法赋值运算符 +=
inumber = 10
inumber += anumber
print(inumber)
estr = "ssss"
'''
错误 str类型不可以和int、float类型+=
estr += inumber
print(estr)
TypeError: can only concatenate str (not "int") to str

estr += afloat
print(estr)
TypeError: can only concatenate str (not "float") to str
'''
estr += astr
print(estr) #ssssstr1Zsan

gfloat = 55.5
gfloat += anumber
print(gfloat)

gfloat = 55.5
gfloat += afloat
print(gfloat)
print("-------------")

#减法赋值运算符-=
inumber = 10
inumber -= anumber
print(inumber)
estr = "ssss"
'''
错误 str类型不可以和int、float类型-=
estr -= inumber
print(estr)
TypeError: can only concatenate str (not "int") to str

estr -= afloat
print(estr)
TypeError: can only concatenate str (not "float") to str

错误 str类型不可使用-=运算符
estr -= astr
print(estr) 
TypeError: unsupported operand type(s) for -=: 'str' and 'str'
'''

gfloat = 55.5
gfloat -= anumber
print(gfloat)

gfloat = 55.5
gfloat -= afloat
print(gfloat)
print("-------------")

#乘法赋值运算符
inumber = 10
inumber *= anumber
print(inumber)

inumber = 10
estr = "asdf"
estr *= inumber
print(estr) # str类型*= int类型则会拼接inumber个estr

'''
错误 不可与float类型进行*=
estr *= afloat
print(estr)
TypeError: can't multiply sequence by non-int of type 'float'

错误 str类型不可与str类型*=
estr *= astr
print(estr)
TypeError: can't multiply sequence by non-int of type 'str'
'''

gfloat = 55.5
gfloat *= anumber
print(gfloat)

gfloat = 55.5
gfloat *= afloat
print(gfloat)
print("--------------")

#除法赋值运算符
inumber = 10
inumber /= anumber
print(inumber)

'''
错误 str类型不能与int类型 /=
inumber = 10
estr = "asdf"
estr /= inumber
print(estr)

错误 不可与float类型进行/=
estr /= afloat
print(estr)
TypeError: can't multiply sequence by non-int of type 'float'

错误 str类型不可 /=
estr = 'asdasdasdasd'
fstr = 'asd'
estr /= fstr
print(estr)
TypeError: unsupported operand type(s) for /=: 'str' and 'str'
'''

gfloat = 55.5
gfloat /= anumber
print(gfloat)

gfloat = 55.5
gfloat /= afloat
print(gfloat)
print("--------------")

#取模运算符 %=
inumber = 10
inumber %= anumber
print(inumber)


'''
错误 str类型不能与int类型 %=
inumber = 10
estr = "asdf"
estr %= inumber
print(estr)
TypeError: not all arguments converted during string formatting

错误 不可与float类型进行%=
estr %= afloat
print(estr)
TypeError: can't multiply sequence by non-int of type 'float'

错误 str类型不可 %=
estr = 'asdasdasdasd'
fstr = 'asd'
estr %= fstr
print(estr)
TypeError: unsupported operand type(s) for /=: 'str' and 'str'
'''

gfloat = 55.5
gfloat %= anumber
print(gfloat)

gfloat = 55.5
gfloat %= afloat
print(gfloat)
print("--------------")

#幂赋值运算符 **=
inumber = 10
inumber **= anumber
print(inumber)

'''
错误 str类型不能与int类型 **=
inumber = 10
estr = "asdf"
estr **= inumber
print(estr)
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

错误 不可与float类型进行**=
estr = "asdf"
estr **= afloat
print(estr)
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'

错误 str类型不可 **=
estr = 'asdasdasdasd'
fstr = 'asd'
estr **= fstr
print(estr)
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'str'
'''

gfloat = 55.5
gfloat **= anumber
print(gfloat)

gfloat = 55.5
gfloat **= afloat
print(gfloat)
print("--------------")

# 取整除赋值运算符，请参考除号与除等运算符结果

#逻辑运算符
# and (a and b)并且关系。a=true且b=true则整体结果为true。否则为false
# or 或者关系。or两边一个为true则整体结果为true
# not 非，结果为true则最终结果为false，结果为false则最终结果为true

#成员关系
#in 如果在指定的序列中找到值返回True,否则返回False
#not in 如果在指定序列中没有找到值返回True，否则返回False

#数据类型 int、float、complex、bool、str
