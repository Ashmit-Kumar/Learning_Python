def reverse_characters_with_commas(input_string):
    reversed_string = ','.join(input_string)
    return reversed_string


input_filename = 'abc.txt'
output_filename = 'abc_reversed.txt'

try:
    with open(input_filename, 'r') as file:
        original_content = file.read().strip()  


    modified_content = reverse_characters_with_commas(original_content)
    with open(output_filename, 'w') as file:
        file.write(modified_content)

    print(f"Modified content written to {output_filename}: {modified_content}")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
