"""
Это попытки приминения алгоритма Евклида.
Он вроде даже работает, но как его применить у меня никак не получилось((
"""
x = 38
y = 180

a = x
b = y

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

    e = a + b
print(e)
print(x / e)
print(y / e)

