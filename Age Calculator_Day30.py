#AGE CALCULATOR:

def Age():

    
    Birth_Date    = int(input('Enter the Birth Date:'))
    present_Date  = int(input('Enter the present Date:'))
    Birth_Month   = int(input('Enter Birth Month in Numericals:'))
    Present_Month = int(input('Enter Present Month in Numericals:'))
    Birth_year    = int(input('Enter your birth year :'))
    Present_year  = int(input('Enter the present year:'))

    Year          = int(Present_year - Birth_year)
    Month         = int(Present_Month - Birth_Month)
    Date          = int(present_Date - Birth_Date)
    ALL_MONTHS    = int(((Present_year - Birth_year)*12)+(Present_Month - Birth_Month))

    if Month < 0:
        Year -=1
        Month += 12

    if Date < 0:
        Month -=1
        Date  +=30    

    AGE = (f'Your Current Age is{Year}Year,{Month}Month,{Date}Day',
           f'or the Excat Month is {ALL_MONTHS} Months, {Date}Days')
    
    print(AGE)
    


Age()
