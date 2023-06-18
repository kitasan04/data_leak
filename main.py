import data_size
import move


def main():
    while True:
        print("What you want to do?") 
        print("(0) Check the data")
        print("(1) Leak or Restore")
        print("(2) Quite")
        opt = input("Opt=")
        print("\n")
        if opt == '0':
            data_size.SelectMode()
        elif opt == '1':
            move.SelectMode()
        elif opt =='2':
            print("Quite!")
            break
        else:
            print("Please input 0 or 1 \n")
            main()


main()
