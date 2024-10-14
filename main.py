
with open("fredHeadAndBodyPattern.txt") as file:
    pattern = file.read()

c_rounds = pattern.splitlines()
c_rounds_num = len(c_rounds)

c_round = c_rounds[1].split()
s_num = 0
s_total = 0
s_type = ''

for item in c_round:
    if item.isnumeric():
        s_num = int(item)
        continue
    elif '(' in item:
        s_total = item.strip('()')
    else:
        s_type = item

print(s_num, s_type, s_total)

new_string = ''
for x in range(s_num):
    new_string += (s_type + ' ')

print(new_string)
