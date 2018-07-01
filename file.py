
words = list()

email = list()
email_id = list()
email_address = list()

target = "mbox-short.txt"





with open(target) as f:
    for line in f.readlines():
        if not line.strip().startswith("From"):
            continue

        line = "tephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

        line[1].split()
        'e'.split()


        line.split()[1]
        ["from" "tephen.marquard@uct.ac.za", "Sat", "Jan", "5", "09:14:16", "2008"][1]

        print(line)
        break

        email_address = line.split()[1]
        username, domain = email_address.split("@")
        print(username, domain, email_address)


fhand = open('mbox-short.txt')

exit()


for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    words = line.split()
    print(lin)
    email = words[1].split('@')
    email_id = email[0]
    email_address = email[1]
    print('email id:', email_id , '// email address:' ,email_address)
