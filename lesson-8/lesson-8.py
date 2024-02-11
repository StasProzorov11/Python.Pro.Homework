#   Сделал я
class Hotel:
    def __init__(self, price: float, currency: str):
        self.price = price
        self.currency = currency


class Flight:
    def __init__(self, price: float, currency: str):
        self.price = price
        self.currency = currency


class Price:
    def __init__(self, price: float, currency: str):
        self.price = price
        self.currency = currency


_average_rate = {
    "CHF": 10,
    "USD": 1,
    "UAH": 40,
}


def convert_to_chf(price: float, currency: str) -> float:
    if currency == "CHF":
        return price
    else:
        converted_price = price / _average_rate[currency]
        return converted_price * _average_rate["CHF"]  # этот кусок не я


def add_prices(price1: Price, price2: Price) -> Price:
    if price1.currency == price2.currency:
        total_price = price1.price + price2.price  # я
        return Price(total_price, price1.currency)
    else:
        converted_price = convert_to_chf(price2.price, price2.currency)  # не я
        total_price = price1.price + converted_price
        return Price(total_price, "CHF")


hotel_price = float(input("Enter hotel price: "))
hotel_currency = input("Enter hotel currency: ")

flight_price = float(input("Enter the flight price: "))
flight_currency = input("Enter your flight currency: ")
# не я
hotel = Hotel(hotel_price, hotel_currency)
flight = Flight(flight_price, flight_currency)

hotel_price_obj = Price(hotel.price, hotel.currency)
flight_price_obj = Price(flight.price, flight.currency)

if hotel_price_obj.currency == flight_price_obj.currency:
    total_price = hotel_price_obj.price + flight_price_obj.price
    total_currency = hotel_price_obj.currency
else:
    hotel_total_chf = convert_to_chf(hotel_price_obj.price, hotel_price_obj.currency)
    flight_total_chf = convert_to_chf(flight_price_obj.price, flight_price_obj.currency)
    total_price = hotel_total_chf + flight_total_chf
    total_currency = "CHF"

print(f"Total cost of flight and hotel: {total_price} {total_currency}")
