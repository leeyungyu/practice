# 생성날짜 : 20180210 01:30AM
# 제작한놈 : 이윤규
# 만든목적 : 크롤링 시범가동

from Coin import Coin
from Pairs import Pairs
from Algorithm import Algorithm
import myfunc as mf
import time
import datetime


print('importing done')

'''
find_pairs = Pairs()
find_base = find_pairs.find_base('ETH') # 이더리움으로 거래되는 코인 목록을 뽑아옴
coin_list = [coin for coin in find_base[:,0]]
print('list crawling done')
'''
coin_list = 'TRX,NEO,BLZ,ICX,EOS,VEN,XRP,ADA,XLM,FUN,BNB,DGD,LTC,IOTA,CTR,WTC,CND,QSP,OMG,PPT,ZRX,IOST,GXS,XVG,BQX,LSK,REQ,POWR,POE,ELF,QTUM,ENG,BTS,AION,XMR,VIBE,SNT,KNC,ETC,MANA,VIB,LEND,SUB,OST,SALT,ZEC,ENJ,NEBL,HSR,NULS,LINK,BCD,LRC,WABI,TNB,GTO,ARK,TRIG,DASH,APPC,STRAT,MTL,SNGLS,MDA,INS,GVT,TNT,AST,BAT,BTG,MCO,CDT,LUN,ARN,AMB,WAVES,ADX,FUEL,BRD,RCN,XZC,MOD,NAV,EVX,DNT,KMD,BNT,ICN,BCPT,STORJ,DLT,EDO,WINGS,SNM,MTH,OAX,YOYO'.split(',')

crawl = Coin(coin_list, 800, 1)

'''
crawl.process()
print('All savings done!')
'''

n = 0

while True:
    now = time.time()//1



    print('start appending')

    crawl.appending()

    n += 1

    print('cycle {} done. {}'.format(n, datetime.datetime.fromtimestamp(now)))

    time.sleep(600)




