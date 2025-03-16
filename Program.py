import pandas as pd
import time

# Start execution time
start_time = time.time()

# File paths
file_user_details = "C:/Users/hp/Desktop/HACKATHON/XX_2_USER_DETAILS_RPT.xlsx"
file_user_role_mapping = "C:/Users/hp/Desktop/HACKATHON/XX_3_USER_ROLE_MAPPING_RPT.xlsx"
file_role_master_details = "C:/Users/hp/Desktop/HACKATHON/XX_4_ROLE_MASTER_DETAILS_RPT.xlsx"

# Load data with USER_ID as string to avoid type mismatches
user_details = pd.read_excel(file_user_details, dtype={"USER_ID": str})
user_role_mapping = pd.read_excel(file_user_role_mapping, dtype={"USER_ID": str})
role_master_details = pd.read_excel(file_role_master_details)

# Get user input
user_id_input = input("Enter USER_ID: ").strip()

# Check if USER_ID exists in either file
user_in_details = user_id_input in user_details["USER_ID"].values
user_in_roles = user_id_input in user_role_mapping["USER_ID"].values

if not user_in_details and not user_in_roles:
    print("User not found in the system.")
    exit()

if user_in_details and not user_in_roles:
    print("User found, but has no assigned roles.")
    exit()

# Merge user-role mapping with role details
user_roles = user_role_mapping.merge(role_master_details, on="ROLE_ID", how="left")

# Merge with user details to get user names
user_roles = user_roles.merge(user_details, on="USER_ID", how="left")

# Convert date columns to datetime
user_roles["EFFECTIVE_START_DATE"] = pd.to_datetime(user_roles["EFFECTIVE_START_DATE"], errors="coerce")
user_roles["EFFECTIVE_END_DATE"] = pd.to_datetime(user_roles["EFFECTIVE_END_DATE"], errors="coerce")

# Filter for the given USER_ID
user_roles = user_roles[user_roles["USER_ID"] == user_id_input]

# If no roles are found for the user
if user_roles.empty:
    print("User found, but has no assigned roles.")
    exit()

# Find users with multiple overlapping roles
overlapping_roles = user_roles.groupby("USER_LOGIN").filter(lambda x: len(x) > 1)

# Display results
if not overlapping_roles.empty:
    print(overlapping_roles[["USER_LOGIN", "USER_DISPLAY_NAME", "ROLE_NAME", "EFFECTIVE_START_DATE", "EFFECTIVE_END_DATE"]]
          .sort_values(["USER_LOGIN", "EFFECTIVE_START_DATE"]))
    print("Conflict detected: The user has multiple overlapping roles.")
else:
    print("No conflict detected: The user does not have overlapping roles.")

# End execution time
end_time = time.time()
print(f"Execution Time: {end_time - start_time:.4f} seconds")
