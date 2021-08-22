from io import FileIO
import pyautogui
import time
import pyperclip
import json

# Simple func for y\n input
def getyn():
    while True:
        d = input("(y/n): ")
        if d == "y":
            return True
        elif d == "n":
            return False
        else:
            print("y|n")

class Handler:
    def __init__(self):
        self.p = pyautogui.Point(0, 0)
        self.m = ""
        self.loop = 3
        self.between_loop = "\n"
        self.t_interval = 1
        

    # Keep Showing & Gain mouse position
    def get_mouse_pos(self):
        print("\"ctrl+c\" to end (KeyboardInterrupt)")
        try:
            while True:
                self.p = pyautogui.position()
                print(f"Mouse postion: ({self.p.x}, {self.p.y})")
                time.sleep(0.5)
        except KeyboardInterrupt:
            print(f"Decided Position: ({self.p.x}, {self.p.y})")

    # Store message
    def read_message(self, s: str = ""):
        if s == "":     # ! no outer argument
            self.m = ""
            print("Read until \"ctrl+z\" (EOF)")
            try:
                while True:
                    self.m += input(": ") + "\n"
            except EOFError:
                self.m = self.m[:-1]
                print(f"Want output: {repr(self.m)}")
        else:
            self.m = s
            print(f"Want output: {repr(self.m)}")


    # Auto type
    def type_to_pos(self):
        print("typing")
        try:
            for i in range(self.loop):
                pyautogui.moveTo(self.p.x, self.p.y)
                pyautogui.click(self.p.x, self.p.y)
                time.sleep(0.5)
                pyperclip.copy(self.m)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.typewrite(self.between_loop)
                time.sleep(self.t_interval)
        except pyautogui.FailSafeException:
            print("Setting hasn't be loaded correctly!!")

    # Current Setting
    def now_info(self):
        print(f"\tPosition: ({self.p.x}, {self.p.y}),\n\
        loop time: {self.loop},\n\
        between loop: {repr(self.between_loop)},\n\
        time interval: {self.t_interval},\n\
        output message: {repr(self.m)}")

    # Save current setting
    def save_to_file(self):
        to_write: dict = {
            "loop":self.loop,
            "between_loop":self.between_loop,
            "time_interval":self.t_interval,
            "message":self.m,
            "Position":[self.p.x, self.p.y]
        }
        with open("setting.txt", "w", encoding="utf-8") as fp:
            json.dump(to_write, fp)
        print("Saved.")

    # Read formor setting
    def load_from_file(self):
        data = {}
        with open("setting.txt", "r", encoding="utf-8") as fo:
            data = json.load(fo)
            self.m = data["message"]
            self.loop = int(data["loop"])
            self.between_loop = data["between_loop"]
            self.t_interval = int(data["time_interval"])
            self.p = pyautogui.Point(int(data["Position"][0]), int(data["Position"][1]))
        print("Loaded.")

    # For making changes on setting
    def change_setting(self):
        # mouse pos
        print(f"Want to change mouse position?\n\
            (now is ({self.p.x}, {self.p.y}))")
        if getyn():
            self.get_mouse_pos()
        # message        
        print(f"Want to change message?\n\
            (now is '{repr(self.m)}')")
        if getyn():
            self.read_message()
        # loop repeat
        print(f"Want to change the number of loop?\n\
            (now is {self.loop})")
        if getyn():
            while True:
                try:
                    n = int(input("number: "))
                    self.loop = n
                    break
                except ValueError:
                    print("Wrong")
        # charactor between loop
        print(f"Want to change words/charactor between each loop?\n\
            (now is {repr(self.between_loop)})")
        if getyn():
            s = input(": ")
            self.between_loop = s
        # time interval
        print(f"Want to change the interval?\n\
            (now is {self.t_interval} s)")
        if getyn():
            while True:
                try:
                    n = float(input("number: "))
                    self.t_interval = n
                    break
                except ValueError:
                    print("Wrong")

