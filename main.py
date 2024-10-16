import re

# Read file and split by line, store total rounds for later
with open("fredHeadAndBodyPattern.txt") as file:
    pattern = file.read()

c_pattern = pattern.splitlines()
c_rounds_num = len(c_pattern)

c_rounds = []

# Parse string to store round number, steps, and number of total steps.
for item in c_pattern:
    r_num = c_pattern.index(item) + 1
    s_total = int(re.findall(r'\((.*?)\)', item)[0])
    steps = item.split('(', 1)[0]
    new_c_round = dict(r_num=r_num, steps=steps, s_total=s_total)
    c_rounds.append(new_c_round)

# Convert steps into form that lists out all steps individually
for item in c_rounds:
    # For rounds with a step containing Brackets, convert to standard format
    if '[' in item['steps']:
        text = re.findall(r'\[(.*?)\]', item['steps'])[0]
        # Breakdown:
        #     multi = item['steps'].split('x')
        #     multi_1 = multi[1]
        #     multi_2 = multi_1.split(',')
        #     multi_3 = multi_2[0]
        #     multi_4 = multi_3.strip()
        #     multi_5 = int(multi_4)
        multi = int(item['steps'].split('x')[1].split(',')[0].strip())

        new_text = ''
        for x in range(multi):
            new_text += (text + ', ')

        split_steps = item['steps'].split(',')
        new_steps = ''
        for step in split_steps:
            index = split_steps.index(step)
            if '[' in step:
                split_steps[index] = new_text.strip(', ')
                split_steps.pop(index + 1)
            new_steps += split_steps[index].lstrip() + ', '

        item['steps'] = new_steps.strip(', ')

    #TODO Go through steps and list out each stich type individually based on the number next to it
