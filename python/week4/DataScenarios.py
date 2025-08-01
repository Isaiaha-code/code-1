print("Scenario 1: A restaurant menu with prices for each item")
print("Best Data Structure: Dictionary - because each menu item maps to a specific price")
menu = {
    "Burger": 9.99,
    "Pizza": 12.49,
    "Salad": 7.99,
    "Fries": 3.50
}
for item, price in menu.items():
    print(f"{item}: ${price}")

print("\n" + "-"*40 + "\n")

print("Scenario 2: High scores to an arcade game")
print("Best Data Structure: List - because scores are ordered and can be changed")
high_scores = [10000, 8500, 7600, 6200, 5000]
for score in high_scores:
    print(f"Score: {score}")

print("\n" + "-"*40 + "\n")

print("Scenario 3: All of the months of the year")
print("Best Data Structure: Tuple - because the months don't change and have a fixed order")
months = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
)
for month in months:
    print(month)

print("\n" + "-"*40 + "\n")

print("Scenario 4: All the items in your backpack")
print("Best Data Structure: List - because you might add or remove items")
backpack = ["Notebook", "Laptop", "Pen", "Water Bottle"]
for item in backpack:
    print(f"Backpack Item: {item}")

print("\n" + "-"*40 + "\n")

print("Scenario 5: Look up Student emails by their names")
print("Best Data Structure: Dictionary - because names map to email addresses")
student_emails = {
    "Isaiah": "isaiah@example.com",
    "Emily": "emily@example.com",
    "Liam": "liam@example.com"
}
for name, email in student_emails.items():
    print(f"{name}: {email}")

print("\n" + "-"*40 + "\n")


print("Scenario 6: A shopping cart of groceries")
print("Best Data Structure: List - because you can have duplicate items and change the cart")
shopping_cart = ["Apple", "Banana", "Apple", "Milk", "Bread"]
for item in shopping_cart:
    print(f"Cart Item: {item}")

print("\n" + "-"*40 + "\n")

print("Scenario 7: A list of unique music genres in a playlist")
print("Best Data Structure: Set - because we want only unique genres")
music_genres = {"Hip-Hop", "Jazz", "Pop", "Rock", "Hip-Hop"}
for genre in music_genres:
    print(f"Genre: {genre}")