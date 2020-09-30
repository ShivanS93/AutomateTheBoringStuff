#! python3

# selectiveCopy.py Program walks through folder tree and searches files ending with .pdf or .jpg into a new folder
# using ./SelectiveCopy/americanFiles as a test

import os, shutil

#function to copy
def copyFormat(folder,fileFormat):

    folder = os.path.abspath(folder)
    print('\nFOLDER to copy...\n %s\n' % folder)
    print(f'Searching for format: \'{fileFormat}\'\n')
    print('FILES to copy:')

    newLocation = folder + '_new'
    if not os.path.exists(newLocation):
        os.mkdir(newLocation)

    # walk the tree
    for folderName, subfolders, filenames in os.walk(folder):


        for filename in filenames:

            if filename.endswith(fileFormat):
                fileToCopy = folderName + '\\' + filename
                print('filename: %s' % fileToCopy)
                shutil.copy(fileToCopy, newLocation + '\\' + filename)

    print('\nFILES copied to...\n%s\n' % newLocation)


def main():
    # select file formats
    fileFormat = '.txt'
    path_ = r'Chapter9\SelectiveCopy\americanFiles'
    pathToCopy = os.path.join(os.getcwd(), path_)

    print(pathToCopy)

    copyFormat(pathToCopy, fileFormat)

if __name__ == '__main__':
    main()