#Task-2
items = int(input("Enter the number of different items: "))

total = 0.0
for i in range(items):
    print("\nItem {}:".format(i + 1))  
    price = float(input("Enter the price of the item: ₹"))
    quantity = int(input("Enter the quantity: "))
    total += price * quantity

gst = total * 0.18
grand_total = total + gst

print("\nSubtotal: ₹{:.2f}".format(total))
print("GST (18%): ₹{:.2f}".format(gst))
print("Total Amount Payable: ₹{:.2f}".format(grand_total))
