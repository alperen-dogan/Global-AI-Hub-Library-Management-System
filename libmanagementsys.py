class Library:
    def __init__(self, filename="books.txt"):
        self.filename = filename
        self.file = open(self.filename, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        for line in lines:
            book_info = line.split(',')
            if len(book_info) == 5:
                book_id, book_title, book_author, release_date, num_pages = book_info
                print(f"ID: {book_id}, Title: {book_title}, Author: {book_author}, Release Date: {release_date}, Pages: {num_pages}")
            else:
                print("Invalid data format in the file.")

    def add_book(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()

        # Filter out empty lines before extracting existing book IDs
        non_empty_lines = [line for line in lines if line.strip()]

        if non_empty_lines:
            existing_ids = [int(line.split(',')[0]) for line in non_empty_lines]
            new_id = str(max(existing_ids) + 1)
        else:
            new_id = '1'

        book_title = input("Enter book title: ")
        book_author = input("Enter book author: ")
        release_date = input("Enter release date: ")
        num_pages = input("Enter number of pages: ")

        book_info = f"{new_id},{book_title},{book_author},{release_date},{num_pages}"

        if len(book_info.split(',')) == 5:
            if lines:
                book_info = "\n" + book_info
            self.file.write(book_info + "\n")
            print("Book added successfully.")
        else:
            print("Invalid input. Please enter all the required information.")

    def remove_book(self):
        remove_option = input("Do you want to remove by ID or title? Enter 'ID' or 'title': ").lower()

        if remove_option == 'id':
            book_id_to_remove = input("Enter the ID of the book to remove: ")
            self.remove_by_id(book_id_to_remove)
        elif remove_option == 'title':
            book_title_to_remove = input("Enter the title of the book to remove: ")
            self.remove_by_title(book_title_to_remove)
        else:
            print("Invalid option. Please enter 'ID' or 'title'.")

    def remove_by_id(self, book_id):
        self.file.seek(0)
        lines = self.file.read().splitlines()

        updated_lines = [line for line in lines if not line.startswith(book_id)]

        self.file.seek(0)
        self.file.truncate()
        self.file.write('\n'.join(updated_lines))

        print(f"Book with ID '{book_id}' removed successfully.")

    def remove_by_title(self, book_title):
        self.file.seek(0)
        lines = self.file.read().splitlines()

        updated_lines = [line for line in lines if not line.split(',')[1] == book_title]

        self.file.seek(0)
        self.file.truncate()
        self.file.write('\n'.join(updated_lines))

        print(f"Book with title '{book_title}' removed successfully.")

# Create the Library object
lib = Library()

# Menu interaction
while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("0) Exit")

    user_input = input("Enter your choice (0-3): ")

    if user_input == "1":
        lib.list_books()
    elif user_input == "2":
        lib.add_book()
    elif user_input == "3":
        lib.remove_book()
    elif user_input == "0":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 0 and 3.")
