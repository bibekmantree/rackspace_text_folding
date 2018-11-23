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
	line = chunk[0]
	number_of_astr = len(line) - len(line.lstrip("*"))
	flag = get_number(flag, number_of_astr)
	print(".".join([str(i) for i in flag]), line.lstrip("*"), end="")
	

chunk = []
flag = [0]
for line in fileinput.input():
	if line.startswith("*"):
		my_print(chunk, flag)
		chunk = []
		chunk.append(line)
	else:
		chunk.append(line)
	
		