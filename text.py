filename = input("entrez le nom du fichier texte : ")
file = open(filename, "r")
tab=list()
for line in file:
    print(line)
    tab.append(line)
file.close()
i = int()
i = len(tab) - 2
print("la dernière ligne du fichier nommée {filetext}, est : {world}.".format(filetext=filename, world=tab[i]))
