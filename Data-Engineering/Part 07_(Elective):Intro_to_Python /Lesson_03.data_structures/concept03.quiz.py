month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
#num_days = [len(days_in_month) - 1]
num_days = days_in_month[9]
#Juno's code: num_days = days_in_month[month - 1]

print(num_days)

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
print(eclipse_dates[-3:])
