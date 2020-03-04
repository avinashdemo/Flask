#import os

#for root, dirs, files in os.walk("."):

#    for file in files:
#        print (*)


#os.listdir(path='.')

#fpath = '/home/ubuntu/flaskapp';

#listOfFiles = getListOfFiles(fpath)


import os

# List all subdirectories using os.listdir
basepath = '/home/ubuntu/flaskapp'
for entry in os.listdir(basepath):
    if os.path.isdir(os.path.join(basepath, entry)):
        print(entry)


