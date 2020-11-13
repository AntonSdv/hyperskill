def status(water, milk, beans, cups, money):
    print('The coffee machine has:')
    print(water, ' of water')
    print(milk, ' of milk')
    print(beans, ' of coffee beans')
    print(cups, ' of disposable cups')
    print(money, ' of money')


def buy(w, m, b, c, my):
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    c = input()
    global water, beans, cups, milk, money
    if c == '1':
        if water < 250:
            print('Sorry, not enough water!')
        elif beans < 16:
            print('Sorry, not enough cofee beans!')
        elif cups < 1:
            print('Sorry, not enough cups!')
        else:
            water -= 250
            beans -= 16
            cups -= 1
            money += 4
            print('I have enough resources, making you a coffee!')

    if c == '2':
        if water < 350:
            print('Sorry, not enough water!')
        elif milk < 75:
            print('Sorry, not enough milk!')
        elif beans < 20:
            print('Sorry, not enough cofee beans!')
        elif cups < 1:
            print('Sorry, not enough cups!')
        else:
            water -= 350
            milk -= 75
            beans -= 20
            cups -= 1
            money += 7
            print('I have enough resources, making you a coffee!')

    if c == '3':
        if water < 200:
            print('Sorry, not enough water!')
        elif milk < 100:
            print('Sorry, not enough milk!')
        elif beans < 12:
            print('Sorry, not enough cofee beans!')
        elif cups < 1:
            print('Sorry, not enough cups!')
        else:
            water -= 200
            milk -= 100
            beans -= 12
            cups -= 1
            money += 6
            print('I have enough resources, making you a coffee!')
    if c == 'back':
        return



def fill(w, m, b, c, my):
    global water, beans, cups, milk, money
    print('Write how many ml of water do you want to add:')
    water += int(input())
    print('Write how many ml of milk do you want to add:')
    milk += int(input())
    print('Write how many grams of coffee beans do you want to add:')
    beans += int(input())
    print('Write how many disposable cups of coffee do you want to add:')
    cups += int(input())


def take(m):
    global money
    print('I gave you $', money)
    money = 0


water = 400
milk = 540
beans = 120
cups = 9
money = 550
a = 0
while a != 'exit':
    print('Write action (buy, fill, take, remaining, exit):')
    a = input()
    if a == 'buy':
        buy(water, milk, beans, cups, money)
    elif a == 'fill':
        fill(water, milk, beans, cups, money)
    elif a == 'take':
        take(money)
    elif a == 'remaining':
        status(water, milk, beans, cups, money)
