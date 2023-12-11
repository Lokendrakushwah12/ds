def linear(num):
    c = 0
    nu = int(input("enter the number to be searched: "))
    for  i in range(0, len(num)):
        if(nu == num[i]):
            c = 1
    if(c==0):
        print("the number was not present")
    else:
        print("the number was present")    

def fibonacci(num):
    tf = int(input("enter the number to be searched: "))
    nu = len(num)
    num.sort()
    m2 = 0
    m1 = 1
    m = 1
    while(m<nu):
        m2 = m1
        m1 = m
        m = m1 + m2
    
    offset = 0
    call = 0
    while(m>1):
        i = min(offset+m2, nu-1)
        if (tf == num[i]):
            call = 1
            break
        elif(tf > num[i]):
            m = m1
            m1 = m2
            m2 = m-m1
            offset = i
        elif(tf < num[i]):
            m = m2
            m1 = m1- m2
            m2 = m -m1    
    if(call == 0):
        print("number was not present")
    else:
        print("number was present")


n =  int(input("enter the number of elements: "))
num = list()
for i in range(0, n):
    x = int(input("enter the number: "))
    num.append(x)

print("enter 1 for linear search")
print("enter 2 for fibonacci search")
choice = int(input("enter the choice: "))
if(choice == 1):
    linear(num)
elif(choice == 2):
    fibonacci(num)
