# Global constants for conversion rates
USD_TO_EUR_RATE = 0.9254
GBP_TO_INR_RATE = 101.8
JPY_TO_USD_RATE = 0.006954
EUR_TO_GBP_RATE = 0.8571

# OOP: class grouping all conversion methods
class CurrencyConverter:
    # USD → EUR
    def convert_usd_to_eur(self, usd):
        return usd * USD_TO_EUR_RATE

    # GBP → INR
    def convert_gbp_to_inr(self, gbp):
        return gbp * GBP_TO_INR_RATE

    # JPY → USD
    def convert_jpy_to_usd(self, jpy):
        return jpy * JPY_TO_USD_RATE

    # EUR → GBP
    def convert_eur_to_gbp(self, eur):
        return eur * EUR_TO_GBP_RATE

# Show the menu options
def display_menu():
    print("Enter 1 for USD to EUR conversion.")
    print("Enter 2 for GBP to INR conversion.")
    print("Enter 3 for JPY to USD conversion.")
    print("Enter 4 for EUR to GBP conversion.")
    print("Enter 5 to exit the program.")

# Prompt user and return a float
def get_amount(currency):
    amt_str = input("Please enter the amount in " + currency + ":\n")
    return float(amt_str)

# Each of these calls converter, shows “Computing…”, then prints result
def usd_to_eur(converter):
    usd = get_amount("USD")
    print("Computing...")
    eur = converter.convert_usd_to_eur(usd)
    print("The amount in EUR is " + str(round(eur, 2)) + " (rounded to 2 decimal places).")

def gbp_to_inr(converter):
    gbp = get_amount("GBP")
    print("Computing...")
    inr = converter.convert_gbp_to_inr(gbp)
    print("The amount in INR is " + str(round(inr, 2)) + " (rounded to 2 decimal places).")

def jpy_to_usd(converter):
    jpy = get_amount("JPY")
    print("Computing...")
    usd = converter.convert_jpy_to_usd(jpy)
    print("The amount in USD is " + str(round(usd, 2)) + " (rounded to 2 decimal places).")

def eur_to_gbp(converter):
    eur = get_amount("EUR")
    print("Computing...")
    gbp = converter.convert_eur_to_gbp(eur)
    print("The amount in GBP is " + str(round(gbp, 2)) + " (rounded to 2 decimal places).")

# ---- main program starts here ----
name = input("Please enter your name:\n")
print("Welcome " + name + " to the Currency Converter Application.")

converter = CurrencyConverter()

while True:
    display_menu()
    choice = input()
    if choice == "1":
        usd_to_eur(converter)
    elif choice == "2":
        gbp_to_inr(converter)
    elif choice == "3":
        jpy_to_usd(converter)
    elif choice == "4":
        eur_to_gbp(converter)
    elif choice == "5":
        print("Exiting...")
        print("Thank you for using the Currency Converter Application.")
        break
    else:
        print("That is not a valid option...")
