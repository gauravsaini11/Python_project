from random import choice

questions = ["Why is the sky Blue?", "Why is there face on the moon?","Where are all the dinosaurs?"]
questions = choice(questions)
answer = input(questions).strip().lower()

while answer != "just because":
    answer = input("Why? : ").strip().lower()
print("Oh okey")
