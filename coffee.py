class Coffee:
    def __init__(self, hot_water, hot_milk, ginger_syrup, sugar_syrup, tea_leaves_syrup):
        self.hot_water = hot_water
        self.hot_milk = hot_milk
        self.ginger_syrup = ginger_syrup
        self.sugar_syrup = sugar_syrup
        self.tea_leaves_syrup = tea_leaves_syrup

class HotTea:
    def __init__(self, hot_water, hot_milk, ginger_syrup, sugar_syrup, tea_leaves_syrup):
        self.hot_water = hot_water
        self.hot_milk = hot_milk
        self.ginger_syrup = ginger_syrup
        self.sugar_syrup = sugar_syrup
        self.tea_leaves_syrup = tea_leaves_syrup

class Blacktea:
    def __init__(self, hot_water, ginger_syrup, sugar_syrup, tea_leaves_syrup):
        self.hot_water = hot_water
        self.ginger_syrup = ginger_syrup
        self.sugar_syrup = sugar_syrup
        self. tea_leaves_syrup = tea_leaves_syrup

class Greentea:
    def __init__(self, hot_water, ginger_syrup, sugar_syrup, green_mixture):
        self.hot_water = hot_water
        self.ginger_syrup = ginger_syrup
        self.sugar_syrup = sugar_syrup
        self.green_mixture = green_mixture


class Beverage:
    hot_coffee = Coffee(100, 400, 30, 50, 30)
    tea1 = HotTea(200, 100, 10, 10, 30)
    black_tea1 = Blacktea(300, 30, 50, 30)
    green_tea1 = Greentea(100, 30, 50, 30)


# noinspection SpellCheckingInspection
class Resources:
    def __init__(self):
        self.hot_water = 400
        self.hot_milk = 540
        self.ginger_syrup = 100
        self.sugar_syrup = 100
        self.tea_leaves_syrup = 100
        self.green_mixture = 0

    def prepare_coffee(self, coffee):
        """Checks enough resources for making coffee, if there are enough resources, it makes coffee"""
        hot_water = self.hot_water - coffee.hot_water
        hot_milk = self.hot_milk - coffee.hot_milk
        ginger_syrup = self.ginger_syrup - coffee.ginger_syrup
        sugar_syrup = self.sugar_syrup - coffee.sugar_syrup
        tea_leaves_syrup = self.tea_leaves_syrup - coffee.tea_leaves_syrup
        
        if hot_water < 0:
            print('Sorry, coffee cannot be prepared because not enough water!')
        elif hot_milk < 0:
            print('Sorry, coffee cannot be prepared because not enough milk!')
        elif ginger_syrup < 0:
            print('Sorry,coffee cannot be prepared because not enough ginger syrup!')
        elif sugar_syrup < 0:
            print('Sorry, coffee cannot be prepared because not enough sugar syrup!')
        elif tea_leaves_syrup < 0:
            print('Sorry, coffee cannot be prepared because not enough tea leaves syrup!')
        else:
            print('Coffee Prepared!')
            self.hot_water = hot_water
            self.hot_milk = hot_milk
            self.ginger_syrup = ginger_syrup
            self.sugar_syrup = sugar_syrup
            self.tea_leaves_syrup = tea_leaves_syrup
    
    def prepare_hot_tea(self, tea):

        """Checks enough resources for making coffee, if there are enough resources, it makes tea"""
        hot_water = self.hot_water - tea.hot_water
        hot_milk = self.hot_milk - tea.hot_milk
        ginger_syrup = self.ginger_syrup - tea.ginger_syrup
        sugar_syrup = self.sugar_syrup - tea.sugar_syrup
        tea_leaves_syrup = self.tea_leaves_syrup - tea.tea_leaves_syrup
        
        if hot_water < 0:
            print('Sorry, hot tea cannot be prepared beacause not enough water!')
        elif hot_milk < 0:
            print('Sorry, hot tea cannot be prepared beacause not enough milk!')
        elif ginger_syrup < 0:
            print('Sorry, hot tea cannot be prepared beacause not enough ginger syrup!')
        elif sugar_syrup < 0:
            print('Sorry, hot tea cannot be prepared beacause not enough sugar syrup!')
        elif tea_leaves_syrup < 0:
            print('Sorry, hot tea cannot be prepared beacause not enough tea leaves syrup!')
        else:
            print('Hot tea Prepared!')
            self.hot_water = hot_water
            self.hot_milk = hot_milk
            self.ginger_syrup = ginger_syrup
            self.sugar_syrup = sugar_syrup
            self.tea_leaves_syrup = tea_leaves_syrup
    
    def prepare_black_tea(self, black_tea):
        """Checks enough resources for making coffee, if there are enough resources, it makes black tea"""

        hot_water = self.hot_water - black_tea.hot_water
        ginger_syrup = self.ginger_syrup - black_tea.ginger_syrup
        sugar_syrup = self.sugar_syrup - black_tea.sugar_syrup
        tea_leaves_syrup = self.tea_leaves_syrup - black_tea.tea_leaves_syrup
        
        if hot_water < 0:
            print('Sorry, black tea cannot be prepared beacause not enough water!')
        elif ginger_syrup < 0:
            print('Sorry, black tea cannot be prepared beacause not enough ginger syrup!')
        elif sugar_syrup < 0:
            print('Sorry, black tea cannot be prepared beacause not enough sugar syrup!')
        elif tea_leaves_syrup < 0:
            print('Sorry, black tea cannot be prepared beacause not enough tea leaves syrup!')
        else:
            print('Black tea Prepared!')
            self.hot_water = hot_water
            self.ginger_syrup = ginger_syrup
            self.sugar_syrup = sugar_syrup
            self.tea_leaves_syrup = tea_leaves_syrup
    
    def prepare_greem_tea(self, green_tea):
        """Checks enough resources for making coffee, if there are enough resources, it makes green tea"""

        hot_water = self.hot_water - green_tea.hot_water
        ginger_syrup = self.ginger_syrup - green_tea.ginger_syrup
        sugar_syrup = self.sugar_syrup - green_tea.sugar_syrup
        green_mixture = self.green_mixture - green_tea.green_mixture
        
        if hot_water < 0:
            print('Sorry, Green tea cannot be prepared beacause not enough water!')
        elif ginger_syrup < 0:
            print('Sorry, Green tea cannot be prepared beacause not enough ginger syrup!')
        elif sugar_syrup < 0:
            print('Sorry, Green tea cannot be prepared beacause not enough sugar syrup!')
        elif green_mixture < 0:
            print('Sorry, Green tea cannot be prepared beacause not enough green tea mixture!')
        else:
            print('green tea prepared!')
            self.hot_water = hot_water
            self.ginger_syrup = ginger_syrup
            self.sugar_syrup = sugar_syrup
            self.green_mixture = green_mixture

    def make_coffee(self):
        """Asks the user what kind of coffee he wants and makes it"""
        choice = input('What do you want to buy? 1 - coffee, 2 - Hot tea, 3 - Black tea, 4- Green Tea, back - to main menu: ')
        if choice == '1':
            self.prepare_coffee(Beverage.hot_coffee)
        if choice == '2':
            self.prepare_hot_tea(Beverage.tea1)
        if choice == '3':
            self.prepare_black_tea(Beverage.black_tea1)
        if choice == '4':
            self.prepare_greem_tea(Beverage.green_tea1)

    

    def remaining(self):
        """Output current amount of resources"""
        print(f'The coffee machine has:')
        print(f'{self.hot_water} of water')
        print(f'{self.hot_milk} of milk')
        print(f'{self.ginger_syrup} of ginger syrup')
        print(f'{self.sugar_syrup} of sugar syrup')
        print(f'{self.tea_leaves_syrup} of tea leaves')
        print(f'{self.green_mixture} of green mixture')


class CoffeeMachine:
    def __init__(self):
        self.cup_of_coffee = Beverage()
        self.resources = Resources()
        self.run_machine()

    def run_machine(self):
        """Basic program loop and processing user commands"""
        while True:
            action = input('Write action (buy, remaining, exit): ')
            print()
            if action == 'buy':
                self.resources.make_coffee()
                print()
            elif action == 'remaining':
                self.resources.remaining()
                print()
            elif action == 'exit':
                break


machine = CoffeeMachine()