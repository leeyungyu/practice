import matplotlib.pyplot as plt
import time
import numpy as np
import csv
from module.function import *
import pandas as pd
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------
class Coin: # 코인 데이터를 크롤링 하는 class

    def __init__(self, coin_lists, limit = 500, aggregate = 1):
        # 당신이 원하는 코인, 데이터포인트 개수, 시간간격을 정한다.
        # 나는 바이낸스를 쓰므로 바이낸스로 크롤링 할 것임.
        # status가 P이면 루프가 돌고, 다른 상태면 루프 종료
        self.coin_lists = coin_lists
        self.history = {}
        self.limit = limit
        self.aggregate = aggregate

    def process(self):

        for index, coin in enumerate(self.coin_lists):

            try:
                data_sheet = data_crawl(coin, 'ETH', self.limit, self.aggregate) # 내 코인 정보 데이터시트 생성

                self.history[coin] = data_sheet # history에 저장
                print('Coin data for {} crawled. {} of {}'.format(coin, index+1, len(self.coin_lists)))

                data_sheet.to_csv('data_csv/data_{}_KRW.csv'.format(coin), encoding='utf-8')
                print('File for {} successfully saved'.format(coin))

            except AttributeError as err:
                print('error for {} occurred. {} of {}'.format(coin,index+1, len(self.coin_lists)))
                pass

            except Exception as err:
                print(err)

        self.coin_lists = list(self.history.keys())


    def appending(self): # 데이터를 이어붙인다.

        self.history = load_csv(self.coin_lists)

        for index, coin in enumerate(self.coin_lists):

            data_sheet = self.history[coin]
            last_time = data_sheet.time.iloc[-1]
            n = float(time.time() - last_time)//3600

            if n > 0:

                new_sheet = data_crawl(coin, 'ETH', n, 1)
                print('New data of {} crawled'.format(coin))

                new_sheet.drop(new_sheet.index[[0]]) # 첫 데이터는 뺸다. 이미 있기 때문.
                refreshed_sheet = pd.concat([data_sheet, new_sheet]).drop(['Unnamed: 0'], axis = 1) # 새로 생기는 인덱스 삭제
                print('New data for {} appended to databse(csv).'.format(coin))

                self.history[coin] = refreshed_sheet

                refreshed_sheet.to_csv('data_csv/data_{}_KRW.csv'.format(coin), encoding='utf-8')
                print('New data saved to csv file. {} of {}'.format(index+1, len(self.coin_lists)))

    def save_graph(self):
        # 가격 그래프 저장
        # Coin().my_price()를 한 다음 Coin().save_graph()
        self.history = load_csv(self.coin_lists)

        for coin in self.coin_lists:
            ds = self.history[coin]
            plt.plot(ds.timestamp, ds.KRW)
            plt.xlabel('Date')
            plt.ylabel('KRW')
            plt.xticks(rotation=20)
            plt.title('{}'.format(coin))
            plt.gcf().savefig('data_graph/graph_{}_KRW.jpg'.format(coin))
            plt.close()

