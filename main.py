import os


def read_file_name():
    print("Welcome to the News Analyzer!")
    print("This program will help you analyze news headlines from a file of your choice.")

    f_name = input("Enter file name: ")
    while not os.path.isfile(f_name):
        f_name = input(f"Error: The file '{f_name}' does not exist. Please try again: ")
    return f_name


def read_file(f_name):
    with open(f_name, "r") as file:
        return file.readlines()


def line_shortest(lines):
    longest_line = ""
    shortest_line = None
    for line in lines:
        line = line.strip()
        if shortest_line is None or len(line) < len(shortest_line):
            shortest_line = line
        if len(line) > len(longest_line):
            longest_line = line
    print(f'The shortest headline is: "{shortest_line}"')
    print(f'The longest headline is: "{longest_line}"')


def word_finder(lines):
    target_word = input('Enter target word: ').strip()
    counter = 0
    for line in lines:
        words = line.split()
        for word in words:
            if word.lower() == target_word.lower():
                counter += 1
    print(f'"{target_word}" appears {counter} times in the file.')


def write_headlines_with_word(lines):
    keyword = input("Enter keyword: ")
    output_file = input("Enter the name of the output file: ").strip()
    with open(output_file, "w") as file:
        for line in lines:
            if keyword.lower() in line.lower():
                file.write(line + "\n")
    print(f"Headlines containing the word '{keyword}' have been written to {output_file}.")


def average_headline_length(lines):
    if not lines:
        print("No headlines to analyze.")
        return

    total_length = sum(len(line) for line in lines)
    average_length = total_length / len(lines)
    print(f'Average length of a headline is {average_length:.2f} characters.')


def main():
    file_name = read_file_name()
    lines = read_file(file_name)

    while True:
        print("\nMenu:")
        print("1. Count headlines containing a specific word")
        print("2. Write headlines containing a specific word to a new file")
        print("3. Calculate the average length of headlines")
        print("4. Find the longest and shortest headline")
        print("5. Load a new file")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            word_finder(lines)
        elif choice == "2":
            write_headlines_with_word(lines)
        elif choice == "3":
            average_headline_length(lines)
        elif choice == "4":
            line_shortest(lines)
        elif choice == "5":
            file_name = read_file_name()
            lines = read_file(file_name)
        elif choice == "6":
            print("Thanks for using News Analyzer!")
            break
        else:
            print("Invalid input. Please try again.")


main()