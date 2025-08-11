def  calculate_discount():
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage (e.g. 20 for 20%): "))

    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        price = price - discount
        return price
    else:
        return price

print(f"The final price after discount is: {calculate_discount()}")