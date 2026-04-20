class atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin
    def cash_withdrawal():
        print("withdhraw cash")
    def cash_depoist():
        print("deposit cash")
    def check_balance():
        print("check balance")
user=atm(0000,1234)
print(user.cash_withdrawal)
print(user.cash_depoist)
print(user.check_balance)