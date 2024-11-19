import os

def read_file_name():
    print("Welcome to the News Analyzer!")
    print("This program will help you analyze news headlines from a file of your choice.")



    f_name = input("Enter file name: ")
    while not os.path.isfile(f_name):
            f_name = input(f"Error: The file '{f_name}' does not exist.")
    return f_name

def read_file(f_name):
    file = open(f_name, "r")
    return file.readlines()

def line_shortest(file):
    longest_line = ""
    shortest_line = None
    for line in file:
        line = line.strip()
        if shortest_line is None or len(line) < len(shortest_line):
            shortest_line = line
        if len(line) > len(longest_line):
            longest_line = line
    print(f' the shortest line is {shortest_line}')
    print(f' the longest line is {longest_line}')

def word_finder(lines):
    counter = 0
    target_word = input('enter target word: ').strip()
    for line in lines:
        words = line.split()
        for word in words:
            if word.lower() == target_word.lower():
                counter += 1
    print(f"{target_word} appears {counter} times in file")
    return counter

def write_headlines_with_word(lines, file):
    with open(file, "w") as file:
        keyword = input("Enter keyword: ")
        for line in lines:
            if keyword.lower() in line.lower():
                file.write(line + "\n")

def average_headline_length(lines):
    total_length = sum(len(line) for line in lines)
    average_length = total_length / len(lines)
    print(f'Average length of a headline is {average_length}')

def menu():
    print("\nMenu:")
    print("1. Count headlines containing a specific word")
    print("2. Write headlines containing a specific word to a new file")
    print("3. Calculate the average length of headlines")
    print("4. Find the longest and shortest headline")
    print("5. Load a new file")
    print("6. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        line_shortest(read_file_name())
    elif choice == "2":
        word_finder(read_file_name())
    elif choice == "3":
        write_headlines_with_word(read_file_name())
    elif choice == "4":
        average_headline_length(read_file_name())
    elif choice == "5":
        print("Thanks for using News Analyzer!")
    else:
        print("Invalid input. Please try again.")


def main():
    read_file_name()
    read_file()
    line_shortest(read_file_name())
    word_finder(read_file_name())
    average_headline_length(read_file_name())
    write_headlines_with_word(read_file_name(), read_file_name())
main()