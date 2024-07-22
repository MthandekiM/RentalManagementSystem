# Creating Property class and it's attributes
class Property:

    def __init__(self, property_id, property_type, address, price):

        self.property_id = property_id
        self.property_type = property_type
        self.address = address
        self.price = price


    # Defining method to display property info
    def display_info(self):

        print(f"Property ID: {self.property_id}")
        print(f"Type: {self.property_type}")
        print(f"Address: {self.address}")
        print(f"Price: ${self.price}")


    # Defining method to update property information
    def update_info(self, property_type = None, address = None, price = None):

        if property_type:
            self.property_type = property_type

        if address:
            self.address = address

        if price:
            self.price = price

        print("Property information updated successfully.")


# Defining main function
def main():

    properties = {}

    # Creating command menu
    while True:

        print("\nProperty Management System")
        print("1. Add Property")
        print("2. Display Properties")
        print("3. Update Property")
        print("4. Delete property")
        print("5. Exit")

        choice = input("Enter your choice: ")

        # Responding according to user choice
        if choice == "1":

            property_id = input("Enter property ID: ")
            property_type = input("Enter property type (e.g. Apartment, House, Commercial): ")
            address = input("Enter property address: ")
            price = float(input("Enter property price: "))
            properties[property_id] = Property(property_id, property_type, address, price)

            print("Property added successfully!")

        elif choice == "2":

            property_id = input("Enter property ID: ")

            if property_id in properties:
                properties[property_id].display_info()
            else:
                print("Property not found.")

        elif choice == "3":

            property_id = input("Enter property ID: ")

            if property_id in properties:
                property_type = input("Enter new property type (or press Enter to skip): ")
                address = input("Enter new property address (or press Enter to skip): ")
                price = float(input("Enter new property price (or press Enter to skip): "))

                properties[property_id].update_info(property_type, address, price)
            else:
                print("Property not found.")

        elif choice == "4":

            property_id = input("Enter property ID: ")

            if property_id in properties:

                del properties[property_id]
                print("Property deleted successfully!")
            else:
                print("Property not found.")

        elif choice == "5":

            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Adding code to run script
if __name__ == "__main__":
    main()
