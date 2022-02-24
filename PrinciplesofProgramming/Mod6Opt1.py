# Import sys library to get file input
import sys
# Get file name from command line
file = sys.argv[1]
# Open the file
text = open(file)
# List with the correct answers
correctAnswers = ['A','C','A','A','D','B','C','A','C','B','A','D','C','A','D','C','B','B','D','A']
# Empty list to be added to
studentsAnswers = []
# Initiating variable
correctAnswerCount = 0
# Initiating variable
wrongAnswerCount = 0
# Iterating over file to grab answers
for answer in text.read().split():
    # Appending to next index and making it uppercase
    studentsAnswers.append(answer.upper())
# Iterating through question 1 to 20     
for question in range(0,20):
    # Check if answer is correct
    if correctAnswers[question] == studentsAnswers[question]:
        # If correct print it to the screen
        print("Answer is correct.")
        # Add one to counter
        correctAnswerCount += 1
    # Else, if the question is wrong.
    else:
        # Print that out with the correct answer.
        print("The correct answer for question {0} is {1}".format(correctAnswers[question], studentsAnswers[question]))
        # Add one to the counter
        wrongAnswerCount += 1
# Print number of correct answers        
print("You answered {} questions correctly".format(correctAnswerCount))
# Print number of incorrect answers
print("You answered {} questions wrong".format(wrongAnswerCount))
# Check if passed.
if correctAnswerCount >= 15:
    # Print passed.
    print("You passed!")
# Didn't pass.
else:
    # Print didn't pass
    print("You did not pass :(")
