from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
  order_name = input(f"​What would you like? Type: {menu.get_items()} ")

  if order_name == "off":
    is_on = False
    print('Turning coffee machine off.')

  elif order_name == "report":
    coffee_maker.report()
    money_machine.report()

  else:
    drink = menu.find_drink(order_name)

    if drink is not None:
      can_make = coffee_maker.is_resource_sufficient(drink)

      if can_make:
        payment = money_machine.make_payment(drink.cost)
        if payment:
          coffee_maker.make_coffee(drink)



