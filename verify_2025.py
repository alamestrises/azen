
import os

file_path = r"c:\Users\roger\Downloads\voo teste - voo teste.csv.csv"

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '2025' in content:
        print("ALERT: '2025' still found in the file!")
        # Print where
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if '2025' in line:
                print(f"Line {i+1}: {line}")
                if i > 10: break # limit output
    else:
        print("Verification successful: No '2025' found.")

except Exception as e:
    print(f"Error: {e}")
