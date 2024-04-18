from collections import Counter
import sys

def get_top_words(file_path, n=5):
    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
            word_counts = Counter(words)
            top_words = word_counts.most_common(n)
            return top_words
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)

def main():
    file_path = input("Enter the path to the text file: ")
    top_words = get_top_words(file_path)
    if top_words:
        print("Top 5 most common words:")
        for word, count in top_words:
            print(f"{word}: {count}")

if __name__ == "__main__":
    main()