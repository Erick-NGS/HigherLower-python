import art, random, os
from game_data import data

def format_data(account):
    """Format the data into printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

# Printin game logo
print(art.logo)

# os.system('cls||clear')

# Selecting 2 random assets from 'game_data.data'
account_a = random.choice(data)
account_b = random.choice(data)
# Checking to make sure that both accounts are different from each other
if account_a == account_b:
    account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}")
print(art.vs)
print(f"Against B: {format_data(account_b)}")