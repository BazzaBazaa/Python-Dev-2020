def savings_info(years, amount, percent):
    total = 0
    for x in range(years):
        total = (total + amount) * percent
    total = round(total,2)
    return f'''
    After {years} years, if you save {amount} a year.
    At {int((percent-1) *100)}% interest rate per year. No withdrawls. 
    You will have saved {total}.
    '''

years = int(input('how many years will you invest?'))
amount = int(input('how much will you invest each year?'))
percent = float(input('how much percent interest will you get each year?'))
print(savings_info(years, amount, (1+(percent/100))))


