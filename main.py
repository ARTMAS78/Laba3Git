import re


def check_control_sum(snils):
    snils = re.sub(r'[-]', r'', snils)
    sum = 0
    a = 9
    for i in range(9):
        sum += a * int(snils[i])
        a -= 1
    if sum == 100:
        sum = sum % 100
    if sum >= 101:
        sum = sum % 101
    control_sum = 10*int(snils[-2]) + int(snils[-1])
    if sum == control_sum:
        return True
    else:
        return False

with open('snils.txt') as file:
    s = file.readline()

#s = 'berheifheofhef333-344-034 22 182-027-351 44drd 116-973-385 89'
result = re.findall(r"\d{3}[-]\d{3}[-]\d{3}\s\d{2}", s)

for i in result:
    if check_control_sum(i) == True:
        print(i)
