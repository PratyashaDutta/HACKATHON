# User Role Validation Script

Overview:
This Python script checks for user role conflicts by analyzing data from multiple Excel reports. It determines if a given user exists, has assigned roles, and detects overlapping roles.

Features
1)Reads user details, user-role mapping, and role master details from Excel files.
2)Verifies if a user exists in the dataset.
3)Checks if the user has assigned roles.
4)Identifies conflicts where a user has multiple overlapping roles.
5)Displays execution time for performance analysis.

Prerequisites
Python 3.x

Required Python libraries:
1)pandas
2)openpyxl

Usage
1)Place the required Excel files in the specified directory:
a)XX_2_USER_DETAILS_RPT.xlsx
b)XX_3_USER_ROLE_MAPPING_RPT.xlsx
c)XX_4_ROLE_MASTER_DETAILS_RPT.xlsx
2)Run the script:
python user_role_validation.py
3)Enter the USER_ID when prompted.
4)The script will:
a)Check if the user exists.
b)Verify if the user has assigned roles.
c)Detect overlapping roles and display relevant details.

File Structure:
|-- user_role_validation.py  # Main script
|-- XX_2_USER_DETAILS_RPT.xlsx  # User details
|-- XX_3_USER_ROLE_MAPPING_RPT.xlsx  # User-role mapping
|-- XX_4_ROLE_MASTER_DETAILS_RPT.xlsx  # Role master details
|-- README.md  # Documentation

Example Output:
Enter USER_ID: 12345
USER_LOGIN   USER_DISPLAY_NAME   ROLE_NAME   EFFECTIVE_START_DATE   EFFECTIVE_END_DATE
JohnDoe      John Doe            Admin       2023-01-01              2024-01-01
JohnDoe      John Doe            Manager     2023-06-01              2024-06-01
Conflict detected: The user has multiple overlapping roles.
Execution Time: 0.0254 seconds

License
This project is licensed under the MIT License.
