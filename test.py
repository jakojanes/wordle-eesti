def loe_failist():
    f = open("andmed.txt").read().splitlines()
    return f

def kirjuta_faili(list):
    f = open("andmed.txt", "w")
    for i in list:
        f.write("{}".format(i))
        f.write("\n")

    f.close()
loe_failist()

kirjuta_faili([1,2,3])