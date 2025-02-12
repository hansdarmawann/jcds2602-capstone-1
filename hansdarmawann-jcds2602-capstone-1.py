from tabulate import tabulate
import datetime
import os
import platform

cars = [
    {
        "license_plate": "B1071PDM",
        "car_name": "Range Rover P615",
        "mileage": 12345.678,
        "available": "No",
        "borrower_name": "Fitra Eri",
        "contact": "081234567891",
        "borrow_date": datetime.date(2024, 6, 24),
        "return_date": datetime.date(2024, 6, 30),
        "reason": "Review Purpose"
    },
    {
        "license_plate": "B1010LKX",
        "car_name": "Mercedes Benz G63 AMG",
        "mileage": 901.23,
        "available": "Yes",
        "borrower_name": "",
        "contact": "",
        "borrow_date": "",
        "return_date": "",
        "reason": ""
    }
]

def view_cars(license_plate=None):
    """View car details based on license plate or all cars."""
    try:
        if license_plate:
            license_plate = license_plate.upper().replace(" ", "")
            filtered_cars = [car for car in cars if car["license_plate"] == license_plate]
            if not filtered_cars:
                print("Data not found.")
                return
            data = filtered_cars
        else:
            data = cars

        print(tabulate(data, headers="keys", maxcolwidths=[15 for _ in range(len(data[0]))]))
    except Exception as e:
        print(f"An error occurred while displaying data: {e}")

def delete_car(license_plate):
    """Delete a car from the list based on license plate."""
    try:
        license_plate = license_plate.upper().replace(" ", "")
        for car in cars:
            if car["license_plate"] == license_plate:
                if car["available"] == "Yes":
                    cars.remove(car)
                    print("Data deleted.")
                else:
                    print("The car must be returned before it can be deleted.")
                return
        print("Data not found.")
    except Exception as e:
        print(f"An error occurred while deleting data: {e}")

def add_car():
    """Add a new car to the list."""
    while True:
        license_plate = input("Enter car license plate: ").upper().replace(" ", "")
        if not license_plate:
            print("License plate cannot be empty!")
            continue

        if any(car["license_plate"] == license_plate for car in cars):
            print("License plate already exists. Please enter a different license plate.")
            continue

        print("License plate successfully added.")
        break

    while True:
        car_name = input("Enter car name: ")
        if not car_name:
            print("Car name cannot be empty!")
            continue

        print("Car name successfully added.")
        break

    while True:
        try:
            mileage = float(input("Enter car mileage: "))
            if mileage < 0:
                print("Mileage cannot be negative!")
                continue

            print("Data successfully added.")
            break
        except ValueError:
            print("Mileage must be a valid number!")

    new_car = {
        "license_plate": license_plate,
        "car_name": car_name,
        "mileage": mileage,
        "available": "Yes",
        "borrower_name": "",
        "contact": "",
        "borrow_date": "",
        "return_date": "",
        "reason": ""
    }
    cars.append(new_car)

def update_car(license_plate):
    """Update car information based on license plate."""
    try:
        license_plate = license_plate.upper().replace(" ", "")
        for car in cars:
            if car["license_plate"] == license_plate:
                view_cars(license_plate)
                car["car_name"] = input("Enter new car name (leave blank to keep current): ") or car["car_name"]
                while True:
                    try:
                        mileage = input("Enter new mileage (leave blank to keep current): ")
                        if mileage == "":
                            car["mileage"] = car["mileage"]
                            break
                        else:
                            mileage = float(mileage)
                            if mileage < 0:
                                print("Mileage cannot be negative!")
                                continue
                            else:
                                car["mileage"] = round(mileage, 2)
                                break
                    except ValueError:
                        print("Mileage must be a valid number!")
                print("Car information updated.")
                return
        print("Data not found.")

    except Exception as e:
        print(f"An error occurred while updating data: {e}")

def return_car(license_plate):
    """Return the borrowed car information based on license plate."""
    try:
        license_plate = license_plate.upper().replace(" ", "")
        for car in cars:
            if car["license_plate"] == license_plate and car["available"] == "No":
                view_cars(license_plate)
                return_car = {
                    "license_plate": car["license_plate"],
                    "car_name": car["car_name"],
                    "mileage": car["mileage"],
                    "available": "Yes",
                    "borrower_name": "",
                    "contact": "",
                    "borrow_date": "",
                    "return_date": "",
                    "reason": ""
                }
                car.update(return_car)
                print("The car has been successfully returned.")
                return
            elif car["license_plate"] == license_plate and car["available"] == "Yes":
                view_cars(license_plate)
                print("The car is available and has no borrower yet.")
                return
        print("Data not found.")

    except Exception as e:
        print(f"An error occurred while updating data: {e}")

def borrow_car(license_plate):
    """Borrow a car if it is available."""
    try:
        license_plate = license_plate.upper().replace(" ", "")
        for car in cars:
            if car["license_plate"] == license_plate:
                if car["available"] == "Yes":
                    car["borrower_name"] = input("Enter borrower name: ")
                    car["contact"] = input("Enter contact number: ")
                    while True:
                        try:
                            borrow_date_str = input("Enter borrow date (YYYY-MM-DD): ")
                            car["borrow_date"] = datetime.datetime.strptime(borrow_date_str, "%Y-%m-%d").date()
                            break
                        except ValueError:
                            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                    while True:
                        try:
                            return_date_str = input("Enter return date (YYYY-MM-DD): ")
                            car["return_date"] = datetime.datetime.strptime(return_date_str, "%Y-%m-%d").date()
                            if car["return_date"] < car["borrow_date"]:
                                print("Return date must be after borrow date. Please enter a valid return date.")
                            else:
                                break
                        except ValueError:
                            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                    car["reason"] = input("Enter reason for borrowing: ")
                    car["available"] = "No"
                    print("Car has been successfully borrowed.")
                    return
                else:
                    print("The car is currently unavailable.")
                    return
        print("Data not found.")
    except Exception as e:
        print(f"An error occurred while borrowing the car: {e}")

def clear_screen():
    """Clear the console screen."""
    os_name = platform.system()
    input("Press Enter to continue...")
    if os_name == 'Windows':
        os.system("cls")
    else:
        os.system("clear")

def main():
    """Main function to run the car rental system."""
    while True:
        try:
            print("""
            Welcome to the XYZ Car Rental System
            Please choose an option below:
                1. View Data
                2. Add Car
                3. Update Car
                4. Borrow Car
                5. Return Car
                6. Delete Car
                7. Exit
            """)
            menu = int(input("Enter your choice: "))
            if menu == 1:
                license_plate = input("Enter license plate (leave blank to view all data): ")
                view_cars(license_plate)
                clear_screen()
            elif menu == 2:
                add_car()
                clear_screen()
            elif menu == 3:
                license_plate = input("Enter license plate of the car to update: ")
                update_car(license_plate)
                clear_screen()
            elif menu == 4:
                license_plate = input("Enter license plate of the car to borrow: ")
                borrow_car(license_plate)
                clear_screen()
            elif menu == 5:
                license_plate = input("Enter license plate of the car to return: ")
                return_car(license_plate)
                clear_screen()
            elif menu == 6:
                license_plate = input("Enter license plate of the car to delete: ")
                delete_car(license_plate)
                clear_screen()
            elif menu == 7:
                print("Thank you, see you next time!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
