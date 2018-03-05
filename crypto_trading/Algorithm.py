# 파일명 : Algorithm.py
# 제작자 : 이윤규
# 설 명 : 투자 알고리즘.
# ------ Invest().main_alg()
# ------ Invest().save_graph()

from bs4 import BeautifulSoup
from urllib.request import urlopen

import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
import myfunc as mf

class Algorithm:
    # 알고리즘 클래스
    def __init__(self, coin_lists, hist = 30, curv = 10):
        # lists : 코인들
        # hist : 몇개치 데이터?
        # curv = 변곡점 판단할때 데이터 몇개 쓸건가?
        self.coin_lists = coin_lists
        self.hist = hist
        self.curv = curv
        self.history = mf.load_csv(self.coin_lists)

        for coin in self.coin_lists: # 원래 DB에서 가져와야 하는데 지금은 편하게 엑셀에서 긁어옴

            data_sheet = self.history[coin]
            ma = mf.ma(data_sheet.timestamp, data_sheet.KRW, self.hist)
            slope = mf.slope(data_sheet.timestamp, ma, self.hist)

            data_sheet['ind'] = ma / slope
            print('invest data made for {}'.format(coin))


    def main_alg(self): # 메인 알고리즘 무조건 수정해야함

        for coin in self.coin_lists:

            length = len(self.history[coin].time)
            data_sheet = self.history[coin]
            ind = data_sheet.ind
            curv = self.curv

            for i in range(length-curv, length):

                if ind[i] < -0.015 and mf.iscurv_dn(i, ind, 6)==True:
                    data_sheet[['buy'][i]] = 'buy'
                    print('Buy signal detected for {}'.format(coin))
                    #data_sheet['buy'][i] = buy

                elif ind[i] > 0.002 and mf.iscurv_up(i, ind, 6)==True:
                    data_sheet[['buy'][i]] = 'sell'
                    print('Sell signal detected for {}'.format(coin))
                    #data_sheet['sell'][i] = sell

    def save_graph(self): # 그래프 저장

        for coin in self.coin_lists:

            data_sheet = self.history[coin]
            ts = [datetime.datetime.fromtimestamp(d) for d in data_sheet.time]
            length = len(ts)

            plt.plot(ts, data_sheet.KRW, 'black')
            for i in range(length):
                if data_sheet.buy[i] == 'buy':
                    plt.plot(ts[i], data_sheet.KRW[i], 'ro', markersize = 3)
                elif data_sheet.buy[i] == 'sell':
                    plt.plot(ts[i], data_sheet.KRW[i], 'bo', markersize =3)

            plt.title('{}'.format(coin))
            plt.xticks(rotation = 20)
            plt.gcf().savefig('data_invest/graph_{}_KRW.jpg'.format(coin))
            plt.close()






