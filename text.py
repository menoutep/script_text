filename = input("entrez le nom du fichier texte : ")
file = open(filename, "r")
tab=list()
for line in file:
    print(line)# cette ligne permet d'afficher chaque ligne du fichier texte si vous ne desiserz pas afficher le fichier texte, supprimez simplement cette ligne  
    tab.append(line)
file.close()
i = int()
i = len(tab) - 2
print("la dernière ligne du fichier nommée {filetext}, est : {world}.".format(filetext=filename, world=tab[i]))
