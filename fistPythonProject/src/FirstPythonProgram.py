import random
secret = random.randint(1,10)
print("-------------第一个python脚本程序-------------")
indexnum = 3
print(secret)
temp = input("猜数字？共3次机会：")
guess = int (temp)
if guess == secret:
    print("对了，神经病")
    print("对了第二行")
else:
    while guess != secret and indexnum > 0:
        indexnum = indexnum - 1
        guess = int(temp)
        if guess == secret:
            print("对了，神经病")
            print("对了第二行")
        else:
            if indexnum == 0:
                print("机会用完了，low逼")
            else:
                if guess > secret:
                    print("大了,你还有", indexnum, "次机会")
                    temp = input("重新猜wdnmd？！：")
                else:
                    print("小了,你还有", indexnum, "次机会")
                    temp = input("重新猜wdnmd？！：")
print("结束目测是必定输出的end")
