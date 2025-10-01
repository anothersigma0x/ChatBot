print("\n=== Welcome to the Friendly Chat Bot ===")

# Pedir el nombre con validación
while True:
    name = input("Hello! What is your name? ").strip()
    if name:
        break
    print("Please enter a valid name.")

print(f"Nice to meet you, {name}!")

# Pedir la edad con validación
while True:
    try:
        age_input = input("How old are you? ").strip()
        age = int(age_input)
        if age > 0:
            break
        print("Please enter a positive number for your age.")
    except ValueError:
        print("Please enter a valid number for your age.")

bot_age = 3
age_difference = age - bot_age
print(f"You are {age_difference} years older than me. I'm only {bot_age} years old!")

# Pedir el color favorito con validación
while True:
    color = input("What's your favorite color? ").strip()
    if color:
        break
    print("Please enter a valid color.")

print(f"Oh, {color} is a beautiful color!")
print("\nThanks for chatting with me!")