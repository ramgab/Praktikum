import os
import sys
import shutil 

path = "C:/Users/User/Documents/workDir" 

os.chdir(path) #Переместимся в папку workDir, тем самым сделаем ее основной

def makeDir(dirName): #Создание папки
    os.mkdir(path + "/" + dirName)
    print("make dir " + path + "/" + dirName)
    
def removeDir(dirName): #Удаление папки
    os.rmdir(path + "/" + dirName)
    print("remove dir " + path + "/" + dirName)
    
def makeFile(fileName): #Создание файла
    filepath = os.path.join('C:/Users/User/Documents/workDir', fileName)
    f = open(filepath, "a")
    print("make file " + path + "/" + fileName)
    f.close()
    
def removeFile(fileName): #Удаление файла
    filepath = os.path.join('C:/Users/User/Documents/workDir', fileName)
    os.remove(filepath)
    print("remove file " + path + "/" + fileName)
    
def renameFile(fileName, newFileName): #Переименование 
    os.rename(path + "/" + fileName, path + "/" + newFileName)
    print("rename file " + path + "/" + fileName)
    
def textFile(fileName): #Заполнение файла
    filepath = os.path.join('C:/Users/User/Documents/workDir', fileName)
    f = open(filepath, "w")
    text = str(input())
    f.write(text)
    f.close()
    
def readFile(fileName): #Просмотр содержимого текстового файла
    filepath = os.path.join('C:/Users/User/Documents/workDir', fileName)
    f = open(filepath, "r")
    file_contents = f.read()
    print (file_contents)
    f.close()
    
def pathChange(dirName): #Перемещение
    path = (os.getcwd())
    backup = path
    newpath = path + "/" + str(dirName)
    path = newpath
    os.chdir(path)
    print(os.getcwd())
    
def movingFiles(fileName, dirName): #Перемещение файла в другую папку
    filepath = path + "/" + dirName + "/" + fileName
    os.replace(fileName, filepath)
    
def copyFile(fileName, copyPath): #Копирование файла в другую папку
    copyPath = path + "/" + copyPath
    shutil.copyfile(path + '/' + fileName, copyPath)
    
while True:
    command = input("Введите команду: ")
    command = command.split(' ')
    if command[0] == "exit": #Выход
        sys.exit()
    elif command[0] == "makeDir": #Создание папки
        makeDir(command[1])
    elif command[0] == "removeDir": #Удаление папки
        removeDir(command[1])
    elif command[0] == "makeFile": #Создание файла
        makeFile(command[1])
    elif command[0] == "removeFile": #Удаление файла
        removeFile(command[1])
    elif command[0] == "renameFile": #Переименование
        renameFile(command[1], command[2])
    elif command[0] == "textFile": #Запись текста в файл
        textFile(command[1])
    elif command[0] == "readFile": #Просмотр содержимого текстового файла
        readFile(command[1])
    elif command[0] == "pathChange":
        pathChange(command[1])
    elif command[0] == "movingFiles": #Перемещение файла в другую папку
        movingFiles(command[1], command[2])
    elif command[0] == copyFile: 
        copyFile(command[1], command[2])
