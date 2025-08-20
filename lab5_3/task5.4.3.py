import random

# Sample product catalog
products = [
    {"id": 1, "name": "Wireless Mouse", "category": "Electronics"},
    {"id": 2, "name": "Yoga Mat", "category": "Fitness"},
    {"id": 3, "name": "Water Bottle", "category": "Fitness"},
    {"id": 4, "name": "Bluetooth Speaker", "category": "Electronics"},
    {"id": 5, "name": "Notebook", "category": "Stationery"},
    {"id": 6, "name": "Pen Set", "category": "Stationery"},
]

# Example user history (list of product ids)
user_history = [1, 5]

def recommend_products(user_history, products, num_recommendations=3):
    # Transparency: Explain how recommendations are made
    print("Recommendations are based on your previous product interactions.")
    print("We aim to provide fair and diverse suggestions.")

    # Find categories from user history
    history_categories = set(
        p["category"] for p in products if p["id"] in user_history
    )

    # Recommend products from the same categories, excluding already seen
    recommendations = [
        p for p in products
        if p["category"] in history_categories and p["id"] not in user_history
    ]

    # Fairness: If not enough, add random products from other categories
    if len(recommendations) < num_recommendations:
        other_products = [
            p for p in products
            if p["category"] not in history_categories and p["id"] not in user_history
        ]
        recommendations += random.sample(
            other_products, min(num_recommendations - len(recommendations), len(other_products))
        )

    # Limit to requested number
    return recommendations[:num_recommendations]

# Example usage
recommended = recommend_products(user_history, products)
print("Recommended products:")
for p in recommended:
    print(f"- {p['name']} ({p['category']})")