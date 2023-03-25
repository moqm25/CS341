# Name - UCID
# CS 341 - 006

'''This program was tested on the NJIT AFS machines and it worked successfully there'''

print(
    '''Project 1 for CS 341
Section number: 006
Semester: Spring 2023
Written by: Name - UCID
Instructor: Marvin Nakayama, marvin@njit.edu



(This program was tested on the NJIT AFS machines and it worked successfully there)
''')

'''Defining the alphabet'''
Σ = {
    "Ψ": {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'},
    "Υ": {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'},
    "∆": {'.'},
    "Θ": {'@'}
}


COLORS = dict(list(zip(["red", "green", "yellow"], [31, 32, 33],)))

results = {}


if input("\nWould you like to enter a string (enter 'y' or 'n'): ") != 'y':
    exit()

'''outer while loop runs continously until user inputer 'n' and the loop breaks'''
while True:
    success = False
    string = input("Enter string: ")
    l = [*string]

    STATE = 1

    i = 0
    print()
    '''while loop which iterates over each character in the string'''
    while i < len(l):
        
        '''start state which checks if the next character is a character a...z'''
        if STATE == 1:
            print("\033[%dm%s" %
                    (COLORS['yellow'], f"...State q1") + "\033[0m")
            print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Checking letter {l[i]}") + "\033[0m")

            if (l[i] in Σ["Ψ"]):
                STATE = 2
            else:
                STATE = "other"
            
            '''State 2 which checks if it's a character or number, if so, stays in state 2. if its a dot, it goes to state 1. if its an @ sign, it goes to 3 '''
        elif STATE == 2:
            print("\033[%dm%s" %
                    (COLORS['yellow'], f"...State q2") + "\033[0m")
            print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Checking letter {l[i]}") + "\033[0m")

            if (l[i] in Σ["Ψ"] or l[i] in Σ["Υ"]):
                STATE = 2
            elif (l[i] in Σ["∆"]):
                STATE = 1
            elif (l[i] in Σ["Θ"]):
                STATE = 3
            else:
                STATE = "other"

            '''state 3, if a letter, goes to state 4'''
        elif STATE == 3:
            print("\033[%dm%s" %
                    (COLORS['yellow'], f"...State q3") + "\033[0m")
            print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Checking letter {l[i]}") + "\033[0m")

            if (l[i] in Σ["Ψ"]):
                STATE = 4
            else:
                STATE = "other"
            
            '''state 4 checks if there is a dot, goes to state 5, if number/letter, goes to state 4 '''
        elif STATE == 4:
            print("\033[%dm%s" %
                    (COLORS['yellow'], f"...State q4") + "\033[0m")
            print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Checking letter {l[i]}") + "\033[0m")

            if (l[i] in Σ["∆"]):
                STATE = 5
            elif (l[i] in Σ["Ψ"] or l[i] in Σ["Υ"]):
                STATE = 4
            else:
                STATE = "other"

            '''state 5, if the letter 'e' then state 6, if a letter other than e, then state 4'''
        elif STATE == 5:
            print("\033[%dm%s" %
                    (COLORS['yellow'], f"...State q5") + "\033[0m")
            print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Checking letter {l[i]}") + "\033[0m")

            if (l[i] == 'e'):
                STATE = 6
            elif (l[i] in Σ["Ψ"]):
                STATE = 4
            else:
                STATE = "other"

            '''state 6, if the letter 'd' then state 7, if a letter/number other than d, then state 4, if dot, state 5'''
        elif STATE == 6:
            print("\033[%dm%s" %
                    (COLORS['yellow'], f"...State q6") + "\033[0m")
            print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Checking letter {l[i]}") + "\033[0m")

            if (l[i] == 'd'):
                STATE = 7
            elif (l[i] in Σ["Ψ"] or l[i] in Σ["Υ"]):
                STATE = 4
            elif (l[i] in Σ["∆"]):
                STATE = 5
            else:
                STATE = "other"

            '''state 7, if the letter 'u' then state 8 and checks if its the final letter, if a letter/number other than u, then state 4, if dot, state 5'''
        elif STATE == 7:
            print("\033[%dm%s" %
                    (COLORS['yellow'], f"...State q7") + "\033[0m")
            print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Checking letter {l[i]}") + "\033[0m")

            if (l[i] == 'u'):
                print("\033[%dm%s" %
                        (COLORS['yellow'], f"...State q8") + "\033[0m")

                STATE = 8
                if (i == len(string)-1):
                    print("\033[%dm%s" %
                            (COLORS['yellow'], f"......String Exhausted (no letters remaining)") + "\033[0m")
                    print("\033[%dm%s" %
                            (COLORS['green'], f"\n** String {string} was Successful **") + "\033[0m")

                    results[string] = "Success"
                    success = True
                    break
                elif (l[i] in Σ["Ψ"] or l[i] in Σ["Υ"]):
                    STATE = 4
                elif (l[i] in Σ["∆"]):
                    STATE = 5
                else:
                    STATE = "other"

            elif (l[i] in Σ["Ψ"] or l[i] in Σ["Υ"]):
                STATE = 4
            elif (l[i] in Σ["∆"]):
                STATE = 5
            else:
                STATE = "other"
            
            '''state 8, if another letter/number, go to state 4, if dot, state 5'''
        elif STATE == 8:
            print("\033[%dm%s" %
                    (COLORS['yellow'], f"...State q8") + "\033[0m")
            print("\033[%dm%s" %
                    (COLORS['yellow'], f"......Checking letter {l[i]}") + "\033[0m")

            if (l[i] in Σ["Ψ"] or l[i] in Σ["Υ"]):
                STATE = 4
            elif (l[i] in Σ["∆"]):
                STATE = 5
            else:
                STATE = "other"

        else:
            break
        i += 1

    print("\033[%dm%s" %
          (COLORS['red'], f"\n**String: '{string}' is an invalid string**") + "\033[0m") if (not success) else print()

    if ((not success)):
        results[string] = "Failure"

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
