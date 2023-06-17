import os
import glob
import shutil
import random
# put your data directory path
dir_path = ''


def move(N=10):
    class_dirnames = glob.glob(dir_path+'test/*')
    move_paths = []
    for class_dirname in class_dirnames:
        paths = glob.glob(class_dirname+'/*')
        choice_paths = random.sample(paths, N)
        for choice_path_old in choice_paths:
            choice_path_new = choice_path_old.replace('test/', 'train/')
            shutil.move(choice_path_old, choice_path_new)
            move_path = choice_path_new.replace(dir_path, '')
            move_paths.append(move_path)
    txts = ''
    with open(dir_path+'move_paths.txt') as f:
        txts += f.read()
    with open(dir_path+'move_paths.txt', 'w') as f:
        for move_path in move_paths:
            move_path += '\n'
            txts += move_path
        f.write(txts)


def moveback():
    pass_paths = []
    with open(dir_path+'move_paths.txt') as f:
        names = f.readlines()
        for name in names:
            path_old = name.replace("\n", "")
            path_new = path_old.replace("train/", "test/")
            if os.path.exists(dir_path+path_old):
                shutil.move(dir_path+path_old, dir_path+path_new)
            else:
                pass_paths.append(path_old)
    with open(dir_path+'move_paths.txt', 'w') as f:
        txts = ''
        for pass_path in pass_paths:
            pass_path += '\n'
            txts += pass_path
        f.write(txts)


def SelectMode(seed=42):
    random.seed(seed)
    print("Select Mode")
    print("(0) Change the seed value from "+str(seed))
    print("(1) Move N pieces of each class")
    print("(2) Restore the data set to its original state")
    print("(3) Quite")
    mode = input("mode=")
    if mode == '0':
        seed = int(input('seed='))
        print("Done!\n\n")
        SelectMode(seed)
    elif mode == '1':
        N = int(input('N='))
        if 77 < N:
            return
        move(N)
        print("Done!\n\n")
        return
    elif mode == '2':
        moveback()
        print("Done!\n\n")
        return
    elif mode == '3':
        print("Quite!\n\n")
        return
    else:
        print("Please input 0~3\n\n")
        SelectMode(seed)


SelectMode()
