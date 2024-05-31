import pandas as pd

# Load the original CSV file
original_csv_path = 'C:\\Users\\Leon\\Desktop\\AI Project\\archive_10\\Transactions.csv'

df = pd.read_csv(original_csv_path)

# Reduce the DataFrame to 1 million instances
sample_df = df.sample(n=300000, random_state=42)  # Adjust 'n' as needed

# Save the reduced DataFrame to a new CSV file
reduced_csv_path = 'reduced.csv'
sample_df.to_csv(reduced_csv_path, index=False)

print("Reduced CSV file saved successfully.")
