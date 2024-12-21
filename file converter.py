import os


def extract_shiftjis(file_path, output_file):
    """
    Extracts Shift-JIS encoded text from a binary file. Decodes valid Shift-JIS characters
    and represents undecodable bytes as hex escapes (e.g., [0xXX]).
    """
    with open(file_path, "rb") as f:
        #reads binary code from original file path
        data = f.read()

    text = ""
    i = 0
    while i < len(data):
        try:
            # Attempt to decode a single Shift-JIS character
            char = data[i:i + 2].decode("shift_jis")
            text += char
            # Move by the byte size of the decoded char
            i += len(char.encode("shift_jis"))
        except UnicodeDecodeError:
            # If undecodable, convert the byte to a hex escape
            text += f"[0x{data[i]:02X}]"
            i += 1

    # Write the text to the output file
    with open(output_file, "w", encoding="utf-8") as out:
        out.write(text)

    print(f"Extracted data from {file_path} to {output_file} successfully.")

#the paths to folders, this code converts every single file in a folder.
input_folder = 'input folder'
output_folder = "output folder"
#if you only want to convert one file:

#extract_shiftjis("input_file_path\input_file.bin","output_file_path\output_file.txt")


# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    #change the .bin to whatever format you want to convert
    if filename.endswith(".bin"):
        file_path = os.path.join(input_folder, filename)
        
        # Define the output file path
        output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + ".txt")
        
        # Convert the file
        extract_shiftjis(file_path, output_file)

print("Conversion complete.")