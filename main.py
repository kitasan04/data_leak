import data_size
import move


def main():
    print("What you want to do?")
    print("(0) Check the data")
    print("(1) Leak or Restore")
    opt = input("Opt=")
    print("\n")
    if opt == '0':
        data_size.SelectMode()
    elif opt == '1':
        move.SelectMode()
    else:
        print("Please input 0 or 1 \n")
        main()


main()
