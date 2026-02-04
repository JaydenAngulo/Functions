# Challenge 1:

# PROCEDURE calculator(a,b)
# {
#  DISPLAY(a + b)
#  DISPLAY(a - b)
#  DISPLAY(a / b)
#  DISPLAY(a * b)
# }

# calculator(a,b)

def calculator(a,b):
    print(a + b)
    print(a - b)
    print(a / b)
    print(a * b)

calculator(a,b)

# Challenge 2:

# PROCEDURE average_finder(a,b,c)
# {
# sum <- a + b + c
# average <- sum / 3
# RETURN(average)
# }

# average_finder(a,b,c)

# DISPLAY(average)

def average_finder(a,b,c):
    sum = a + b + c
    average = sum / 3
    return average

average_finder(a,b,c)

print(average)

# Challenge 3:

# PROCEDURE is_even(a):
# {
#  IF(a % 2 == 0)
#  {
#   RETURN("Even")
#   DISPLAY("Even")
#  }
#  IF(a % 2 == 1)
#  {
#   RETURN("Odd")
#   DISPLAY("Odd")
#  }
# }

# is_even(a)

def is_even(a):
    if a % 2 == 0:
        return "Even"
        print("Even")
    if a % 2 == 1:
        return "Odd"
        print("Odd")

is_even(a)

# Challenge 4:

# PROCEDURE analyze_word(word):
# {
#  IF(type(word) == "string")
#  {
#  vowelCount <- 0
#  consonantCount <- 0
#  vowels <- ["a", "e", "i", "o", "u"]
#  FOR ch IN word
#  {
#   IF(ch in vowels)
#   {
#    vowelCount += 1
#   }
#   ELSE
#   {
#    consonantCount += 1
#   }
#  }
#  statement <- f"There are {vowelCount} vowels and {consonantCount} consonants"
#  RETURN(statement)
#  }
# }

# analyze_word(word)
# print(statement)

def analyze_word(word):
    vowelCount = 0
    consonantCount = 0
    vowels = ["a", "e", "i", "o", "u"]
    for ch in word:
        if ch in vowels:
            vowelCount += 1
        else:
            consonantCount += 1
    statement = f"There are {vowelCount} vowels and {consonantCount} consonants."
    return statement

analyze_word(word)
print(statement)