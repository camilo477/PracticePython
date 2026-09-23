account = {
    "owner": "Camilo",
    "balance": 1200,
    "active": True
}

# ejemplo: 
# account
# ├── "owner"   → "Camilo"
# ├── "balance" → 1200
# └── "active"  → True

totals = {"food": 200}

category = "food"
amount = 50

totals[category] = totals.get(category, 0) + amount

# en este caso quedaria {"food" : 250}

