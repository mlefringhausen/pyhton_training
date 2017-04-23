fname = raw_input("Enter file name: ")
if len(fname) == 0: fname = 'romeo.txt'
fh = open(fname)
lst = []
for line in fh:
    for word in line.split():
        if word not in lst:
            lst.append(word)
lst.sort()
print lst
