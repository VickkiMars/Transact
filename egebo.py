import string

def remove_bad_characters(input_filename, output_filename):
    # Open the file in binary mode
    with open(input_filename, 'rb') as file:
        # Read the binary content
        binary_content = file.read()

    # Decode the binary content, ignoring characters that cause errors
    text_content = binary_content.decode('utf-8', errors='ignore')

    # Write the cleaned content to a new file
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(str(content in string.ascii_letters for content in text_content))

    

    print(f"Cleaned content has been written to '{output_filename}'")



# Example usage
input_filename = r"C:\Users\Victor\Desktop\Transaction\.txt files\names.txt"
output_filename = 'cleaned_example.txt'  # Replace with the desired output file name
remove_bad_characters(input_filename, output_filename)
