from os import name
import sys
from libs.translator import Translator

def border(time: int):
    s = ""
    for i in range(time):
        s += "@"
    return s

def controller(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as fp:
            f = fp.read()
            t = Translator()
            t.parse(f)
    except FileNotFoundError:
        sys.stderr.write(f"Can't find {file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write(f"Wrong on argument\nThere are {len(sys.argv)} (need 2)")
    else:
        print(f"\n{border(5)}controller start.{border(5)}")
        controller(sys.argv[1])
        print(f"{border(6)}controller end.{border(6)}") 