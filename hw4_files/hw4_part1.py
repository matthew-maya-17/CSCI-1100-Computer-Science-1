# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 13:57:02 2019

@author: matth
"""
"""The objective of this program is ask the user for a password and see if it satisfies 
all five rules in order to be valid or else the computer will suggest a password"""

"""The objective of this function is to define the restrictions and properties for rule 1"""
def rule_1(password):
    is_long_enough = len(password) <= 25 and len(password) >= 10
    if is_long_enough and password[0].isalpha(): #isalpha() function returns true if the first character of password iis a letter otherwise returns false
        return True
    
    return False

"""The objective of this function is to define the restrictions and properties for rule 2"""
def rule_2(password):
    if (password.find("@") >= 0 or password.find("$") >= 0) and password.find("%") < 0:
        return True
    return False

"""The objective of this function is to define the restrictions and properties for rule 3"""
def rule_3(password):
    uppercase_value = False
    lowercase_value = False
    numeric_value = False
    for char in password:
        if char.isupper():
            uppercase_value = True
        elif char.islower():
            lowercase_value = True
        elif char.isnumeric():
            if int(char) <= 4 and int(char) >= 1:
                numeric_value = True

    if (uppercase_value == True and lowercase_value == True) or numeric_value == True:
        return True
    
    return False

"""The objective of this function is to define the restrictions and properties for rule 4"""
def rule_4(password):
    uppercase_call = True
    i = 1
    for val in range(0,len(password)):
        if password[val].isupper():
            if password.find("_",val,val+i):
                uppercase_call = False
                i+=1
    return uppercase_call

"""The objective of this function is to define the restrictions and properties for rule 5"""
def rule_5(password): 
    for char in password: 
        if char.isnumeric():
            if char > '4' or char < '1':
                return False

    return True 

if __name__ == "__main__":
#if and else statements that prints whether the rule is satisfied or not depending on what is returned for each function correlating to each rule    
    password = str(input("Enter a password => "))
    print(password)
    if rule_1(password) == True:
        print("Rule 1 is satisfied")
    else:
        print ("Rule 1 is not satisfied")
    if rule_2(password) == True:
        print("Rule 2 is satisfied")
    else:
        print("Rule 2 is not satisfied")
    if rule_3(password) == True:
        print("Rule 3 is satisfied")
    else:
        print("Rule 3 is not satisfied")
        
    if rule_4(password) == True:
        print("Rule 4 is satisfied")
    else:
        print("Rule 4 is not satisfied")
    
    if rule_5(password) == True:
        print("Rule 5 is satisfied")
    else:
        print("Rule 5 is not satisfied")

#if statement which states if all rules are True then it prints the password is valid
    if rule_1(password) and rule_2(password) and rule_3(password) and rule_4(password) and rule_5(password):
        print("The password is valid")
#if statement which states if rule 1 is satisfied but the others are not then the computer will suggest a password with 42 in between 8 characters on both sides       
    elif rule_1(password):
        pass_list = list(password)
        if len(pass_list):
            pass_list = pass_list[0:8]
            pass_list.append('4')
            pass_list.append('2')
            almost_final_string = pass_list + list(password)[len(password)-8:len(password)]
            final_string = ''.join(almost_final_string)
        print("A suggested password is: " + final_string)
#if neither all are satisfied or rule one isnt satisfied then print The password is not valid
    else:
        print("The password is not valid")
        