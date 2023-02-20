





gross_income = int(input("What is your gross income?"))
tax_group_1 = (gross_income * 0.05)
tax_group_2 = (gross_income * 0.16)
tax_group_3 = (gross_income * 0.19)
tax_group_4 = (gross_income * 0.30)

if gross_income <= 100000 :
    print("gross_income:",gross_income)
    print("Net_income",gross_income - tax_group_1)
elif (gross_income >= 100001) & (gross_income <= 150000):
     print("gross_income:", gross_income)
     print("Net_income:", gross_income - tax_group_2)
elif(gross_income >=1500001) & (gross_income <= 300000): 
    print("gross_income:",gross_income)
    print("Net_income:",gross_income - tax_group_3)
else:
    print("gross_income:",gross_income)
    print("Net_income:",gross_income - tax_group_4)