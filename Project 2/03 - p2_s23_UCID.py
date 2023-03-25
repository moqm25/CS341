# Name - UCID
# CS 341 - 006

'''This program was tested on the NJIT AFS machines and it worked successfully there'''

print(
'''Project 2 for CS 341
Section number: 006
Semester: Spring 2023
Written by: Name, UCID
Instructor: Marvin Nakayama, marvin@njit.edu


(This program was tested on the NJIT AFS machines and it worked successfully there)
''')

COLORS = dict(list(zip(["red", "green", "yellow"], [31, 32, 33],)))

if input("\nWould you like to enter a string (enter 'y' or 'n'): ") != 'y':
    exit()

results = {}


'''outer while loop runs continously until user inputer 'n' and the loop breaks'''
while True:
    success = True
    input_string = input("Enter string: ")
    
    l = [*input_string]

    STATE = 1
    stack = []
    i = 0
    print()
    '''while loop which iterates over each character in the string'''
    while i < len(l):
        pop = "ε"
        push = "ε"

        if STATE==1:
            print("\033[%dm%s" %
                    (COLORS['yellow'], f"...State Q1: {l[i]}") + "\033[0m")
            print(f"Stack: {stack}")
            if l[i] == '$':
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: {l[i]}") + "\033[0m")
                stack.append('$')
                STATE = 2
            else:
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: ε") + "\033[0m")                
                success=False
        elif STATE==2:
            print("\033[%dm%s" %
                (COLORS['yellow'], f"...State Q2: {l[i]}") + "\033[0m")
            print(f"Stack: {stack}")

            if l[i] == '$':
                
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: {l[i]}") + "\033[0m")
                stack.append('$')
                STATE = 3
            else:
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: ε") + "\033[0m")  
                success=False
        elif STATE==3:
            print("\033[%dm%s" %
                (COLORS['yellow'], f"...State Q3: {l[i]}") + "\033[0m")
            print(f"Stack: {stack}")

            if  l[i] == '.':
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: ε") + "\033[0m")
                STATE = 5
            elif l[i].isdigit() and int(l[i]) >= 0:
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: ε") + "\033[0m")
                STATE = 4
            elif l[i] == '(':
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: {l[i]}") + "\033[0m")
                stack.append('(')
                STATE = 7
            else:
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: ε") + "\033[0m")  
                success=False


        elif STATE==4:
            print("\033[%dm%s" %
                (COLORS['yellow'], f"...State Q4: {l[i]}") + "\033[0m")
            print(f"Stack: {stack}")

            if l[i] == '.':
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: ε") + "\033[0m")
                STATE = 5
            elif l[i].isdigit() and int(l[i]) >= 0:
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: ε") + "\033[0m")
                STATE = 4
            elif l[i] == '(':
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: {l[i]}") + "\033[0m")
                stack.append('(')
                STATE = 7
            else:
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: ε") + "\033[0m")
                success=False


        elif STATE==5:
            print("\033[%dm%s" %
                (COLORS['yellow'], f"...State Q5: {l[i]}") + "\033[0m")

            print(f"Stack: {stack}")

            if l[i].isdigit() and int(l[i]) >= 0:
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: ε") + "\033[0m")
                STATE = 5

            elif l[i] == '(':
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: {l[i]}") + "\033[0m")
                stack.append('(')
                STATE = 7

            elif l[i] == ')' and stack and stack[-1] == '(':
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: {l[i]} - Symbol Pushed: ε") + "\033[0m")
                stack.pop()
                STATE = 8

            elif l[i] in '+ - / *':
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: ε") + "\033[0m")
                STATE = 6

            elif l[i] == '$' and stack and stack[-1] == '$':
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: {l[i]} - Symbol Pushed: ε") + "\033[0m")
                stack.pop()
                STATE = 9

            else:
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: ε") + "\033[0m")
                success=False
        elif STATE==6:
            print("\033[%dm%s" %
                (COLORS['yellow'], f"...State Q6: {l[i]}") + "\033[0m")
                
            print(f"Stack: {stack}")

            if l[i].isdigit() and int(l[i]) >= 0:
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: ε") + "\033[0m")
                STATE = 4

            elif l[i] == '.':
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: )") + "\033[0m")
                stack.append(')')
                STATE = 8

            elif l[i] == '(':
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: {l[i]}") + "\033[0m")
                stack.append('(')
                STATE = 7
            else:
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: ε") + "\033[0m")
                success=False
        elif STATE==7:
            print("\033[%dm%s" %
                (COLORS['yellow'], f"...State Q7: {l[i]}") + "\033[0m")
           
            print(f"Stack: {stack}")
            
            if l[i] == '(':
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: {l[i]}") + "\033[0m")
                stack.append('(')
                STATE = 7
         
            elif l[i].isdigit() and int(l[i]) >= 0:
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: ε") + "\033[0m")
                STATE = 4
          
            elif l[i] == '.':
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: ε") + "\033[0m")
                STATE = 5
            
            elif l[i] in '+-/*':
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: ε") + "\033[0m")
                STATE = 6
           
            else:
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: ε") + "\033[0m")
                success=False
        
        
        elif STATE==8:
            print("\033[%dm%s" %
                (COLORS['yellow'], f"...State Q8: {l[i]}") + "\033[0m")
            
            print(f"Stack: {stack}")
            
            if l[i] == ')' and stack and stack[-1] == '(':
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: {l[i]} - Symbol Pushed: ε") + "\033[0m")
                stack.pop()
                STATE = 8
            
            elif l[i].isdigit() and int(l[i]) >= 0:
                if stack and stack[-1] == ')':
                    print("\033[%dm%s" %
                        (COLORS['yellow'], f"......Symbol popped: ) - Symbol Pushed: ε") + "\033[0m")
                    stack.pop()
                    STATE = 5
                else:
                    print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: ε") + "\033[0m")
                    STATE = 4
            
            elif l[i] in '+-/*':
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: ε") + "\033[0m")
                STATE = 6
            
            elif l[i] == '(':
                
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: {l[i]}") + "\033[0m")

                stack.append('(')
                STATE = 7
            
            elif l[i] == '$' and stack and stack[-1] == '$':
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: {l[i]} - Symbol Pushed: ε") + "\033[0m")

                stack.pop()
                STATE = 9
            
            else:
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: ε") + "\033[0m")
                success=False


        elif STATE == 9 :
            print("\033[%dm%s" %
                (COLORS['yellow'], f"...State Q8: {l[i]}") + "\033[0m")
            
            print(f"Stack: {stack}")

            if l[i] == '$' and stack and stack[-1] == '$':
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: {l[i]} - Symbol Pushed: ε") + "\033[0m")
                
                stack.pop()
                STATE = 10
                success=True
                results[input_string] = "Success"  
            else:
                print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Symbol popped: ε - Symbol Pushed: ε") + "\033[0m")
                success=False
        else:
            break
    
        i+=1
        if not success:
            break

    if success:
        print("\033[%dm%s" %
            (COLORS['green'], f"\n**String: '{input_string}' is a valid string**") + "\033[0m")
    else:
        print("\033[%dm%s" %
          (COLORS['red'], f"\n**String: '{input_string}' is an invalid string**") + "\033[0m") 
        results[input_string] = "Failure"        

    if input("\nWould you like to enter a string (enter 'y' or 'n'): ") != 'y':
        break

print("\n\n-=-=-=-=-=-=-=-=-= Final Results =-=-=-=-=-=-=-=-=-")

'''prints out all the strings run'''
for x in results:
    if (results[x] == "Failure"):
        print("\033[%dm%s" %
              (COLORS['red'], f"{x} : {results[x]}") + "\033[0m")
    else:
        print("\033[%dm%s" %
              (COLORS['green'], f"{x} : {results[x]}") + "\033[0m")