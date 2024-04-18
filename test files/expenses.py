expenses = [10.50, 8, 5, 15, 20, 5, 3]

sum(expenses)

print('You spent $', sum(expenses), sep = '')

newExpenses = []
for i in range(7):
    newExpenses.append(float(input('Enter an expense:\n')))

print('You spent $', sum(newExpenses), sep = '')