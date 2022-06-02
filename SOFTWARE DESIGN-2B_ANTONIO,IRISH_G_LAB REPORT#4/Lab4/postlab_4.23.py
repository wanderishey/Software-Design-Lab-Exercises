from os import listdir
from os.path import isfile, join

def find(path, filename):
    for f in listdir(path):
        if isfile(join(path, f)):
            if filename in f:
                print(f)
            else:
                find(join(path, f), filename)
find(r'''C:/Users/Irish/Downloads/FEC_Books''', "pdf")
find(r'''C:/Users/Irish/Desktop/Laboratory_SD/Laboratory/Lab4''', ".py")