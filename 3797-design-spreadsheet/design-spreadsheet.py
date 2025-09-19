class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = defaultdict(int)
        
    def setCell(self, cell: str, value: int) -> None:
        self.sheet[cell] = value
   
    def resetCell(self, cell: str) -> None:
        self.sheet[cell] = 0

    def getValue(self, formula: str) -> int:
        a,b = formula[1:].split('+')
        if a.isdigit():
            num1 = int(a)
        else:
            num1 = self.sheet[a]
        if b.isdigit():
            num2 = int(b)
        else:
            num2 = self.sheet[b]
        return num1 + num2

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)