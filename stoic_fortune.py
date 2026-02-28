# Read my fortune function!!

def fortune():
    import random
    cookie = random.randint(1, 8)
    if cookie == 1:
        print("We suffer more in imagination than in reality.")
    elif cookie == 2:
        print("You have power over your mind, not outside events. Realize this, and you will find strength.")
    elif cookie == 3:
        print("He who fears death will never do anything worthy of a living man.")
    elif cookie == 4:
        print("Make the best use of what is in your power, and take the rest as it happens.")
    elif cookie == 5:
        print("Waste no more time arguing what a good man should be. Be one.")
    elif cookie == 6:
        print("It is not that I am brave, but that I know what is not worth fearing.")
    elif cookie == 7:
        print("Begin at once to live, and count each separate day as a separate life.")
    else:
        print("The happiness of your life depends upon the quality of your thoughts.")

fortune()
