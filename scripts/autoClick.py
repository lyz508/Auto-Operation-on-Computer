import os
import pyautogui
import time
import pyperclip

class Handler:
    def __init__(self):
        self.p = pyautogui.Point(0, 0)
        self.m = ""
        self.loop = 3
        self.between_loop = "\n"
        self.t_interval = 2
        

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
            print("Read until \"ctrl+z\" (EOF)")
            try:
                while True:
                    self.m += input(": ") + "\n"
            except EOFError:
                print(f"Want output: {self.m}")
        else:
            self.m = s
            print(f"Want output: {self.m}")


    # Auto type
    def type_to_pos(self):
        print("typing")
        for i in range(self.loop):
            pyautogui.click(self.p.x, self.p.y)
            pyperclip.copy(self.m)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.typewrite(self.between_loop)
            time.sleep(self.t_interval)

    # Current Setting
    def now_info(self):
        print(f"\tloop time: {self.loop}\n\
        between loop: {ord(self.between_loop)}\n\
        time interval: {self.t_interval}")

    # Setter
    def set_m(self, s):
        self.m = s
    def set_loop(self, i):
        self.loop = i
    def set_between_loop(self, c):
        self.between_loop = c
    def set_interval(self, i):
        self.t_interval = i

def main():
    action = [
        "full process",
        "set mouse position",
        "set message",
        "type to specified position",
        "show setting"
    ]

    h = Handler()
    for index, i in enumerate(action):
        print(f"({index}) {i}")
    
    try:
        a = int(input("act: "))
        if a == 0:
            h.get_mouse_pos()
            h.read_message()
            h.type_to_pos()
        elif a == 1:
            h.get_mouse_pos()
        elif a == 2:
            h.read_message()
        elif a == 3:
            h.type_to_pos()
        elif a == 4:
            h.now_info()
        else:
            raise ValueError
    except ValueError:
        print("Please input correctly.")
    time.sleep(1)


if __name__ == "__main__":
    try:
        while True:
            print("ctrl+c to quit")
            main()
    except KeyboardInterrupt:
        print("End.")