
import csv
import os

FILE_NAME = "portfolio.csv"


def load_portfolio():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r", newline="") as file:
        return list(csv.DictReader(file))


def save_portfolio(portfolio):
    fields = ["name", "quantity", "buy_price", "current_price"]

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(portfolio)


def add_stock(portfolio):
    name = input("Enter stock name: ").strip()

    if not name:
        print("Stock name cannot be empty.")
        return

    try:
        quantity = int(input("Enter quantity: "))
        buy_price = float(input("Enter purchase price: "))
        current_price = float(input("Enter current price: "))

        if quantity <= 0 or buy_price < 0 or current_price < 0:
            print("Enter positive quantity and non-negative prices.")
            return

    except ValueError:
        print("Please enter valid numbers.")
        return

    stock = {
        "name": name,
        "quantity": quantity,
        "buy_price": buy_price,
        "current_price": current_price
    }

    portfolio.append(stock)
    save_portfolio(portfolio)
    print("Stock added successfully!")


def view_portfolio(portfolio):
    if not portfolio:
        print("Your portfolio is empty.")
        return

    total_investment = 0
    total_current_value = 0

    print("\n--- YOUR STOCK PORTFOLIO ---")

    for stock in portfolio:
        quantity = int(stock["quantity"])
        buy_price = float(stock["buy_price"])
        current_price = float(stock["current_price"])

        investment = quantity * buy_price
        current_value = quantity * current_price
        profit_loss = current_value - investment

        total_investment += investment
        total_current_value += current_value

        print(f"\nStock: {stock['name']}")
        print(f"Quantity: {quantity}")
        print(f"Investment: Rs. {investment:.2f}")
        print(f"Current value: Rs. {current_value:.2f}")
        print(f"Profit/Loss: Rs. {profit_loss:.2f}")

    print("\n--- PORTFOLIO SUMMARY ---")
    print(f"Total investment: Rs. {total_investment:.2f}")
    print(f"Current value: Rs. {total_current_value:.2f}")
    print(
        f"Total Profit/Loss: "
        f"Rs. {total_current_value - total_investment:.2f}"
    )


def main():
    portfolio = load_portfolio()

    while True:
        print("\n===== STOCK PORTFOLIO TRACKER =====")
        print("1. Add Stock")
        print("2. View Portfolio")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_stock(portfolio)
        elif choice == "2":
            view_portfolio(portfolio)
        elif choice == "3":
            print("Thank you for using Stock Portfolio Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
