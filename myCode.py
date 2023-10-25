#1.
n1=int(input("請輸入數字一: "))
n2=int(input("請輸入數字二: "))
print("請輸入運算: +, -, *, /, %, //, ^")
op=input()
if op== "+":
    print("答案為:",n1+n2)
elif op== "-":
    print("答案為:",n1-n2)
print("new branch")
#2.
for i in range(1, 10):
    for j in range(1, 10):
        print("%s * %s = %2s" % (j, i, i*j),end="  ")
    print()