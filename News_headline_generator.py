import random

# Lists of words
subjects = ["Salman Khan", "Narendra Modi", "Virat Kohli", "Elon Musk", "Donald Trump",
    "Taylor Swift", "A Cat", "Monkeys", "Auto wala", "Nirmala Sitharaman",
    "Shah Rukh Khan", "Aliens", "Superman", "Your Neighbor", "School Principal",
    "Rickshaw Driver", "ChatGPT", "Sunny Leone", "Police Inspector", "Baba Ramdev"]

actions = ["launches", "cancels", "eats", "orders", "celebrates", "fights with",
    "hugs", "bans", "buys", "sells", "discovers", "invents", "wins", "loses",
    "paints", "steals", "teaches", "sings", "dances on", "destroys"]

places_or_things = ["Red Fort", "Train", "Samosa", "Delhi", "IPL match", "Chennai",
    "Moon", "Mars", "Pizza", "Big Boss House", "Parliament", "Taj Mahal",
    "Washing Machine", "Classroom", "Google Office", "Gym", "Wedding",
    "Metro Station", "School Canteen", "Hospital"]

# Headline generator loop
while True:
    subject = random.choice(subjects)                # ✅ pick from list
    action = random.choice(actions)                  # ✅ pick from list
    place_or_thing = random.choice(places_or_things) # ✅ pick from list

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}!"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? yes/no: ").strip().lower()
    if user_input == "no":
        break

print("\nThanks for using the Fake News Headline Generator. Have a fun day! 🎉")
