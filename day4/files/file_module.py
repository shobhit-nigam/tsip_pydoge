import os
class File:
    def __init__(self, f):
        self.file = f
        if not os.path.exists(self.file):
            print("file not found, defaulting to None")
            print("please do not use class methods")

    def read_column(self, col):
        with open(self.file, "r") as fa: 
            stra = fa.read()

        lista = stra.splitlines()

        listc = []

        for line in lista:
            listc.append(line.split()[col])
        return listc
    
    def read_int_column(self, col):
        with open(self.file, "r") as fa: 
            stra = fa.read()
        
        lista = stra.splitlines()

        listc = []

        for line in lista:
            temp = line.split()
            if temp[col].isdigit():
                listc.append(int(temp[col]))
            else:    
                print("type of column non integer, written empty list")
                return []
        return listc