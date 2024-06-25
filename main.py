import art, random, os
from game_data import data

def format_data(account):
    """Format the account data into printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_guess(guess, a_followers, b_followers):
    """Checks the user answer with an if statement to verify if it was right"""
    if a_followers > b_followers:
        return guess == "a"
    elif b_followers > a_followers:
        return guess == "b"


# Printin game logo
print(art.logo)
score = 0
game_over = False
account_b = random.choice(data)

while not game_over:
    # Selecting 2 random assets from 'game_data.data'
    account_a = account_b
    account_b = random.choice(data)
    # Checking to make sure that both accounts are different from each other
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(art.vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_right = check_guess(guess, a_follower_count, b_follower_count)

    # Clear screen
    os.system('cls||clear')
    print(art.logo)

    # Printing if the user got his answer right nad keeping a tally of his score
    if is_right:
        score += 1
        print(f"You are correct! Current score: {score}")
    else:
        game_over = True
        print(f"Sorry, you are wrong! Final score: {score}")