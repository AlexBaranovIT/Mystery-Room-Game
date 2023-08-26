class MysteryRoom:

    
    def __init__(self):
        self.has_key = False
        self.drawer_opened = False 

    
    def describe_room(self):
        print("You find yourself in a mysterious room with a locked door.")
        print("In the room, there's a bookshelf and a painting.")
        print("Your objective is to find a way out!")

    
    def check_bookshelf(self):
        print("\nThe bookshelf has several books with numbers on their spines: 3, 1, 4, 2.")
        order = input("Enter the order in which you want to pull the books (e.g. 3142): ")
        if order == "3142":
            self.has_key = True
            print("You hear a click sound and find a key!")
        else:
            print("Nothing happens.")

    
    def check_painting(self):
        print("\nYou look behind the painting and find a riddle:")
        print("\"I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?\"")
        answer = input("Your answer: ").lower().strip()
        if answer == "echo":
            print("A secret drawer in the bookshelf opens revealing a numeric keypad.")
            self.drawer_opened = True
        else:
            print("Nothing happens.")

    
    def check_drawer(self):
        if not self.drawer_opened:
            print("\nYou don't see any drawer.")
            return
        code = input("\nEnter the code to unlock the drawer: ")
        if code == "2023":
            print("The drawer opens revealing another key!")
            self.has_key = True
        else:
            print("Wrong code.")

    
    def check_door(self):
        if self.has_key:
            print("\nYou use the key to unlock the door and escape the room. Congratulations!")
            exit()
        else:
            print("\nThe door is locked. You need a key.")

    
    def start_game(self):
        self.describe_room()
        while True:
            print("\nWhat would you like to do?")
            print("1. Check the bookshelf")
            print("2. Look behind the painting")
            print("3. Check the drawer (if found)")
            print("4. Try to open the door")
            choice = input("> ")

            if choice == "1":
                self.check_bookshelf()
            elif choice == "2":
                self.check_painting()
            elif choice == "3":
                self.check_drawer()
            elif choice == "4":
                self.check_door()
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    game = MysteryRoom()
    game.start_game()
