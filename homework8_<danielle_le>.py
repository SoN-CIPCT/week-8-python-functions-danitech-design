def italian_sub(*ingredients):
    print("\nItalian Sub Order Summary")
    print("-" * 30)
    print(f"Total ingredients: {len(ingredients)}")

    for ingredients in ingredients:
        print(f"- {ingredients}")

    print("Your Italian sub is ready!\n")

italian_sub("Salami","Pepperoni","Provolone","Lettuce","Tomato")

italian_sub(
    "Ham",
    "Capicola",
    "Salami",
    "Provolone",
    "Lettuce",
    "Tomato",
    "Onion",
    "Banana Peppers",
    "Italian Dressing"
)