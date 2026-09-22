cart_total = 49.16
is_vip = True
is_guest = False
promo_code = "SAVE10"
entered_promo_code = input("Enter promo code:")
if cart_total >= 50 or is_vip:
    print("You have got free shiping.")
else:
    print("You have to pay for shiping.")
if not is_guest and promo_code == entered_promo_code:
    print(f"10% discount was applied. Final total price ${cart_total*0.9:.2f}")
else:
    print(f"Discount was not applied. Final total price ${cart_total:.2f}")