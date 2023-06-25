import os
import glob
import shutil
import random
from sklearn.model_selection import train_test_split
# put your data directory path


def move(dir_path,N=10):
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
    with open('texts/move_paths.txt') as f:
        txts += f.read()
    with open('texts/move_paths.txt', 'w') as f:
        for move_path in move_paths:
            move_path += '\n'
            txts += move_path
        f.write(txts)


def excute_classname_from_path(path):
    return '/'.join(path.split('/')[:-1])


def train_val_split(dir_path,val_p, seed):
    file_paths = glob.glob(dir_path+"train/**/**")
    class_paths = list(map(excute_classname_from_path, file_paths))
    train_paths, val_paths, train_labels,  val_labels = train_test_split(
        file_paths,
        class_paths,
        shuffle=True,
        test_size=val_p,
        random_state=seed,
        stratify=class_paths
    )
    for i in range(len(val_paths)):
        val_path_old = val_paths[i]
        val_paht_new = val_path_old.replace('train/', 'val/')
        val_label = val_labels[i].replace('train/', 'val/')
        shutil.move(val_path_old, val_paht_new)


def move_leak(dir_path,N=10):
    class_dirnames = glob.glob(dir_path+'test/*')
    move_paths = []
    for class_dirname in class_dirnames:
        paths = glob.glob(class_dirname+'/*')
        choice_paths = random.sample(paths, N)
        for choice_path_old in choice_paths:
            choice_path_new = choice_path_old.replace('test/', 'leak/')
            shutil.move(choice_path_old, choice_path_new)
            move_path = choice_path_new.replace(dir_path, '')
            move_paths.append(move_path)
    txts = ''
    if os.path.exists('texts/leak_paths.txt'):
        with open('texts/leak_paths.txt') as f:
            txts += f.read()
    with open('texts/leak_paths.txt', 'w') as f:
        for move_path in move_paths:
            move_path += '\n'
            txts += move_path
        f.write(txts)


def moveback(dir_path):
    pass_paths = []
    with open('texts/move_paths.txt') as f:
        names = f.readlines()
        for name in names:
            path_old = name.replace("\n", "")
            path_new = path_old.replace("train/", "test/")
            if os.path.exists(dir_path+path_old):
                shutil.move(dir_path+path_old, dir_path+path_new)
            else:
                pass_paths.append(path_old)
    with open('texts/move_paths.txt', 'w') as f:
        txts = ''
        for pass_path in pass_paths:
            pass_path += '\n'
            txts += pass_path
        f.write(txts)


def moveback_leak(dir_path):
    pass_paths = []
    with open('texts/leak_paths.txt') as f:
        names = f.readlines()
        for name in names:
            path_old = name.replace("\n", "")
            path_new = path_old.replace("leak/", "test/")
            if os.path.exists(dir_path+path_old):
                shutil.move(dir_path+path_old, dir_path+path_new)
            else:
                pass_paths.append(path_old)
    with open('texts/leak_paths.txt', 'w') as f:
        txts = ''
        for pass_path in pass_paths:
            pass_path += '\n'
            txts += pass_path
        f.write(txts)


def moveback_val(dir_path):
    paths = glob.glob(dir_path+'val/**/**')
    for path in paths:
        path_old = path
        path_new = path.replace('val/', 'train/')
        shutil.move(path_old, path_new)


def SelectMode(dir_path,seed=42):
    random.seed(seed)
    print("Select Mode")
    print("(0) Change the seed value from "+str(seed))
    print("(1) Move N pieces of each class from test")
    print("(2) Restore the data")
    print("(3) Split train data into train data and val data")
    print("(4) Quite")
    mode = input("mode=")
    print("\n")

    if mode == '0':
        seed = int(input('seed='))
        print("Done!\n")
        SelectMode(dir_path,seed)

    elif mode == '1':
        print("Move N pieces of each class from test")
        print("Select where to move the data")
        print("(0) to train")
        print("(1) to leak")
        print("(2) Quite")
        destination = input("destination=")
        if destination == '2':
            print("Quite!\n")
            SelectMode(dir_path,seed)
            return
        try:
            N = int(input('N='))
        except TypeError:
            print('Please input integer!\n')
            SelectMode(dir_path,seed)
        if 77 < N:
            print(
                'Please input the number less than the smallest class in the test data!\n')
            SelectMode(dir_path,seed)
        if destination == '0':
            move(dir_path,N)
            print("Done!\n")
            return
        elif destination == '1':
            move_leak(dir_path,N)
            print("Done!\n")
            return
        else:
            print("Please input 0~2\n")
            SelectMode(dir_path,seed)

    elif mode == '2':
        print("Restore the data set to its original state")
        print("Select the source of the move")
        print("(0) from train")
        print("(1) from leak")
        print("(2) from val")
        print("(3) Quite")
        source = input("source=")
        if source == '0':
            moveback(dir_path)
            print("Done!\n")
            return
        elif source == '1':
            moveback_leak(dir_path)
            print("Done!\n")
            return
        elif source == '2':
            moveback_val(dir_path)
            print("Done!\n")
            return
        elif source == '3':
            print("Quite!\n")
            SelectMode(dir_path,seed)
            return
        else:
            print("Please input 0~3\n")
            SelectMode(dir_path,seed)

    elif mode == '3':
        try:
            val_p = float(input('percentage of validation data='))
        except TypeError:
            print('Please input decimals!\n')
            SelectMode(dir_path,seed)
        if not(0 < val_p < 1):
            print(
                'Please input the percentage of validation data as a value between 0 and 1!\n')
            SelectMode(dir_path,seed)
        train_val_split(dir_path,val_p, seed)
        print("Done!\n")
        return
    elif mode == '4':
        print("Quite!\n")
        return
    else:
        print("Please input 0~4\n")
        SelectMode(dir_path,seed)
