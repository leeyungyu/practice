from bs4 import BeautifulSoup
from urllib.request import urlopen

import requests
import datetime
import pandas as pd
import numpy as np


def data_crawl(a, b, c, d): # 과거 데이터를 크롤링한다.
    # cryptocompare 사이트로 바이낸스 정보 크롤링
    # 이게 쉬워서 했는데 바이낸스에서 바로 긁어오는게 더 빠를 듯
    url = 'https://min-api.cryptocompare.com/data/histohour?fsym={}&tsym={}&limit={}&aggregate={}&e=Binance'.format(a,b, c, d)
    page = requests.get(url)
    data = page.json()['Data']
    df = pd.DataFrame(data)
    df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
    df = df[['timestamp', 'time', 'close', 'volumeto']]
    return df

def exchange_rate(): # 네이버 검색결과로 환율정보 크롤링
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=1%EB%8B%AC%EB%9F%AC'
    web = urlopen(url)
    source = BeautifulSoup(web, 'html.parser')
    box = source.find('div', {'class' : 'rate_tlt'})
    a = box.find('strong').get_text()
    exrate = float(a.replace(',','')) # 환율의 쉼표를 제거해주고 숫자로 변환
    return exrate

def slope(x, y, limit = 2): # limit시간동안의 변동을 최소제곱법 기울기로 보는 함수
    slope = []
    for i in range(limit-1, len(x)):
        x_lim = np.array(list(range(limit)))
        y_lim = np.array(y[i-limit+1:i+1])
        A = np.vstack([x_lim, np.ones(len(x_lim))]).T # 일차함수는 y = Ap, A = [x,1], p = [m,c]로 구할 수 있음.
        m = np.linalg.lstsq(A, y_lim)[0][0]
        slope.append(m)
    slope_array = np.array([0]*(limit-1) + slope)
    return slope_array

def ma(x, y, limit = 2 , gap = 1): # 이동평균(moving average)내는 함수
    ma_list = []
    for i in range(len(y)-limit+1):
        mean = np.mean(y[i:i+limit:gap])
        ma_list.append(mean)
    ma_array = np.array([0]*(limit-1) + ma_list)
    return ma_array

def load_csv(coin_list): #csv 데이터 로딩.
    history = {}
    for coin in coin_list:
        data_sheet = pd.read_csv('data_csv/data_{}_KRW.csv'.format(coin), encoding='utf-8')
        history[coin] = data_sheet
    return history
'''
def iscurv_up(index, y, limit):
    last = index
    middle = index - limit//2
    first = index - limit

    left = [bool(y[i]-y[i+1]<0) for i in range(first,middle-1)]
    right = [bool(y[i]-y[i+1]>0) for i in range(middle-1, last-1)]

    return bool(sum(left) + sum(right) == len(right) + len(left)) # True if 위로 볼록

def iscurv_dn(index, y, limit): # 10, 6
    last = index # 10
    middle = index - limit//2 # 7
    first = index - limit # 4

    left = [bool(y[i]-y[i+1]>0) for i in range(first,middle-1)] # 5 6
    right = [bool(y[i]-y[i+1]<0) for i in range(middle-1, last-1)] # 7 8

    return bool(sum(left) + sum(right) == len(right) + len(left)) # True if 아래로 볼록
'''

