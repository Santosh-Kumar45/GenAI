
# PROBLEM 5
# Print numbers from 1 to 20.
# Stop completely when the number reaches 12.
# Skip all even numbers before that point.

for number in range(1, 21):
    if number == 12:
        break
    if number % 2 == 0:
        continue
    print(number)
