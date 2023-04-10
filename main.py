import sys
import random

def main():

    print('Добро пожаловать в игру "Подбор имён для напарника" '
          'как в сериале Ясновидец\n')
    print('Наподобие того как это делал Шин для напарника Гаса:\n\n')

    first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
            "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite'",
            'Butterbean', 'Buttermilk', 'Buttocks', 'Chad',
            'Chesterfield', 'Chewy', 'Chigger', 'Cinnabans', 'Cleet',
            'Cornbread', 'Crab Meat', 'Crapps', 'Dark Skies',
            'Dennis Clawhammer', 'Dicman', 'Elphonso', 'Fancypants',
            'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
            'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
            'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"',
            'Mergatroid', '"Mr Peabody"', 'Oil-Can', 'Oinks',
            'Old Scratch', 'Ovaltine', 'Pennywhistle', 'Pitchfork Ben',
            'Potato Bug', 'Pushmeet', 'Rock Candy', 'Schlomo',
            'Scratchensniff', 'Scut', "Sid 'The Squirts'",
            'Skidmark', 'Slaps', 'Snakes', 'Snoobs', 'Snorki',
            'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
            'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
            "Winston 'Jazz Hands'", 'Worms')

    last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
            'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
            'Cocktoasten', 'Endicott', 'Fewhairs', 'Goobedapple',
            'Goodensmith', 'Goodpasture', 'Guster', 'Henderson',
            'Hooperbag', 'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins',
            'Jingley-Schmidt', 'Johnson', 'Kingfish', 'Listenbee',
            "M'Bembo", 'McFadden', 'Moonshine', 'Nettles', 'Noseworthy',
            'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf', 'Oxhandler',
            'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow', 'Pinkerton',
            'Porkins', 'Putney', 'Quakenbush', 'Rainwater', 'Rosenthal',
            'Rubbins', 'Sackride', 'Snuggleshine', 'Splern', 'Stevens',
            'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
            'Turnipseed', 'Vinaigrette', 'Walkigstick', 'Wallbanger',
            'Weewax', 'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch',
            'Winterkorn', 'Woolysocks')

    while True:
        # с помощью функции choice из кортежа first
        # выбирается один из элементов
        first_name = random.choice(first)
        # с помощью функции choice из кортежа last
        # выбирается один из элементов
        last_name = random.choice(last)

        print("\n\n")
        # мы форматируем и переданные значения first_name и
        # last_name печатаются в {} {} в том порядке,
        # в котором указаны в format()
        print("{} {}".format(first_name, last_name), file = sys.stderr)
        print("\n\n")

        try_again = input("\n\n Enter чтобы продолжить, n чтобы выйти\n")
        if try_again.lower() == 'n':
            break

        input("\n Enter to exit.")
if __name__ == "__main__":
    main()