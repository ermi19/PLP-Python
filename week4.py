def process_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()

        modified_content = content.upper()

        output_filename = f"modified_{filename}"

        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Successfully created '{output_filename}' with modified content.")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Please check the filename and try again.")
    except IOError as e:
        print(f"An unexpected error occurred: {e}")

def main():
    user_filename = input("Enter the filename to read: ").strip()
    process_file(user_filename)

if __name__ == "__main__":
    main()
