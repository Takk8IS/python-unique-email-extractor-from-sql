# Copyright (c)
# License: Attribution 4.0 International (CC BY 4.0)
# Author: David C Cavalcante
# LinkedIn: https://www.linkedin.com/in/hellodav/
# Medium: https://medium.com/@davcavalcante/
# Takk™ Innovate Studio
# Positive results, rapid innovation
# Leading the Digital Revolution as the Pioneering 100% Artificial Intelligence Team
# URL: https://takk.ag/
# Medium: https://takk8is.medium.com/

# Designed to help you. From AIs to human-beans.
# Every donation propels us forward.
# $USDT (TRC-20): TP6zpvjt2ZNGfWKPevfp65ZrcbKMWSQXDi

import re

def find_unique_emails(file_path):
    """
    This function meticulously processes your file, such as a SQL file (alter the extension to TXT or another as required), parsing it line by line. It leverages a sophisticated regular expression to discern unique email addresses, subsequently printing each distinct email encountered. Additionally, it aggregates and displays the total count of unique email addresses identified.

    :param file_path: Specifies the path to the SQL file designated for analysis.
    """

    # Regular expression pattern for matching email addresses
    email_pattern = r'[\w.-]+@[\w.-]+\.[\w]{2,}'

    # Set to store unique email addresses
    unique_emails = set()

    try:
        # Open the file in read mode
        with open(file_path, 'r', encoding='utf-8') as file:
            print("Searching for email addresses...")

            # Read the file line by line
            for line in file:
                # Find all email addresses in the current line
                found_emails = re.findall(email_pattern, line)

                # Loop through found email addresses
                for email in found_emails:
                    # If the email is not already in the set, print and add it
                    if email not in unique_emails:
                        print(email)
                        unique_emails.add(email)

        # After processing the entire file, print the count of unique email addresses
        print(f"\nTotal of unique email addresses listed: {len(unique_emails)}")

    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path to your file here
file_path = 'database.sql'

# Call the function with the path to your file
find_unique_emails(file_path)
