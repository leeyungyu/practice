
import Algorithm as al
from datetime import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import myfunc as mf

lists = 'TRX,NEO,BLZ,ICX,EOS,VEN,XRP,ADA,XLM,FUN,BNB,DGD,LTC,IOTA,CTR,WTC,CND,QSP,OMG,PPT,ZRX,IOST,GXS,XVG,BQX,LSK,REQ,POWR,POE,ELF,QTUM,ENG,BTS,AION,XMR,VIBE,SNT,KNC,ETC,MANA,VIB,LEND,SUB,OST,SALT,ZEC,ENJ,NEBL,HSR,NULS,LINK,BCD,LRC,WABI,TNB,GTO,ARK,TRIG,DASH,APPC,STRAT,MTL,SNGLS,MDA,INS,GVT,TNT,AST,BAT,BTG,MCO,CDT,LUN,ARN,AMB,WAVES,ADX,FUEL,BRD,RCN,XZC,MOD,NAV,EVX,DNT,KMD,BNT,ICN,BCPT,STORJ,DLT,EDO,WINGS,SNM,MTH,OAX,YOYO'.split(',')

lists = ['STORJ']
history = mf.load_csv(mf.load_csv(lists))

for coin in lists:

    ds = history[coin] # 데이터 로드

    ts = [dt.fromtimestamp(d) for d in ds.time] # 시간좌표

    length = len(ts)

    ma = mf.ma(ts, ds.KRW, 24)

    volumema = mf.ma(ts, ds.volumeto, 72)

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    d = 72
    x = length
    l = 72

    ax1.plot(ts[d:x], ds.KRW[d:x], 'black')
    ax1.plot(ts[d:x], ma[d:x], 'r')
    #ax1.plot(ts[d:x], ma5[d:x], 'r')



    #for i in range(d,x):

        #volumedel = volumema[d:x]/volumema[d-l:x-l]
        #volumedel = np.array([0]*d + volumedel.tolist())

    ax2.plot(ts[d:x], ds.volumeto[d:x]/volumema[d:x])#, bottom = 0, width = 0.05)
    #ax2.plot(ts[d:x], volumedel2[d:x], 'r')#, bottom = 0, width = 0.05)

    #for i in range(d,x):
        #if volumedel[i] > 1.25:
            #ax1.plot(ts[i],ds.KRW[i],'co', markersize = 4)





    plt.grid(True)
    plt.title('{}'.format(coin))
    #plt.gcf().savefig('data_invest/graph_{}_KRW.jpg'.format(coin), dpi = 600)
    print('{} saved'.format(coin))
    plt.show()
    plt.close()


# 빨간 점에서 사고, 10프로 떨어지면 바로 sell 혹은 40프로 오르면 바로 sell.