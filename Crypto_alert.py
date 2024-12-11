import requests
import time

# Replace these with your actual values
TELEGRAM_API_TOKEN ='Telegram api token bot'
CHAT_ID = 'Telegram chat id here'
CRYPTO_ID = 'bitcoin'  # Example: 'bitcoin' for Bitcoin
TARGET_PRICE = 98500  # Example: 50000 for $50,000
CHECK_INTERVAL = 60  # Check every 60 seconds

def get_crypto_price(crypto_id):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data[crypto_id]['usd']

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_API_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    requests.post(url, data=payload)

def main():
    while True:
        current_price = get_crypto_price(CRYPTO_ID)
        print(f'Current price of {CRYPTO_ID}: ${current_price}')

        if current_price >= TARGET_PRICE:
            message = f'The price of {CRYPTO_ID} has reached ${TARGET_PRICE}!'
            send_telegram_message(message)
            break

        time.sleep(CHECK_INTERVAL)

if __name__ == '__main__':
    main()
