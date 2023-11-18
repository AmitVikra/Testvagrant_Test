class Product:
    def __init__(self, product_name, unit_price, gst_percentage, quantity):
        self.name = product_name
        self.unit_price = unit_price
        self.gst_percentage = gst_percentage
        self.quantity = quantity

    def calculate_total_price(self):
        total_price = self.unit_price * self.quantity
        gst_amount = (total_price * self.gst_percentage) / 100
        total_price_with_gst = total_price + gst_amount

        if self.unit_price >= 500:
            discount = (total_price_with_gst * 5) / 100
            total_price_with_gst -= discount

        return total_price_with_gst


def identify_max_gst_product(basket):
    max_gst_product = max(basket, key=lambda product: product.gst_percentage)
    return max_gst_product


def calculate_total_payment(basket):
    total_payment = sum(product.calculate_total_price() for product in basket)
    return total_payment

basket = [
    Product("Leather wallet", 1100, 18, 1),
    Product("Umbrella", 900, 12, 4),
    Product("Cigarette", 200, 28, 3),
    Product("Honey", 100, 0, 2)
]

max_gst_product = identify_max_gst_product(basket)
total_payment = calculate_total_payment(basket)

print("\n\nProduct with maximum GST:\n")
print(f"Name: {max_gst_product.name}, GST Percentage: {max_gst_product.gst_percentage}%")

print("\nTotal amount to be paid to the shopkeeper: Rs", total_payment)
print()