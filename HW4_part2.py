# Phong Nguyen
# CPTS355
# TESTED ON WINDOWS 10 x64

import re

# -----------------Part 1----------------
# The operand stack
opstack = []


# now define functions to push and pop values on the opstack (i.e, add/remove
# elements to/from the end of the Python list)
# Recall that `pass` in python is a no-op: replace it with your code.
def empty(x):  # Check if argument list is empty
    if len(x) == 0:
        return True
    else:
        return False


def opPop():
    if (empty(opstack)):
        print("Error empty list")
    else:
        return opstack.pop()


def opPush(value):  # Pushes value onto list. If it detects a varaible, it will search dictstack for value
    if (type(value) == str):
        if (value[0] != '/'):
            r = lookup(value)
            if (r != None):
                for i in dictstack:
                    if (i.get(value) != None):
                        opstack.append(i[value])
            else:
                print("Variable not defined in dictstack")
            return
    opstack.append(value)


# Remember that there is a Postscript operator called "pop" so we choose
# different names for these functions.


# -------------------------- 20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations

dictstack = []


# now define functions to push and pop dictionaries on the dictstack, to define
# name, and to lookup a name

def dictPop():  # pops top of the dictstack
    if (empty(dictstack)):
        print("Error empty stack")
    else:
        return dictstack.pop()


# dictPop pops the top dictionary from the dictionary stack.

def dictPush(d):
    dictstack.append(d)


# dictPush pushes the dictionary ‘d’ to the dictstack. Note that, your
# interpreter will call dictPush only when Postscript “begin” operator is called.
# “begin” should pop the empty dictionary from the opstack and push it onto the
# dictstack by calling dictPush.

def define(name, value):  #Defines a variable and pushes it to dictstack
    if (empty(dictstack)):
        d = {}
        d[name[1:]] = value  # Removes the '/' character
        dictstack.append(d)
    elif (dictstack[-1].get(name[1:]) != None):  # Checks if variable is already on dictstack of the top dictionary
        dictstack[-1][name[1:]] = value
    else:
        dictstack[len(dictstack) - 1][name[1:]] = value


# add name:value pair to the top dictionary in the dictionary stack. Your psDef
# function should pop the name and value from operand stack and call the “define”
# function.

def lookup(name):  #Finds the variable name on dictstack and returns the value. If not there, it returns None
    if (not empty(dictstack)):
        for i in reversed(dictstack):
            r = i.get(name)
            if (r != None):
                return r
    print("Not found in dictionary stack")


# return the value associated with name
# What is your design decision about what to do when there is no definition for
# “name”? If “name” is not defined, your program should not break, but should
# give an appropriate error message.

# --------------------------- 10% -------------------------------------
# Arithmetic operators: define all the arithmetic operators here --
# add, sub, mul, div, mod
def add():
    global opstack
    if (len(opstack) < 2):
        print("error, stack is too small")
    else:
        a = opPop()
        b = opPop()
        if (type(a) == int or type(a) == float or type(b) == int or type(b) == float):
            opPush(b + a)
            return
        opPush(b)
        opPush(a)
        print("Type error")


def sub():
    global opstack
    if (len(opstack) < 2):
        print("error, stack is too small")
    else:
        a = opPop()
        b = opPop()
        if (type(a) == int or type(a) == float or type(b) == int or type(b) == float):
            opPush(b - a)
            return
        opPush(b)
        opPush(a)
        print("Type error")


def mul():
    global opstack
    if (len(opstack) < 2):
        print("error, stack is too small")
    else:
        a = opPop()
        b = opPop()
        if (type(a) == int or type(a) == float or type(b) == int or type(b) == float):
            opPush(b * a)
            return
        opPush(b)
        opPush(a)
        print("Type error")


def div():
    global opstack
    if (len(opstack) < 2):
        print("error, stack is too small")
    else:
        a = opPop()
        b = opPop()
        if (type(a) == int or type(a) == float or type(b) == int or type(b) == float):
            opPush(b / a)
            return
        opPush(b)
        opPush(a)
        print("Type error")


def mod():
    global opstack
    if (len(opstack) < 2):
        print("error, stack is too small")
    else:
        a = opPop()
        b = opPop()
        if (type(a) == int or type(a) == float or type(b) == int or type(b) == float):
            opPush(b % a)
            return
        opPush(b)
        opPush(a)
        print("Type error")


# Make sure to check the operand stack has the correct number of parameters and
# types of the parameters are correct.

# --------------------------- 15% -------------------------------------
# Array operators: define the array operators
# length, get
def length():  #Pushes length of the array
    if (empty(opstack)):
        print("Error Empty Stack. No Array to evaluate")
    else:
        a = opPop()
        if (type(a) == list):
            opPush(len(a))
        else:
            print("Type Error")
            opPush(a)


def get():
    if (empty(opstack)):  # Error Handling
        print("Error Empty Stack")
    else:
        index = opPop()
        arr = opPop()
        if (type(index) == int and type(arr) == list):
            opPush(arr[index])  # Pushes the value at array index to stack
        else:  # Error Handling
            print('Type Error')
            opPush(arr)
            opPush(index)


# --------------------------- 25% -------------------------------------
# Define the stack manipulation and print operators:
# dup, exch, pop, roll, copy, clear, stack

def dup():  #Duplicates the top value
    if (empty(opstack)):
        print("Error Empty Stack")
    else:
        d = opPop()
        opPush(d)
        opPush(d)


def exch():  # Exchanges the top two values
    if (empty(opstack)):
        print("Error Empty Stack")
    else:
        a = opPop()
        b = opPop()
        opPush(a)
        opPush(b)


def pop():
    if (empty(opstack)):
        print("Error Empty Stack")
    else:
        opstack.pop()


def roll():
    global opstack  # Without this, python will assume I am using a local opstack variable
    if (len(opstack) < 3):
        print("Error Stack too small")
    else:
        a = opPop()  # iterator
        b = opPop()  # index
        if (type(a) != int or type(b) != int or b > len(opstack)):
            print("Error in index, type, or iterator")
            opPush(b)
            opPush(a)
            return
        elif (a == 0 or b == 0):
            return
        if (a > 0):  # Clockwise rotation
            while (a > 0):
                c = opstack.pop()
                if(b-1 == len(opstack)):  # If index is bottom of the stack
                    opstack = [c] + opstack[0:]
                else:
                    opstack = opstack[0:b - 2] + [c] + opstack[b - 2:]
                a -= 1
        else:  # CounterClockwise Rotation (b is negative)
            a = -a
            while (a > 0):
                c = opstack.pop(b - 1)
                opstack = [c] + opstack
                a -= 1

def copy():  # Copy takes a single int value and uses that number to determine the number of copies
    if (empty(opstack)):
        print("Error Empty Stack")
    else:
        iter = opstack.pop()
        if (iter > len(opstack) or iter < 0):  # Error Handling
            print("error")
            opPush(iter)
            return
        l = []
        while iter > 0:
            l.append(opPop())
            iter -= 1
        l += l  # Repeats the values in list
        for i in reversed(l):  # Pushes back the copied values in the right order
            opPush(i)


def clear():  # Clears opstack and dictstack
    global opstack
    global dictstack
    opstack = []
    dictstack = []


def stack():  # Prints the operator stack
    for i in reversed(opstack):
        print(i)


# --------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in
# Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and
# call your own "define" operator (pass those values as parameters). Note that
# psDef()won't have any parameters.

def psDict():
    pop()
    opPush({})


def psDef():
    if len(opstack) < 2:
        print("Error Stack too small")
    else:
        a = opPop()
        b = opPop()
        if ((type(b) == str and b[0] == '/') and (type(a) == int or type(a) == float or type(a) == list)):
            define(b, a)
        else:
            print("ERROR TYPE")  # Error Handling


def begin():
    if (empty(opstack)):
        print("Error Empty Stack")
    else:
        dictPush(opPop())


def end():
    if (empty(dictstack)):
        print("Error Empty Stack")
    else:
        dictPop()


# -----------------Part 2--------------------------------




def tokenize(s):
    retValue = re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[[][a-zA-Z0-9_\s!][a-zA-Z0-9_\s!]*[]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]",
                          s)
    return retValue


# print(tokenize("/fact{ 0 dict begin /n exch def 1 n -1 1 {mul} for end } def [1 2 3 4 5] dup 4 get pop length fact sack"))

def checkFloat(s):  # Checks if you can convert from string to float without errors
    try:
        float(s)
        return True
    except Exception:  # Checks for ValueError or TypeError
        return False

def checkInt(s):  # Checks if you can convert from string to int without errors
    try:
        int(s)
        return True
    except Exception:  # Checks for ValueError or TypeError
        return False

def groupHelper(s):  # Checks if string is a int or float and returns the correct value, otherwise return None
    if(checkFloat(s)):
        if(checkInt(s)):
            if(int(s) == float(s)):  #if 6.0 = 6, return 6
                return int(s)
        return float(s)
    else:
        return None

def groupMatching(it):  # Create sub-list for the code arrays
    res = []
    for c in it:
        if c == '}':  # End of code array
            return res
        elif c == '{':
            res.append(groupMatching(it))
            pass
        else:
            if (groupHelper(c) != None):
                res.append(groupHelper(c))
            elif c[0] == '[':  # convert string to list
                arr = []  # string to list
                for x in c:  # Convert all values in list to int
                    if(groupHelper(x) != None):
                        arr.append(int(x))
                res.append(arr)
            else:
                res.append(c)
    return False  # Unmatched brackets


def parse(tokens):
    parsedList = []  # returned list of the parsed tokens
    it = iter(tokens)  #iterator
    for c in it:
        if c == '{':
             rList = groupMatching(it)  #Create sublist
             if (rList == False):  # If Unmatched brackets
                 return False
             parsedList.append(rList)  # Append sublist to parsedList
        elif tokens[0] == '}':  # Checks for unmatched brackets
            return False
        else:
            if(groupHelper(c) != None):  # Checks to see if string can be converted to int or float, returns None, if not
                parsedList.append(groupHelper(c))
            elif c[0] == '[':  # convert string to list
                arr = []
                for x in c:  # Converts all values in list to int. Only can have a array of integers (Rubric)
                    if(groupHelper(x) != None):
                        arr.append(int(x))
                parsedList.append(arr)
            else:
                parsedList.append(c)  # Not a int or list, therefore it should be left as string
    return parsedList


#print(parse(['/fact', '{', '0', 'dict', 'begin', '/n', 'exch', 'def', '1', 'n', '-1', '1', '{', 'mul', '}', 'for', 'end', '}','def', '[1 2 3 4 5]', 'dup', '4', 'get', 'pop', 'length', 'fact', 'stack']))

def interpretHelper(s):  # Checks if list is either a array of integers or a code array
    for x in s:
        if(not checkInt(x)):  # Checks if all values in list is a int. We will only expect arrays of integers (Rubric)
            return False  # Return False if not an array of integers
    return True

def interpret(code):  # code is a code array
    # Dictionaries of all the functions that can be called. If not in this list, then the string must be a variable
    functionsDict = {'begin': begin, 'get': get, 'length': length, 'stack': stack, 'dup': dup, 'exch': exch,
'pop': pop, 'roll': roll, 'copy': copy, 'clear': clear, 'def': psDef, 'lookup': lookup,
'add': add, 'sub': sub, 'mul': mul, 'div': div, 'mod': mod, 'end': end, 'dict': psDict, 'for': psFor}
    for token in code:  # Traverse through list of Postscript code
        if isinstance(token, int) or isinstance(token, float) or isinstance(token, list):  #  Check if token is int, float, or list
            opPush(token)
        elif isinstance(token, str):  # If not above, Token should be a name, function call or variable
            if(token[0] == '/'):  # Checks if token is a name
                opPush(token)
            else:
                x = functionsDict.get(token)  # Searches functionsdict to see if token is a function call
                if(x != None):  # True, if Token is in funtdictionary
                    x()  # Call Function
                else:  # If Token isn't a function call, then it should be a variable
                    x = lookup(token)  # Checks dict stack and returns value of token, otherwise returns None
                    if x != None:  #  True, if x is in dictstack
                        if(type(x) == list):  # Checks whether value of variable token, is a list
                            if(interpretHelper(x)):  # True, if it is a array of integers
                                opPush(x)
                            else:  # Not an array of integers, therefore it is a code array and we must interpret
                                interpret(x)  # Interpret the code array
                        else:  # Token's value is not a list, therefore we should push it on opstack
                            opPush(x)
                    else:
                        print("Not a name, function, or variable --> ERROR")  # Error Handling
        else:
            print("TYPE ERROR")  # Error Handling


def interpreter(s):  # s is a string
    r = parse(tokenize(s))
    if (r == False):
        print("Unmatched Curly Braces --> ERROR")  # Error Handling
        return
    interpret(r)


def psFor():
    if(len(opstack) < 4):
        print("opStack too small --> ERROR")
    else:
        a = opPop()  # Code Array
        b = opPop()  # final
        c = opPop()  # increment
        d = opPop()  # initial
        if(type(a) == list and type(b) == int and type(c) == int and type(d) == int):
            if ((c < 0 and b > d) or (c > 0 and b < d) or (c == 0)):  # Error Handling of a infinite loop
                print("Infinite Loop Error")
                return
            elif (c < 0):  # If increment is a negative
                while d >= b:
                    opPush(d)
                    interpret(a)
                    d += c
            else:  # If increment is positive
                while d <= b:
                    opPush(d)
                    interpret(a)
                    d += c
        else:  #If we get a type error, push back the popped values
            print("TYPE ERROR")
            opPush(d)
            opPush(c)
            opPush(b)
            opPush(a)



# -----------------Part 1 TEST FUNCTIONS-----------------

def testDefine():
    r = True
    define("/a1", 3)
    if lookup("a1") != 3:
        r = False
    define("/a2", 5)
    if lookup("a2") != 5:
        r = False
    define("/a3", 9)
    if lookup("a3") != 9:
        r = False
    define("/a1", 20)
    if lookup("a1") != 20:
        r = False
    if lookup("NotHere") != None:  # Should print, "Not found in dictionary stack", and not crash the program
        r = False
    return r


def testLookup():
    r = True
    opPush("/n1")
    opPush(5)
    psDef()
    if lookup("n1") != 5:
        r = False
    opPush("/n2")
    opPush(10)
    psDef()
    if lookup("n2") != 10:
        r = False
    opPush("/n3")
    opPush(123)
    psDef()
    if lookup("n3") != 123:
        r = False
    opPush("/n4")
    opPush(0)
    psDef()
    if lookup("n4") != 0:
        r = False
    return r


# Arithmatic operator tests
def testAdd():
    r = True
    opPush(4)
    opPush(2)
    add()
    if opPop() != 6:
        r = False
    opPush(5)
    opPush(6)
    add()
    if opPop() != 11:
        r = False
    opPush(10)
    opPush(12)
    add()
    if opPop() != 22:
        r = False
    opPush(3)
    opPush(9)
    add()
    if opPop() != 12:
        r = False
    return r


def testSub():
    r = True
    opPush(12)
    opPush(5.5)
    sub()
    if opPop() != 6.5:
        r = False
    opPush(5)
    opPush(10)
    sub()
    if opPop() != -5:
        r = False
    opPush(20)
    opPush(2)
    sub()
    if opPop() != 18:
        r = False
    opPush(92)
    opPush(93)
    sub()
    if opPop() != -1:
        r = False
    return r


def testMul():
    r = True
    opPush(2.2)
    opPush(5)
    mul()
    if opPop() != 11:
        r = False
    opPush(2)
    opPush(3)
    mul()
    if opPop() != 6:
        r = False
    opPush(9)
    opPush(9)
    mul()
    if opPop() != 81:
        r = False
    opPush(4)
    opPush(7)
    mul()
    if opPop() != 28:
        r = False
    return r


def testDiv():
    r = True
    opPush(10)
    opPush(4)
    div()
    if opPop() != 2.5:
        r = False
    opPush(5)
    opPush(5)
    div()
    if opPop() != 1:
        r = False
    opPush(2)
    opPush(4)
    div()
    if opPop() != 0.5:
        r = False
    opPush(90)
    opPush(10)
    div()
    if opPop() != 9:
        r = False
    return r


def testMod():
    r = True
    opPush(10)
    opPush(3)
    mod()
    if opPop() != 1:
        r = False
    opPush(12)
    opPush(3)
    mod()
    if opPop() != 0:
        r = False
    opPush(21)
    opPush(4)
    mod()
    if opPop() != 1:
        r = False
    opPush(33)
    opPush(7)
    mod()
    if opPop() != 5:
        r = False
    return r


# Array operator tests
def testLength():
    r = True
    opPush([1])
    length()
    if opPop() != 1:
        r = False
    opPush([1, 2])
    length()
    if opPop() != 2:
        r = False
    opPush([1, 2, 3])
    length()
    if opPop() != 3:
        r = False
    opPush([])
    length()
    if opPop() != 0:
        r = False
    return r


def testGet():
    r = True
    opPush([1, 2, 3, 4, 5])
    opPush(1)
    get()
    if opPop() != 2:
        r = False
    opPush([1, 2, 3, 4, 5])
    opPush(0)
    get()
    if opPop() != 1:
        r = False
    opPush([1, 2, 3, 4, 5])
    opPush(3)
    get()
    if opPop() != 4:
        r = False
    opPush([1, 2, 3, 4, 5])
    opPush(2)
    get()
    if opPop() != 3:
        r = False
    return r


# stack manipulation functions
def testDup():
    r = True
    opPush(10)
    dup()
    if opPop() != opPop():
        r = False
    opPush([1, 2, 3])
    dup()
    if opPop() != opPop():
        r = False
    opPush('/a')
    dup()
    if opPop() != opPop():
        r = False
    opPush(2)
    dup()
    if opPop() != opPop():
        r = False
    return r


def testExch():
    r = True
    opPush(1)
    opPush("/x")
    exch()
    if opPop() != 1 and opPop() != "/x":
        r = False
    opPush("/a")
    opPush("/b")
    exch()
    if opPop() != "/a" and opPop() != "/b":
        r = False
    opPush(5)
    opPush(2)
    exch()
    if opPop() != 5 and opPop() != 2:
        r = False
    opPush([1, 2, 3])
    opPush([4, 5, 6])
    exch()
    if opPop() != [1, 2, 3] and opPop() != [4, 5, 6]:
        r = False
    return r


def testPop():
    r = True
    l1 = len(opstack)
    opPush(10)
    pop()
    l2 = len(opstack)
    if l1 != l2:
        r = False
    l1 = len(opstack)
    opPush(11)
    opPush(12)
    pop()
    pop()
    l2 = len(opstack)
    if l1 != l2:
        r = False
    l1 = len(opstack)
    opPush(13)
    opPush(14)
    pop()
    l2 = len(opstack)
    if l1 == l2:
        r = False
    l1 = len(opstack)
    opPush(15)
    pop()
    l2 = len(opstack)
    if l1 != l2:
        r = False
    return r


def testRoll():
    r = True
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(4)
    opPush(3)
    opPush(-2)
    roll()
    if opPop() != 5 and opPop() != 4 and opPop() != 4 and opPop() != 3 and opPop() != 2:
        r = False
    clear()
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(1)
    opPush(2)
    roll()
    if opPop() != 5 and opPop() != 4 and opPop() != 3 and opPop() != 2 and opPop() != 1:
        r = False
    clear()
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(2)
    opPush(-3)
    roll()
    if opPop() != 4 and opPop() != 5 and opPop() != 3 and opPop() != 2 and opPop() != 1:
        r = False
    clear()
    return r


def testCopy():
    r = True
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(3)
    copy()
    if opPop() != 5 and opPop() != 4 and opPop() != 3 and opPop() != 5 and opPop() != 4 and opPop() != 3:
        r = False
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(4)
    copy()
    if opPop() != 5 and opPop() != 4 and opPop() != 3 and opPop() != 2 and opPop() != 5 and opPop() != 4:
        r = False
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(1)
    copy()
    if opPop() != 5 and opPop() != 5 and opPop() != 4 and opPop() != 3 and opPop() != 2 and opPop() != 1:
        r = False
    return r


def testClear():
    r = True
    opPush(11)
    opPush(11)
    opPush(11)
    opPush("/a")
    clear()
    if len(opstack) != 0:
        r = False
    opPush(2)
    opPush(2)
    opPush(2)
    opPush(2)
    opPush(2)
    opPush("/b")
    clear()
    if len(opstack) != 0:
        r = False
    opPush(8)
    opPush("/x")
    opPush("/x")
    opPush("/x")
    opPush("/x")
    clear()
    if len(opstack) != 0:
        r = False
    opPush(10)
    opPush("/x")
    opPush([1, 2, 3])
    clear()
    if len(opstack) != 0:
        r = False
    return r


# dictionary stack operators
def testDict():
    r = True
    opPush(2)
    psDict()
    if opPop() != {}:
        r = False
    opPush(5)
    psDict()
    if opPop() != {}:
        r = False
    opPush(100)
    psDict()
    if opPop() != {}:
        r = False
    return r


def testBeginEnd():
    r = True
    opPush("/q")
    opPush(10)
    psDef()
    opPush({})
    begin()
    opPush("/w")
    opPush(4)
    psDef()
    if lookup("w") != 4:
        r = False
    opPush("/p")
    opPush(13)
    psDef()
    opPush("/u")
    opPush(14)
    psDef()
    if lookup("p") != 13:
        r = False
    if lookup("u") != 14:
        r = False
    return r


def testpsDef():
    r = True
    opPush("/test1")
    opPush(11)
    psDef()
    if lookup("test1") != 11:
        r = False
    opPush("/test2")
    opPush(12)
    psDef()
    if lookup("test2") != 12:
        r = False
    opPush("/test3")
    opPush(13)
    psDef()
    if lookup("test3") != 13:
        r = False
    return r


def testpsDef2():
    r = True
    opPush("/t1")
    opPush(11)
    psDef()
    opPush(1)
    psDict()
    begin()
    if lookup("t1") != 11:
        end()
        r = False
    opPush("/t2")
    opPush(120)
    psDef()
    opPush(1)
    psDict()
    begin()
    if lookup("t2") != 120:
        end()
        r = False
    opPush("/t3")
    opPush(1110)
    psDef()
    opPush(1)
    psDict()
    begin()
    if lookup("t3") != 1110:
        end()
        r = False
    end()
    return r


def main_part1():
    testCases = [('define', testDefine), ('lookup', testLookup), ('add', testAdd), ('sub', testSub), ('mul', testMul),
                 ('div', testDiv), ('mod', testMod), \
                 ('length', testLength), ('get', testGet), ('dup', testDup), ('exch', testExch), ('pop', testPop),
                 ('roll', testRoll), ('copy', testCopy), \
                 ('clear', testClear), ('dict', testDict), ('begin', testBeginEnd), ('psDef', testpsDef),
                 ('psDef2', testpsDef2)]
    # add you test functions to this list along with suitable names
    failedTests = [testName for (testName, testProc) in testCases if not testProc()]
    print(
        "\nYou will notice a lot of prints stating, Not found in dictionary stack. This is normal and part of error handling")
    if failedTests:
        return ('Some tests failed', failedTests)
    else:
        return ('\n\n\nAll part-1 tests OK\n\n\n')


print(main_part1())  # Calls all of the test functions from part 1. If any test were to fail, it will print a fail message


# -----------------Part 2 TEST FUNCTIONS-----------------

def testFor():
    r = True
    clear()
    opPush(1)
    opPush(1)
    opPush(3)
    opPush([10, 'mul'])
    psFor()
    if(opPop() != 30 or opPop() != 20 or opPop() != 10):
        r = False
    clear()
    opPush(1)
    opPush(1)
    opPush(5)
    opPush(['dup'])
    psFor()
    if (opPop() != 5 or opPop() != 5 or opPop() != 4 or opPop() != 4 or opPop() != 3):
        r = False
    clear()
    opPush(12)
    opPush(1)
    opPush(1)
    opPush(5)
    opPush(['add'])
    psFor()
    if (opPop() != 27):
        r = False
    clear()
    opPush(20)
    opPush(5)
    opPush(-1)
    opPush(0)
    opPush(['sub'])
    psFor()
    if(opPop() != 5):
        r = False
    return r


def testTokenize():
    r = True
    s = tokenize("/test 2 def 1 2 3 4 5 /n { 0 mul } def [1 2 3 4 5]")
    if (s != ['/test', '2', 'def', '1', '2', '3', '4', '5', '/n', '{', '0', 'mul', '}', 'def', '[1 2 3 4 5]']):
        r = False
    s = tokenize("[1 2 3 4 5] 1 a b c d")
    if (s != ['[1 2 3 4 5]', '1', 'a', 'b', 'c', 'd']):
        r = False
    s = tokenize("1 2 mul sub add mod 23 /n { [2 3 4 5] } def")
    if (s != ['1', '2', 'mul', 'sub', 'add', 'mod', '23', '/n', '{', '[2 3 4 5]', '}', 'def'] ):
        r = False
    return r

def testIntepret():
    r = True
    interpret(['/fact', [0, 'dict', 'begin', '/n', 'exch', 'def', 1, 'n', -1, 1,
['mul'], 'for', 'end'], 'def', [1, 2, 3, 4, 5], 'dup', 4, 'get',
'pop', 'length', 'fact'])
    if (opPop() != 120):
        r = False
    clear()
    interpret([0, 1, 2, 3, 4, 'add', 'add', 'mul'])
    if(opPop() != 9 or opPop() != 0):
        r = False
    clear()
    interpret(['/n', 5, 'def', 'n', 'n', 'mul'])
    if(opPop() != 25):
        r = False
    clear()
    interpret(['/test', 10, 'def', [1, 2, 3, 4, 5], '/n', 'exch', 'def', 'n', 'test'])
    if(opPop() != 10 or opPop() != [1,2,3,4,5]):
        r = False
    clear()
    return r


def testInterpreter():
    r = True
    clear()
    interpreter("/fact{0 dict begin /n exch def 1 n -1 1 {mul} for end} def [1 2 3 4 5] dup 4 get pop length fact")
    if(opPop() != 120):
        r = False
    clear()
    interpreter("0 1 2 3 4 add add mul")
    if (opPop() != 9 or opPop() != 0):
        r = False
    clear()
    interpreter("/n 5 def n n mul")
    if (opPop() != 25):
        r = False
    interpreter("/test 10 def [1 2 3 4 5] /n exch def n test")
    if (opPop() != 10 or opPop() != [1, 2, 3, 4, 5]):
        r = False
    return r


def testParse():
    r = True
    clear()
    s = parse(['/fact', '{', '0', 'dict', 'begin', '/n', 'exch', 'def', '1', 'n', '-1', '1', '{', 'mul', '}',
               'for', 'end', '}', 'def', '[1 2 3 4 5]', 'dup', '4', 'get', 'pop', 'length', 'fact', 'stack'])
    if (s != ['/fact', [0, 'dict', 'begin', '/n', 'exch', 'def', 1, 'n', -1, 1, ['mul'], 'for', 'end'], 'def',
              [1, 2, 3, 4, 5], 'dup', 4, 'get', 'pop', 'length', 'fact', 'stack']):
        r = False
    s = parse(['/test', '2', 'def', '1', '2', '3', '4', '5', '/n', '{', '0', 'mul', '}', 'def', '[1 2 3 4 5]'])
    if (s != ['/test', 2, 'def', 1, 2, 3, 4, 5, '/n', [0, 'mul'], 'def', [1, 2, 3, 4, 5]]):
        r = False
    s = parse(['[1 2 3 4 5]', '1', 'a', 'b', 'c', 'd'])
    if (s != [[1, 2, 3, 4, 5], 1, 'a', 'b', 'c', 'd']):
        r = False
    s = parse(['1', '2', 'mul', 'sub', 'add', 'mod', '23', '/n', '{', '[2 3 4 5]', '}', 'def'])
    if (s != [1, 2, 'mul', 'sub', 'add', 'mod', 23, '/n', [[2, 3, 4, 5]], 'def']):
        r = False
    return r

def main_part2():
    testCases = [('for', testFor), ('tokenize', testTokenize), ('interpret', testIntepret), ('interpreter', testInterpreter),
                 ('parse', testParse)]
    # add you test functions to this list along with suitable names
    failedTests = [testName for (testName, testProc) in testCases if not testProc()]
    print(
        "\nYou will notice a lot of prints stating, Not found in dictionary stack. This is normal and part of error handling")
    if failedTests:
        return ('Some tests failed', failedTests)
    else:
        return ('\n\n\nAll part-2 tests OK\n\n\n')

print(main_part2())  # Calls all of the test functions from part 2. If any test were to fail, it will print a fail message

def main_part23():

#---------Test Case 1 -------
    print('---------Test Case-1 (15%)-------')
    testcase1= """
    /fact{
    0 dict
            begin
                    /n exch def
                    1
                    n -1 1 {mul} for
            end
    }def
    [1 2 3 4 5] dup 4 get pop
    length
    fact
    stack
    """
    interpreter(testcase1)
    #output should print 120
    clear() #clear the stack for next test case
    clear()

#---------Test Case 2a -------
    print('---------Test Case-2a (15%)-------')
    testcase2a = """
    /L [4 3 2 1] def
    /lengthL {L length 1 sub} def
    /getL {L exch get} def
    0 1 lengthL {getL dup mul} for 
    stack
    """
    interpreter(testcase2a)
    #should print : 1 4 9 16
    clear() #clear the stack for next test case
    clear()

#---------Test Case 2b -------
    print('---------Test Case-2b (5%)-------')
    testcase2b = """
    /L [4 3 2 1] def
    /lengthL { [4 3 2 1] length 1 sub} def
    /getL { [4 3 2 1] exch get} def
    0 1 lengthL {getL dup mul} for 
    stack
    """
    interpreter(testcase2b)
    #should print : 1 4 9 16
    clear() #clear the stack for next test case
    clear()


#---------Test Case 3 -------
    print('---------Test Case-3 (20%) -------')
    testcase3 = """
     /x 10 def 
     /y 5 def
     /f1 { x y 1 dict begin
                /y /z y def x def
                /x z def
                x y sub
         end} def 
     f1 3 1 roll sub     
     stack
    """
    interpreter(testcase3)
    #should print 5  -5
    clear() #clear the stack for next test case
    clear()

#---------Test Case 4 -------
    print('---------Test Case-4 (15%)-------')
    testcase4 = """
        /sum { -1 0 {add} for} def 
        0 
        [1 2 3 4] length 
        sum 
        2 mul 
        [1 2 3 4] 2 get 
        add  
        stack 
    """
    interpreter(testcase4)
    # should print 23
    clear() #clear the stack for next test case
    clear()

#---------Test Case 5 -------
    print('---------Test Case-5 (15%) -------')
    testcase5 = """
        /a 2 def
        /b 3 def
        /f1 { 1 dict begin 
                a 1 add /a exch def 
                2 dict begin 
                a 1 sub /a exch def 
                b 1 add /b exch def 
             end
             a b mul
             end } def
        f1
        stack
    """
    interpreter(testcase5)
    # should print 9
    clear() #clear the stack for next test case
    clear()

    print('---------Test Case-6 (15%) -------')
    testcase6 = """
        /x 2 def
        /y 3 def
        /fn { x y add
              x y mul
        } def
        fn add 
        stack
    """
    interpreter(testcase6)
    print("---------------------------")
    # should print 11
    clear() #clear the stack for next test case
    clear()

if __name__ == '__main__':
    main_part23()