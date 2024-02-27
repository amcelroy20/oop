import CellPhoneClass as cell

def main():
    phone = cell.CellPhone()

    print('The manufacturer of the phone is: ', phone.get_manufact())
    print('The model of the phone is: ', phone.get_model())
    print(f'The price of the phone is: $', format(phone.get_retail_price(),',.2f'))

    x=input('would you like to input new values? y or n')

    while x != 0:
    
        if x == 'y':
            phone.set_manufact(input('Phone manufacturer?'))
            phone.set_model(input('Phone Model?'))
            phone.set_retail_price(input('Phone Price?'))

            print('The manufacturer of the phone is: ', phone.get_manufact())
            print('The model of the phone is: ', phone.get_model())
            print(f'The price of the phone is: $', format(int(phone.get_retail_price()),',.2f'))

            print('Thank you, have a nice day.')
            x=0
        elif x == 'n':
            print('Thank you, have a nice day.')
            x=0
        else:
            x=input('would you like to input new values? y or n')

main()