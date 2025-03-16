#!/usr/bin/env python3

# Python Beginner Quiz - 30 Minutes
# Instructions:
# - This quiz contains 6 questions of varying difficulty
# - You have 30 minutes to complete all questions
# - Try to solve each problem by writing Python code
# - Each question includes the expected output to help you verify your solution

# -------------------------------------------------------
# Question 1 (Low Complexity)
# Write a function called `reverse_string` that takes a string as input and returns the string reversed.
#
# Example:
# Input: "hello"
# Output: "olleh"
# -------------------------------------------------------

def reverse_string(s):
    # Your code here
    return s[::-1]


# -------------------------------------------------------
# Question 2 (Low Complexity)
# Create a function `is_palindrome` that checks if a given string is a palindrome 
# (reads the same backward as forward), ignoring spaces and case.
#
# Example:
# Input: "Race car"
# Output: True
#
# Input: "hello"
# Output: False
# -------------------------------------------------------

def is_palindrome(s):
    # Your code here
    s2= s.lower()
    l2= s2.split()
    s3= ''.join(l2)
    rev = s3[::-1]
  
    if rev ==s3:
        print('True')
    else:
        print('False')


# -------------------------------------------------------
# Question 3 (Medium Complexity)
# Write a function `count_words` that takes a string and returns a dictionary 
# with each word as a key and its frequency as the value. Ignore case and punctuation.
#
# Example:
# Input: "Hello world, hello Python!"
# Output: {'hello': 2, 'world': 1, 'python': 1}
# -------------------------------------------------------

def count_words(str1):
    # Your code here

    str2= str1.lower()
    str2=str1[:-1] 
    text2 = str2.split()
    dict1 = {}
    
    for word in text2:
        dict1[word]= dict1.get(word,0)+1
    print(dict1)
    

# -------------------------------------------------------
# Question 4 (Medium Complexity)
# Create a function `find_missing_number` that takes a list of integers from 1 to n 
# with one number missing, and returns the missing number.
#
# Example:
# Input: [1, 2, 4, 5, 6]
# Output: 3
# -------------------------------------------------------

def find_missing_number(nums):
    # Your code here
    sum1 =sum(nums)
    n =len(nums)
    sum2= (n*(n+1))//2

    return sum1 -sum2


# -------------------------------------------------------
# Question 5 (High Complexity)
# Create a function `group_anagrams` that takes a list of strings and groups anagrams together 
# (words that have the same characters but in a different order).
#
# Example:
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
# -------------------------------------------------------

def group_anagrams(words):
    # Your code here
    ang=dict()
    list2 =words
    
    for word in list2:
        word1=''.join(sorted(word))
        if word1 not in ang:
            ang[word1]=[]
        ang[word1].append(word)
        
    list3=list(ang.values())
    return list3
        
            

# -------------------------------------------------------
# Question 6 (High Complexity)
# Write a function called `validate_sudoku` that takes a 9x9 Sudoku board as a 2D list 
# and returns True if it's a valid Sudoku solution, False otherwise.
#
# A valid Sudoku has:
# - Each row containing digits 1-9 without repetition
# - Each column containing digits 1-9 without repetition
# - Each of the nine 3x3 sub-boxes containing digits 1-9 without repetition
#
# Example (partial board shown for brevity):
# Input: [
#    [5, 3, 4, 6, 7, 8, 9, 1, 2],
#    [6, 7, 2, 1, 9, 5, 3, 4, 8],
#    # ... and so on for all 9 rows
# ]
# Output: True
# -------------------------------------------------------

def validate_sudoku(board):
    # Your code here
    board1 = board
    for row in board1:    
        set1 =set()
        for num in row:
            set1.add(num)
        if len(set1)<9:
            return False
        

    for j in range(len(board1)):
        set2=set()
        for k in range(9):
            set2.add(board1[k][j])    
        if len(set2)<9:
            return False


# Test your functions here
if __name__ == "__main__":
    # Test reverse_string
    print(reverse_string("hello"))  # Should print: olleh
    
    # Test is_palindrome
    print(is_palindrome("Race car"))  # Should print: True
    print(is_palindrome("hello"))  # Should print: False
    
    # Test count_words
    print(count_words("Hello world, hello Python!"))  # Should print: {'hello': 2, 'world': 1, 'python': 1}
    
    # Test find_missing_number
    print(find_missing_number([1, 2, 4, 5, 6]))  # Should print: 3
    
    # Test group_anagrams
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # Should print something like: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    
    # Test validate_sudoku with a valid board (simplified example)
    valid_board = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    print(validate_sudoku(valid_board))  # Should print: True
