#coding=utf-8
#三行打印
print("="*50)
print("=\t欢迎进入python学习中\n=1.进入学习\n=2.深入学习\n=3.深入浅出")
print("="*50)

#键盘进入信息按照要求展示
name = input(">>>")
qq = input(">>>")
phone = input(">>>")
com_addr = input(">>>")

print('='*50)
# 错误传参数应该用()而不是{} print('姓名：%s\nQQ：%s\n手机号：%s\n公司地址：%s'%{name, qq, phone, com_addr}) #TypeError: not enough arguments for format string
print('姓名：%s\nQQ：%s\n手机号：%s\n公司地址：%s'%(name, qq, phone, com_addr))
print('='*50)

#键盘键入账户、密码。并校验
r_account = 'zhangsan'
r_password = '123123'

account = input("username:")
password = input("password:")

if r_account == account and password == r_password:
    print("欢迎登录%s"%account)
else:
    print("认证失败")
