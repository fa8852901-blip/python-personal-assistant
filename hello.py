even_number = 0
odd_number = 0

print("Even numbers: ")
for num in range(1, 51):
    if num % 2 == 0:
        print(num)
        even_number += 1

print("Odd numbers: ")
for num in range(1, 51):
    if num % 2 != 0:
        print(num)
        odd_number += 1
    
print(f"Total even numbers: {even_number}")
print(f"Total odd numbers: {odd_number}")