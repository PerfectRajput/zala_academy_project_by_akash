import os

# ---------------- Question 1: Read a text file ----------------
def read_text_file(filename):
    try:
        with open(filename, "r") as f:
            print("\n--- File Content ---")
            print(f.read())
    except FileNotFoundError:
        print("File not found!")

# ---------------- Question 2: Write text to .txt file ----------------
def write_text_file(filename):
    text = input("Enter text to write: ")
    with open(filename, "w") as f:
        f.write(text)
    print("Text written successfully.")

# ---------------- Question 3: Read a file stream (line by line) ----------------
def read_file_stream(filename):
    try:
        with open(filename, "r") as f:
            print("\n--- File Stream ---")
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("File not found!")

# ---------------- Question 4: Read a file stream with random access ----------------
def random_access_read(filename):
    try:
        with open(filename, "r") as f:
            pos = int(input("Enter byte position to start reading: "))
            length = int(input("Enter number of characters to read: "))
            f.seek(pos)
            data = f.read(length)
            print(f"Data from position {pos}: {data}")
    except FileNotFoundError:
        print("File not found!")

# ---------------- Question 5: Read a file at a particular index using seek() ----------------
def read_at_index(filename):
    try:
        with open(filename, "r") as f:
            index = int(input("Enter index to read character: "))
            f.seek(index)
            char = f.read(1)
            print(f"Character at index {index}: {char}")
    except FileNotFoundError:
        print("File not found!")

# ---------------- Question 6: Check file read/write access permissions ----------------
def check_permissions(filename):
    print(f"Readable: {os.access(filename, os.R_OK)}")
    print(f"Writable: {os.access(filename, os.W_OK)}")

# ---------------- MAIN MENU ----------------
def main():
    filename = "example.txt"  # default file name
    while True:
        print("\n--- File Handling Menu ---")
        print("1. Read text file")
        print("2. Write text to file")
        print("3. Read file stream (line by line)")
        print("4. Random access read")
        print("5. Read at particular index using seek()")
        print("6. Check file read/write permissions")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            read_text_file(filename)
        elif choice == "2":
            write_text_file(filename)
        elif choice == "3":
            read_file_stream(filename)
        elif choice == "4":
            random_access_read(filename)
        elif choice == "5":
            read_at_index(filename)
        elif choice == "6":
            check_permissions(filename)
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
