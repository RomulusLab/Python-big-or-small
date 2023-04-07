total = 0
expenses = []
num_expenses = int(input("Enter # of expenses:\n"))
for e in range(num_expenses):
    expenses.append(float(input("Enter your expenses:\n")))

total = "{:.2f}".format(sum(expenses))

print("You spend $", total, sep="")