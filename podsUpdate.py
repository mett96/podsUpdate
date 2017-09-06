# creato da Mattia Sanchioni

import os

def update():
    os.system("pod update")


#print os.path.dirname(os.path.realpath(__file__))

print "\ntrascina la cartella"                # la cartella nel nome non puo' contenere i caratteri '\' e '/'

directory = raw_input()
directory = directory.replace("\ ", " ")    # rimuove il carattere "\" che viene associato al " "
directory = directory[:-1]                  # rimuove l'ultimo carattere, perche' quando si trascina inserisce uno spazio
#print directory

os.chdir(directory)

folders = os.listdir(directory)
#print folders

#controlla se la cartella trascinata contiene il file Podfile

find = False

for folder in folders:
    if folder == "Podfile":
        find = True

# se lo trova lo aggiorna
if find:
    update()

# se non lo trova la cartella conteneva diversi progetti e li aggiorna tutti
else:
    for folder in folders:
        #print folder
        if folder == ".DS_Store":
            continue
        else:
            print "\n\n" + "*"*50 + "\n\n"
            print("Vuoi aggiornare " + folder + "? \t [Y/n]")
            choose = raw_input()

            if choose == "":
                choose = "Y"

            while not choose.isalpha :
                print("Vuoi aggiornare " + folder + "? \t [Y/n]")
                choose = raw_input()

            choose = (choose.upper())[0]

            if choose == "Y":
                #print directory + folder
                os.chdir(directory + "/" + folder)
                update()
                os.chdir(directory)
