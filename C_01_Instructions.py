print("Roll it 13")
want_instructions = input("Do you want to read the instructions")
print(f"if you answerd {want_instructions} to the queston")

if want_instructions == "yes" or want_instructions == "y":
    print("You choose yes")
elif want_instructions == "no" or want_instructions == "n" :
    print("you choose no")
else:
    print("not a valid response")
print("you did not choose a valid response")
