import sys
import shutil
import os , csv
def create_folders():
    with open ("students.csv") as file:
        header = next(file)
        csv_reader = csv.reader(file)
        for line in csv_reader:
            if not os.path.exists(line[0]):
                os.mkdir(line[0])
def get_path():
    os.chdir("Tutorials")
    path_tutorial = os.getcwd()
    os.chdir('..')
    os.chdir("Games")
    path_games = os.getcwd()
    os.chdir('..')
    os.chdir("data")
    path_data = os.getcwd()
    os.chdir('..')
    return path_tutorial, path_games, path_data
if __name__ == '__main__':#cual es el archivo principal dentro del packete
    
    lista = os.listdir()
    #print(lista)
    create_folders()
    path1 , path2, path3 = get_path()
    #print(path1)
    #print(path2)
    #print(path3)
    lista2 = os.listdir(path3)
    #print(lista2)
    word = 'game'
    tutorials = 'python'
    for i in lista2:
        if not ('.'in i): #if os.path.isdir(i):
            print(i)
            if word in i.lower():
                #print(i)
                shutil.move(path3 +"/" +i, path2)
                #os.path.join(path2, i)
        if tutorials in i.lower():
            #print('I find: '+i)
            shutil.move(path3 +"/" +i, path1)
    #print(enter_data())
    
    