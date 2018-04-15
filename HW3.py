#Phong Nguyen
#CPTS 355
#Tested on WINDOWS 10 x64

from functools import reduce
import inspect
import math


# ---------------------Function Answers to HW3---------------------

# addDict(d) adds up the number of hours studied for each of the courses
#   during the week and returns the summed values as a dictionary
def addDict(d):
    value = d.values()
    newDictionary = {}
    for x in value:
        y = x.keys()
        for w in y:
            if(w not in newDictionary):
                newDictionary[w] = x.get(w,0)
            else:
                newDictionary[w] += x.get(w,0)
    return newDictionary


# Combines two dictionaries into one
def addDictNHelper(x,y):
    newDictionary = {}
    for w in x.keys():
        if(w not in newDictionary):
            newDictionary[w] = x.get(w,0)
        else:
            newDictionary[w] += x.get(w,0)
    for w in y.keys():
        if(w not in newDictionary):
            newDictionary[w] = y.get(w,0)
        else:
            newDictionary[w] += y.get(w,0)
    return newDictionary

# addDictN takes a list of weekly log dictionaries and returns a dictionary which
# includes the total number of hours that you have studied for your enrolled courses throughout the
# semester. Calls addDictNHelper function to do combine two dictionaries into one. Makes use of map and reduce
def addDictN(L):
    tempList = []
    newDictionary = list(map(addDict, L))
    return reduce(addDictNHelper, newDictionary)


# charCount(s) counts the number of times that each character appears in a given string.
# Sorted first by the first element of the tuple and then sorted by the second element of the tuple
def charCount(s):
    result = []
    for x in s:
        sum = 0
        if(x != ' '):
            for y in s:
                if(x == y):
                    sum += 1
            result.append((x,sum))
    return sorted(sorted(list(set(result))), key = lambda item: item[1])


#This is the same as charCount(s), but using list comprehension
#I could also do this function on one line, all on the return line
def charCount2(s):
    result = [(w, s.count(w)) for w in s if (w != ' ')]
    return sorted(sorted(list(set(result))), key = lambda item: item[1])


# LookupVal takes a list of dictionaries L and a key k as input and checks each
# dictionary in L starting from the end of the list
#Will return None if argument k is not in list or k has the none value
def lookupVal(L,k):
    for i in reversed(L):   #Reads from right to left of the given list --> reverse order
        r = i.get(k)
        if(r != None):
            return r



# LookupVal2 takes a list of tuples (tL) and a key k as input. Each tuple in the
# input list includes an integer index value and a dictionary. The integer value is the index.
# Makes use of the recursive function lookupVal2Helper
def lookupVal2(tL,k):
    start = (list(reversed(tL)))[0]  # Starting index of the list
    return lookupVal2Helper(tL,k,start)


#Recursive function
def lookupVal2Helper(tL,k,index):
    r = index[1].get(k)
    if(r != None):    # Found in Dictionary
        return r
    elif(index == tL[(index[0])]):  # Avoid a infinite loop
        return None
    else:
        index = tL[(index[0])]
        return lookupVal2Helper(tL,k,index)   # Recursion


# funRun(d,name,args) that takes a dictionary (d), a function name (name), and the
# list of arguments that will be passed to the function f (i.e.,args)
def funRun(d, name, args):
    fun = d.get(name)
    num = len(inspect.getfullargspec(fun).args) #number of arguments for the function
    if(num > len(args) or len(args) > 3 ):
        return "Error"
    elif(num == 1):
        return fun(args[0])
    elif(num == 2):
        return fun(args[0],args[1])
    else:
        return fun(args[0],args[1],args[2])


# Basically a function to count the number of paths from the top left of a matrix to the bottom right of a matrix
# Recursive
def numPaths(m,n):
    if(m == 0 or n == 0):
        return 0
    elif(m == 1 or n == 1):
        return 1
    else:
        return numPaths(m-1,n) + numPaths(m,n-1)


# An iterator that represents the sequence of squares of natural numbers starting at 1.
class iterSquares(object):
    def __init__(self):
        self.current = 1

    def __next__(self):
        result = (self.current)**2
        self.current += 1
        return result

    def __iter__(self):
        return self


# numbersToSum takes an iterator “iNumbers”
# and a positive integer value sum, and returns the next n elements from iNumbers
# such that the next n elements of the iterator add to less than sum, but the next (n + 1) elements of
# the iterator add to sum or more.
# local variable current will be one iteration behind the class's current iteration (iNumbers.current)
def numbersToSum(iNumbers,sum):
    total = 0;
    r = []
    if(iNumbers.current > 1):
        current = ((iNumbers.current-1)**2)   # current iteration = iNumbers.current iteration
    else:
        current = iNumbers.__next__()
    while (total+current) < sum:
        total += current
        r.append(current)
        current = iNumbers.__next__()
    return r


#Stream Class defined in lecture slides
class Stream(object):
    def __init__(self, first, compute_rest, empty= False):
        self.first = first
        self._compute_rest = compute_rest
        self.empty = empty
        self._rest = None
        self._computed = False
    @property
    def rest(self):
        assert not self.empty, 'Empty streams have no rest.'
        if not self._computed:
            self._rest = self._compute_rest()
            self._computed = True
        return self._rest


# streamSquares(k) creates an infinite stream of positive squared integers starting at k
# Expecting k to be an int
def streamSquares(k):
    def compute_rest():
        return streamSquares(int(math.sqrt(k)+1)**2)
    return Stream(k, compute_rest)


# evenStream takes a stream of integers as input and returns the Stream of
# even integers from the input stream. Same as streamSquares, but it only keeps the even values
def evenStream(stream):
    if(stream.empty):
        return stream
    def compute_rest():
        return evenStream(stream.rest)
    if(stream.first % 2 != 0):
        stream = stream.rest
    return Stream(stream.first, compute_rest)



# -----------------------TEST CODE BELOW-----------------------
#All Test functions is expected to return True



def addDictTest():
    d = {'Tue':{'360':2,'455':1,'221':2},'Fri':{'455':2,'360':3},
    'Sat':{'221':3,'455':2,'360':3}, 'Sun':{'221':2}}

    if(addDict(d) != {'360': 8, '455': 5, '221': 7}):
        return False

    d = {'Mon': {'112': 2, '113': 1, '114': 2}, 'Tue': {'114': 2, '113': 3},
         'Wed': {'112': 3, '113': 2, '114': 3}, 'Thur': {'112': 2}}

    if(addDict(d) != {'112': 7, '113': 6, '114': 7}):
        return False

    d = {'Mon': {'311': 3, '312': 2, '313': 1}, 'Tue': {'313': 3},
         'Wed': {'311': 1, '313': 3}, 'Thur': {'312': 2, '311': 2}, 'Fri': {'312': 2},
         'Sat': {'311': 1, '312': 3, '313': 3}, 'Sun': {'313': 2}}

    if(addDict(d) != {'311': 7, '312': 9, '313': 12}):
        return False

    d = {'Mon':{'355':2,'451':1,'360':2},'Tue':{'451':2,'360':3},
    'Thu':{'355':3,'451':2,'360':3}, 'Fri':{'355':2},
    'Sun':{'355':1,'451':3,'360':1}}

    if(addDict(d) != {'355': 8, '451': 8, '360': 9}):
        return False

    return True



def addDictNTest():
    d = [{'Tue':{'360':2,'455':1,'221':2},'Fri':{'455':2,'360':3},
    'Sat':{'221':3,'455':2,'360':3}, 'Sun':{'221':2}},
    {'Tue':{'360':2,'455':1,'221':2},'Fri':{'455':2,'360':3},
    'Sat':{'221':3,'455':2,'360':3}, 'Sun':{'221':2}}]

    if (addDictN(d) != {'360': 16, '455': 10, '221': 14}):
        return False

    d = [{'Mon': {'112': 2, '113': 1, '114': 2}, 'Tue': {'114': 2, '113': 3},
         'Wed': {'112': 3, '113': 2, '114': 3}, 'Thur': {'112': 2}}, {'Mon': {'112': 2, '113': 1, '114': 2},
         'Tue': {'114': 2, '113': 3}, 'Wed': {'112': 3, '113': 2, '114': 3}, 'Thur': {'112': 2}}]

    if (addDictN(d) != {'112': 14, '113': 12, '114': 14}):
        return False

    d = [{'Mon': {'311': 3, '312': 2, '313': 1}, 'Tue': {'313': 3},
         'Wed': {'311': 1, '313': 3}, 'Thur': {'312': 2, '311': 2}, 'Fri': {'312': 2},
         'Sat': {'311': 1, '312': 3, '313': 3}, 'Sun': {'313': 2}},
         {'Mon': {'311': 3, '312': 2, '313': 1}, 'Tue': {'313': 3},
         'Wed': {'311': 1, '313': 3}, 'Thur': {'312': 2, '311': 2}, 'Fri': {'312': 2},
         'Sat': {'311': 1, '312': 3, '313': 3}, 'Sun': {'313': 2}},
         {'Mon': {'311': 3, '312': 2, '313': 1}, 'Tue': {'313': 3},
         'Wed': {'311': 1, '313': 3}, 'Thur': {'312': 2, '311': 2}, 'Fri': {'312': 2},
         'Sat': {'311': 1, '312': 3, '313': 3}, 'Sun': {'313': 2}}]

    if (addDictN(d) != {'311': 21, '312': 27, '313': 36}):
        return False

    d = [{'Mon': {'355': 2, '451': 1, '360': 2}, 'Tue': {'451': 2, '360': 3},
         'Thu': {'355': 3, '451': 2, '360': 3}, 'Fri': {'355': 2},
         'Sun': {'355': 1, '451': 3, '360': 1}}, {'Mon': {'355': 2, '451': 1, '360': 2},
         'Tue': {'451': 2, '360': 3}, 'Thu': {'355': 3, '451': 2, '360': 3}, 'Fri': {'355': 2},
         'Sun': {'355': 1, '451': 3, '360': 1}}]

    if (addDictN(d) != {'355': 16, '451': 16, '360': 18}):
        return False

    return True




def charCountTest():
    result = charCount('Cpts355 --- Assign1')
    if(result != [('1', 1), ('3', 1), ('A', 1), ('C', 1), ('g', 1), ('i', 1), ('n', 1),
('p', 1), ('t', 1), ('5', 2), ('-', 3), ('s', 3)]):
        return False

    result = charCount('TEST TEST TEST TEST')
    if(result != [('E', 4), ('S', 4), ('T', 8)]):
        return False

    result = charCount('Computer Science Major')
    if(result != [('C', 1), ('M', 1), ('S', 1), ('a', 1), ('i', 1), ('j', 1),
                  ('m', 1), ('n', 1), ('p', 1), ('t', 1), ('u', 1), ('c', 2), ('o', 2), ('r', 2), ('e', 3)]):
        return False

    result = charCount('Please Give Me An A+')
    if(result != [('+', 1), ('G', 1), ('M', 1), ('P', 1), ('a', 1),
                  ('i', 1), ('l', 1), ('n', 1), ('s', 1), ('v', 1), ('A', 2), ('e', 4)]):
        return False

    return True




def charCount2Test():
    result = charCount2('Cpts355 --- Assign1')
    if (result != [('1', 1), ('3', 1), ('A', 1), ('C', 1), ('g', 1), ('i', 1), ('n', 1),
                   ('p', 1), ('t', 1), ('5', 2), ('-', 3), ('s', 3)]):
        return False

    result = charCount2('TEST TEST TEST TEST')
    if (result != [('E', 4), ('S', 4), ('T', 8)]):
        return False

    result = charCount2('Computer Science Major')
    if (result != [('C', 1), ('M', 1), ('S', 1), ('a', 1), ('i', 1), ('j', 1),
                   ('m', 1), ('n', 1), ('p', 1), ('t', 1), ('u', 1), ('c', 2), ('o', 2), ('r', 2), ('e', 3)]):
        return False

    result = charCount2('Please Give Me An A+')
    if (result != [('+', 1), ('G', 1), ('M', 1), ('P', 1), ('a', 1),
                   ('i', 1), ('l', 1), ('n', 1), ('s', 1), ('v', 1), ('A', 2), ('e', 4)]):
        return False

    return True




def lookupValTest():
    L = [{"a":5, "b": 3, "c":1, "d":True}, {"a":False}, {"c": 5}]
    if(lookupVal(L, "a") != False):
        return False
    if(lookupVal(L, "b") != 3):
        return False
    if(lookupVal(L, "c") != 5):
        return False
    if(lookupVal(L, "d") != True):
        return False
    return True

def lookupVal2Test():
    L = [(0,{"a":0,"b":True,"c":"zero"}),
    (0,{"d":1}), (1,{"a":False}), (1,{"b":3, "c": "Three"}),(2,{}),
    (3, {"a": 9, "b": True, "c": "hello"}), (4, {"d": False})]

    if(lookupVal2(L, "a") != False):
        return False
    if(lookupVal2(L, "b") != True):
        return False
    if(lookupVal2(L, "c") != "zero"):
        return False
    if(lookupVal2(L, "d") != False):
        return False
    return True





def funRunTest():
    d = {"sub": lambda x,y: (x-y), "concat2": lambda a,b: (a+","+b),
         "add": lambda x,y: (x+y), "multi": lambda x,y: (x*y),
         "tuple": lambda x,y: (x,y)}

    if(funRun(d,"sub",[5,2]) != 3):
        return False
    if (funRun(d, "concat2", ["Computer", "Science"]) != "Computer,Science"):
        return False
    if (funRun(d, "add", [5, 2]) != 7):
        return False
    if (funRun(d, "multi", [5, 2]) != 10):
        return False
    if (funRun(d, "tuple", [5, 2]) != (5, 2)):
        return False
    return True




def numPathsTest():
    if(numPaths(1,1) != 1):
        return False
    if(numPaths(0,1) != 0):
        return False
    if(numPaths(1,0) != 0):
        return False
    if(numPaths(0,0) != 0):
        return False
    if(numPaths(3, 3) != 6):
        return False
    if(numPaths(2,2) != 2):
        return False
    return True




def iterSquaresTest():
    squares = iterSquares()
    if(squares.__next__() != 1):
        return False
    if (squares.__next__() != 4):
        return False
    if (squares.__next__() != 9):
        return False
    if (squares.__next__() != 16):
        return False
    if (squares.__next__() != 25):
        return False
    return True




def numbersToSumTest():
    squares = iterSquares()
    if(numbersToSum(squares, 25) != [1,4,9]):
        return False
    if (numbersToSum(squares, 50) != [1,4,9,16]):
        return False
    if (numbersToSum(squares, 75) != [1,4,9,16,25]):
        return False
    if (numbersToSum(squares, 100) != [1,4,9,16,25,36]):
        return False
    return True




def streamSquaresTest():
    sqStream = streamSquares(4)
    myList = []
    while sqStream.first < 100:
        myList.append(sqStream.first)
        sqStream = sqStream.rest
    if(myList != [4, 9, 16, 25, 36, 49, 64, 81]):
        return False

    sqStream = streamSquares(25)
    myList = []
    while sqStream.first < 350:
        myList.append(sqStream.first)
        sqStream = sqStream.rest
    if (myList != [25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324]):
        return False

    sqStream = streamSquares(49)
    myList = []
    while sqStream.first < 200:
        myList.append(sqStream.first)
        sqStream = sqStream.rest
    if (myList != [49, 64, 81, 100, 121, 144, 169, 196]):
        return False

    return True




#Should return the even numbers from list in the streamSquaresTest
def evenStreamTest():
    evenS = evenStream(streamSquares(4))
    myList = []
    while evenS.first < 100:
        myList.append(evenS.first)
        evenS = evenS.rest
    if(myList != [4, 16, 36, 64]):
        return False

    evenS = evenStream(streamSquares(25))
    myList = []
    while evenS.first < 350:
        myList.append(evenS.first)
        evenS = evenS.rest
    if(myList != [36, 64, 100, 144, 196, 256, 324]):
        return False

    evenS = evenStream(streamSquares(49))
    myList = []
    while evenS.first < 200:
        myList.append(evenS.first)
        evenS = evenS.rest
    if(myList != [64, 100, 144, 196]):
        return False

    return True



# ---------------------Main Program---------------------
# Used to call all of the test functions
if __name__ == '__main__':
    passedMsg = "%s passed"
    failedMsg = "%s failed"
    if addDictTest():
        print ( passedMsg % 'addDictTest' )
    else:
        print ( failedMsg % 'addDictTest' )
    if addDictNTest():
        print ( passedMsg % 'addDictNTest' )
    else:
        print ( failedMsg % 'addDictNTest' )
    if charCountTest():
        print ( passedMsg % 'charCountTest' )
    else:
        print ( failedMsg % 'charCountTest' )
    if charCount2Test():
        print ( passedMsg % 'charCount2Test' )
    else:
        print ( failedMsg % 'charCount2Test' )
    if lookupValTest():
        print ( passedMsg % 'lookupValTest' )
    else:
        print ( failedMsg % 'lookupValTest' )
    if lookupVal2Test():
        print ( passedMsg % 'lookupVal2Test' )
    else:
        print ( failedMsg % 'lookupVal2Test' )
    if funRunTest():
        print ( passedMsg % 'funRunTest' )
    else:
        print ( failedMsg % 'funRunTest' )
    if numPathsTest():
        print ( passedMsg % 'numPathsTest' )
    else:
        print ( failedMsg % 'numPathsTest' )
    if iterSquaresTest():
        print ( passedMsg % 'iterSquaresTest' )
    else:
        print ( failedMsg % 'iterSquaresTest' )
    if streamSquaresTest():
        print ( passedMsg % 'streamSquaresTest' )
    else:
        print ( failedMsg % 'streamSquaresTest' )
    if evenStreamTest():
        print ( passedMsg % 'evenStreamTest' )
    else:
        print ( failedMsg % 'evenStreamTest' )

