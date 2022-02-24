# Create list
weights = []
# Get user input and put it in the list
for i in range(0,4):
    # Add the input to the last index
    weights.append(float(input("Enter weight in pounds: ")))
# Print out the list
print("Weights: ", weights)
# Print out the average weight
print("Average weight: {:.2f}".format(sum(weights)/4))
# Print out the max weight
print("Max Weight: {:.2f}".format(max(weights)))
