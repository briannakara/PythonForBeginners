import random
print("let's pick your coffee for today!")

#holds flavors for the 'choose for me' option
fancy_flavors_iced_es = ["you should drink a tiramisu latte! here's a recipe for you: https://www.coffeesphere.com/tiramisu-latte/", "you should drink an iced white chocolate mocha! here's a recipe for you: https://www.coffeesphere.com/iced-white-chocolate-mocha/", "you should drink an iced brown sugar shaken espresso! here's a recipe for you: https://basilandbubbly.com/iced-brown-sugar-oatmilk-shaken-espresso-starbucks-copycat/"]
fancy_flavors_hot_es = ["you should drink a smore's latte! here's a recipe for you: https://www.coffeesphere.com/smores-latte/", "you should drink a white chocolate mocha! here's a recipe for you: https://bakingamoment.com/white-chocolate-mocha/", "you should drink a honey flat white! here's a recipe for you: https://www.coffeesphere.com/almondmilk-honey-flat-white/"]
fancy_flavors_iced_no = ["you should drink a cinnamon iced coffee! here's a recipe for you: https://whatthefroth.com/cinnamon-iced-coffee/", "you should drink an iced mocha! here's a recipe for you: https://coffeeatthree.com/iced-mocha/", "you should drink a dalgona coffee! here's a recipe for you: https://coffeeatthree.com/dalgona-coffee/"]
fancy_flavors_hot_no = ["you should drink a mint mocha! here's a recipe for you: https://www.whattheforkfoodblog.com/2016/11/28/easy-mint-mocha-coffee-recipe/", "you should drink a cinnamon dolce latte! here's a recipe for you: https://diethood.com/starbucks-cinnamon-dolce-latte/", "you should try a lavender latte! here's a recipe for you: https://blondieishatkitchen.com/en_US/domace-levandulove-latte/"]


#possible drinks include: iced vanilla latte, iced caramel latte, hot vanilla latte, hot caramel latte, hot drip coffee
#determines if drink is iced or hot
weather = input("what's the weather like? (\"hot\" or \"cold\") ").lower()
flavor = input("what's your preferred coffee flavor? (\'vanilla\' or \'caramel\' or \'something interesting\' or \'neither\') ").lower()
espresso_machine = input("do you have access to an espresso machine? (\'yes\' or \'no\') ").lower()

#codes for the drinks
if weather == "hot" and flavor == "vanilla" and espresso_machine == "yes":
    print("you should drink an iced vanilla latte! here's a recipe for you: https://www.acouplecooks.com/iced-vanilla-latte/ ")
elif weather == "hot" and flavor == "vanilla" and espresso_machine == "no":
    print("you should drink an iced vanilla latte! here's a recipe for you: https://snacksandsips.com/iced-vanilla-latte-starbucks-copycat/")
elif weather == "hot" and flavor == "caramel" and espresso_machine == "yes":
    print("you should drink an iced caramel latte! here's a recipe for you: https://coffeeaffection.com/iced-caramel-latte-recipe/")
elif weather == "hot" and flavor == "caramel" and espresso_machine == "no":
    print("you should drink an iced caramel latte! here's a recipe for you: https://snacksandsips.com/iced-caramel-latte-starbucks-copycat/")
elif flavor == "neither":
    print("ok... drink some black drip coffee.")
elif weather == "cold" and flavor == "vanilla":
    print("you should drink a hot vanilla latte! here's a recipe for you: https://coffeeaffection.com/how-to-make-a-vanilla-latte/")
elif weather == "cold" and flavor == "caramel":
    print("you should drink a hot caramel latte! here's a recipe for you: https://coffeeaffection.com/how-to-make-a-caramel-latte/")
elif weather == "hot" and flavor == "something interesting" and espresso_machine == "yes":
    programs_choice = random.choice(fancy_flavors_iced_es)
    print(programs_choice)
elif weather == "cold" and flavor == "something interesting" and espresso_machine == "no":
    programs_choice_hn = random.choice(fancy_flavors_hot_no)
    print(programs_choice_hn)
elif weather == "hot" and flavor == "something interesting" and espresso_machine == "no":
    programs_choice_cn = random.choice(fancy_flavors_iced_no)
    print(programs_choice_cn)
elif weather == "cold" and flavor == "something interesting" and espresso_machine == "yes":
    programs_choice_hy = random.choice(fancy_flavors_hot_es)
    print(programs_choice_hy)