from math import log, exp, ceil

def calculate_retirement(yearly_deposit, min_target_balance):
    '''
    @param yearly_deposit_ (int) yearly deposit amount
    @param min_target_balance (int) minimum target balance
    @return dictionary of (interest rate (int), years to save (int))
    '''
    # s = d * (1 + r) * ((1 + r) ** n - 1) / r
    # n = log(s * r / (d * (1 + r)) + 1) / log(1 + r)
    d = yearly_deposit
    s = min_target_balance
    ret = {}
    for i in range(6):
        r = (i + 1) / 100.0
        n = log(s * r / (d * (1 + r)) + 1) / log(1 + r)
        n = int(ceil(n))
        ret[i + 1] = n
    return ret
