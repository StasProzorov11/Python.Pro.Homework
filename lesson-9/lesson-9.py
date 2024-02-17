import datetime
import json
from dataclasses import dataclass

import requests

MIDDLE_CURRENCY = "CHF"
API_KEY = "8P3U1BVFD1QJE3TI"


@dataclass
class Price:
    value: float
    currency: str

    def add(self, other: "Price") -> "Price":
        return self.add_prices(other)

    def add_prices(self, other: "Price") -> "Price":
        left_in_middle: float = convert_to(
            value=self.value,
            currency_from=self.currency,
            currency_to=MIDDLE_CURRENCY,
        )
        right_in_middle: float = convert_to(
            value=other.value,
            currency_from=other.currency,
            currency_to=MIDDLE_CURRENCY,
        )
        total_in_left_currency: float = convert_to(
            value=left_in_middle + right_in_middle,
            currency_from=MIDDLE_CURRENCY,
            currency_to=self.currency,
        )
        return Price(value=total_in_left_currency, currency=self.currency)


def convert_to(value: float, currency_from: str, currency_to: str) -> float:
    response = requests.get(
        f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={currency_from}&to_currency={currency_to}&apikey={API_KEY}"
    )
    result = response.json()
    print(result)

    with open("log.json", "a") as log:
        time_now = datetime.datetime.now()
        time = time_now.strftime("%d/%m/%y %H:%M")
        log_data = {
            "currency_from": result["Realtime Currency Exchange Rate"][
                "1. From_Currency Code"
            ],
            "currency_to": result["Realtime Currency Exchange Rate"][
                "3. To_Currency Code"
            ],
            "rate": result["Realtime Currency Exchange Rate"]["5. Exchange Rate"],
            "timestamp": time,
        }
        json.dump(log_data, log, indent=2)
        log.write("\n")
        coefficient = float(
            result["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
        )
        return value * coefficient


hotel_price = float(input("Enter hotel price: "))
hotel_currency = input("Enter hotel currency: ")
flight_price = float(input("Enter the flight price: "))
flight_currency = input("Enter your flight currency: ")

flight = Price(value=flight_price, currency=flight_currency)
hotel = Price(value=hotel_price, currency=hotel_currency)

total = flight.add_prices(hotel)
print(total)
