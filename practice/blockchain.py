import hashlib
import json
from time import time

class Blockchain(object):
    # 체인을 관리하는 역할

    def __init__(self):
        self.chain = []
        self.current_transactions=[]

        #새로운 제네시스 블록(이전 블록이 없는 최최의 블록) 만들기
        self.new_block(previous_hash=1, proof=100)

    def new_block(self,proof,previous_hash=None):
        # 새로운 블록을 생성하고 체인에 넣는다

        '''
        index는 블록의 번호, timestamp는 블록이 만들어진 시간이다.
        transaction은 블록에 포함될 거래이다.
        proof는 논스값이고 previous_hash는 이전 블록의 해쉬값이다.
        '''
        block = {
            'index':len(self.chain)+1,
            'timestamp':time(),
            'transaction':self.current_transactions,
            'proof':proof,
            'previous_hash': previous_hash of self.hash(self.chain[-1])
        }

        # 거래 리스트 초기화
        self.current_transactions = []
        return block

    def new_transaction(self,sender,recipient,amount):
        '''
        새로운 거래는 다음으로 채굴될 블록에 포함되게 된다. 거래는 3개의 인자로 구성되어 있다.
        sender와 recipient는 string으로 각각 수신자와 송신자의 주소이다.
        amount는 int로 전송되는 양을 의미한다. return은 해당 거래가 속해질 블록의 숫자를 의미한다.
        '''

        self.current_transactions.append({
            'sender':sender,
            'recipient':recipient,
            'amount':amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # 블록의 해시값을 출력한다.
        
        '''
        SHA-256을 이용하여 블록의 해시값을 구한다.
        해시값을 만드는데 block이 input 값으로 사용된다.
        '''

        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        # 체인의 가장 마지막 블록을 반환한다.
        pass


block = {
    'index': 1,
    'timestamp': 1506057125.900785,
    'transactions': [
        {
            'sender': "8527147fe1f5426f9dd545de4b27ee00",
            'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
            'amount': 5,
        }
    ],
    'proof': 324984774000,
    'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
    # 이전 블록의 해쉬를 포함한다.
    # 블록체인에 변경 불가능성을 넣어준다.
}

