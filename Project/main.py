import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

conn = sqlite3.connect('temperature_database.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS temperature
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              date TEXT,
              time TEXT,
              temperature REAL)''')

url = 'https://www.example-weather-website.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
temperature = soup.find('div', {'class': 'temperature'}).text


now = datetime.now()
date = now.strftime('%Y-%m-%d')
time = now.strftime('%H:%M:%S')
c.execute("INSERT INTO temperature (date, time, temperature) VALUES (?, ?, ?)", (date, time, temperature))

conn.commit()
conn.close()
