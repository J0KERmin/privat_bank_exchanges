Currency Rate Fetcher
Currency Rate Fetcher is a console utility for retrieving currency exchange rates (EUR and USD) from PrivatBank for the past few days using the PrivatBank public API. The utility can fetch exchange rates for a maximum of the last 10 days.

Features
Fetches EUR and USD exchange rates for cash transactions at PrivatBank.
Allows querying up to 10 days of historical data.
Utilizes asynchronous HTTP requests via aiohttp.
Follows SOLID principles for clean and maintainable code.
Handles network errors gracefully.
Requirements
Python 3.8+
aiohttp package
Installation
Clone the repository or download the script.


bash
Copy code
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Install dependencies.

bash
Copy code
pip install -r requirements.txt
Or manually install aiohttp if there is no requirements.txt:

bash
Copy code
pip install aiohttp
Usage
To use the script, run it from the terminal and provide the number of days you wish to fetch the exchange rates for. For example, to get exchange rates for the last 3 days:

bash
Copy code
python main3.py 3
Example Output
json
Copy code
[
  {
    "2022-11-03": {
      "EUR": {
        "sale": 39.4,
        "purchase": 38.4
      },
      "USD": {
        "sale": 39.9,
        "purchase": 39.4
      }
    }
  },
  {
    "2022-11-02": {
      "EUR": {
        "sale": 39.4,
        "purchase": 38.4
      },
      "USD": {
        "sale": 39.9,
        "purchase": 39.4
      }
    }
  }
]
Command-Line Arguments
Days (required): The number of days for which you want to fetch exchange rates (from 1 to 10).
Error Handling
If there are any network issues, the program will catch and display an appropriate error message without crashing.
License
This project is licensed under the MIT License.

Notes
Make sure the aiohttp library is properly installed for async HTTP requests.
You can modify the script to support additional currencies or other API sources in the future.
This README.md provides clear instructions for using and setting up the utility, explaining how to pass arguments and showcasing example outputs.
