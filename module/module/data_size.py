import glob
import os


def init(dir_path):
    class_paths = glob.glob(dir_path+'test/**')
    txts = "{:<28s}{:>8s}{:>8s}{:>8s}{:>8s}".format(
        "label", "train", "val", "test", "leak")+"\n"
    txts += '-'*60+'\n'
    class_names = []
    for path in class_paths:
        class_names.append(path.replace(dir_path+'test/', ''))
    class_names.sort()
    if not(os.path.exists(dir_path+'leak/')):
        os.mkdir(dir_path+'leak/')
    if not(os.path.exists(dir_path+'val/')):
        os.mkdir(dir_path+'val/')
    for class_name in class_names:
        train_amount = len(glob.glob(dir_path+'train/'+class_name+'/*'))
        if not(os.path.exists(dir_path+'val/'+class_name+'/')):
            os.mkdir(dir_path+'val/'+class_name+'/')
        val_amount = len(glob.glob(dir_path+'val/'+class_name+'/*'))
        test_amount = len(glob.glob(dir_path+'test/'+class_name+'/*'))
        if not(os.path.exists(dir_path+'leak/'+class_name+'/')):
            os.mkdir(dir_path+'leak/'+class_name+'/')
        leak_amount = len(glob.glob(dir_path+'leak/'+class_name+'/*'))
        txts += "{:<28s}{:>8d}{:>8d}{:>8d}{:>8d}".format(class_name,
                                                         train_amount, val_amount, test_amount, leak_amount)+"\n"
    if not(os.path.exists('texts')):
        os.mkdir('texts')
    with open("texts/data_size.txt", 'w') as f:
        f.write(txts)
    with open("texts/move_paths.txt", 'w') as f:
        f.write("")


def show_origin():
    with open('texts/data_size.txt') as f:
        txts = f.read()
        print(txts)


def show_now(dir_path):
    class_paths = glob.glob(dir_path+'test/**')
    print("{:<28s}{:>8s}{:>8s}{:>8s}{:>8s}".format(
        "label", "train", "val", "test", "leak"))
    print('-'*60)
    class_names = []
    for path in class_paths:
        class_names.append(path.replace(dir_path+'test/', ''))
    class_names.sort()
    for class_name in class_names:
        train_amount = len(glob.glob(dir_path+'train/'+class_name+'/*'))
        val_amount = len(glob.glob(dir_path+'val/'+class_name+'/*'))
        test_amount = len(glob.glob(dir_path+'test/'+class_name+'/*'))
        leak_amount = len(glob.glob(dir_path+'leak/'+class_name+'/*'))
        print("{:<28s}{:>8d}{:>8d}{:>8d}{:>8d}".format(
            class_name, train_amount, val_amount, test_amount, leak_amount))
    with open('texts/data_size.txt') as f:
        original_train_amount = int(f.readlines()[-1].split()[1])
        print()
        print("{:<15s}{:<8d}{:<15s}".format("test->train",
              int(train_amount-original_train_amount+val_amount), "in each class"))
        print("{:<15s}{:<8d}{:<15s}".format(
            "test->leak", leak_amount, "in eack class"))
        print()


def SelectMode(dir_path):
    print("Select Mode")
    print("(0) Init data size")
    print("(1) Show original data size")
    print("(2) Show current data size")
    print("(3) Quite")
    mode = input("mode=")
    if mode == '0':
        conf = input("Do you really want to initialize it?(yes,no)")
        if conf == 'yes':
            init(dir_path)
            print('Done!\n')
            return
        else:
            print('Didn\'t do it\n')
    elif mode == '1':
        show_origin()
        return
    elif mode == '2':
        show_now(dir_path)
        return
    elif mode == '3':
        print("Quite!\n")
        return
    else:
        print("Please input 0~3\n")
        SelectMode(dir_path)
