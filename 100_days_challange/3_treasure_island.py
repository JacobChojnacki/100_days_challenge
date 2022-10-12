
print("Welcome to Treasure Island.")
side = input("Do you wanna go left or right").lower()
action = input("Swim or Wait?").lower()
door = input("Red, Blue, Yellow").lower()
while True:
    if side == "right":
        print("Game Over")
        break
    if action == "swim":
        print("Game Over")
        break
    if door != "yellow":
        print("Game Over")
        break
    else:
        print("You win!")
        break

