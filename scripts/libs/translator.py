import re
import time
import pyautogui
from handler import Handler

# re pattern
sys_cmd = "pause|gain_mouse_l|gain_mouse|gain_string|enter"
mouse_cmd = "click|move_to"
p_cmd = "press"
hot_cmd = "hotkey"
t_cmd = "write"
point = r"(-?\d\d*), (-?\d\d*)"
p_key = r"(\w)"
hot_key = r"(\w\w*), (\w\w*| )"


class Translator:
    def __init__(self) -> None:
        self.cmd = ""
        self.str = ""
        self.sec = 0
        self.point = [0, 0]
        self.press = " "
        self.hotkey = ["", ""]
        self.message = ""   # message are not recommand for placing space in front of colon
        self.parser = re.compile(f"({sys_cmd}) ?(\d*)|({mouse_cmd}) *{point}|({t_cmd}) meg=(.*)|({p_cmd}) {p_key}|({hot_cmd}) {hot_key}\s*;")
    
    def parse(self, s: str):
        h = Handler()

        res = self.parser.findall(s)
        for cmd in res:
            if cmd[0] != "":  # syscall
                self.cmd = cmd[0]
                if cmd[1] != "":
                    self.sec = int(cmd[1])
                print(f"{self.cmd} {self.sec}s")
                if self.cmd == "pause":
                    time.sleep(self.sec)
                elif self.cmd == "gain_mouse_l":
                    t = int(input("time: "))
                    l = []
                    for i in range(t):
                        h.get_mouse_pos()
                        l.append(h.p)
                    print(f"mouse info: {l}")
                elif self.cmd == "gain_mouse":
                    h.get_mouse_pos()
                    print(f"mouse info: {h.p}")
                elif self.cmd == "gain_string":
                    h.read_message()
                    self.message = h.m
                elif self.cmd =="enter":
                    pyautogui.typewrite("\n")
            elif cmd[2] != "":    # mouse cmd
                self.cmd = cmd[2]
                self.point = [int(cmd[3]), int(cmd[4])]
                print(f"{self.cmd} ({self.point[0]}, {self.point[1]})")
            elif cmd[5] != "":    # write cmd
                self.cmd = cmd[5]
                if cmd[6][:-1] != "":
                    self.message = cmd[6][:-1]
                else:
                    print("message is empty.")
                    h.read_message()
                    self.message = h.m
                pyautogui.typewrite(self.message)
                print(f"{self.cmd} meg:'{self.message}'")
            elif cmd[7] != "":    # press cmd
                self.cmd = cmd[7]
                self.press = cmd[8]
                print(f"{self.cmd} '{self.press}'")
            elif cmd[9] != "":    # hot key
                self.cmd = cmd[9]
                self.hotkey = [cmd[10], cmd[11]]
                pyautogui.hotkey(self.hotkey[0], self.hotkey[1])
                print(f"{self.cmd} '{self.hotkey}'")


if __name__ == "__main__":
    t = Translator()
    strrr = "pause 1;\nclick 1, 2;\nwrite meg=ll;\npress k;\nhotkey alt,  ;"
    strr = "gain_mouse;"
    power_toy = "hotkey alt,  ;\nwrite meg=wt;\nenter;"
    res = t.parser.findall(power_toy)
    print(res)
    t.parse(power_toy)