b=1000
PIN=9550
chances=3
print('**************************WELCOME TO FEDERAL BANK *********************')
while chances>=0:
    x=int(input('Enter PIN number')) 
    if x==PIN:
        print('***************login sucessful**************')
        x=int(input('press 1 to continue:'))
        if x==1:
           print('1.check balance')     
        print('2.withdraw amount')
        d=int(input('Enter your choice:'))
        if d==1:
            print('your balance is')
            print(b)
        elif d==2:
            w=int(input('Enter amount to withdraw:'))
            if w<b:
               print('withdraw successful')
            else:
                print('insufficient funds')  
    else:
             print('successfully logged out')   
else:
        print('*************invalid password**************')
chances=chances-1
if chances==0:
    print('*********************account blocked***************')
                      