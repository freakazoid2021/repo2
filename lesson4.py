for element in range(9):
    print(element)

str1 = "this is a string"

for letter in str1:
    print(letter, end=" ")

print()

str2 = ["this", "is", "a", "string"]
for word in str2:
    if word == "is":
        print(word.upper())
    else:
        print(word[::-1])

if str2[0] == "is":
    print(str2[0].upper())
else:
    print(str2[0][::-1])
if str2[1] == "is":
    print(str2[1].upper())
else:
    print(str2[1][::-1])
if str2[2] == "is":
    print(str2[2].upper())
else:
    print(str2[2][::-1])
if str2[3] == "is":
    print(str2[3].upper())
else:
    print(str2[3][::-1])

str3 = str1.split()
print(str3)
# for(int i = 0; i < str3.size(); i+=1){
#     cout << str3[i] << endl;
# }

for i in range(len(str3)):  # 4
    print(str3[i], i)

dig2 = []
for i in range(20):
    dig2.append(i)

print(dig2)

dig1 = [i for i in range(20)]
print(dig1)
# range(30)  for(int i = 0; i < 20; i += 1){ print(i) }
# for digit in dig1:
#     if digit % 2 != 0:

for i in dig1:
    if i % 2 == 0:
        print(i * 3, end=' ')
    else:
        print(i + 1)

fruits = ["apple", "mango", "pineapple", "banana"]

for fruit in fruits:
    if fruit == "orange":
        print("I'm not eat it. I'm allergic")
        break
    print("Tasty fruit " + fruit)
else:
    print("Cool. without orange")

print("fruits are empty")
summ = 0
for i in dig1:
    if i % 2 != 0:
        print(i)
        summ += i
    else:
        print(i, end=" ")

print(f"\n{summ=}")
#text = text.split()
list1 = ["a", "b", 20, 30]
list2 = ["b", 25]
print()
for i in list2:
    for j in list1:
        if j == i:
            print(i, "was found")
            break
    else:
        print(i, "not found")

counter = 0
s = "hello , guys! how hello are hello you"
print(s.split())
for word in s.split():
    if "hello" == word:
        counter += 1
else:
    print(f"{counter=}")
# set, dict
# {}, [], ()
for x in range(5):
    for y in range(5):
        print(x * y, end=' ')
    print()
