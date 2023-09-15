'''
Author: Nagendran Sandraprakasam 
Description: Script to "Count Digit Anagram" and display "Pairs of Anagram" given a source of input
'''

from collections import Counter

# Array of numbers
numbers = [25, 35, 872, 228, 53, 278, 872]  #output 4
#numbers = [10, 12, 21, 0, 112, 121]         #output 2
#numbers = [21, 12, 44, 43, 44]              #output 2
#numbers = [21, 12, 44, 43, 44, 44, 44]      #output 7

# Create list to store Anagram pairs
pairs_of_digit_anagrams = []

# Function to convert numbers to string and compare the values
def compare_numbers(num1, num2):
    str_num1 = str(num1)
    str_num2 = str(num2)

    # Check if the two strings are the same value
    return Counter(str_num1) == Counter(str_num2)

# Loop the Array of numbers and store in the List if values matches
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if compare_numbers(numbers[i], numbers[j]):
            pairs_of_digit_anagrams.append((numbers[i], numbers[j]))

# Output pairs of Digit Anagrams
for pair in pairs_of_digit_anagrams:
    print(f"Pair of digit anagrams: {pair[0]} and {pair[1]}")

# Output Digit Anagram Pairs Count
print(f"Total Digit Anagram Count: {len(pairs_of_digit_anagrams)}")