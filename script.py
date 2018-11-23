import fileinput


def get_number(flag, number_of_astr):
    position = number_of_astr - 1
    try:
        flag[position] += 1
        flag = flag[:position+1]
    except:
        flag.append(1)
    return flag


def my_print(chunk, flag):
    block = []
    line = chunk[0]
    number_of_astr = len(line) - len(line.lstrip("*"))
    flag = get_number(flag, number_of_astr)
    print(".".join([str(i) for i in flag]), line.lstrip("*"), end="")
    for line in chunk[1:]:
        number_of_dots = len(line) - len(line.lstrip("."))
        block.append({"number_of_dots": number_of_dots, "line": line.lstrip(".")})
        print(block)


chunk = []
flag = [0]
for line in fileinput.input():
    if line.startswith("*") and not fileinput.isfirstline():
        my_print(chunk, flag)
        chunk = []
        chunk.append(line)
    else:
        chunk.append(line)
my_print(chunk, flag)