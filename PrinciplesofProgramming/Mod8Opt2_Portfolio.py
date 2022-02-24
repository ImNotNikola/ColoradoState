# Create players dictionary
players = {}

# Create a function called printMenu to print the menu to the screen.
def printMenu():
    # Create the menu variable.
    menu = """MENU
a - Add player
d - Remove player
u - Update player rating
r - Output players above as rating
o - Output roster
q - Quit
"""
    return menu


def main():
    # Infinite loop
    while True:
        # Print menu
        print(printMenu())
        # Get user input
        letter = raw_input("Choose an option: ")
        #Check if letter is q for quit
        if letter.lower() == 'q':
            # If so, quit the program
            break
        # Else if it's an a for add
        elif letter.lower() == 'a':
           # Get user input
           newJerseyNumber = int(input("Enter a new player's jersey number: "))
           # Get user input
           newPlayerRating = int(input("Enter a new player's rating: "))
           # Check if the player's jersey number is NOT already in the dictionary
           if newJerseyNumber not in players:
                # If it isn't then the player's rating will be added to the jersey number.
               players[newJerseyNumber] = newPlayerRating
           else:
                # Else print player already in the list.
               print("Player is already in the list")
        # Else if the letter is d for delete
        elif letter.lower() == 'd':
            # Get user input
            getUserInputJersey = int(input("Enter a jersey number: "))
            # If player is in the dictionary delete it.
            if getUserInputJersey in players:
               del players[getUserInputJersey]
        # Else if the letter is u for update a player rating
        elif letter.lower() == 'u':
            # Get user input
            getUserInputJersey = int(input("Enter a jersey number: "))
            # Check if jersey number is in player dictionary
            if getUserInputJersey in players:
                # If it is then enter a new player rating
               newPlayerRating = int(input("Enter a new rating for the player: "))
               players[getUserInputJersey] = newPlayerRating
        # Else if letter is r out players above a rating.
        elif letter.lower() == 'r':
            # Get user input
            getPlayerRating = int(input("Enter the player's rating: "))
            # For loop to iterate over keys and values in a sorted dictionary.
            for k,v in sorted(players.items()):
                # If value is greater than what the user input print it to the screen.
                if v > getPlayerRating:
                    print("Jersey number: %d, Rating: %d" % (k,v))
        # Else if letter is o output roster
        elif letter.lower() == 'o':
            # For loop to iterarte over keys and values in a sorted dictionary.
           for k,v in sorted(players.items()):
                # Print ratings out
               print("Jersey number: %d, Rating: %d" % (k,v))
        # For edge cases, if not an option above print an error.
        else:
            print("Not an option")


# Main function
if __name__ == "__main__":
    main()
