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
        for declaredAllergen in foodAllergens:
            allergensToDelete = []
            if declaredAllergen in allergens:
                for f in allergens[declaredAllergen]:
                    if f not in foodIngredients:
                        allergensToDelete.append(f)
                for f in allergensToDelete:
                    allergens[declaredAllergen].remove(f)
            else:
                allergens[declaredAllergen] = foodIngredients.copy()
    changed = True
    while changed:
        changed = False
        # Check if there are allergens with a single possible ingredient
        for allergen in allergens:
            if len(allergens[allergen]) == 1:
                # print(allergen + " has only the element " + allergens[allergen][0] + ", deleting doubles...")
                for otherAllergen in allergens:
                    if otherAllergen != allergen and allergens[allergen][0] in allergens[otherAllergen]:
                        changed = True
                        # print("Double found in " + otherAllergen + ", deleting...")
                        allergens[otherAllergen].remove(allergens[allergen][0])
        if changed:
            continue
        # Check for unicity of the ingredient
        for allergen in allergens:
            if len(allergens[allergen]) != 1:
                uniqueIngredients = []
                for ingredient in allergens[allergen]:
                    unique = True
                    for a in allergens:
                        if a != allergen and ingredient in allergens[a]:
                            unique = False
                            break
                    if unique:
                        uniqueIngredients.append(ingredient)
                if len(uniqueIngredients) != 0 and len(uniqueIngredients) != len(allergens[allergen]):
                    changed = True
                    ingredientsToDelete = []
                    for e in allergens[allergen]:
                        if e not in uniqueIngredients:
                            ingredientsToDelete.append(e)
                    for e in ingredientsToDelete:
                        allergens[allergen].remove(e)
    allergenIngredients = set()
    for allergen in allergens:
        for e in allergens[allergen]:
            allergenIngredients.add(e)
    sum = 0
    for food in foods:
        for ingredient in food.ingredients:
            if ingredient not in allergenIngredients:
                sum += 1
    print(sum)
    allergensList = list(map(lambda e: allergens[e][0], sorted(allergens)))
    s = ""
    for a in allergensList:
        s += a + ","
    s = s[:-1]
    print(s)


main()
