print("________________________________________________________________________________________________")
print("                                    LawRam Tech ")
print("                                   Money Controller")
print("________________________________________________________________________________________________")
print('\n')
print(' Welcome...!!! ')

def getting_details():
    userid=input(str("Enter the user ID : "))
    passwd = input(str('Enter the password :'))
    if userid == 'srinivasan2003':
        print('Welcome back, Srinivasan')
    else:
        print(' Invalid user ID , Try Again ')
        getting_details()
    if (passwd == 'dd@genius'):
            print('YaY,Access Granted ... !!!')

    else :
            print('Oops.. Sorry , Wrong Password. Try again.')
            getting_details()
getting_details()
def operation() :
    print(' Controll your Money ...  ')
    ti=float(input(' Enter Your Income Amount : '))
    ts=(ti/100)*20
    ps=(ti/100)*20
    savings=ts+ps
    remaining=ti-savings
    de=remaining

    print(' Your Temporary Savings is : Rs.'+str(ts)+'/-')
    print(' Your Permanent Savings is : Rs.' + str(ps) + '/-')
    print(' Your Total savings is : Rs.' + str(savings) + '/-')
    print(' Your Daily Expenditure is : Rs.' + str(de) + '/-')

operation()


