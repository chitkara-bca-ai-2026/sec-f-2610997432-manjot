
text = input()

# Step 1: Clean the string (remove spaces and convert to lowercase)
cleaned_text = text.replace(" ", "").lower()

# Step 2: Reverse using slicing and compare
if cleaned_text == cleaned_text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
