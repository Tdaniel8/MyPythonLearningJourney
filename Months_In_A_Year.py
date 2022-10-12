print('Enter day: ')
Month = int(input())

Months_of_year = ('January(30)','Febuary(28)','March(31)','April(30)',
                  'May(31)','June(30)',
                  'July(31)','August(31)','September(30)','Octomber(31)',
                  'November(30)','December(31)'
                  )
if (Month > 0) and (0 < 13):
    print(Months_of_year[Month-1])
else:
    print('Invalid Format')
