string1 = "hello|world"
str2 = r"C:\user\download\file.txt"

# char_ch = "h" + "e" + "l" + "l" + "o"
str_h = ["h", 'e', 'l', 'l', 'o']
print(str_h)
str_h[0] = "g"
print(str_h)

print(str2)
new_str2 = str2.replace(".csv", ".")

print(new_str2)
print(string1)

str3 = string1[::-1]
print(str3)
str4 = "red, blue, green, gray"
str5 = str4.split(", ")
# str5[2] = "orange"
str6 = "/*/".join(str5)
print(str6)

index_start = str4.find("green")

print(str4[index_start:])

print(str4.find("e", 4))
print(str4.rfind("e"))
# print(str5)
# print(str4.replace(", ", '-'))

str6 = "45"
print(str6.isdigit())

str7 = "ksuhsudvks"
print(str6.isalpha())

str8 = "+"
print(str8.isalnum())

str9 = "aucakjdc"
str10 = "KJDCNKJNC"
print(str10.isupper())

str11 = "\vsd"
print(str11)
print(str11.isspace())

str12 = "Petr"
print(str12.istitle())

print(str12.upper())

print(str12.lower())

print(ord("0"))
print(chr(165))

str13 = "1sergey"

print(str9.capitalize())

# print(dir(str4))
print(str4.count("e"))
a = 10

b = 20

msg = ""

# if a > b:
#     msg = "a = {0} > b = {1} ".format(a, b)
#
# else:
#     msg = "a = {0} < b = {1} ".format(b, a)

if a > b:
    msg = f"{a} > {b}"
else:
    msg = f"{a} < {b}"

msg = "{0:.3f}".format(20/6)

num = 20.1234324123

msg = f"num = {num:.3f}"

print(msg)

msg = "length - {}, width - {}, height - {}"

print(msg.format(3, 10, 20))
text = """this
is 
multy 
level
string"""
print(text)
