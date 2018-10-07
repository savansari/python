def reverseList(x):   
    for i in range(int(len(x)/2)):
       x[i],x[len(x)-i-1]=x[len(x)-i-1],x[i]
    return x

def isPalindrome(x):
    i=0
    while i<int(len(x)/2) and x[i]==x[len(x)-1-i]:
        i+=1
    if i<int(len(x)/2):
        return False
    return True

def payInCoinsDic(x):
    coins=[25,10,5]
    num={"Quarters":0,"Dimes":0,"Nickel":0,"Pennies":0}
    for i in range(len(coins)):
        while x+1>coins[i]:
            x-=coins[i]
            if i==0:
                num["Quarters"]+=1
            if i==1:
                num["Dimes"]+=1
            if i==2:
                num["Nickel"]+=1
    num["Pennies"]=x
    return num

def payInCoins(x):
    coins=[25,10,5]
    num=[0,0,0,0]
    for i in range(len(coins)):
        while x+1>coins[i]:
            x-=coins[i]
            num[i]+=1
    num[3]=x
    return num

print(payInCoins(0))
print(payInCoins(1))
print(payInCoins(5))
print(payInCoins(10))
print(payInCoins(25))
print(payInCoins(12))
print(payInCoins(99))
print(payInCoins(76))

def Factorial(n):
    if n==0 or n<0:
        return 0
    if n==1:
        return 1
    return n*Factorial(n-1)

print(Factorial(0))
print(Factorial(-2))
print(Factorial(5))
print(Factorial(12))

def Fib(n):
    if n==0 or n<0:
        return 0
    if n==1:
        return 1
    return Fib(n-2)+Fib(n-1)

print(Fib(0))
print(Fib(1))
print(Fib(5))
print(Fib(12))