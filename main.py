from module import data_size, move
import os


def data_path_init(data_dir):
    print(f"data directory path = {data_dir}")
    dir_path_change = input(
        'Do you want to change the data directory path?(yes,no)')
    if dir_path_change == 'yes':
        data_dir = input('data path =')
        with open('texts/data_dir.txt','w') as f:
            f.write(data_dir)
    print('\n')
    return data_dir


def main(data_dir='./'):
    if not(os.path.exists('texts')):
        os.mkdir('texts')
    if not(os.path.exists('texts/data_dir.txt')):
        print('Data path needs to be set')
        data_dir = data_path_init(data_dir)
        with open('texts/data_dir.txt', 'w') as f:
            f.write(data_dir)
    else:
        with open('texts/data_dir.txt') as f:
            data_dir = f.read()
    while True:
        print("What you want to do?")
        print(f"(0) Change the data path(data_path={data_dir})")
        print("(1) Check the data")
        print("(2) Leak or Restore")
        print("(3) Quite")
        opt = input("Opt=")
        print("\n")
        if opt == '0':
            data_dir = data_path_init(data_dir)
        elif opt == '1':
            data_size.SelectMode(data_dir)
        elif opt == '2':
            move.SelectMode(data_dir)
        elif opt == '3':
            print("Quite!")
            return
        else:
            print("Please input 0~3 \n")


main()
