from libs.handler import Handler
import time
# import os

def main():
    action = [
        "Full process",
        "Type with current settings",
        "Change Settings",
        "Show settings",
        "Save current settings",
        "Load formor settings"
    ]

    h = Handler()
    try:
        while True:
            for index, i in enumerate(action):
                print(f"({index}) {i}")
            
            try:
                a = int(input("act: "))
                if a == 0:
                    h.get_mouse_pos()
                    h.read_message()
                    h.type_to_pos()
                elif a == 1:
                    h.type_to_pos()
                elif a == 2:
                    h.change_setting()
                elif a == 3:
                    h.now_info()
                elif a == 4:
                    h.save_to_file()
                elif a == 5:
                    h.load_from_file()
                else:
                    raise ValueError
            except ValueError:
                print("Please input correctly.")
            time.sleep(1)
            # os.system("cls")
    except KeyboardInterrupt:
        print("End.")
        return


if __name__ == "__main__":
    main()