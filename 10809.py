import string 

alpa = string.ascii_lowercase
al = {}
for str_ in alpa:
    al[str_] = -1

str_input = input()
str_input = list(str_input) # 문자열은 list만 해도 가능

for i,str_ in enumerate(str_input):
    if al[str_] == -1:
        al[str_] = i

for i in al.values():
    print(i, end = " ")   