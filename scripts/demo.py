"""
 * @author yzlin
 * @email thomas7892009@gmail.com
 * @create date 2021-08-21 17:20:36
 * @modify date 2021-08-22 16:12:54
 * @desc auto operation, support script
"""
from libs.handler import Handler
from libs.translator import Translator
from pathlib import Path
import os

DEFAULT_SCRIPT = "autoScript.txt"

action = [
    "Simple Type",
    "Read Script"
]

simple_type = [
    "Full process",
    "Type with current settings",
    "Change Settings",
    "Show settings",
    "Save current settings",
    "Load formor settings",
    "Back."
]

read_script = [
    f"Default script name ({DEFAULT_SCRIPT})",
    "Enter script name",
    "Show avalible",
    "Back."
]

def print_list(l: list):
    for index, i in enumerate(l):
        print(f"({index}) {i}")

# get integer, with exception handle
def get_selection(s: int, l: int) -> int:
    while True:
        try:
            a = int(input(f"({s}~{l}): "))
            if a >= s and a <= l:
                return a
            else:
                raise ValueError
        except ValueError:
            print(f"({s}~{l})")

def main():
    h = Handler()
    t = Translator()
    
    # main interface
    try:
        while True:
            print("@@'ctrl'+'c' to end@@")
            print_list(action)
            act = get_selection(0, len(action)-1)
            os.system("cls")
            # simple type
            if act == 0:
                while True:
                    print("@@'ctrl'+'c' to end@@")
                    print_list(simple_type)
                    act = get_selection(0, len(simple_type)-1)
                    if act == 0:
                        h.get_mouse_pos()
                        h.read_message()
                        h.type_to_pos()
                    elif act == 1:
                        h.type_to_pos()
                    elif act == 2:
                        h.change_setting()
                    elif act == 3:
                        h.now_info()
                    elif act == 4:
                        h.save_to_file()
                    elif act == 5:
                        h.load_from_file()
                    elif act == 6:
                        os.system("cls")
                        break
            # Read Script
            elif act == 1:
                while True:
                    print("@@'ctrl'+'c' to end@@")
                    print_list(read_script)
                    act = get_selection(0, len(read_script)-1)
                    script_file = DEFAULT_SCRIPT
                    if act == 0 or act == 1:
                        if act == 1:
                            script_file = input("Enter file name: ")
                        try:
                            with open(script_file, "r", encoding="utf-8") as fp:
                                s = fp.read()
                                t.parse(s)
                        except FileNotFoundError:
                            print(f"can't find {script_file}")
                    elif act == 2:
                        for i in Path().iterdir():
                            print(i)
                    elif act == 3:
                        os.system("cls")
                        break
    except KeyboardInterrupt:
        print("End.")
        return


if __name__ == "__main__":
    main()