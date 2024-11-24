1. define read_file_name
# Purpose:to read file of users choice  
# Name: read_file_name
# Parameters: none
# Return: f_name
# Algorithm
    1. Prompt the user to enter a file name.
    2. Check if the file exists:
    3. If the file does not exist, prompt the user again until a valid file name is provided.
    4. Return the valid file name as a variable f_name.
2. define read_file
# Purpose: open file
# Name: read_file
# Parameters: f_name
# Return: file.readlines()
# Algorithm
    1. Open the file in read and read all the lines from the file.
    2. Store the lines as a list of strings in variable called file
3. define line_shortest_longest
# Purpose: find longest and shortest line 
# Name: lines_shortest_longest
# Parameters: f_name
# Return: nothing 
# Algorithm
    1. set longest equal to a blank soace shortes line equal to none
    2. for every line in lines
        1. strip line 
        2. if shortest_line is None or line is shorter then shortest line
            1. set line equal to shortest line
        3. if line is loneger then longest_line
            1. set equal to longest line
    3. print value of longest and shortest line
4. define word_finder
# Purpose: find how many times a word is in a file
# Name: word_finder
# Parameters: lines
# Return: nothing
# Algorithm
    1. set target word to user choice
    2. set counter to zero 
    3. for line in lines
        1. words is equal to line split 
        2. for word in words
            1.if word set to lowercase is equal to target wourd set to lowercase 
                1. add one to the value of counter
    4. print value of counter as the amount the target word is in the file 
5. def write_headlines_with_word
# Purpose: write a headline containing a specific word into a new file
# Name: write_headlines_with_word
# Parameters: lines
# Return: nothing
# Algorithm
    1. set keyword equal to user choice 
    2. ask user to name the new file
    3. open the new file in write mode
        1. for every line in lines
            1. if the keyword set to all lowercase is in the line set to all lowercase
                1. write that line into the new file
    4. output to the user the a new file has been created
6. define average_headline_length
# Purpose: find the average headline length 
# Name: average_headline_length 
# Parameters: lines
# Return: nothing
# Algorithm
    1. if no line in file
        1. output 'No headlines to analyze'
    2. total length equals the sum of the lengths of line for every line in lines
    3. average length is equal to total length divided by length of lines
    4. output the value of average length touser 
7. define main
# Purpose: to creat a menu that allows users to pick how they'd like to analyze the news file
# Name: main
# Parameters: none
# Return: nothing
# Algorithm
    1. set file name equal to function read_file_nameo
    2. lines equal to read_file(file_name)
    3. Display a menu with the following options:
        1. Count headlines containing a specific word.
        2. Write headlines containing a specific word to a new file.
        3. Calculate the average length of headlines.
        4. Find the longest and shortest headline.
        5. Load a new file.
        6. Quit the program.
    4. if user chooses 1
        1. call the word_finder function
    5. if user chooses 2
        1. call the write_headlines_with_word function
    6. if user chooses 3
        1. call the average_headline_length function
    7. if user chooses 4
        1. line_shortest_longest
    8. if user selects 5
        1. call read_file_name function and the call read_file function
    9. if user selects 6
        1. output "Thanks for using the news analyzer"
    10. if user enters anything else
        1. output "Invalid input: Please try again."
8. call main function