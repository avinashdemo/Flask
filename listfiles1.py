import os

fpath = '/home/ubuntu'


def getfiles(dir):
    filenames = os.listdir(dir)
    for filename in filenames:
        print (filename)


if __name__ == '__main__':

   getfiles(fpath)
