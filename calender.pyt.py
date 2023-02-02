#import calendar module
import calendar;

yy=int(input("Enter year: "))
mm=int(input("Enter month: "))
print(calendar.month(yy,mm))
user_input = (input('Enter month: '))


while user_input != 'stop':
    print(calendar.month(yy,int( user_input )))
    user_input = input('Enter month: ')
