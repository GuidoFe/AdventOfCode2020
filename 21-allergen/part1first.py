class Food:
    def __init__(self, ingredients, declared):
        self.ingredients = ingredients
        self.declared = declared

    def __repr__(self):
        return "Declared: " + str(self.declared) + "\nIngredients: " + str(self.ingredients) + "\n"


def main():
    f = open("input")
    foods = []
    allergens = {}
    countIngredients = {}
    for line in f:
        line = line.strip()
        if len(line) == 0:
            continue
        line = line.replace(")", "")
        parts = line.split(" (contains ")
        foodIngredients = parts[0].split(" ")
        if len(parts) == 2:
            foodAllergens = parts[1].split(", ")
        else:
            foodAllergens = []
        foods.append(Food(foodIngredients, foodAllergens))
        for allergen in foodAllergens:
            if allergen in allergens:
                for f in allergens[allergen]:
                    if f not in foodIngredients:
                        allergens[allergen].remove(f)
            else:
                allergens[allergen] = foodIngredients.copy()
        for i in foodIngredients:
            if i in countIngredients:
                countIngredients[i] += 1
            else:
                countIngredients[i] = 1
    changed = True
    while changed:
        changed = False
        # Check if there are allergens with a single possible ingredient
        for allergen in allergens:
            if len(allergens[allergen]) == 1:
                for otherAllergen in allergens:
                    if otherAllergen != allergen and allergens[allergen][0] in allergens[otherAllergen]:
                        changed = True
                        allergens[otherAllergen].remove(allergens[allergen][0])
        for allergen in allergens:
            if len(allergens[allergen]) != 1:
                for ingredient in allergens[allergen]:
                    unique = True
                    for a in allergens:
                        if a != allergen and ingredient in allergens[a]:
                            unique = False
                            break
                    if unique:
                        changed = True
                        allergens[allergen] = [ingredient]
                        break
    for allergen in allergens:
        for e in allergens[allergen]:
            if e in countIngredients:
                del countIngredients[e]
    sum = 0
    print(foods)
    print(allergens)
    print(countIngredients)
    for e in countIngredients:
        sum += countIngredients[e]
    print(sum)


main()
