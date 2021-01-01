def future_value_investment(PV,r,n):

    FV = PV*(1+r/100)**n
    return FV
print(future_value_investment(10000,3.5,7))