import glob
import os
import shutil
import time


class AnimationSorter:
    """A simple sorter class"""

    def __init__(self):
        self.prefix = ''
        self.folders_count = 0
        self.files_count = 0

    def set_prefix(self):
        self.prefix = raw_input('Type in the prefix of the animations.\nPrefix: ')
        #self.prefix = "___character_"
        print self.prefix

    def get_animations(self):
        #path = "C:\Users\\2dgam\Desktop\Rifleman\Animations\\dual eye\\"
        path = os.getcwd() + '\\'
        anims = glob.glob(path + '*.png')
        return anims

    def sortanim(self):

        anims = self.get_animations()

        if not anims:
            print('No files found.')
            return False

        self.files_count = len(anims)

        for i, x in enumerate(anims):

            basedir, filename = os.path.split(x)

            result = x.replace(str(self.prefix), "", 1)
            n = result.split("_", 1)
            result = n[0]
            result = result.translate(None, '_')

            dir_name, ext = os.path.splitext(result)

            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
                print 'new directory: ' + dir_name
                self.folders_count += 1

            try:
                shutil.move(x, dir_name + '\\' + filename)
            except IOError as (errno, strerror):
                print "I/O error({0}): {1}".format(errno, strerror)
            except ValueError:
                print "Could not convert data to an integer."
            except:
                print "Unexpected error:"
                raise

            self.files_count += 1
            # print 'moving file success'

        return True


if __name__ == "__main__":

    print '___________ SORT ANIMATION EXPORTS ___________\n\n'
    sorter = AnimationSorter()

    sorter.set_prefix()

    start = time.time()
    # call your code here

    if sorter.sortanim():
        end = time.time()
        print 'Done.' \
              '\nTotal files: ' + str(sorter.files_count - 1) + \
              '\nTotal Folders: ' + str(sorter.folders_count) + \
              '\nTime needed: ' + str(end - start) + 's'

    k = raw_input('\n\nPress any key to close.\n')
