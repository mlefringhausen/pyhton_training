# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
if len(fname) == 0: fname = 'mbox-short.txt'
fh = open(fname)
count = 0
sum_from_lines = 0
for line in fh:
    if not line.startswith("From "):
        continue
    line = line.rstrip()
    print line.split()[1]
    count += 1
print "There were", count, "lines in the file with From as the first word"

