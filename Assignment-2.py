# 1. Check if a number is prime
def is_prime(n):
  if (n <= 1):
    return False
  for i in range(2, int(n /2)+ 1):
    if(n % i == 0):
      return False
    return True
print("1. Prime or Not:",is_prime(12))

# 2. Area of a rectangle
length, width = 5, 3
print("2. Rectangle area:", length * width)

# 3. Maximum of three numbers
a, b, c = 4, 9, 2
print("3. Max of 3 numbers:", max(a, b, c))

# 4. Reverse a string
s = "hello"
print("4. Reversed string:", s[::-1])

# 5. Count vowels in a string
s = "education"
print("5. Vowel count:", sum(1 for i in s if i.lower() in 'aeiou'))

# 6. Palindrome check
s = "madam"
print("6. Is palindrome:", s == s[::-1])

# 7. Sum of list
lst = [1, 2, 3]
print("7. Sum of list:", sum(lst))

# 8. Fibonacci sequence
n = 5
a, b = 0, 1
fib = []
for _ in range(n):
    fib.append(a)
    a, b = b, a + b
print("8. Fibonacci:", fib)

# 9. Celsius to Fahrenheit
c = 25
print("9. Celsius to F:", (c * 9/5) + 32)

# 10. Minimum in list
lst = [3, 1, 4]
print("10. Min in list:", min(lst))

# 11. Count char in string
s, ch = "banana", "a"
print("11. Count char:", s.count(ch))

# 12. Perfect number check
n = 28
print("12. Is perfect:", sum(i for i in range(1, n) if n % i == 0) == n)

# 13. Sum of digits
n = 123
print("13. Digit sum:", sum(int(i) for i in str(n)))

# 14. Char frequency
s = "apple"
d = {}
for i in s:
    d[i] = d.get(i, 0) + 1
print("14. Char freq:", d)

# 15. Average of list
lst = [4, 6, 8]
print("15. Average:", sum(lst)/len(lst))

# 16. Multiplication table
n = 3
print("16. Table:")
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

# 17. Reverse list
lst = [1, 2, 3]
print("17. Reversed list:", lst[::-1])

# 18. Second largest number
lst = [4, 7, 1, 7]
print("18. Second largest:", sorted(set(lst))[-2])

# 19. Even numbers from list
lst = [1, 2, 3, 4]
print("19. Evens:", [i for i in lst if i % 2 == 0])

# 20. Unique characters check
s = "abcd"
print("20. All unique:", len(set(s)) == len(s))

# 21. GCD of two numbers
a, b = 54, 24
while b:
    a, b = b, a % b
print("21. GCD:", a)

# 22. LCM of two numbers
a, b = 4, 6
gcd = a
b2 = b
while b2:
    gcd, b2 = b2, gcd % b2
print("22. LCM:", abs(a * b) // gcd)

# 23. Remove duplicates
lst = [1, 2, 2, 3]
print("23. No duplicates:", list(set(lst)))

# 24. Factorial (recursive)
def fact(n): return 1 if n == 0 else n * fact(n - 1)
print("24. Factorial:", fact(5))

# 25. Armstrong number check
n = 153
print("25. Is Armstrong:", n == sum(int(i)**len(str(n)) for i in str(n)))

# 26. All primes up to n
n = 10
print("26. Primes:", [i for i in range(2, n+1) if all(i % j != 0 for j in range(2, int(i**0.5)+1))])

# 27. Longest word in sentence
s = "Python is awesome"
print("27. Longest word:", max(s.split(), key=len))

# 28. Power using recursion
def power(x, y): return 1 if y == 0 else x * power(x, y-1)
print("28. Power:", power(2, 3))

# 29. Flatten nested list
def flatten(lst):
    r = []
    for i in lst:
        if isinstance(i, list): r += flatten(i)
        else: r.append(i)
    return r
print("29. Flattened:", flatten([1, [2, [3]]]))

# 30. List sorted check
lst = [1, 2, 3]
print("30. Is sorted:", lst == sorted(lst))

# 31. Merge sorted lists
l1, l2 = [1, 3], [2, 4]
print("31. Merged:", sorted(l1 + l2))

# 32. Most frequent element
lst = [1, 2, 2, 3]
print("32. Most frequent:", max(set(lst), key=lst.count))

# 33. Median of list
lst = [3, 1, 2]
s = sorted(lst)
l = len(s)
print("33. Median:", s[l//2] if l % 2 else (s[l//2 - 1] + s[l//2])/2)

# 34. Intersection of lists
l1, l2 = [1, 2, 3], [2, 3, 4]
print("34. Intersection:", list(set(l1) & set(l2)))

# 35. Product of args
def prod(*args):
    r = 1
    for i in args: r *= i
    return r
print("35. Product:", prod(2, 3, 4))

# 36. List of (element, index)
lst = ['a', 'b', 'c']
print("36. Tuples:", [(v, i) for i, v in enumerate(lst)])

# 37. Word count in string
s = "hello world hello"
d = {}
for w in s.split(): d[w] = d.get(w, 0) + 1
print("37. Word count:", d)

# 38. Pangram check
s = "The quick brown fox jumps over the lazy dog"
print("38. Is pangram:", set('abcdefghijklmnopqrstuvwxyz') <= set(s.lower()))

# 39. Index of value
lst = [1, 2, 3]
val = 2
print("39. Index of val:", lst.index(val) if val in lst else -1)

# 40. Count upper and lower case
s = "Hello World"
u = sum(1 for i in s if i.isupper())
l = sum(1 for i in s if i.islower())
print("40. UPPER/lower:", f"{u} upper, {l} lower")