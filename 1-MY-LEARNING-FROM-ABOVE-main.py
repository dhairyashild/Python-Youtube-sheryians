comments == """multiline """"        /      #

FUNCTION = JECHYA NANTAR () eto tyala function mhanatat eg- print() , range(), input()
Exiting Early (Guard Clauses): Stopping a function if data is invalid.
Returning Boolean (Flags): Checking if a condition (like "is model trained") is met.
Returning Results: Passing processed data or predictions back to the main program.

print(a[DEFAULTZERO:DEFAULTLAST:DEFAULT1])

print(name,age)  == akarsh,23
print("Hello", end=" ");           ----  print came with \n but u can replace it with anything like = " " / "_"
print("World")
-----------> 
Hello World
age=input("PROMPT JI DISTE")     /     int(input("hello what is your age")) #ERROR-int need to get number from user so math apply with them

TYPE CONVERSION==
var1=str(var1)       ----a converted as string here
a=int(a)       WRONG  ONLY NUMBER WHICH IS STORED AS STRING CONVERTED INTO INT

Numeric Conversions
python
int("5")      # str → int
float("3.14") # str → float  
int(3.9)      # float → int (truncates)
str(42)       # int/float → str
bool(0)       # 0→False, non-zero→True
complex(3)    # int → complex

Collection Conversions
python
list("abc")    # str → list ['a','b','c']
set([1,2,2])   # list → set {1,2}
tuple([1,2])   # list → tuple
list((1,2))    # tuple → list
dict(a=1,b=2)  # kwargs → dict


---------------------------------
a=1
print(bool(a))        == True  - only if a   has any value given
a=0                    /False/0/0.0/" "/[]/ {} /()/None         ==ALL THESE VALUES GIVE FALSE AND ANY NUMBER GIVES TRUE    - none/false shows error=NameError: name 'none' is not defined.
print(bool(a))        == False

# OPERATOR
ARITHMETIC 
print(b//a)    ==6    IT CONVERTS ABOVE O/P INTO INTEGER MEANS POINT KADTO       
print(5**2)    ==25   VARG
print(32%5)    ==2    BAKI 

ASSIGNMENT OP
a += 30     AND  a=a+30   BOTH SAME

COMPARISON OP  === print chya atal condition varun True/False dete.
print(a == b)      == True
print(a != b)    == False
print(45 < 67)   == True

== IF ELIF ELSE=         if:    else:    elif:
if condition1:                                   if value1=="m":         --ERROR- DOUBLE INVERTED FORGET TO ADD to string
        # RUN Code if condition1 is True
elif condition2:                         elif temp >=0 and temp <=10:   --ERROR- condition made = nantar dyave (correct way >=/<=)(wrong =>/ =<)
        # RUN Code if condition2 is True
else:
        # RUN  Code if all conditions are False

#REMEMBER ONLY THIS FOR if not----- if not var=null: run below code  else: run code after else
######### if not var=zero/null in list/set/False :  then code run   else var has value: then else code run 
value = 30  # True (non-zero)
if not value:  # not 30 →  means if after not value= null then only below code run 
    print("Value is falsy")  # Won't run
else:
    print("Value is truthy")  # Runs: True


value = 0  # Falsy value = False prints but false not print as boolean works for capital F in False
if not value:  # not 0 → True (runs block)
    print("Value is falsy")  # Runs this as line as if not 0 means null/False


LOGICAL OPERATOR==
AND ==== ALL MUST TRUE
print(12 >20 and 123 > 100 and 34 == 34 and 45 < 90)    ==FALSE

OR  ==== ANY 1 MUST TRUE

------------------------------------------------------------    2 hr notes            ----------------------------------------------------------------------------------
------ 1. Formula: Last Value = Stop - Step (always works for any direction).   ##########################
# LOOPS   
FOR LOOP NOTES BELOW 4 LINES SARANSH - 

range(start      ,stop+1,     step 1/-1 IF REVERSE)      =   range(stop)    ---- because start=1 & step=+1 is default ,u need just stop+1 value to give lke below
range(0   ,50+1  ,   1/-1 IF REVESRSE)                            =   range(51) ALSO GIVES SAME RESULT        
-- so above case       range(len(a))    =   a       --- both can be used in for loop
--w="abcd"
from above we get that    w= w0=a  +  w1=b  + w2=c   + w3=d
------------------------------------------------------------------------------
1)#FOR LOOP WITH NUMBERS    - ERROR FORGET : AT END
# FOR NEGATIVE NUMS REMMEBER BELOW 2 CODES ONLY
for i in range(-11,-1,1):    = -11 ,-10...-2     - GIVE MIDDLE NUMBER WITH -1         # U  can use any word instead of i       
  print(i)                         ---- ONLY LAST NUMBER ALSO WORKS LIKE range(21)    # need indentation space for 2nd line  
for i in range(-1,-11,-1):   = -1,-2... -10     ----    - GIVE MIDDLE NUMBER WITH +1      
  print(i) 

PROGRAMME-1    PRINT TABLEOF 5                       table of any number ==take n as i/p
for i in range(5,51,5)                       for i in range(n,(n*10)+1,n)
  print(i)

2) FOR LOOP FOR STRING
name= " dhairya s beast "
print(len(name))                     ========17

a = "SHERYIANS TEACHES INDUSTRY THINGS"
print(len(a))                            =====34
for i in range(len(a)):                  ===== range(34) runs here , here no need to add +1 to stop number as len gives +1 number already
    print(a[i], end="\n")                ===== (a[34])      = (a[start:stop:step])        == u can replace default \n with " "/"_"/"anything      


for i in a:                     HERE IT TAKES CHLETTERS FROM a DIRECTLY NO NEED OF NUMBERS
  print(i)            -----also gives full of a value but to cut a string we use string
-- so above case       range(len(a))    =   a       --- both can be used in for loop


--palendromic/not              w[i] remember only
w=(input("give value"))
rev=""
for i in range(len(w)-1,-1,-1):
    rev=rev+w[i]
if rev==w:
    print("palendromic")
else:
    print("not")


-REVERSE STRING= 4 times reverse must to print   /    print(a[::-1])   also gives revrse
w="abcd"
reverse=""
for i in range(len(w)-1,-1,-1):
        reverse=reverse+w[i]
print(reverse)
---------------> dcba
-- from above we get that    w= w0=a  +  w1=b  + w2=c   + w3=d

---------------------------------------------------------------------------------------------
-- FOR LOOP WITH LIST

data = [10, 20, 30, 40, 50]

# 1) BASIC - Each item
for x in data: print(x)                    # 10 20 30 40 50     --THIS ALSO WORKS print IN SAME LINE OF for 

# 2) INDEX - enumerate()
for i ,j in enumerate(data):
    print(i,j)    ---------->
0 10
1 20
2 30
3 40
4 50

for i,x in enumerate(data): print(i,x, end=" ")  ------->  0 10 1 20 2 30 3 40 4 50

# 3) MODIFY - Change items  
for i in range(len(data)): data[i] *= 2    # [20,40,60,80,100]

# 4) FILTER - List comprehension
evens = [x for x in data if x%2==0]        # [20,40,60,80,100]

# 5) ZIP - Multiple lists
for a,b in zip(data, ['A','B','C']): print(a,b)  # 20:A 40:B 60:C



---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------   WHILE LOOP     --------------------------------------------------------------------------------------------------------------------------------------


WHILE LOOP - Interview Qs + LeetCode/HackerRank Problems (Simple Logics)
All in 1 Block - Key Points + Code Solutions

# 1. COMMON INTERVIEW QUESTIONS
Q1: What is while loop? Syntax?
A: Runs while CONDITION True. Syntax: while condition: code
i=0; while i<5: print(i); i+=1  # 0 1 2 3 4 [web:11]

Q2: for vs while?
for: Known iterations (range/list). while: Condition-based [web:11]

Q3: Infinite loop? Fix?
while True: ... → Add break/False condition [web:11]

Q4: break vs continue?
break: Exit loop. continue: Skip to next iter [web:14]

Q5: while-else?
else runs if NO break [web:12]
nums=[4,2,7]; i=0; while i<len(nums): 
    if nums[i]==7: print(i); break; i+=1
else: print("Not found")  # Prints 2 [web:11]

## 2. HACKERRANK: LOOPS (Print i**2 for i=0 to n-1)
if __name__=='__main__':
    n=int(input())
    i=0
    while i<n: print(i**2); i+=1  # Ex: n=5 → 0,1,4,9,16 [web:31][web:35]

## 3. LEETCODE EASY/MEDIUM w/ WHILE (Simple Versions)

# LC 704: Binary Search (while mid)
def search(nums, target):
    l,r=0,len(nums)-1
    while l<=r:
        mid=(l+r)//2
        if nums[mid]==target: return mid
        elif nums[mid]<target: l=mid+1
        else: r=mid-1
    return -1  # Sorted array [web:24]




# LC 1: Two Sum Brute (Nested while - O(n^2))
def twoSum(nums, target):
    i=0
    while i<len(nums):
        j=i+1
        while j<len(nums):
            if nums[i]+nums[j]==target: return [i,j]
            j+=1
        i+=1
    return []  # Use hashmap for O(n) [web:21]

# my code
def twoSum(nums, target=9):
    for i,n in enumerate(nums):
        need=target-n
        if need in nums:
            return i,nums.index(need)
        
print(twoSum([13,4,3,8,3,5]))

===============================  PYTHON AND CODES FROM GPT MUST KNOW FOR DSA        ========================================
# --- ESSENTIAL LIST OPERATIONS (O-Notation included for DSA) ---
my_list = [1, 2, 3]          # Create: Initialize [1, 2, 3]
my_list.append(4)            # Add End: [1, 2, 3, 4] | O(1)
my_list.insert(0, 0)         # Add at Index: [0, 1, 2, 3, 4] | O(n)
my_list.extend([5, 6])       # Add Iterable: [0, 1, 2, 3, 4, 5, 6] | O(k)
my_list[1] = 9               # Replace: [0, 9, 2, 3, 4, 5, 6] | O(1)
val = my_list.pop()          # Remove End: val=6, list=[0, 9, 2, 3, 4, 5] | O(1)
my_list.pop(0)               # Remove Index: returns 0, list=[9, 2, 3, 4, 5] | O(n)
my_list.remove(9)            # Remove Value: [2, 3, 4, 5] | O(n)
del my_list[0:2]             # Delete Slice: [4, 5] | O(n)
item_count = len(my_list)    # Length: 2 | O(1)
occurrences = my_list.count(5)# Count Value: 1 | O(n)
idx = my_list.index(5)       # Find Index: 1 (returns first match) | O(n)
my_list.sort()               # Sort In-place: [4, 5] | O(n log n)
my_list.reverse()            # Reverse In-place: [5, 4] | O(n)
exists = 5 in my_list        # Membership: True | O(n)

# --- ESSENTIAL DICTIONARY OPERATIONS (Fast Lookups) ---
my_dict = {"a": 1, "b": 2}   # Create: {'a': 1, 'b': 2}
my_dict["c"] = 3             # Add/Update: {'a': 1, 'b': 2, 'c': 3} | O(1)
my_dict.update({"d": 4})     # Merge: {'a': 1, 'b': 2, 'c': 3, 'd': 4} | O(k)
val = my_dict.get("z", 0)    # Safe Access: 0 (returns default if key missing) | O(1)
del my_dict["b"]             # Delete: {'a': 1, 'c': 3, 'd': 4} | O(1)
removed = my_dict.pop("c")   # Pop Key: removed=3, dict={'a': 1, 'd': 4} | O(1)
exists = "a" in my_dict      # Search Key: True | O(1)
all_keys = my_dict.keys()    # View Keys: dict_keys(['a', 'd'])
all_vals = my_dict.values()  # View Values: dict_values([1, 4])
all_items = my_dict.items()  # View Pairs: dict_items([('a', 1), ('d', 4)])
dict_size = len(my_dict)     # Count: 2 | O(1)
my_dict.clear()              # Empty: {} | O(1)                                         # {}
=========================================================================
# LC 20: Valid Parentheses (while stack)
def isValid(s):
    stack=[]
    pairs={'(':')','{':'}','[':']'}
    i=0
    while i<len(s):
        if s[i] in pairs: stack.append(s[i])
        elif not stack or pairs[stack.pop()]!=s[i]: return False
        i+=1
    return len(stack)==0

# LC 141: LinkedList Cycle (Floyd's - slow/fast pointers)
# Slow while logic (simple counter version)
def hasCycle(head):
    seen=set()
    cur=head
    while cur:
        if cur in seen: return True
        seen.add(cur)
        cur=cur.next
    return False  # While cur.next [web:24]

# LC 202: Happy Number (while not seen)
def isHappy(n):
    seen=set()
    while n!=1 and n not in seen:
        seen.add(n)
        n=sum(int(d)**2 for d in str(n))
    return n==1

# LC 876: Middle of LinkedList (two pointers while)
def middleNode(head):
    slow=fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow

## 4. SIMPLE PRACTICE PROBLEMS (Interview Style)
# Print 1 to N
n=5; i=1; while i<=n: print(i); i+=1  # 1 2 3 4 5

# Sum 1 to N
n=5; i=1; s=0; while i<=n: s+=i; i+=1; print(s)  # 15

# Factorial
n=5; i=1; f=1; while i<=n: f*=i; i+=1; print(f)  # 120

# Fibonacci (first n)
n=5; a,b=0,1; i=0; while i<n: print(a); a,b=b,a+b; i+=1  # 0 1 1 2 3

# Reverse digits
n=123; rev=0; while n>0: rev=rev*10 + n%10; n//=10; print(rev)  # 321

## TIPS for INTERVIEWS
# - ALWAYS update counter/pointer INSIDE loop (avoid infinite)
# - Use while for: Binary search, Two pointers, Unknown iterations
# - Time: O(n) single, O(n^2) nested → Optimize with hash/pointers
# - Test edges: n=0, n=1, empty list [web:11][web:21]


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------    FUNCTION       --------------------------------------------------------------------------------------------------------------------------------------
Function: Reusable code block for a task.                        
Parameter: Variable name in function definition.     / == varname
Argument: Value passed to function                   / == var-value


def FUNCTION-NAME-GIVE-WORD-THAT-U-GET-CODE-SARANSH(PARA-1,PARA-2,......):
    BLOCK OF REUSABLE CODE

FUNCTION-NAV(ARGUMENT-1 FOR PARAmeter-1 ,    ARG-2 FOR PARA-2)                   /         FUNCTION-NAV()       ------TO CALL
OR
FUNCTION-NAV()                    ------------IF PARAMETER NOT WRITTEN IN BRACKET THEN DIRECT NAME ONLY TO CALL FUNCTION


-- GPT FUNCTION NOTES
# 1. To send a result back to the caller
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(f"The sum is: {result}")

# 2. To exit a function early (Guard Clause)
def check_age(age):
    if age < 18:
        return "Access Denied"
    return "Access Granted"
status = check_age(15)
print(status)

# 3. To return multiple values (as a tuple)
def get_user_data():
    name = "Alice"
    level = 10
    return name, level # Provider: Throws values out in order
# LHS catches <--- RHS provides
user_name, user_level = get_user_data() # LHS = vars to store; RHS = call function
print(f"User: {user_name}, Level: {user_level}")

# 4. To stop execution (returning None)
def simple_exit(condition):
    if condition:
        return # Returns None and stops here
    print("This only prints if condition is False")
simple_exit(True)
-----------------------------------------------------
KEYWORD ARGUMENT = given in argument with key=value

def greet(name, message):
    print(f"{message}, {name}!")
  
greet( message="Hello",name="Alice")  # Output: Hello, Alice!    --   U CAN CHNAGE SEQUENCE  AS HERE  name used later
-----------------------------------------------------------------------------------------
--POSITIONAL ARGUMENT =

def add(a, b):
    return a + b           ---o/p of function from here given to below where we call function

result = add(5, 3)         ---given to here where function called function
print(result)  # 8

--------------------------------------------------------------------------------------
--DEFAULT ARG = given in parameter direct

def greet(name, age=32):
    print(f"{name} is {age} years old!")

greet("Alice")        ==========Alice is 32 years old!
greet("Bob", 25)      =========Bob is 25 years old!
--------------------------------------------------------------------------------------
# Use Case OF RETURN  1: The 'Unreachable' code
def model_status():
    return "Offline"
    print("This will NOT run.") # The function already closed

# Use Case 2: Returning True/False (Validation)
def is_data_clean(data):
    if len(data) == 0:
        return False # Exit early if empty
    return True      # Continue if data exists

# Use Case 3: Returning a Result
def get_prediction(x):
    prediction = x * 0.5
    return prediction # Sends 0.5 back to the user
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
LIST===

MUTABLE ,
IN ORDER (ACCESS BY THAT POSITION) ,
DUPLICATES ,
ALL DATAS + FUNCTIONS IN IT


numbers = [1, 2, 3, 5, 3]

numbers.append(10);               print("append:", [1, 2, 3, 5, 3, 10])           # ADD AT LAST ✓
numbers.pop();                    print("pop:", [1, 2, 3, 5, 3])                 # REMOVE LAST ✓

numbers.extend([20,25]);          print("extend:", [1, 2, 3, 5, 3, 20, 25])      # ADD MULTIPLE AT END ✓
numbers.insert(1,15);             print("insert:", [1, 15, 2, 3, 5, 3, 20, 25])  # INSERT AT INDEX 1 ✓
numbers.remove(3);                print("remove:", [1, 15, 2, 5, 3, 20, 25])     # REMOVE FIRST 3 ✓

numbers.sort();                 print("sort:", [1, 2, 3, 5, 15, 20, 25])       # SORT ASCENDING ✓
numbers.reverse();              print("reverse:", [25, 20, 15, 5, 3, 2, 1])     # REVERSE ORDER ✓

new_list = numbers.copy();      print("copy:", [25, 20, 15, 5, 3, 2, 1])        # CREATE COPY ✓
numbers.clear();                print("clear:", [])                            # EMPTY LIST ✓

numbers.index(5)     # FIND INDEX NUMBER OF 5 ✓
numbers.count(3)     # COUNT HOW MANY 3 IN LIST ✓

numbers.append(10)             VS         numbers.pop()                 = LAST APPEND VS POP(REMOVE)
numbers.sort()                 VS         numbers.reverse()             = SORT(ASCEND) VS REVERSE(DESCEND)
new_list = numbers.copy()      VS         numbers.clear()               = COPY         VS CLEAR LIST


l=[0,1,2,3]
l[0]=55                   ----u can replace any value by indexing, u cant do this in string
print(l)
-------->[55, 1, 2, 3]
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
TUPLE === IMMUTABLE + comma in GOLbracket ( , )  + oredred  +  tuple unpacking

- IMMUTBLE ---- U CAN CHANGE ANY VLUE UNDER (    )   --BAKI SAME LIST SARAKHE

a=(1)  
type(a)=== integer
a(1,)=== tuple la comma hawa

a,b,c=(1,2,3)
print(a)=1
      b =2
      c =3
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
SET=== NO DUPLICATES   +  {    }  + UNOREDRED(CANT ACCESS BY INDEXING)






---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
DICTIONARY ==== { KEY1  : VALUE1    ,    KEY2  : "VALUE2"

d = {1:10 ,2:20}
d[1]  ------>10   - OREDERD access by key   ----
print(d[1])    ----->10
d[1]  =80      - KEY CANT CHANGE BUT VALUES U CAN CHNAGE  see above 10 chnaged to 80
print(d[1])    ----->80
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  SARANSH
=with open("superman.txt", "w") as f:      === these 2 work same for create fiel f====     f=open("superman.txt", "w") 
=with not need to f.close to close file but f=open... need to close it is must to close with f.close for above example
=open( "filename", "r").read()
=open( "filename", "w").write("write anything in file)           # Overwrites file contents.
=open( "filename", "a").write("write anything that u want after existing data)
=Best Practice-Always use with open() because it prevents file corruption                          
# =====================================================
 COMPLETE FILE HANDLING NOTES - ALL MODES (r, w, x, a)
# =====================================================

1. 'r' MODE -Default + READ (file must exist)

# MANUAL WAY
file = open("data.txt", "r")
content = file.read()                    /   open("data.txt", "r").read()  
print(content)
file.close()

# WITH WAY (auto-close)
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
    # No close() needed

2. 'w' MODE - WRITE (creates OR overwrites)

# MANUAL WAY
file = open("output.txt", "w")
file.write("Hello World!\n")                     /   open("data.txt", "w").write("Hello World!\n")      === checked this also creates file
file.close()

# WITH WAY
with open("output.txt", "w") as file:
    file.write("Hello World!\n")
    # Auto-closes

- If you just want to create the file and do nothing else, use pass:
with open("file1", "w") as f:
    pass 


3. 'x' MODE - CREATE NEW (fails if file exists)

# MANUAL WAY
file = open("newfile.txt", "x")
file.write("This is NEW file\n")
file.close()

# WITH WAY
with open("newfile.txt", "x") as file:
    file.write("This is NEW file\n")

4. 'a' MODE - APPEND (adds to end)
with open("file1", "a") as f: 
    f.write("New data here") # glue the new text directly to the end of the last character in the file.

# MANUAL WAY (your example)
file = open("superman.txt", "a")
file.write("and now I am appending some content inside the file\n")
file.close()

# WITH WAY
with open("superman.txt", "a") as file:
    file.write("and now I am appending some content inside the file\n")

## SUMMARY TABLE
| Mode | What it does | File exists? | WITH auto-close |
|------|--------------|--------------|-----------------|
| 'r'  | Read only    | YES required | ✅ Yes         |
| 'w'  | Write/Overwrite | Any       | ✅ Yes         |
| 'x'  | Create new   | NO (fails if yes) | ✅ Yes    |
| 'a'  | Append       | Any         | ✅ Yes         |

**Key Rule:** WITH = safer (auto-close). Manual = works but risky if forget close().

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------        OOPS - PYHTON        ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        --  My CLASS CODE NEUROVED REMEMBER DEF AFTER CODE LINE AS IT IS   --   

class Car:        #  1. Class: Template(blueprint) to create objects.      1st word capital + Never use _ in its name    == eg= class Dog:
    species= "german sheferd"        #  CLASS VARIABLE  = SHARED BY ALL OBJECTS OF CLASS 
    def __init__(self, color="blue" ,age=0):       # 4. 'def __init__': CONSTRUCTOR is function called automatically when created new object.
        self.color = color           # INSTANCE VARIABLE = UNIQUE TO EACH CLASS (OPPOSITE TO CLASS VAR)  -- GIVE SAME NAME MOSLY BUT U CAN GIVE self.color= paint (on RHS  anything will be ok )
        self.age = age           # INSTANCE VAR
      
            
#  METHODs can get above constructor vars = SO must use self.name + self.age to get constructor var into next method/function
    def info(self,country):         ############# this  country is METHID VAR called without using self
        return f"{self.color} is {self.age} years old and {country}"  

        # call another method of SAME object
        self.show_info()
            
-----  THIS 5 LINES ADDED LATER TO CHECK METHOD VAR INTERCHANGEBLE IN ALL METHOD OF OBJECT - MAY HAVE DIFFERENT VARS FROM ABOVE SO NOT CONFUSE ----
    def show_info(self):
        # can use both self.color and self.country here
        print(f"{self.color} car from {self.country}")
c1 = Car("red",25)
c1.set_country("India")   # this will internally call show_info()
-------------------------------------------------------------------------------------------------------------------------------------------------

# YOUR ORIGINAL EXAMPLE
c1 = Car("red",25)     # 2. Object: INSTANCE of a class that occupies memory.--Relationship: If a "Car" is the Class (the design), a "Red Tesla" is the Object (the physical thing).
print(c1.color)        # red          -- PRINT INSTANCE VAR VALUE
print(c1.info("india")) # red is 25 years old and india            
# print(Car("red",25).info("india")) works same as above, it will create a new Car object and immediately call info("india") on it.

# DEFAULT EXAMPLE
print("\n=== DEFAULT VALUES ===")
c2 = Car()             # NO args → DEFAULTS
print(c2.color)        # blue
print(c2.info("usa"))

# OVERRIDE EXAMPLE
print("\n=== OVERRIDE DEFAULT ===")
c3 = Car("black", 10)  # OVERRIDE defaults
print(c3.color)        # black

# CLASS VARIABLE EXAMPLE
print("\n=== CLASS VARIABLE SHARED ===")
print(c1.species)      # german sheferd
print(c2.species)      # german sheferd
print(c3.species)      # german sheferd - SAME for ALL!


# 1. Class type
print(type(MyClass))         # <class 'type'>
# 2. Object type  
obj = MyClass()
print(type(obj))             # <class '__main__.MyClass'>

# 3. IN-Built CLASS type LIKE INT, FLOAT ....
a = 3.2
print(type(a))               # <class 'float'>      


5. 'self' keyword: Represents the specific instance currently being used in code.
6. Industry Best Practice: Always use 'PascalCase' for naming your Python classes.
7. Real-time Use: Classes group data and logic to make code reusable.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Lecture 15: Python OOP - Classes, Encapsulation & Inheritance | Complete Tutorial in Hindi 🐍


class Test:
    def __init__(self):
        self.pub = "public"      # Public
        self._pro = "protected"  # Protected  
        self.__pri = "private"   # Private
    
    def pub_method(self): print("public method")
    def _pro_method(self): print("protected method")
    def __pri_method(self): print("private method")
    
    def show_all(self):  # Inside class - CAN access everything
        print(self.pub, self._pro, self.__pri)
        self.pub_method()
        self._pro_method()
        self.__pri_method()

class Sub(Test):
    def show(self):  # Subclass - CAN access public & protected
        print(self.pub, self._pro)  # ✅ ✅
        # print(self.__pri)  # ❌ ERROR!
        self.pub_method()   # ✅
        self._pro_method()  # ✅
        # self.__pri_method()  # ❌ ERROR!

# CREATING OBJECTS
t = Test()
s = Sub()

print("=== INSIDE CLASS ===")
t.show_all()  # ✅ Everything works

print("\n=== OUTSIDE CLASS ===")
print(t.pub)          # ✅ public
print(t._pro)         # ⚠️ protected (works but don't)
# print(t.__pri)      # ❌ private - ERROR!

t.pub_method()        # ✅ public
t._pro_method()       # ⚠️ protected (works but don't)
# t.__pri_method()    # ❌ private - ERROR!

print("\n=== SUBCLASS ===")
s.show()  # ✅ public & protected only


           | pub | _pro | __pri
-----------|-----|------|------
Inside     | ✅  | ✅   | ✅
Outside    | ✅  | ⚠️  | ❌
Subclass   | ✅  | ✅   | ❌
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅
OOPS NOTES------

-- Types of Attribute
1=Class attribute = variable created inside  class
2=Instance attribute = created using an instance like self.name, self.age
# class Animal:
#     name = "lion"                    #class attribute
#     def __init__(self,age):
#         self.age = age               #instance attribute


Types of Methods--
1=instance method =Works with object of the class.
2= classmethod=works with the class itself it will not target object.    
3-staticmethod  =This method doesn’t access class or instancedirectly it also uses a decorator @staticmethod
#     def show(self):                                     # instance method 
#         print(f"how are you your agger is {self.age}")

#     @classmethod                                        # classmethod
#     def hello(cls):
#         print(f"how are you brother {cls.age}")

#     @staticmethod                                        # staticmethod  
#     def static():
#         print("how are you")

###### Inheritance  

inherited class has all the powers of parent class that means all
1=methods, 
2=attributes
+ CODE REUSABILITY

class A: def __init__(self): self.x=1               # Auto-inherited if no __init__
class B(A): pass                                    # No super needed
class C(A): def __init__(self): super().__init__()  # super() required

Types of Inheritance===
1= Single Inheritance)

2=Multiple Inheritance= 2 parent classes and only 1 child class and  child class will inherit all
 =constructor function will be inherited of the firstclass that has been Inherited. This is MRO(Method Resolution Order)
class Father: 
class Mother: 
class Child(Father, Mother):
        
3=Multilevel Inheritance
class Grandparent: heritage = lambda s: print("Heritage")
class Parent(Grandparent): pass
class Child(Parent): pass

Method Overriding: Redefining a parent's method in the child class to change its behavior.

interview q shortest form gpt on inheritance
Q: Goal?
A: Code reuse.

Q: super()?
A: Calls parent's __init__.

Q: Overriding?
A: Replacing parent methods.

Q: MRO?
A: Method search order.

Q: Multiple?
A: Python allows 2+ parents.
--------------------------------------------------------------------------------------------------------------------------------------------------

--------- Polymorphism = allows same  method name to behave differently

Types of Polymorphism
1-method overiding = CHILD class overides methos of PARENT class (IN 2 DIFFERENT CLASS THERE)

class Animal:
    def speak(self):
        return "Generic sound"
class Dog(Animal):
    def speak(self):  #    Overriding parent method so this speak works not above works called method overiding
        return "Woof!"

2-DUCK TYPING = If 2 object has SAME  methods, you use it without checking its type or class
class Duck:
    def walk(self): print("Waddles")
class Person:
    def walk(self): print("Walking like a duck")
--------------------------------------------------------------------------------------------------------------------------------------------------

Encapsulation =Hiding data inside a class and accessing it only through methods.

Access modifiers in python
1-Public Attributes and Methods= VAR+ METHOD ALL CAN BE ACCESED OUTSIDE CLASS(IN CHILD CLASS)

2-protected Attributes and Methods= NO USE JUST NAMING CONVENTION , CANT BALE TO HIDE  ANY VAR/METHOD

3-Private Attributes and Method" =cannot be accessed from outside class — only from inside the class where it is defined

class Demo:
    def __init__(self):
        self.name = "Public Member"   # Public
        self._age = 21                # Protected (by convention)
        self.__salary = 50000         # Private (name-mangled)

    def show(self):
        print("Public:", self.name)             ✅
        print("Protected:", self._age)          ✅
        print("Private:", self.__salary)        ONLY THIS ACCESED IN THIS BUT NOT IN CHILD CLASS     

--------------------------------------------------------------------------------------------------------------------------------------------------
ABSTRACT METHOD === TO SET RULES BEFORE CREATING CLASS
✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


