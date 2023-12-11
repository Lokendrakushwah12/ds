def linear(num):
    c = 0
    nu = int(input("enter the number to be searched"))
    for  i in range(0, len(num)):
        if(nu == num[i]):
            c = 1
    if(c==0):
        print("the number was not present")
    else:
        print("the number was present")    
    
def sentinel(num):
    c=0
    nu = int(input("the number to be searched"))
    num.append(nu)
    i = 0
    while(num[i] != nu):
        i += 1
    if(i!=len(num)-1):
        print("the number was present")
    else:
        print("the numbe was not present")

def binary(num):
    c=0
    nu = int(input("the number to be searched"))
    num.sort()
    l = 0
    h = len(num) - 1
    while((h-l)>=0):
        mid = (l+h)/2
        if(nu == num[mid]):
            c = 1
            print("the number was found")
            break
        elif(nu<num[mid]):
            h = mid - 1
        else:
            l = mid + 1
    
def fibonacci(num):
    tf = int(input("enter the number to be searched"))
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


n =  int(input("enter the number of elements"))
num = list()
for i in range(0, n):
    x = int(input("enter the number"))
    num.append(x)

print("enter 1 for linear search")
print("enter 2 for fibonacci search")
choice = int(input("enter the choice"))
if(choice == 1):
    linear(num)
elif(choice == 2):
    fibonacci(num)
