
name = input ('enter file: ')
hand = open(name)

counts = dict()
for line in hand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bogword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)


list = sorted(lst, reverse = True)

for key, val in lst[:10]:
    print(key, val)
