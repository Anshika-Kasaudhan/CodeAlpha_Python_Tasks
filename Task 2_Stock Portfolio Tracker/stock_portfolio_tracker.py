# Task 2: Stock Portfolio Tracker 📊

# Hardcoded stock prices 💰
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 180
}

portfolio = {}

while True:
    print("\n📊 ===== STOCK PORTFOLIO TRACKER =====📊")
    print("1️⃣  Add Stock")
    print("2️⃣  View Portfolio")
    print("3️⃣  Calculate Total Investment")
    print("4️⃣  Save Portfolio")
    print("5️⃣  Exit")

    choice = input("👉 Enter your choice: ")

    # Add Stock
    if choice == "1":
        stock = input("📌 Enter stock name: ").upper()

        if stock in stock_prices:
            quantity = int(input("🔢 Enter quantity: "))

            if quantity > 0:
                portfolio[stock] = portfolio.get(stock, 0) + quantity
                print("✅ Stock added successfully!")

            else:
                print("⚠️ Quantity must be greater than 0.")

        else:
            print("❌ Stock not available in the list.")

    # View Portfolio
    elif choice == "2":
        if not portfolio:
            print("📭 Your portfolio is empty.")

        else:
            print("\n📋 ----- YOUR PORTFOLIO -----")

            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                investment = price * quantity

                print(
                    f"📌 {stock} | Quantity: {quantity} | "
                    f"Price: ${price} | Investment: ${investment}"
                )

    # Calculate Total Investment
    elif choice == "3":
        total_investment = 0

        for stock, quantity in portfolio.items():
            total_investment += stock_prices[stock] * quantity

        print(f"\n💰 Total Investment: ${total_investment}")

    # Save Portfolio
    elif choice == "4":
        total_investment = 0

        with open("portfolio.txt", "w") as file:
            file.write("===== STOCK PORTFOLIO =====\n\n")

            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                investment = price * quantity
                total_investment += investment

                file.write(
                    f"{stock} | Quantity: {quantity} | "
                    f"Price: ${price} | Investment: ${investment}\n"
                )

            file.write(f"\nTotal Investment: ${total_investment}")

        print("💾 Portfolio saved successfully in portfolio.txt")

    # Exit
    elif choice == "5":
        print("👋 Thank you for using Stock Portfolio Tracker!")
        break

    else:
        print("❌ Invalid choice. Please try again.")
