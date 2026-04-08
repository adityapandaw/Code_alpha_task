import csv

prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 200
}

stock = input("Enter stock name: ").upper()
qty = int(input("Enter quantity: "))

if stock in prices:
    total = prices[stock] * qty
    print("Total Investment:", total)

    
    with open("portfolio.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([stock, qty, total])

else:
    print("Stock not found")