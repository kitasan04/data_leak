import glob
# put your data directory path
dir_path = ''


def init():
    class_paths = glob.glob(dir_path+'test/**')
    txts = "{:<28s}{:<8s}{:<8s}".format("label", "train", "test")+"\n"
    txts += '-'*50+'\n'
    class_names = []
    for path in class_paths:
        class_names.append(path.replace(dir_path+'test/', ''))
    class_names.sort()
    for class_name in class_names:
        train_amount = len(glob.glob(dir_path+'train/'+class_name+'/*'))
        test_amount = len(glob.glob(dir_path+'test/'+class_name+'/*'))
        txts += "{:<28s}{:<8d}{:<8d}".format(class_name,
                                             train_amount, test_amount)+"\n"
    with open("data_size.txt", 'w') as f:
        f.write(txts)
    with open("move_paths.txt", 'w') as f:
        f.write("")


def show_origin():
    with open('data_size.txt') as f:
        txts = f.read()
        print(txts)


def show_now():
    class_paths = glob.glob(dir_path+'test/**')
    print("{:<28s}{:<8s}{:<8s}".format("label", "train", "test"))
    print('-'*50)
    class_names = []
    for path in class_paths:
        class_names.append(path.replace(dir_path+'test/', ''))
    class_names.sort()
    for class_name in class_names:
        train_amount = len(glob.glob(dir_path+'train/'+class_name+'/*'))
        test_amount = len(glob.glob(dir_path+'test/'+class_name+'/*'))
        print("{:<28s}{:<8d}{:<8d}".format(
            class_name, train_amount, test_amount))


def show_leak_data():
    with open('move_paths.txt') as f:
        print(f.read())


def SelectMode():
    print("Select Mode")
    print("(0) Init data size")
    print("(1) Show original data size")
    print("(2) Show current data size")
    print("(3) Show leak data")
    print("(4) Quite")
    mode = input("mode=")
    if mode == '0':
        init()
        print('Done!\n')
        return
    elif mode == '1':
        show_origin()
        return
    elif mode == '2':
        show_now()
        return
    elif mode == '3':
        show_leak_data()
        return
    elif mode == '4':
        print("Quite!\n")
        return
    else:
        print("Please input 0~3\n")
        SelectMode()
