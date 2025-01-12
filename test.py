from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def main():

    url = 'https://robinhood.com/us/en/crypto/BONK/'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    main = soup.find_all('span', {'class': 'css-y3z1hq'})
    output = []
    for index, i in enumerate(main):
        if 2 <= index <= 79:
            output.append(i.text)
    
    return output

if __name__ == '__main__':
    app.run()