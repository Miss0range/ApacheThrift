import org.apache.thrift.TException;

// Generated code
import tutorial.*;

import java.util.HashMap;

public class BankHandler implements Bank.Iface {

  private HashMap<Integer,Integer> accountBalances;

  public BankHandler() {
    accountBalances = new HashMap<Integer, Integer>();
  }

  public void ping() {
    System.out.println("ping()");
  }
	
  public int get_Balance(int account_num){
	return accountBalances.get(acct_num);
  }
  
  public int withdraw(int account_num, int amount) throws InvalidOperation {
	int newBalance = accountBalances.get(account_num) - amount;
	if(newBalance < 0){
		throw new InvalidOperation();
	}
	accountBalances.replace(account_num, newBalance);
	return newBalance;
  }  
  
  public int deposit(int account_num, int amount){
	int newBalance = accountBalances.get(account_num) + amount;
	accountBalances.replace(account_num, newBalance);
	return newBalance;
  }
}
