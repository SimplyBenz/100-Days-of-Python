import art
print(art.logo)
print("Welcome to blind auction!")

def the_winner(bidder_price):

    winner_name=""
    winner_price=0

    for name in bidder_price:
        if bidder_price[name] > winner_price:
            winner_price = bidder_price[name]
            winner_name = name

    print("The winner is "+winner_name+" "+"and the bidding price is "+str(winner_price))

bidder_price={}
conti="yes"

while conti == "yes":
    name = input("What is your name? :")
    price = int(input("What is your Bid? :"))
    conti = input("Are there other bidders. Type 'Yes' or 'No").lower()
    bidder_price[name] = price
    i = 1
    while i==1 or i<101:
        print("\n")
        i += 1

the_winner(bidder_price)
