import re

with open("fredHeadAndBodyPattern.txt") as file:
    pattern = file.read()

c_pattern = pattern.splitlines()
c_rounds_num = len(c_pattern)
c_rounds = []

for item in c_pattern:
    r_num = c_pattern.index(item) + 1
    s_total = int(re.findall(r'\((.*?)\)', item)[0])
    steps = item.split('(', 1)[0]
    new_c_round = dict(r_num=r_num, steps=steps, s_total=s_total)
    c_rounds.append(new_c_round)

for c_round in c_rounds:
    print(c_round['steps'])
