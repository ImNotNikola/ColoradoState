# Get user input first color.
primaryColorA = input("Enter first primary color: ")
# Check if color is correct, no point in continuing if not correct.
if primaryColorA in ['red', 'blue', 'yellow']:
    # Get User input second color.
    primaryColorB = input("Enter second primary color: ")
    # Check if second color is correct.
    if primaryColorB in ['red', 'blue', 'yellow']:
        # Check if blue red or red blue.
        if primaryColorB == 'blue' and primaryColorA == 'red' or primaryColorB == 'red' and primaryColorA == 'blue':
            # If so, print Purple.
            print("Red and Blue makes Purple")
        # Check if blue yellow or yellow blue.
        elif primaryColorB == 'blue' and primaryColorA == 'yellow' or primaryColorB == 'yellow' and primaryColorA == 'blue':
            # If so, print Green.
            print("Blue and Yellow makes Green")
        # Check if red yellow or yellow red    
        elif primaryColorB == 'red' and primaryColorA == 'yellow' or primaryColorB == 'yellow' and primaryColorA == 'red':
            #If so, print Orange
            print("Red and Yellow makes Orange")
        # If it's the same color, it lives here.    
        else:
            # Print same color.
            print("Same color, can't mix and make something new.")
    # Error checking for second color.
    else:
      #Print out the error.  
      print("You did not choose red, blue, or yellow for your second color.")          
# Error checking for first color.
else:
    # Print out the error.
    print("You did not choose red, blue, or yellow for your first color.”)
