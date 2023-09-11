def LEFT(string,length):   
    return string[0:length]

def RIGHT(string,length):
    return string[len(string)-length:len(string)]

def MID (string,start,length):
    return string[start-1:start+length-1]
    
def LENGTH (string):
    return len(string)

def LCASE (char):
    if len(char)>1:
        return("ERROR: Input a single character")
    else:
        return(char.lower())
    
def UCASE(char):
    if len(char)>1:
        return("ERROR: Input a single character")
    else:
        return(char.upper())

def TO_UPPER(string):
    return(string.upper())
 
def TO_LOWER(string):
    return(string.lower())
 
def NUM_TO_STRING(num):
    return(str(num))

def STRING_TO_NUM(string):
    try:
        return(int(string))
    except ValueError:
        print("INPUT A NUMBER")

def INT(num):
    return(int(num))

def ASC(char):
    if len(char)>1:
        return("ERROR: Input a single character")
    else:
        return(ord(char))
    

# example function being called    
choice = input('''
What would you like to do?
    1) Return leftmost x characters from a string
    2) Return rightmost x characters from a string
    3) Return a string starting at position x of length y
    4) Return the length of the string
    5) Convert a character to lower case
    6) Convert a character to upper case
    7) Convert a string to upper case
    8) Convert a string to lower case
    9) Convert a number to a string
    10) Convert a string to a number
    11) Convert a float to a integer
    12) Convert a character into ASCII        
               ''')

if choice == "1":
    string = input("Input the string")
    x = int(input("Input the length of the substring"))
    print(LEFT(string,x))
elif choice =="2":
    string = input("Input the string")
    x = int(input("Input the length of the substring"))
    print(RIGHT(string,x))
elif choice =="3":
    string = input("Input the string")
    x = int(input("Input the start position of the substring"))
    y = int(input("Input the length of the substring"))
    print(MID(string,x,y))
elif choice =="4":
    string = input("Input the string")
    print(LENGTH(string))
elif choice =="5":
    character = input("Input the character")
    print(LCASE(character))
elif choice =="6":
    character = input("Input the character")
    print(UCASE(character))
elif choice =="7":
    string = input("Input the string")
    print(TO_UPPER(string))
elif choice =="8":
    string = input("Input the string")
    print(TO_LOWER(string))
elif choice =="9":
    number = int(input("Input the number"))
    print(NUM_TO_STRING(number))
elif choice =="10":
    string = input("Input the string")
    print(STRING_TO_NUM(string))
elif choice =="11":
    float = float(input("Input the float"))
    print(INT(float))
elif choice =="12":
    character = input("Input the character")
    print(ASC(character))
