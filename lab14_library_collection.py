books = [
    ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
    ("Automate the Boring Stuff", "Al Sweigart", "2020", "Programming"),
    ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "2021", "AI"),
    ("Clean Code", "Robert C. Martin", "2008", "Software Engineering")
]

library_categories = set()
for book in books:
    library_categories.add(book[3])

student_wishlist = {"AI", "Cloud Computing", "Robotics", "Cybersecurity"}

print("=" * 50)
print("        LIBRARY BOOK & CATEGORY MANAGER")
print("=" * 50)

while True:
    print()
    print("Select an operation:")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")
    print()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        print()
        print("--- Current Library Catalog (Fixed Records) ---")
        count = 1
        for book in books:
            title, author, year, category = book
            print(f'{count}. "{title}" by {author} ({year}) | Genre: {category}')
            count += 1
        print("Total Books:", len(books))

    elif choice == "2":
        print()
        print("--- Add New Book Record ---")
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = input("Enter publication year: ")
        category = input("Enter category/genre: ")

        if title and author and year and category:
            new_book = (title, author, year, category)
            books.append(new_book)
            library_categories.add(category)
            print(f'[SUCCESS] "{title}" added as an immutable catalog record.')
            print(f'[INFO] Category set updated with: "{category}"')
        else:
            print("[ERROR] All fields are required.")

    elif choice == "3":
        print()
        print("--- Unique Categories Available in Library (Set) ---")
        for cat in sorted(library_categories):
            print(" -", cat)
        print("Total Unique Genres:", len(library_categories))

    elif choice == "4":
        print()
        print("--- Add to Student Wishlist ---")
        category = input("Enter requested category: ")
        student_wishlist.add(category)
        print(f'[SUCCESS] "{category}" added to student wishlist.')

    elif choice == "5":
        print()
        print("=" * 16, "CATEGORY GAP ANALYSIS", "=" * 16)
        print("Library Holdings (Set): ", sorted(library_categories))
        print("Student Wishlist (Set): ", sorted(student_wishlist))
        print("-" * 54)
        print()
        print("1. Already in Stock (Intersection &):")
        print("  ", sorted(library_categories & student_wishlist))
        print()
        print("2. Purchase Order Needed (Difference -):")
        print("  ", sorted(student_wishlist - library_categories))
        print()
        print("3. Full Combined Genre Coverage (Union |):")
        print("  ", sorted(library_categories | student_wishlist))
        print("=" * 54)

    elif choice == "6":
        print()
        print("Thank you for using the Library Manager. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter a number between 1 and 6.")