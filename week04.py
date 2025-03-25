drinks = ["Ice Americano", "Cafe Latte", "Watermelon Juice"]
prices = [2000, 3000, 4900]
amounts = [0] * len(drinks)
total_price = 0

# drinks = ["Ice Americano", "Cafe Latte"]
# prices = [2000, 3000]
# amounts = [0, 0]
# total_price = 0

DISCOUNT_THRESHOLD = 10000
DISCOUNT_RATE = 0.1

def apply_discount(price: int):
    """
    A function that returns the price by reflecting the discount rate when the total amount exceeds a certain reference value
    :param price: price before discount
    :return: price after discount
    """
    if price >= DISCOUNT_THRESHOLD:
        discount = price * DISCOUNT_RATE
        return price - discount
    return price


def order_process(idx: int):
    """
    Functions that address the beverage order display function, the total cumulative amount calculation function, and the beverage order quantity processing function
    :param idx: list's index number
    """
    global total_price
    print(f"{drinks[idx]} ordered. Price : {prices[idx]}won")
    total_price = total_price + prices[idx]
    amounts[idx] = amounts[idx] + 1


menu_lists = "".join([f"{k+1}) {drinks[k]} {prices[k]}won  " for k in range(len(drinks))])
menu_lists = menu_lists + f"{len(drinks)+1}) Exit : "

while True:
    try:
        menu = int(input(menu_lists))
        if len(drinks) >= menu >= 1:
            order_process(menu - 1)
        elif menu == len(drinks)+1:
            print("Finish order~")
            break
        else:
            print(f"{menu} menu is invalid. please choose from above menu.")
    except ValueError as err:
        print(f"You cannot enter characters. Please enter a valid number.\n{err}")

print("Product  Price  Amount  Subtotal")
for i in range(len(drinks)):
    if amounts[i] > 0:
        print(f"{drinks[i]} {prices[i]} x{amounts[i]} {prices[i] * amounts[i]}")

discounted_price = apply_discount(total_price)
discount_amount = total_price - discounted_price
print(f"Original total price : {total_price} won")
if discount_amount > 0:
    print(f"Discount_amount : {discount_amount} won")
    print(f"Total price after discount : {discounted_price} won")
else:
    print("The discount has not been applied.")
    print(f"Total price : {total_price}won")
