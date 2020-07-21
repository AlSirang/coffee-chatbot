#this is the main script from where all function will be run
from utils import print_message, get_size, order_latte, cancel_order

# function to get order
def coffee_bot():
  print('Welcome to the cafe!')
  order_drink='y'
  drinks=[]
  while order_drink == 'y':
    size = get_size()  
    drink_type = get_drink_type()
    drink = '{} {}'.format(size, drink_type)
    print('Alright, that\'s a {}!'.format(drink))
    drinks.append(drink)
    while True:
      order_drink=input('Would you like to order another drink? (y/n)\n>> ')
      if order_drink in ['y','n', 'yes', 'sure', 'nah', 'N', 'Y']:
        break
  print('Okay, so I have:')
  for drink in drinks:
    print(drink)
  name = input('Can I get your name please? \n> ')
  print('Thanks, {}! Your order will be ready shortly.'.format(name))


#function to get drink type
def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
  cancel_order(res)
  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return order_mocha()
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()
    # if user selects other than given functions it will keep asking him to select from given menu
  
# get mocha type!
def order_mocha():
  while True:
    res=input("Would you like to try our limited-edition peppermint mocha?\n[a] Sure!\n[b] Maybe next time!\n>> ")
    if res == 'a':
      return 'peppermint mocha'
    elif res == 'b':
      return 'mocha'
    
    print_message()

#main function call
coffee_bot()
