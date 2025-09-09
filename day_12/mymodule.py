import random

def random_user_id():
    # 6 digits with numbers or letters
    characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.choice(characters) for _ in range(6))

def user_id_gen_by_user():
    num_chars = int(input("Enter the number of characters for the user ID: "))
    num_ids = int(input("Enter the number of user IDs to generate: "))
    characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    user_ids = []
    for _ in range(num_ids):
        user_id = ''.join(random.choice(characters) for _ in range(num_chars))
        user_ids.append(user_id)

    return user_ids

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"


def shuffle_list(lst):
    random.shuffle(lst)
    return lst

def seven_numbers():
    return random.sample(range(10), 7)