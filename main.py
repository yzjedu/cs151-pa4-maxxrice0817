# Programmers:  Max Rice
# Course:  CS151, Dr. Yalew
# Due Date: 11/22
# Programming Assignment: PA 4
# Problem Statement: analyze data from a list of news headlines from a given year
# Data In: file name and menu option
# Data Out: menu option
# Credits: readme and notes 19-27

import os

#purpose:to read file of users choice
# Parameters: none
# Return: f_name
def read_file_name():
    print("This program will help you analyze news headlines from a file of your choosing.")
    f_name = input("Enter a file name: ")
    while not os.path.isfile(f_name):
        f_name = input(f"Error: The file '{f_name}' does not exist. Please try again: ")
    return f_name

# Purpose: open file
# Parameters: f_name
# Return: file.readlines()
def read_file(f_name):
    with open(f_name, "r") as file:
        return file.readlines()

# Purpose: find longest and shortest line
# Parameters: f_name
# Return: nothing
def line_shortest_longest(lines):
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

# Purpose: find how many times a word is in a file
# Parameters: lines
# Return: nothing
def word_finder(lines):
    target_word = input('Enter target word: ').strip()
    counter = 0
    for line in lines:
        words = line.split()
        for word in words:
            if word.lower() == target_word.lower():
                counter += 1
    print(f'"{target_word}" appears {counter} times in the file.')

# Purpose: write a headline containing a specific word into a new file
# Parameters: lines
# Return: nothing
def write_headlines_with_word(lines):
    keyword = input("Enter keyword: ")
    output_file = input("Enter the name of the output file: ").strip()
    with open(output_file, "w") as file:
        for line in lines:
            if keyword.lower() in line.lower():
                file.write(line + "\n")
    print(f"Headlines containing the word '{keyword}' have been written to {output_file}.")

# Purpose: find the average headline length
# Parameters: lines
# Return: nothing
def average_headline_length(lines):
    if not lines:
        print("No headlines to analyze.")
        return

    total_length = sum(len(line) for line in lines)
    average_length = total_length / len(lines)
    print(f'Average length of a headline is {average_length} characters.')

# Purpose: to creat a menu that allows users to pick how they'd like to analyze the news file
# Parameters: none
# Return: nothing
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
            line_shortest_longest(lines)
        elif choice == "5":
            file_name = read_file_name()
            lines = read_file(file_name)
        elif choice == "6":
            print("Thanks for using the news analyzer")
            break
        else:
            print("Invalid input: Please try again.")


main()