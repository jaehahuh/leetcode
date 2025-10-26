class Bank:

    def __init__(self, balance: List[int]):
        self.n = len(balance)
        self.bank_account = [0] * (self.n + 1)
        for i, money in enumerate(balance):
            self.bank_account[i + 1] = money
    
    def _valid(self, account):
        return 1 <= account <= self.n

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not (self._valid(account1) and self._valid(account2)):
            return False
        if self.bank_account[account1] < money:
            return False
        self.bank_account[account1] -= money
        self.bank_account[account2] += money
        return True
            

    def deposit(self, account: int, money: int) -> bool:
        if not self._valid(account):
            return False
        self.bank_account[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self._valid(account):
            return False
        if self.bank_account[account] < money:
            return False
        self.bank_account[account] -= money
        return True

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)