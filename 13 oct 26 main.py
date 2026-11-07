# Check if a number is an Armstrong number
text = "race"

# Check if text is equal to its reverse
if text == text[::-1]:
    print(f"'{text}' is a palindrome!")
else:
    print(f"'{text}' is NOT a palindrome.")
# A dictionary where values are words
word_dict = {
    "word1": "madam",
    "word2": "python",
    "word3": "racecar",
    "word4": "hello"
}

# Loop through the dictionary to check each value
for key, word in word_dict.items():
    if word == word[::-1]:
        print(f"'{word}' (at key '{key}') is a palindrome!")
    else:
        print(f"'{word}' (at key '{key}') is NOT a palindrome.")
# Check if a number is an Armstrong number
num = 153
num_str = str(num)
power = len(num_str)

total_sum = 0
for digit in num_str:
    total_sum += int(digit) ** power

if total_sum == num:
    print(f"{num} is an Armstrong number!")
else:
    print(f"{num} is NOT an Armstrong number.")
