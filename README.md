# Unique Email Extractor

This Python script is designed to process a file, such as a SQL file, and extract all unique email addresses found within it. It uses a sophisticated regular expression to identify email addresses and adds each unique email to a set to ensure there are no duplicates.

## Functionality

The code consists of a single function called `find_unique_emails` that takes a file path as an argument. Here's a step-by-step breakdown of how the function works:

1. The function defines a regular expression pattern `email_pattern` that matches email addresses in the format `name@domain.tld`.
2. It initialises a set called `unique_emails` to store the unique email addresses.
3. The function attempts to open the file specified by the `file_path` argument in read mode.
4. If the file is successfully opened, the function prints a message indicating that it is searching for email addresses.
5. It then reads the file line by line and uses the `re.findall` function to extract all email addresses found in each line.
6. For each email address found, the function checks if it is already in the `unique_emails` set. If not, it prints the email address and adds it to the set.
7. After processing the entire file, the function prints the total number of unique email addresses found.
8. If the file is not found, the function prints an error message indicating that the file was not found.
9. If any other exception occurs, the function prints a generic error message.

## Usage

To use the script, follow these steps:

1. Ensure you have Python installed on your system.
2. Save the Python script in a directory that contains the file you want to process.
3. Open a terminal or command prompt and navigate to the directory where the script is located.
4. Modify the `file_path` variable in the script to point to the file you want to process (e.g., `file_path = 'database.sql'`).
5. Run the script by typing `python unique-email-extractor-from-sql.py` in the terminal.
6. The script will process the file and print each unique email address found, followed by the total count of unique email addresses.

## Donations

If this script has been helpful for you, consider making a donation to support our work:

-   $USDT (TRC-20): TP6zpvjt2ZNGfWKPevfp65ZrcbKMWSQXDi

Your donations help us continue developing useful and innovative tools.
