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


-----------------------------------
Function: Reusable code block for a task.
Parameter: Variable name in function definition.     / == varname
Argument: Value passed to function                   / == var-value

def FUNCTION-NAV(PARA-1,PARA-2,......):
    BLOCK OF REUSABLE CODE

FUNCTION-NAV(ARGUMENT-1 FOR PARAmeter-1 ,    ARG-2 FOR PARA-2)                   /         FUNCTION-NAV()       ------TO CALL
OR
FUNCTION-NAV()                    ------------IF PARAMETER NOT WRITTEN IN BRACKET THEN DIRECT NAME ONLY TO CALL FUNCTION
-----------------------------------------------------
#########keyword arg = given in argument with key=value
def greet(name, message):
    print(f"{message}, {name}!")
  
greet(name="Alice", message="Hello")  # Output: Hello, Alice!
----------------------------------------------
## DEFAULT ARG =given in parameter direct
def greet(name, age=32):
    print(f"{name} is {age} years old!")

greet("Alice")        ==========Alice is 32 years old!
greet("Bob", 25)      =========Bob is 25 years old!
-------------------------------------------
def add(a, b):
    return a + b           ---o/p of function from here given to below where we call function

result = add(5, 3)         ---given to here where function called function
print(result)  # 8





