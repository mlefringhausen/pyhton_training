import re

#fname = 'regex_sum_42.txt'
fname = 'regex_sum_362387.txt'

fh = open(fname)
number = 0
number_sum = 0

for line in fh:
    line = line.rstrip()
    if re.search('([0-9]+)', line):
        for number in re.findall('([0-9]+)', line):
            number_sum += int(number)
print number_sum
