class ChatBook:

    def __init__(self):
        # Stores all users
        self.users = {}

        # Current logged-in user
        self.current_user = None

        self.menu()

    def menu(self):
        while True:
            print("\n========== CHATBOOK ==========")
            print("1. Sign Up")
            print("2. Sign In")
            print("3. Write Post")
            print("4. View My Posts")
            print("5. Send Message")
            print("6. View Messages")
            print("7. Logout")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.sign_up()

            elif choice == "2":
                self.sign_in()

            elif choice == "3":
                self.write_post()

            elif choice == "4":
                self.view_posts()

            elif choice == "5":
                self.send_message()

            elif choice == "6":
                self.view_messages()

            elif choice == "7":
                self.logout()

            elif choice == "8":
                print("Thank you for using ChatBook.")
                break

            else:
                print("Invalid Choice!")

    # ---------------- SIGN UP ---------------- #

    def sign_up(self):

        username = input("Enter Username: ")

        if username in self.users:
            print("Username already exists!")
            return

        password = input("Enter Password: ")
        email = input("Enter Email: ")

        self.users[username] = {
            "password": password,
            "email": email,
            "posts": [],
            "messages": []
        }

        print("Signup Successful!")

    # ---------------- SIGN IN ---------------- #

    def sign_in(self):

        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if username in self.users and self.users[username]["password"] == password:
            self.current_user = username
            print(f"Welcome {username}!")
        else:
            print("Invalid Username or Password!")

    # ---------------- LOGOUT ---------------- #

    def logout(self):

        if self.current_user:
            print(f"{self.current_user} logged out.")
            self.current_user = None
        else:
            print("No user is logged in.")

    # ---------------- WRITE POST ---------------- #

    def write_post(self):

        if self.current_user is None:
            print("Please Login First!")
            return

        post = input("Write your post: ")

        self.users[self.current_user]["posts"].append(post)

        print("Post Uploaded Successfully!")

    # ---------------- VIEW POSTS ---------------- #

    def view_posts(self):

        if self.current_user is None:
            print("Please Login First!")
            return

        posts = self.users[self.current_user]["posts"]

        if len(posts) == 0:
            print("No Posts Yet.")
            return

        print("\n----- Your Posts -----")

        for i, post in enumerate(posts, start=1):
            print(f"{i}. {post}")

    # ---------------- SEND MESSAGE ---------------- #

    def send_message(self):

        if self.current_user is None:
            print("Please Login First!")
            return

        receiver = input("Enter Friend Username: ")

        if receiver not in self.users:
            print("User does not exist!")
            return

        message = input("Enter Message: ")

        self.users[receiver]["messages"].append(
            f"From {self.current_user}: {message}"
        )

        print("Message Sent Successfully!")

    # ---------------- VIEW MESSAGES ---------------- #

    def view_messages(self):

        if self.current_user is None:
            print("Please Login First!")
            return

        messages = self.users[self.current_user]["messages"]

        if len(messages) == 0:
            print("No Messages.")
            return

        print("\n----- Inbox -----")

        for msg in messages:
            print(msg)


# Driver Code
person = ChatBook()