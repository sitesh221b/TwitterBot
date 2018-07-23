from functions import *

if __name__ == '__main__':
    exec(open("auth.py").read())

    if api.verify_credentials():
        print("Verification Successful!")
        time.sleep(1)
        print("Starting the Bot...")
        time.sleep(2)

    main_menu()
