# simple_block.py
# 아주 간단한 블록체인 구현
# 20180329

import hashlib as hasher # hash 만들어주는 패키지
import datetime as date
import time

class Block:
    def __init__(self, index, timestamp, data, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256() # hash해주는 함수

        str_index = str(self.index) # 모든 데이터를 문자열로 변환하고
        str_ts = str(self.timestamp)
        str_data = str(self.data)
        str_ph = str(self.prev_hash)

        this_hash = str_index + str_ts + str_data + str_ph

        sha.update(this_hash.encode('utf-8')) # hash 시켜준다

        return sha.hexdigest() # hash된 문자열 반환


class Chain:
    def __init__(self):
        self.genesis_block = self.genesis_block()
        self.chain = [self.genesis_block]

    def genesis_block(self): # create genesis block (index = 1)
        return Block(0, date.datetime.now(), 'genesis block', '0')

    def next_block(self, last_block): # create next block
        index = last_block.index + 1
        timestamp = date.datetime.now()
        data = '{} block'.format(index)
        this_hash = last_block.hash

        return Block(index, timestamp, data, this_hash)

    def execute(self, iteration):
        for i in range(iteration):
            prev_block = self.chain[i]
            added_block = self.next_block(prev_block)
            self.chain.append(added_block)
            print('Chain #{} : {}'.format(added_block.index, added_block.hash))
            time.sleep(1)





