import random

a = random.randint(1, 10000)
b = random.randint(1, 10000)
c = a+b

with open('./Pyhton_App_DevOps/Result.txt', 'a+') as result:
    result.seek(0)
    data = result.read(100)
    if len(data) > 0:
        result.write("\n")
    result.write("Sum of {A} + {B} is = {C}".format(A=a, B=b, C=c))

print("Sum of {A} + {B} is = {C}".format(A=a, B=b, C=c))