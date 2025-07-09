def personalized_message():
    name = str(input("Enter your Name 🧑‍💻 : "))
    age = int(input("Enter your age 🎂 : "))
    fav_color = str(input("Enter a favorite colour 🎨 : "))

    # Correctly formatted multiline f-string
    message = f"""
🌟 Meet {name.upper()}! 🌟

At {age} years young, you're painting the world with your love for {fav_color.title()} 🎨✨
That's not just a color — it's your vibe, your energy, your signature! 💫

Keep shining, dreaming, and coloring the world your way! 🚀🌈
"""
    print(message)

# Call the function
personalized_message()
