block = []
with open('fold_input.txt') as fh:
    for line in fh:

        number_of_dots = len(line) - len(line.lstrip("."))
        block.append({"number_of_dots":number_of_dots,"line": line.lstrip(".")})

signs = {True: "+", False: "-"}
block[-1]["switch"] = False
prev_flag_switch = False
prev_number_of_dots = block[-1]["number_of_dots"]

for line in block[-2::-1]:
    # print(line)
    if line["number_of_dots"] < prev_number_of_dots and prev_flag_switch is False :
        line["switch"] = True
        print(1)
    elif line["number_of_dots"] == prev_number_of_dots and prev_flag_switch is False:
        line["switch"] = False
        print(2)
    elif line["number_of_dots"] == prev_number_of_dots and prev_flag_switch is True:
        line["switch"] = False
        print(3)
    elif line["number_of_dots"] < prev_number_of_dots and prev_flag_switch is True:
        line["switch"] = True
        print(4)
    prev_number_of_dots = line["number_of_dots"]
    prev_flag_switch = line["switch"]

for line in block:
    print(line)

