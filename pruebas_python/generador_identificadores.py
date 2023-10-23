import random

characters = ['1', '2', '3', '4', '5', 'A', 'B', 'C', 'D', 'E']
q_list = [random.choice(characters) for _ in range(10)]  # Generate 10 random characters
result = ''.join(q_list)  # Join the characters into a single string
print(result)