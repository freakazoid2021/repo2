# ch = 'F'
#
# if 'a' < ch < 'z':
#     print("lower")
# else:
#     print("upper")
# text = "skd'ddsfsdf'vjn.,'!"
# str2 = ".,?!"
#
# for symbol in str2:
#     text = text.replace(symbol, "")
#
# print(text)
# for(int i = 1; i < 20; i += 2) { print(i); }

# dig2 = []
# for i in range(1, 20 + 1):
#     dig2.append(i)
# print(dig2)
# dig1_cpp[20];
# for(int i = 1; i < 20; i += 2) { dig1_cpp[i]= i; } / c++
# dig1 = [i for i in range(1, 20, 2)] /Python
# print(dig1)
a = 0

b = 10
# f"{a}, {b} " or "{a} {b} ".format(a, b) print("a= " + str(a)) <> print(f"{a=})

while a <= b:
    print(f"{a} <= {b}")
    a += 1

str3 = "123454dafk5svj6njksdd"

while str3:
    print(str3)
    str3 = str3[1:]
# arr = {0,1,2,3,4,5}
# foreach el in arr { print(el); }
for ch in range(len(str3)):
    print(str3)
    str3 = str3[1:]

# while True:
#     #
#     print("CTRL + C to exit")

x = 23
y = x // 2
# 31 // 2 = 15 , 31 / 2 = 15.5, 31 % 2 = 1
# 23 // 2 = 11 ///6 = 1,2,3,6 /// 15 = 1, 3, 5, 15/// 30 = 1, 2, 3, 5, 6, 10, 15
while y > 1:
    if x % y == 0:
        print(x, "has divider", y)
        break
    y -= 1
else:
    print(x, "is prime")

a = 1
b = 20

while b > 0:
    if b % 2 == 0:
        print(b)
    # if b == 3:
    #     break
    b -= 1
else:
    print("cycle done")

x = 10
while x:
    x -= 1
    if x % 2 != 0:
        continue
    print(x)
else:
    print("cycle done")

check = True

# while check:
#     num = int(input("enter number: "))
#     if num == 0:
#         check = False

print("Good buy")

str4 = "asdlfk34298u983nf39nu4kjndskjvnsdkj3489384fn8"
str5 = ""
print(len(str4))
i = 0
while i < len(str4):
    if str4[i].isalpha():
        str5 += str4[i]
    i += 1
print(str5)

i = 0
list1 = []
while i < 10:
    list1 += [j for j in range(10)]
    i += 1

print(len(list1))
# [ , , , , , , , ]
list1 = [2, "a", [2, 4]]

for i in range(len(list1)):
    list1[i] *= i + 1
    print(list1[i])

print(list1)
