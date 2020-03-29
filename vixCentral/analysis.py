import pandas as pd
from datetime import date
import os

AV_API_KEY = os.environ.get('AV_API_KEY')
SH_API_KEY = os.environ.get('SH_API_KEY')

# DELTA
f_date = date(2020, 3, 20)
l_date = date.today()
delta = (l_date - f_date).days

# Read in scraped data
df = pd.read_json(
    f"https://storage.scrapinghub.com/items/438867/1/{delta}?apikey={SH_API_KEY}&format=json")
to_date = df['date'][0].strftime('%Y-%m-%d')
from_date = df['date'][20].strftime('%Y-%m-%d')

# VIX
vix = pd.read_json(
    f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=VIX&apikey={AV_API_KEY}")
vix = vix['Time Series (Daily)']
df['F0'] = [vix.loc[i.strftime("%Y-%m-%d")]["4. close"] for i in df["date"]]

# SPY
spy = pd.read_json(
    f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=SPY&apikey={AV_API_KEY}")
spy = spy['Time Series (Daily)']
df['SPY'] = [spy.loc[i.strftime("%Y-%m-%d")]["4. close"] for i in df["date"]]

# Clean dataframe
df = df[['date', 'SPY', 'F0', 'F1', 'F2',
         'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9']]
df['SPY'] = df['SPY'].astype('float64')
df['F0'] = df['F0'].astype('float64')
df['F9'] = df['F9'].replace('-', 'nan').astype('float64')
df['date'] = df['date'].dt.date
df.set_index('date', inplace=True)

# Calculations
df['C0'] = df['F1']/df['F0']-1
df['C1'] = df['F2']/df['F1']-1
df['C2'] = df['F3']/df['F2']-1
df['C3'] = df['F4']/df['F3']-1
df['C4'] = df['F5']/df['F4']-1
df['C5'] = df['F6']/df['F5']-1


# Output

today = date.today().strftime("%m.%d.%y")
df.to_csv('VIX.csv')
