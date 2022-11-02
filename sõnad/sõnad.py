


from string import punctuation


sõnad = open("sõnad\lemmad.txt","r").read().splitlines()

tähed4 = []
tähed5 = []
tähed6 = []



for i in sõnad:

        if len(i) == 4:
            tähed4.append(i.lower())
        elif len(i) == 5:
            tähed5.append(i.lower())
        elif len(i) == 6:
            tähed6.append(i.lower())


with open("sonad4.txt", 'w', encoding="utf-8") as fp:
    for item in tähed4:
        # write each item on a new line
        fp.write("%s\n" % item)


with open("sonad5.txt", 'w', encoding="utf-8") as fp:
    for item in tähed5:
        # write each item on a new line
        fp.write("%s\n" % item)


with open("sonad6.txt", 'w', encoding="utf-8") as fp:
    for item in tähed6:
        # write each item on a new line
        fp.write("%s\n" % item)

