#1.
n1=int(input("請輸入數字一: "))
n2=int(input("請輸入數字二: "))
print("請輸入運算: +, -, *, /, %, //, ^")
op=input()
print("new branch")
#2.
for i in range(1, 10):
    for j in range(1, 10):
        print("%s * %s = %2s" % (j, i, i*j),end="  ")
    print()