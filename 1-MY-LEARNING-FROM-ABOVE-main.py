comments == """multiline """"        /      #

FUNCTION = JECHYA NANTAR () eto tyala function mhanatat eg- print() , range(), input()

print(a[DEFAULTZERO:DEFAULTLAST:DEFAULT1])

print(name,age)  == akarsh,23

age=input("PROMPT JI DISTE")     /     int(input("hello what is your age")) #ERROR-int need to get number from user so math apply with them

TYPE CONVERSION==
var1=str(var1)       ----a converted as string here
a=int(a)       WRONG  ONLY NUMBER WHICH IS STORED AS STRING CONVERTED INTO INT

a=1
print(bool(a))        == True
a=0                    /Flase/0/0.0/" "/[]/ {} /()         ==ALL THESE VALUES GIVE FALSE AND ANY NUMBER GIVES TRUE
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

in_maintenance = False
x = 15
y = 2
z = 10
# Evaluation order: 1. not, 2. and, 3. or
if not in_maintenance and (x > 10 and y < 5) or z == 0:
    print("Group works")



LOGICAL OPERATOR==
AND ==== ALL MUST TRUE
print(12 >20 and 123 > 100 and 34 == 34 and 45 < 90)    ==FALSE

OR  ==== ANY 1 MUST TRUE

------------------------------------------------------------    2 hr notes            ----------------------------------------------------------------------------------
# LOOPS
FOR LOOP NOTES BELOW 4 LINES SARANSH - 

range(start      ,stop+1/stop-1 IF NEGATIVE,     step 1/-1 IF REVERSE)      =   range(stop)    ---- because start=1 & step=+1 is default ,u need just stop+1 value to give lke below
range(0   ,50+1/(-50-1)  ,   1/-1 IF REVESRSE)                            =   range(51) ALSO GIVES SAME RESULT        
- if reverse in minus number then also stop-1 so increase by -1    ----BUT STRING WORD NO NEED +1 AS IT START FORM 0 
-- so above case       range(len(a))    =   a       --- both can be used in for loop
--w="abcd"
from above we get that    w= w0=a  +  w1=b  + w2=c   + w3=d
------------------------------------------------------------------------------
1)#FOR LOOP WITH NUMBERS
# PRINT -1 TO -10
for i in range(-1,-11,-1):        ----- ERROR FORGET :     - GIVE LAST NUMBER WITH+1  # U  can use any word instead of i        
  print(i)                         ---- ONLYLAST NUMBE ALSO WORKS LIKE range(21)    # need indentation space for 2nd line  


PROGRAMME-1    PRINT TABLEOF 5                       table of any number ==take n as i/p
for i in range(5,51,5)                       for i in range(n,(n*10)+1,n)
  print(i)

2) FOR LOOP FOR STRING
name= " dhairya s beast "
print(len(name))                     ========17

a = "SHERYIANS TEACHES INDUSTRY THINGS"
print(len(a))                            =====34
for i in range(len(a)):                  ===== range(34) runs here , here no need to add +1 to stop number as len gives +1 number already
    print(a[i])                          ===== (a[34])      = (a[start:stop:step])            


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
-----------------------------------------------------
KEYWORD ARGUMENT = given in argument with key=value

def greet(name, message):
    print(f"{message}, {name}!")
  
greet(name="Alice", message="Hello")  # Output: Hello, Alice!
----------------------------------------------
--DEFAULT ARG = given in parameter direct

def greet(name, age=32):
    print(f"{name} is {age} years old!")

greet("Alice")        ==========Alice is 32 years old!
greet("Bob", 25)      =========Bob is 25 years old!
-------------------------------------------
--POSITIONAL ARGUMENT =

def add(a, b):
    return a + b           ---o/p of function from here given to below where we call function

result = add(5, 3)         ---given to here where function called function
print(result)  # 8
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
d([1])  ------>10   - OREDERD access by key   ----
print(d([1]))    ----->10
d([1])  =80      - KEY CANT CHANGE BUT VALUES U CAN CHNAGE  see above 10 chnaged to 80
print(d([1]))    ----->80

