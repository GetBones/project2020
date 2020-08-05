def pars():
    import os, sys

    path = "/home/kali/"
    dirs = os.listdir(path)
    for file in dirs:
        print(file)
    print()
    def ras(s):
        for i in range(len(s)):
            if s[-i] == '.': return s[-i + 1:]

    return None

    tree = os.walk('/home/kali')

    set_ras = set()

    for i in tree:
        for j in i[2]:
            r = ras(j)
            if not r is None: set_ras.add(r)

    tab = {}

    for i in set_ras: tab[i] = 0

    tree = os.walk('/home/kali/')

    for i in tree:
        for j in i[2]:
            r = ras(j)
            if not r is None: tab[r] += 1
    for i in tab.keys():
        print(i, tab[i])
