import os

def write_file_names_to_text(directory_path, output_file_path):
    with open(output_file_path, 'w') as output_file:
        for filename in os.listdir(directory_path):
            base_name, extension = os.path.splitext(filename)
            output_file.write(base_name+' '+base_name + '\n')

# Example usage:
directory_path = 'val'
output_file_path = 'original_captcha.txt'

write_file_names_to_text(directory_path, output_file_path)
