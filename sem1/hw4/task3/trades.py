from trades_logic import begin,  find_birge, share, output

print('Wait please. Program is working (really)')
file_name = 'trades.csv'
timelst, costlst, amountlst, birgelst = begin(file_name)
birge, dictionary = find_birge(birgelst)
LIST = share(timelst, costlst, amountlst, birgelst, birge)
RESULT = output(timelst, LIST, dictionary, birgelst)
print('    begin      ', 'number  ', 'cost   ', 'exchange')
for i in range(0, len(RESULT)):
    print(RESULT[i])
