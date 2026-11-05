# 1. I would use .get() when I'm not sure if a key exists because
# it prevents the program from crashing. I would use bracket notation
# when I know the key should exist and want to catch missing data.

# 2. Exercise 8 reminds me of using PivotTables in Excel to group
# and calculate sales by category. Python is more useful for large
# datasets because it can automatically process information faster
# without having to manually update tables.

# Exercise 1

customer = {"name": "John Smith", "email": "johnsmith@gmail.com", "tier": "Gold", "ytd_spend": 1500}

print(f"Name: {customer['name']}")
print(f"Email: {customer['email']}")
print(f"Tier: {customer['tier']}")
print(f"YTD Spend: {customer['ytd_spend']}")

print(f"Customer: {customer}")
print()

# Exercise 2

customer["phone"] = "123-456-7890"
print(f"After adding phone: {customer}")

customer["tier"] = "platinum"
print(f"After updating tier: {customer}")

del customer["email"]
print(f"After deleting email: {customer}")
print()

# Exercise 3

print(f"Email: {customer.get('email', 'no email on file')}")

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email not found")
print()

# Exercise 4

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items()
for key in customer:
    print(f"{key}")
print()
# .items() gives both the key and value.
# Without .items(), the loop only gives the keys.

# Exercise 5

tier_discounts = {"bronze": 0, "silver": 0.05, "gold": 0.10, "platinum": 0.15}

tier = customer["tier"]
discount = tier_discounts.get(tier, 0)
price = 200
final_price = price * (1 - discount)

print(f"Tier: {tier}")
print(f"Discount Rate: {discount:.0%}")
print(f"Final Price: ${final_price:.2f}")
print()

# Exercise 6

customers = [
    {"name": "John Smith", "tier": "platinum"},
    {"name": "Sarah Johnson", "tier": "gold"},
    {"name": "Mike Brown", "tier": "silver"}
]

price = 300

for customer in customers:
    tier = customer["tier"]
    discount = tier_discounts.get(tier, 0)
    discount_amount = price * discount

    print(f"Name: {customer['name']}")
    print(f"Tier: {tier}")
    print(f"Discount: ${discount_amount:.2f}")
print()

# Exercise 7

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - {details['stock']} remaining")
print()

# Exercise 8

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]
    summary[region] = summary.get(region, 0) + amount

for region in sorted(summary):
    print(f"{region}: ${summary[region]:.2f}")
print()