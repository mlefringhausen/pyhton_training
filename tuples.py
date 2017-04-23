""" 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each
 of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string
 a second time using a colon.

#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below."""

fname = raw_input("Enter file name: ")
if len(fname) == 0: fname = 'mbox-short.txt'
fh = open(fname)
distribution_hours_dict = {}
most_committer_count = 0
for line in fh:
    if not line.startswith("From "):
        continue
    distributor = line.rstrip().split()[1]
    distribution_time = line.rstrip().split()[5]
    distribution_hour = distribution_time.split(':')[0]
    distribution_hours_dict[distribution_hour] = distribution_hours_dict.get(distribution_hour, 0) + 1

sorted_list_of_tuples = sorted([(k, v) for k, v in distribution_hours_dict.items()])
for a, b in sorted_list_of_tuples:
    print a, b
