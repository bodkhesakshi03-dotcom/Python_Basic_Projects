def analyze_string(s):
    if not s:  # handle empty string
        print("Empty string provided.")
        return
    
    print("Length:", len(s))  # length
    print("Reversed:", s[::-1])  # reverse
    
    vowels = "aeiouAEIOU"
    count = sum(1 for ch in s if ch in vowels)
    print("Vowel count:", count)  # vowel count
    
    # print each character with indices
    for i in range(len(s)):
        print(f"Char: {s[i]}, +Index: {i}, -Index: {i - len(s)}")

# Sample run
user_input = input("Enter a string: ")
analyze_string(user_input)