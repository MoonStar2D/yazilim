import os, errno
import shutil
import glob
import  time



def index_containing_substring(the_list, substring):
    for i, s in enumerate(the_list):
        if substring in s:
              return i
    return -1

def sortletter():
    path = os.getcwd() + '\\'
    #path = 'C:\\Users\\2dgam\\Desktop\\world flags\\country flags europe\\library\\flags\\'


    anims = glob.glob(path +'*.png')

    directories = os.walk(path).next()[1]
    comparison_list = [item.lower() for item in directories]

    for i, x in enumerate(anims):
        basedir, filename = os.path.split(x)

        #print basedir
        #print filename[:1]

        index = index_containing_substring(comparison_list,filename[:1])

        source_path = os.path.join(basedir,filename)
        destination_path =  basedir + '\\' + directories[index] + '\\' + filename

        print destination_path

        shutil.move(source_path, destination_path)
        print 'moving file success'



if __name__ == "__main__":
    #shutil.move('C:/Users/2dgam/Desktop/world flags/country flags europe/library/flags/F -', 'C:/Users/2dgam/Desktop/world flags/country flags europe/library/flags/F -/france.png')
    print '___________ SORT PNG BY LETTER ___________\n\n'
    start = time.time()
    # call your code here
    sortletter()
    end = time.time()
    print('\nFinished in : ' + str(end - start) + 's')

    k = input('Done.\n\nPress any key to close.')