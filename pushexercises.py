#Exercisesoneandtwo

#Ex1

# Take input from  user
user_input = input("Enter a string: ")

# Print string backward
print("Backward string:", user_input[::-1])



#Ex2
# input from the user
input_string = input('Enter a string: ')

# lowercase letters from the input
lowercase_letters = ''.join([char for char in input_string if char.islower()])

# uppercase letters from the input
uppercase_letters = ''.join([char for char in input_string if char.isupper()])

# Combine lowercase with uppercase letters
result = lowercase_letters + uppercase_letters

# Print result
print(result)
