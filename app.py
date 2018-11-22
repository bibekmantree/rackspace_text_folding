def get_number(flag, number_of_astr):
    position = number_of_astr - 1
    try:
        flag[position] += 1
        flag = flag[:position+1]
    except:
        flag.append(1)
    return flag

flag = [0]
with open('input.txt') as fh:
    for line in fh:
        if line.strip() and line.startswith("*"):
            number_of_astr = len(line) - len(line.lstrip("*"))
            flag = get_number(flag, number_of_astr)
            print(".".join([str(i) for i in flag]), line.lstrip("*"), end="")




