#restores the txt file to its previous format while maintaining the hex code

def restore_pak(input_txt_path, output_pak_path, encoding="shift_jis"):
    """
    Efficiently restores a text file with hex escapes to a binary .pak file.
    """
    import re

    hex_escape_pattern = re.compile(r"\[0x([0-9A-Fa-f]{2})\]")  # Pattern for hex escapes

    # Read the entire input text
    with open(input_txt_path, "r", encoding="utf-8") as txt_file:
        text = txt_file.read()

    binary_data = bytearray()  # Use a bytearray for efficient appending

    i = 0
    while i < len(text):
        # Match a hex escape pattern
        if match := hex_escape_pattern.match(text, i):
            hex_value = match.group(1)
            binary_data.append(int(hex_value, 16))  # Convert hex to byte
            i = match.end()  # Move past the processed hex escape
        else:
            # Encode valid text directly
            try:
                char_encoded = text[i].encode(encoding)
                binary_data.extend(char_encoded)  # Add the encoded bytes
                i += 1
            except UnicodeEncodeError:
                # Skip unencodable characters (shouldn't occur with valid input)
                print(f"Warning: Skipping unencodable character {text[i]}")
                i += 1

    # Write the binary data to the output file
    with open(output_pak_path, "wb") as pak_file:
        pak_file.write(binary_data)

    print(f"Restored data from {input_txt_path} to {output_pak_path} successfully.")



restore_pak(r'D:\games\emulators roms\gamecube\super robot taisen text\configs_text\charalist.txt', r'D:\games\emulators roms\gamecube\super robot taisen text\configs\charalist.bin', encoding="shift_jis")