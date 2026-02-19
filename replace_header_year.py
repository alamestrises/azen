
import os

file_path = r"c:\Users\roger\Desktop\voos\vo jf.csv"

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    changes_count = 0
    
    for line in lines:
        # Check if line has at least 4 chars and first 4 are digits
        if len(line) >= 4 and line[:4].isdigit():
            # Replace first 4 chars with 2023
            new_line = "2023" + line[4:]
            new_lines.append(new_line)
            changes_count += 1
        else:
            new_lines.append(line)
            
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
        
    print(f"Processed {len(lines)} lines.")
    print(f"Modified {changes_count} lines.")

except Exception as e:
    print(f"Error: {e}")
