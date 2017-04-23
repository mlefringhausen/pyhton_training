# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
if len(fname) == 0: fname = 'mbox-short.txt'
fh = open(fname)
mail_address_count = {}
most_committer_count = 0
for line in fh:
    if not line.startswith("From "):
        continue
    mail_address = line.rstrip().split()[1]
    mail_address_count[mail_address] = mail_address_count.get(mail_address, 0) + 1

for key, value in mail_address_count.items():
    if value > most_committer_count:
        most_committer_count = value
        most_committer = key

print most_committer, most_committer_count