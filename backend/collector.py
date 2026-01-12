import mysql.connector
import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()


DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'port': int(os.getenv('DB_PORT')),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': 'bitcoin,ethereum,cardano',
        'vs_currencies': 'usd'
    }
    response = requests.get(url, params=params)
    return response.json()

def save_to_db(data):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        for coin in data:
            price = data[coin]['usd']
            sql = "INSERT INTO prices (coin_name, price_usd) VALUES (%s, %s)"
            cursor.execute(sql, (coin, price))
            print(f"✅ Αποθηκεύτηκε: {coin} -> {price} USD")
            
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"❌ Σφάλμα βάσης: {e}")

if __name__ == "__main__":
    print("Ξεκινάει ο Collector... (Ctrl+C για έξοδο)")
    while True:
        try:
            prices = fetch_crypto_data()
            save_to_db(prices)
        except Exception as e:
            print(f"❌ Σφάλμα API: {e}")
        
        time.sleep(60)