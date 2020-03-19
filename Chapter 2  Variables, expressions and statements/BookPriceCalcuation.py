price_of_book = 24.95
bookstore_discount_percent = 40
first_book_shipping_cost = 3
additional_book_shipping_cost = 0.75

print(f"price of a book is ${price_of_book:.2f}, but bookstores get a {bookstore_discount_percent}% discount. Shipping costs ${first_book_shipping_cost} for the first copy and {additional_book_shipping_cost*100} cents for each additional copy.")

number_of_books = int(input("How many do you want?"))

book_cost = number_of_books * (price_of_book * (1-(bookstore_discount_percent/100)))
shipping_cost = 0

if number_of_books > 0:
    shipping_cost = first_book_shipping_cost

if number_of_books > 1:
    shipping_cost = shipping_cost + ((number_of_books-1) * additional_book_shipping_cost)

total_cost = book_cost + shipping_cost

if total_cost == 0:
    print("Not ordering anything?")
else:
    print(f"${total_cost:,.2f}")