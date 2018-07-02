fname = input('Enter :')
if len(fname) < 1:
    fname = 'mbox-short.txt'
hand = open(fname)

di = dict()
for lin in hand:
    wds = lin.split()

    print(lin)
    for w in wds:
        di[w] = di.get(w,0) + 1

print(di)
