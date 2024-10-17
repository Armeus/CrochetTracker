import re

# Read file and split by line, store total rounds for later
with open("fredHeadAndBodyPattern.txt") as file:
    pattern = file.read()

c_pattern = pattern.splitlines()
c_rounds_num = len(c_pattern)


def multiply_stitch(mul, stitch):
    txt = ''
    for x in range(mul):
        txt += (stitch + ', ')
    return txt


c_rounds = []

# Parse string to store round number, steps, and number of total steps.
for item in c_pattern:
    r_num = c_pattern.index(item) + 1
    s_total = int(re.findall(r'\((.*?)\)', item)[0])
    steps = item.split('(', 1)[0]
    new_c_round = dict(r_num=r_num, steps=steps, s_total=s_total)
    c_rounds.append(new_c_round)

# Convert steps into form that lists out all steps individually
for c_round in c_rounds:
    # For rounds with a step containing Brackets, convert to standard format
    if '[' in c_round['steps']:
        text = re.findall(r'\[(.*?)\]', c_round['steps'])[0]
        # Breakdown:
        #     multi = item['steps'].split('x')
        #     multi_1 = multi[1]
        #     multi_2 = multi_1.split(',')
        #     multi_3 = multi_2[0]
        #     multi_4 = multi_3.strip()
        #     multi_5 = int(multi_4)
        multi = int(c_round['steps'].split('x')[1].split(',')[0].strip())

        new_text = multiply_stitch(multi, text)

        split_steps = c_round['steps'].split(',')
        new_steps = ''
        for step in split_steps:
            index = split_steps.index(step)
            if '[' in step:
                split_steps[index] = new_text.strip(', ')
                split_steps.pop(index + 1)
            new_steps += split_steps[index].lstrip() + ', '

        c_round['steps'] = new_steps.strip(', ')

    # skip starting round due to special case
    if 'start' in c_round['steps']:
        continue

    # Go through steps and list out each stitch type individually based on the number next to it
    converted_step = ''
    for step in c_round['steps'].split(','):
        s_num = 1
        s_type = ''

        for split in step.split():
            if split.isnumeric():
                s_num = int(split)
            else:
                s_type = split

        converted_step += multiply_stitch(s_num, s_type)

    c_round['steps'] = converted_step.replace(',', '').strip()

print(c_rounds)
