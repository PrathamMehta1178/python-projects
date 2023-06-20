def cheesencrackers(cheese_count, boxes_count):
    print(f'You have {cheese_count} cheeses')
    print(f'You have {boxes_count} boxes of crackers')
    print('Thats enough for a party')
    print('Get a blanket\n')

print("We can just give the function numbers directly")
cheesencrackers(20,30)

print('OR we could use variables in our script:')
amtCheese = 10
amtBoxes = 50

cheesencrackers(amtCheese, amtBoxes)

print('We can do math inside too:')
cheesencrackers(10+20, 5+6)

print('And we can combine the two, variables and math')
cheesencrackers(amtCheese+100, amtBoxes+11 )