# Auto Type to Screen
- Automatically work on computer
- Script base


## Required Python Module
- re
- time
- pyautogui
- pyperclick
- os (flush CLI, Path)




# Auto Script
![show](https://github.com/lyz508/Auto-Operation-on-Computer/blob/master/resources/autoOpration_script.gif)
## System cmd:
```
<CMD> <sec or space>;
```
- commands for interpreter
1. **pause**
2. **gain_mouse_l**
3. **gain_mouse**
4. **gain_string**
## Mouse cmd:
```
<CMD> <x>, <y>;
```
- commands for mouse function
- Must provide **X, Y**.
1. **click**
2. **move_to**
## Keyboard cmd:
1. **press**
    ```
    press <key or specific word>
    # ex
    press enter;
    ```
    - specific word: 'enter', 'ctrl'
2. **hotkey**: for combinational key press
    ```
    hotkey <key1> <key2>
    # ex
    hotkey ctrl, c;
    ```
3. **write**: for input on keyboard
    ```
    write meg=<messages>;
    # ex
    write meg=Hello World!!!;
    ```
    - if want to input several lines, leave empty on meg, then a function will be executed to accept the article.
# Simple Type
- Basic use of auto click and input
![full_process](https://github.com/lyz508/Auto-Operation-on-Computer/blob/master/resources/autoType_full_process.gif)
- Type to specified position
- can set loop **times, interval, character** between loop.


# Manual
- Choose Mode:
    1. Simple Type      
    2. Read Script
## Simple Type
0. Full process
    - Specified -> Input Message -> Type
1. Type with current settings
2. Change Settings
3. Show settings
4. Save current settings
    - default file name: setting.txt
5. Load formor settings
6. Back.
## Script
- Read Script File
0. Default script name (autoScript.txt)
1. Enter script name
2. Show avalible
    - show avalible files in current directory
3. Back.


# Update & Schedule
## Update
### 2021.8.22
- Complete a simple intepreter, which can deal with commands about mouse action and keyboard action.
- Change repository name: **AutoTypeToScreen** -> **Auto-Operation-on-Computer**
- Update detailed README

## Schedule
### ~~Update Record function~~
- scheduled date: 2021.8.21
- Will be able to record the actions
- can afford complex work
- **Complete: 2021.8.22**
### Loop Support
- scheduled date: 2021.8.22
- Will support loop in scripts
### Combinational & Coordination on commands
- scheduled date: 2021.8.22
- will support mouse drag
### Multiple on Write Input
- scheduled date: 2021.8.22
- Problem:
    - when using repr(), colon wont be specified by re expression
    - using temp solution -> call handler function (read_message())
- Expected Solution
    - Optimized re exp.