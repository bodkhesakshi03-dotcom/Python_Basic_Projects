
import math

def unique_words():
    try:
        sentence = input("Enter sentence: ")
        words = sentence.split()
        unique = set(words)
        
        print("Unique Words:", sorted(unique))
        print("Count^2:", math.pow(len(unique), 2))
    except Exception as e:
        print("Error:", e)

unique_words()
