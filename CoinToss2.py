import CoinClass as c 

def show_coin_status(Coin_obj):
    print("This side is up: ", Coin_obj.get_sideup())

def flip(Coin_obj):
    Coin_obj.toss()

my_coin = c.Coin()
show_coin_status(my_coin)
flip(my_coin)