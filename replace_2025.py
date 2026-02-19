
import os

file_path = r"c:\Users\roger\Downloads\voo teste - voo teste.csv.csv"

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if '2025' exists
    if '2025' in content:
        print(f"Found '2025' in {file_path}. Proceeding with replacement.")
        # Perform replacement
        new_content = content.replace('2025', '2023')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Replacement complete.")
    else:
        print("No '2025' found.")

except Exception as e:
    print(f"Error: {e}")
