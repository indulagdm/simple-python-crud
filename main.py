from crud import createUser, getUserAll
from bson.objectid import ObjectId





def main():
    # app logic here

    def menu():
        print("\n1. Add User")
        print("2. View Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")

    while True:
        menu()
        choice = input("Choose: ")

        if choice == "5":
            print("Thank you for choosing us.")
            break

if __name__ == "__main__":
    main()