class Statistics:
    def __init__(self, data):
        self.data = data

    def describe(self):
        count = len(self.data)
        somma = sum(self.data)
        minimo = min(self.data)
        massimo = max(self.data)
        range_var = massimo-minimo
        media = somma/count
        mediana =  sorted(self.data)[count//2] if count % 2 != 0 else \
                  (sorted(self.data)[count//2 - 1] + sorted(self.data)[count//2]) / 2
        moda = max(set(self.data), key=self.data.count)
        varianza = sum((x - media) ** 2 for x in self.data) / count
        deviazione_standard = varianza ** 0.5
        return f"Count: {count}\nSum: {somma}\nMin: \{minimo}\nMax: {massimo}\nRange: {range_var}\nMean: {media:.2f}\nMedian: {mediana}\nMode: {moda}\nVariance: {varianza:.2f}\nStandard Deviation: {deviazione_standard:.2f}"

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print(data.describe())


class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses = {}

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_info(self):
        return f"Account Holder: {self.firstname} {self.lastname}\nTotal Income: {self.total_income()}\nTotal Expense: {self.total_expense()}"

    def add_income(self, description, amount):
        self.incomes[description] = self.incomes.get(description, 0) + amount

    def add_expense(self, description, amount):
        self.expenses[description] = self.expenses.get(description, 0) + amount

    def account_balance(self):
        return self.total_income() - self.total_expense()