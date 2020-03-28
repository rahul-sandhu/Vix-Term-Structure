import pandas as pd
from datetime import date
import os

today = date.today()
date = today.strftime("%m.%d.%y")
API_KEY = os.environ.get('API_KEY')

# Read in scraped data
df = pd.read_json(f"VIX_{date}.json")
to_date = df['date'][0].strftime('%Y-%m-%d')
from_date = df['date'][20].strftime('%Y-%m-%d')

# VIX
vix = pd.read_json(f"https://fmpcloud.io/api/v3/historical-price-full/%5EVIX?from={from_date}&to={to_date}&apikey={API_KEY}")
vix = vix['historical']
df['F0'] = [vix[i]['close'] for i in range(len(vix))] 

# SPY
spy = pd.read_json(f"https://fmpcloud.io/api/v3/historical-price-full/SPY?from={from_date}&to={to_date}&apikey={API_KEY}")
spy = spy['historical']
df['SPY'] = [spy[i]['close'] for i in range(len(vix))] 

# Clean dataframe
df = df[['date', 'SPY', 'F0', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9']]
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




