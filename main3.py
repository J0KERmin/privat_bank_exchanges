import aiohttp
import asyncio
from datetime import datetime, timedelta
import sys


class PrivatBankAPI:
    BASE_URL = "https://api.privatbank.ua/p24api/exchange_rates?json&date={}"

    @staticmethod
    async def fetch_exchange_rate(session, date):
        url = PrivatBankAPI.BASE_URL.format(date)
        async with session.get(url) as response:
            if response.status != 200:
                raise Exception(f"Failed to fetch data for {date}")
            return await response.json()

class ExchangeRateFetcher:
    def __init__(self, days):
        self.days = days

    async def fetch_rates(self):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for i in range(self.days):
                date = (datetime.now() - timedelta(days=i)).strftime("%d.%m.%Y")
                tasks.append(PrivatBankAPI.fetch_exchange_rate(session, date))

            return await asyncio.gather(*tasks)

class ExchangeRateFormatter:
    @staticmethod
    def format_rates(rates):
        formatted = []
        for rate_data in rates:
            date = rate_data['date']
            eur_rate = next((r for r in rate_data['exchangeRate'] if r['currency'] == 'EUR'), None)
            usd_rate = next((r for r in rate_data['exchangeRate'] if r['currency'] == 'USD'), None)

            if eur_rate and usd_rate:
                formatted.append({
                    date: {
                        'EUR': {'sale': eur_rate['saleRate'], 'purchase': eur_rate['purchaseRate']},
                        'USD': {'sale': usd_rate['saleRate'], 'purchase': usd_rate['purchaseRate']}
                    }
                })
        return formatted


async def main(days):
    if days > 10 or days < 1:
        print("Please enter a number between 1 and 10")
        return

    fetcher = ExchangeRateFetcher(days)
    try:
        rates = await fetcher.fetch_rates()
        formatted_rates = ExchangeRateFormatter.format_rates(rates)
        print(formatted_rates)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    try:
        days = int(sys.argv[1])
        asyncio.run(main(days))
    except ValueError:
        print("Please enter a valid number of days.")
