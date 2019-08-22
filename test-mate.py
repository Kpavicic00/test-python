# -*- encoding: utf-8 -*-
a = 12.3456

b = a - int(a)
temp = int(a)
count = 2
print(b)
print("1-a",int(a))
while(count > 0):
    b= b*10
    print("?",b)
    count -=1
e = int(b)
print(e)
print("count",count)
count = 2
e = e/1.0
baza = 10**count
kok = e/baza
print(kok)

# n = 0.4562
# rev = 0.0
#
# while(n > 0):
#     a = n * 10.0
#     # print("n-1",n)
#     print("a-1",a)

print("rez : ", temp  +kok)
