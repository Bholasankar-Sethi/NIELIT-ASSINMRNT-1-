# 1. Print numbers from 1 to 10
print("1. Numbers 1-10:")
for i in range(1, 11):
    print(i)
print('\n')

# 2. Print even numbers from 1 to 20
print("2. Even numbers 1-20:")
print(*range(2, 21, 2), sep=' ')
print()

# 3. Check if a number is positive, negative or zero
print("3. Number check:")
print("Enter a number")
num = 0  # Example number
print("Positive" if num > 0 else "Negative" if num < 0 else "Zero")
print()

# 4. Add two numbers using operators
print("4. Add two numbers:")
a, b = 5, 3
print(f"{a} + {b} = {a + b}")
print()

# 5. Print multiplication table of a number
print("5. Multiplication table:")
n = 5
for i in range(1, 11):
    print(f"{n} × {i} = {n * i}")


# 6. Find the largest among two numbers
print("6. Largest of two numbers:")
x, y = 8, 12
print(max(x, y))
print()

# 7. Use a while loop to print numbers 5 to 1
print("7. Countdown 5-1:")
i = 5
while i > 0:
    print(i, end=' ')
    i -= 1
print('\n')

# 8. Print all characters in a string
print("8. Print string characters:")
s = "Python"
for char in s:
    print(char, end=' ')
print('\n')

# 9. Use logical operator to check if a number is between 10 and 50
print("9. Range check:")
num = 25
print(10 < num < 50)
print()

# 10. Sum of first 10 natural numbers
print("10. Sum of first 10 naturals:")
print(sum(range(1, 11)))
print()

# 11. Print "Odd" or "Even" for numbers 1 to 10
print("11. Odd/Even for 1-10:")
for i in range(1, 11):
    print(f"{i}: {'Odd' if i % 2 else 'Even'}")
print()

# 12. Use "break" to stop loop when number is 5
print("12. Break at 5:")
for i in range(1, 11):
    if i == 5:
        break
    print(i, end=' ')
print('\n')

# 13. Print 1 to 10 and use continue to skip printing 5
print("13. Skip 5:")
for i in range(1, 11):
    if i == 5:
        continue
    print(i, end=' ')
print()
# 14. Print all elements in a list using a loop
print("14. List elements:")
lst = [10, 20, 30, 40]
for item in lst:
    print(item, end=' ')
print('\n')

# 15. Check if a number is divisible by both 3 and 5
print("15. Divisible by 3 and 5:")
num = 15
print(num % 3 == 0 and num % 5 == 0)
print()

# 16. Square of all numbers from 1 to 5
print("16. Squares 1-5:")
for i in range(1, 6):
    print(i**2, end=' ')
print('\n')

# 17. Print ASCII values of characters in a string
print("17. ASCII values:")
s = "ABC"
print(*(ord(c) for c in s), sep=' ')
print()

# 18. Count down from 10 to 1 using while
print("18. Countdown 10-1:")
i = 10
while i >= 1:
    print(i, end=' ')
    i -= 1
print('\n')

# 19. Check if a number is divisible by 2 or 3
print("19. Divisible by 2 or 3:")
num = 6
print(num % 2 == 0 or num % 3 == 0)
print()

# 20. Print sum of digits of a number
print("20. Sum of digits:")
num = 1234
print(sum(int(d) for d in str(num)))
print()

# 21. Swap two numbers using a temporary variable
print("21. Swap numbers:")
a, b = 5, 10
a, b = b, a  # Pythonic swap (no temp needed)
print(f"a: {a}, b: {b}")
print()

# 22. Print numbers from 1 to 100 that are divisible by 7
print("22. Numbers divisible by 7 (1-100):")
print(*range(7, 101, 7), sep=' ')
print()

# 23. Find the factorial of a number
print("23. Factorial:")
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)
print()

# 24. Count vowels in a string
print("24. Count vowels:")
s = "Hello World"
vowels = sum(1 for c in s.lower() if c in 'aeiou')
print(vowels)
print()

# 25. Reverse a number using loop
print("25. Reverse number:")
num = 1234
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num = num // 10
print(reversed_num)
# 26. Find the maximum in a list using loop
print("26. Maximum in list:")
nums = [4, 2, 9, 7, 5]
max_num = nums[0]
for num in nums[1:]:
    if num > max_num:
        max_num = num
print(max_num)
print()

# 27. Prime number check using loop
print("27. Prime check:")
num = 17
is_prime = num > 1
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        is_prime = False
        break
print(is_prime)
print()

# 28. Sum of even numbers in a list
print("28. Sum of evens:")
nums = [1, 2, 3, 4, 5, 6]
print(sum(n for n in nums if n % 2 == 0))
print()

# 29. Print number pattern using nested loops
print("29. Number pattern:")
for i in range(1, 6):
    print(*range(1, i+1))
print()

# 30. Count frequency of digits in a number
print("30. Digit frequency:")
num = 1223334444
freq = {}
for d in str(num):
    freq[d] = freq.get(d, 0) + 1
print(freq)
print()

# 31. GCD of two numbers using loop
print("31. GCD:")
a, b = 48, 18
while b:
    a, b = b, a % b
print(a)
print()

# 32. Check if a number is a palindrome
print("32. Palindrome check:")
num = 121
print(str(num) == str(num)[::-1])
print()

# 33. Count words in a sentence
print("33. Word count:")
sentence = "Hello world from Python"
print(len(sentence.split()))
print()

# 34. Find common elements in two lists
print("34. Common elements:")
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(list(set(list1) & set(list2)))
print()

# 35. Use elif to grade students based on score
print("35. Grading system:")
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(grade)
print()

# 36. Print a right-angled triangle using *
print("36. Right-angled triangle:")
for i in range(1, 6):
    print('*' * i)
print()

# 37. Check if a year is a leap year
print("37. Leap year check:")
year = 2024
print(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
print()

# 38. Print Fibonacci series using loop
print("38. Fibonacci series:")
n = 10
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
print('\n')

# 39. Count uppercase and lowercase letters in a string
print("39. Letter case count:")
s = "Hello World"
upper = sum(1 for c in s if c.isupper())
lower = sum(1 for c in s if c.islower())
print(f"Uppercase: {upper}, Lowercase: {lower}")
print()

# 40. Print numbers from 100 to 1 using loop
print("40. Countdown 100-1:")
for num in range(100, 0, -1):
    print(num, end=' ')
print()