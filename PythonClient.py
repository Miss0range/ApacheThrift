import sys
import glob
sys.path.append()
sys.path.insert()

#Todo import bank_account
from bank import bank

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

def main():
    #socket
    transport = TSocket.TSocket('localhost',9090)
    #Buffering
    transport = TTransport.TBufferedTransport(transport)
    #Wrap
    protocol= TBinaryProtocol.TBinaryProtocal(transport)
    #Create client
    client = bank.Client(protocal)
    #Connect
    transport.open()
    client.ping()

    while True :
        text = raw_input("Operation:")
        if(text == "1"):



        break

if __name__ == '__main__':
    try:
        main()
    except Thrift.TException as tx:
        print('%s' % tx.message)