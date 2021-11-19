FUNCS = ['exit[', 0, 'log[', 1, 'setvar[', 2, 'getvar[', 1]
VARS = ['PS1', 'Bulge >>', 'ShouldQuit', 'No', 'pi', 3.141592]

def Error(error):
    print("Error: " + error)

def SetVar(name, value):
    if name in VARS:
        VARS[VARS.index(name) + 1] = value
    else:
        VARS.append(name)
        VARS.append(value)

def GetVar(name):
    try:
        return VARS[VARS.index(name) + 1]
    except ValueError:
        Error("Variable not found")

def IsFunc(line):
    # Does this line have the syntax of a function?
    if len(line) == 0:
        return False
    if line.replace(' ', '')[-1] == ']' and '[' in line:
        pass
    else:
        return False
    # Is the function defined?
    func = -1
    for i in range(0, len(FUNCS), 2):
        if FUNCS[i] in line:
            func = i
    if func == -1:
        Error("Function not found")
        return False
    return True

def Exit():
    SetVar('ShouldQuit', 'Yes')

def Log(string):
    print(string)

def RunFunc(line):
    if FUNCS[0] in line:
        Exit()
    if FUNCS[2] in line:
        Log(4)

# Shell loop
while GetVar('ShouldQuit') == 'No':
    # Print PS1 and get line to interpret
    Line = input(GetVar('PS1'))
    # Is what the user entered a function?
    if IsFunc(Line):
        # Run the function
        RunFunc(Line)