a = [-11000, 3000, 4000, 6000, 5000, 5000]


cash_flow = [-100,30,20,40,30]
def npv(cash_flow,r):
    total = 0.0
    for i,cash in enumerate(cash_flow):
        total += cash/(1+r)**i
    return round(total,2)

def IRR(cashflow,iterations):
    '''
    returns an internal rate of return
    :param cashflow: [-30,20,10,5]
    :param iterations: 10
    :return: the float number
    '''
    rate = 1.0
    investment = cashflow[0]
    for i in range(1,iterations+1):
        rate*=(1-npv(cashflow,rate)/investment)
    return round(rate,4)

r = IRR(a,iterations=50)
print('r:',r,'%')
print(npv(a,r))