# Task 1: Print numbers from 1 to 10 using a for loop
print("--- Task 1 ---")
for i in range(1,11):
    print(i)
    
    
# Task 2: print numbers from 10 to 1 using a while loop
print("--- Task 2 ---")
num = 10
while num >= 1:
    print(num)
    num -= 1 

# Task 3: Print the multiplication of 5
print("\n--- Task 3 ---")
for i in range(1,11):
    print(f"5 x {i} = {5 * i}")
    
# Task 4: Calculate the sum of numbers from 1 to 10
print("\n--- Task 4 ---")
total_sum = 0
for i in range(1, 11):
    total_sum += i
print("Sum of 1 to 10 is:", total_sum)

# Task 5: Print all even numbers from 1 to 20
print("\n--- Task 5 ---")
for i in range(2, 21, 2):
    print(i)