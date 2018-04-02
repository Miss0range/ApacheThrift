import sys
import glob
sys.path.append()
sys.path.insert()

#Todo import bank_account
import BankHandler as bank

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
        text = input("Operation:1. See balance 2.Withdraw 3.deposit")
        if(text == "1"): 
            text = input("What's your account number?")
            balance = bank.get_balance(int(text))
            print(balance)
        else if(text == "2"):
            acc_num = input("Account number")
            w_draw = input("Amount to withdraw")
            nbalance = bank.withdraw(int(acc_num),int(w_draw))
            print(nbalance)
        else if(text == "3"):
            acc_num = input("Account number")
            d_pos = input("Amount to withdraw")
            nbalance = bank.withdraw(int(acc_num),int(d_pos))
            print(nbalance)
        else:
            print("Invalid operation")

if __name__ == '__main__':
    try:
        main()
    except Thrift.TException as tx:
        print('%s' % tx.message)
