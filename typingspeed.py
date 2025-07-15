from time import *
import random as r

def calculate_accuracy(original, typed):
    original_words = original.split()
    typed_words = typed.split()
    correct = 0

    for o, t in zip(original_words, typed_words):
        if o == t:
            correct += 1

    accuracy = (correct / len(original_words)) * 100
    return round(accuracy, 2)

# Shorter test sentences
paragraphs = [
    "Typing is fun.",
    "I love Python.",
    "Practice makes perfect.",
    "Coding improves skills.",
    "Speed tests are useful.",
    "Try your best.",
    "Keep your focus.",
    "Make fewer mistakes."
]

print("******Typing Speed*******")
test = r.choice(paragraphs)
print(test)
print()

input("Press Enter when you're ready to start...\n")

start_time = time()
testinput = input("Enter: ")
end_time = time()

total_time = round(end_time - start_time, 2)
word_count = len(testinput.split())
speed_wpm = round((word_count / total_time) * 60, 2) if total_time > 0 else 0
accuracy = calculate_accuracy(test, testinput)

print("\n----- Results -----")
print(f"Time Taken: {total_time} seconds")
print(f"Your Typing Speed: {speed_wpm} words per minute (WPM)")
print(f"Accuracy: {accuracy}%")

if accuracy < 60:
    print("\nYou made a mistake. Please try again.")
