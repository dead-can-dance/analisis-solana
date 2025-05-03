import requests
import pandas as pd
from datetime import datetime

# Configura los parámetros
symbol = "SOLUSDT"
interval = "1d"
start_str = "2022-03-13 00:00"
end_str = "2022-04-01 00:00"

# Convierte las fechas a timestamps en milisegundos
start_time = int(datetime.strptime(start_str, "%Y-%m-%d %H:%M").timestamp() * 1000)
end_time = int(datetime.strptime(end_str, "%Y-%m-%d %H:%M").timestamp() * 1000)

# Llama a la API de Binance
url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&startTime={start_time}&endTime={end_time}"
response = requests.get(url)

# Procesa la respuesta
data = response.json()

# Convierte a DataFrame
df = pd.DataFrame(data, columns=[
    "Open time", "Open", "High", "Low", "Close", "Volume",
    "Close time", "Quote asset volume", "Number of trades",
    "Taker buy base asset volume", "Taker buy quote asset volume", "Ignore"
])

# Limpia y guarda
df["Open time"] = pd.to_datetime(df["Open time"], unit='ms')
df = df[["Open time", "Open", "High", "Low", "Close", "Volume"]]
df.to_csv("solana_exponential_data.csv", index=False)

print("CSV guardado como 'solana_exponential_data.csv'")
