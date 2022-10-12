def band_name_generator():
    print("Welcome to the Band Name Generator.")
    city = input("What's name of the city you grew up in?\n")
    pet_name = input("What's pet name?\n")
    band_name = f"Your band name could be {city + ' ' + pet_name}"
    print(band_name)


band_name_generator()
