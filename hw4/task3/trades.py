from trades_logic import begin,  birge, share, output

print('Wait please. Program is working (really)')
file_name = 'trades.csv'
timelst, costlst, Qlst, birgelst = begin(file_name)
birge, dictionary = birge(birgelst)
spisok = share(timelst, costlst, Qlst, birgelst, birge)
RESULT = output(timelst, spisok, dictionary, birgelst)
print('    begin          ', 'number  ', 'cost   ', 'birga')
for i in range(0, len(RESULT)):
    print(RESULT[i])
