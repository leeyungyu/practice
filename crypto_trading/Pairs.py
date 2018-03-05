# 파일명 : Pairs.py
# 제작자 : 이윤규
# 설 명 : 바이낸스에서 이더리움으로 거래를 취급하는 쌍을 모조리 찾아온다.
# ------ Pairs().find_bade(coin)

from bs4 import BeautifulSoup
from urllib.request import urlopen

import collections as col
import numpy as np

class Pairs: # 거래 짝을 찾아내는 코드

    def __init__(self):
        # coinmarketcap 크롤링. 이게 제일 편해보여서.
        self.url = 'https://coinmarketcap.com/exchanges/binance/'
        web = urlopen(self.url)
        source = BeautifulSoup(web, 'html.parser')
        table = source.find('table', {'id' : 'exchange-markets'})
        body = table.find('tbody')
        trades = body.find_all('a', {'target' : '_blank'})
        # BTC/ETH의 꼴로 결과 리스트가 뽑아지는데, 이걸로 어레이를 만든다.
        pairs = [trade.get_text().split('/') for trade in trades]
        pairs_array = np.array(pairs).reshape(len(pairs),2)
        self.pairs = pairs_array
        # 거래 수단으로 쓰이는 코인은?(보통 BTC, ETH, USDT)
        base_dict = dict(col.Counter(self.pairs[:,1]))
        self.base_dict = base_dict

    # 거래 수단을 기준으로 코인 명단을 뽑아보자.
    def find_base(self, coin):
        base_list = []
        for pair in self.pairs:
            if pair[1] == coin.upper():
                base_list.append(pair)
            base_pairs = np.array(base_list)
        return base_pairs