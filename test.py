categories = []

with open('categories.txt', 'r') as file:
    for line in file:
        # Remove leading/trailing white space and quotes
        category = line.strip().strip("'")
        categories.append(category)

print(categories)

