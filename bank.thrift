/**
* This is a Thrift service definition, it lets you define functions for your
* service.  Thrift will create an interface for compatible languages use use
* for your client/server.
**/

service Bank extends shared.SharedService {

    void ping(),

    bool add_account(1:i32 new_account_num),

    i32 get_balance(1:i32 account_num),

    i32 withdraw(1:i32 account_num, 2:i32 amount) throws (1:InvalidOperation insufficient_funds),

    i32 deposit(1:i32 account_num, 2:i32 amount),

}
