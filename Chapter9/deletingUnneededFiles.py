#! python3
# deletingUnneededFiles.py - Walks through a folder to and finds files over 100MB in size'

import os


def sizeFile(path, size):

    path = os.path.abspath(path) #  ensure file path is absolute
    print(f'Providing list of files above {size/(10 ** 6)} MB in size...\n\n')

    for folderName, subfolders, filenames in os.walk(path):

        for filename in filenames:
            combinedPath = folderName + '\\' + filename
            filenameSize = os.path.getsize(combinedPath) / (10 ** 6) #  filenameSize is in MBs

            if filenameSize > (size/(10 ** 6)):
                print(f'    {combinedPath}  {filenameSize} MBs')

def main():
    #   select file formats
    size = 1000 * (10 ** 6)  #   convert to MB
    pathToFolder = 'C:\\'

    sizeFile(pathToFolder,size)
    return

if __name__ == '__main__':
    main()