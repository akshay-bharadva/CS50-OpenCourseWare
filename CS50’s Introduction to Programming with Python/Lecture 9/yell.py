def main():
    yell("This", "is", "CS50")


def yell(*words):
    upper_words = map(str.upper, words)
    print(*upper_words)

if __name__ == "__main__":
    main()
