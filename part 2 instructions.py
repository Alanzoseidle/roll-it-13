#check users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input("Do you want to read the instructions? ").lower

        if response == "yes":
            return "yes"
        elif response == "no":
            return "no"
        else:
            print("You did not choose a valid response")




def instruction():
    print('''

**** instructions ****

Do something
and then do something else
etc

     ''')


# Main routine
print()
print("Roll it 13")
want_instructions = input("Do you want to read the instructions")
print()

print(f"if you answerd {want_instructions} to the queston")


def instructions():
    pass

if want_instructions == "yes" or want_instructions == "y":
     instructions()

elif want_instructions == "no" or want_instructions == "n":
    print("you choose no")
else:
    print("not a valid response")
print("you did not choose a valid response")
