import re
import json
import os

# Get the folder where this Python file is located
current_folder = os.path.dirname(os.path.abspath(__file__))

# Build full path to raw.txt
file_path = os.path.join(current_folder, "raw.txt")

# Read the receipt text from raw.txt
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

def to_float(price_text):
    # Remove spaces inside the number
    price_text = price_text.replace(" ", "")
    
    # Replace comma with dot
    price_text = price_text.replace(",", ".")
    
    return float(price_text)

# Find product blocks
item_pattern = re.compile(
    r"\d+\.\s*\n"
    r"(.+?)\n"
    r"(\d+,\d{3})\s*x\s*([\d ]+,\d{2})\n"
    r"([\d ]+,\d{2})",
    re.MULTILINE
)

matches = item_pattern.findall(text)

products = []
prices = []

for match in matches:
    name = match[0].strip()
    quantity = match[1].strip()
    unit_price = to_float(match[2])
    final_price = to_float(match[3])

    products.append({
        "name": name,
        "quantity": quantity,
        "unit_price": unit_price,
        "final_price": final_price
    })

    prices.append(final_price)

product_names = [item["name"] for item in products]

calculated_total = sum(prices)

total_match = re.search(r"ИТОГО:\s*\n([\d ]+,\d{2})", text)
official_total = to_float(total_match.group(1)) if total_match else None

datetime_match = re.search(r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})", text)
date_value = datetime_match.group(1) if datetime_match else "Not found"
time_value = datetime_match.group(2) if datetime_match else "Not found"

payment_match = re.search(r"(Банковская карта|Наличные|Карта)", text)
payment_method = payment_match.group(1) if payment_match else "Not found"

result = {
    "product_names": product_names,
    "prices": prices,
    "calculated_total": calculated_total,
    "official_total": official_total,
    "date": date_value,
    "time": time_value,
    "payment_method": payment_method,
    "products": products
}

print("----- RECEIPT PARSING RESULT -----")
print("Payment method:", payment_method)
print("Date:", date_value)
print("Time:", time_value)
print("Calculated total:", calculated_total)
print("Official total:", official_total)
print()

print("Products:")
for item in products:
    print(f"- {item['name']}")
    print(f"  Quantity: {item['quantity']}")
    print(f"  Unit price: {item['unit_price']}")
    print(f"  Final price: {item['final_price']}")
    print()

print("----- JSON OUTPUT -----")
print(json.dumps(result, indent=4, ensure_ascii=False))