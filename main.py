import random

# Sample dataset of influencers
influencers = [
    {"name": "Emma Chamberlain", "handle": "@emmachamberlain", "brief_bio": "Lifestyle and fashion influencer known for her YouTube vlogs.", "followers": 12000000},
    {"name": "Charli D'Amelio", "handle": "@charlidamelio", "brief_bio": "TikTok star who gained fame through her dance videos.", "followers": 150000000},
    {"name": "Zach King", "handle": "@zachking", "brief_bio": "Filmmaker known for his ‘magic vines’ that appear as real-life illusions.", "followers": 66000000},
    {"name": "Addison Rae", "handle": "@addisonraee", "brief_bio": "TikTok personality and dancer, also featured in various films.", "followers": 88000000},
    {"name": "MrBeast", "handle": "@mrbeast", "brief_bio": "YouTuber known for viral stunts and charitable acts.", "followers": 120000000},
    {"name": "Liza Koshy", "handle": "@lizakoshy", "brief_bio": "Comedian and actress with a huge following on YouTube and Instagram.", "followers": 17000000},
    {"name": "James Charles", "handle": "@jamescharles", "brief_bio": "Beauty guru and makeup artist.", "followers": 23000000},
    {"name": "Bella Poarch", "handle": "@bellapoarch", "brief_bio": "TikTok sensation known for her lip-syncing videos and debut music career.", "followers": 92000000},
    {"name": "David Dobrik", "handle": "@daviddobrik", "brief_bio": "YouTube vlogger known for comedy skits and pranks.", "followers": 20000000},
    {"name": "Huda Kattan", "handle": "@hudabeauty", "brief_bio": "Founder of Huda Beauty and one of the top beauty influencers.", "followers": 51000000},
    {"name": "PewDiePie", "handle": "@pewdiepie", "brief_bio": "Swedish YouTuber and gamer, widely known for his comedic content.", "followers": 110000000},
    {"name": "Dixie D'Amelio", "handle": "@dixiedamelio", "brief_bio": "Singer and TikTok personality, also Charli’s sister.", "followers": 57000000},
    {"name": "Nikkie de Jager", "handle": "@nikkietutorials", "brief_bio": "Makeup artist and beauty vlogger known for her tutorials.", "followers": 16000000},
    {"name": "Kim Kardashian", "handle": "@kimkardashian", "brief_bio": "Reality TV star, business mogul, and beauty influencer.", "followers": 340000000},
    {"name": "Lele Pons", "handle": "@lelepons", "brief_bio": "Comedian, actress, and singer with a massive following on Instagram.", "followers": 47000000},
    {"name": "Logan Paul", "handle": "@loganpaul", "brief_bio": "YouTuber, boxer, and podcaster.", "followers": 23000000},
    {"name": "Kylie Jenner", "handle": "@kyliejenner", "brief_bio": "Beauty mogul and reality TV star, founder of Kylie Cosmetics.", "followers": 400000000},
    {"name": "Khaby Lame", "handle": "@khaby.lame", "brief_bio": "TikTok star known for his humorous videos debunking over-complicated life hacks.", "followers": 160000000},
    {"name": "Loren Gray", "handle": "@lorengray", "brief_bio": "Singer and TikTok influencer with millions of followers.", "followers": 54000000},
    {"name": "Markiplier", "handle": "@markiplier", "brief_bio": "YouTuber and gamer known for his Let's Play videos.", "followers": 31000000},
    {"name": "Sommer Ray", "handle": "@sommerray", "brief_bio": "Fitness influencer and model with a large following on Instagram.", "followers": 27000000},
    {"name": "Amanda Cerny", "handle": "@amandacerny", "brief_bio": "Actress and social media star known for her comedy skits.", "followers": 25000000},
    {"name": "Shane Dawson", "handle": "@shanedawson", "brief_bio": "YouTuber known for documentaries and conspiracy videos.", "followers": 23000000},
    {"name": "Jay Shetty", "handle": "@jayshetty", "brief_bio": "Motivational speaker, author, and former monk.", "followers": 13000000},
    {"name": "JoJo Siwa", "handle": "@itsjojosiwa", "brief_bio": "Singer, dancer, and actress popular with young audiences.", "followers": 12000000},
    {"name": "Rhett & Link", "handle": "@rhettandlink", "brief_bio": "YouTubers known for their comedic talk show Good Mythical Morning.", "followers": 17000000},
    {"name": "Emma Watson", "handle": "@emmawatson", "brief_bio": "Actress and activist, best known for her role in the Harry Potter series.", "followers": 68000000},
    {"name": "Naomi Campbell", "handle": "@naomi", "brief_bio": "Supermodel and philanthropist with a strong influence in fashion.", "followers": 15000000},
    {"name": "Chiara Ferragni", "handle": "@chiaraferragni", "brief_bio": "Fashion blogger and entrepreneur.", "followers": 29000000},
    {"name": "Tana Mongeau", "handle": "@tanamongeau", "brief_bio": "YouTuber and social media personality known for her storytime videos.", "followers": 5700000},
    {"name": "Patrick Starrr", "handle": "@patrickstarrr", "brief_bio": "Makeup artist and beauty guru with his own cosmetic line.", "followers": 4300000},
    {"name": "Ariana Grande", "handle": "@arianagrande", "brief_bio": "Singer and actress with one of the largest Instagram followings.", "followers": 380000000},
    {"name": "Selena Gomez", "handle": "@selenagomez", "brief_bio": "Singer, actress, and producer.", "followers": 430000000},
    {"name": "Virat Kohli", "handle": "@virat.kohli", "brief_bio": "Indian cricketer and one of the top athletes on social media.", "followers": 250000000},
    {"name": "Gigi Hadid", "handle": "@gigihadid", "brief_bio": "Supermodel and fashion icon.", "followers": 78000000},
    {"name": "Kendall Jenner", "handle": "@kendalljenner", "brief_bio": "Supermodel and reality TV star.", "followers": 310000000},
    {"name": "Will Smith", "handle": "@willsmith", "brief_bio": "Actor and rapper known for his humorous Instagram and TikTok posts.", "followers": 64000000},
    {"name": "Dwayne Johnson", "handle": "@therock", "brief_bio": "Actor, producer, and former wrestler known for motivational and fitness content.", "followers": 400000000},
    {"name": "Billie Eilish", "handle": "@billieeilish", "brief_bio": "Singer and songwriter, popular among Gen Z.", "followers": 110000000},
    {"name": "Camila Cabello", "handle": "@camila_cabello", "brief_bio": "Singer-songwriter and former member of Fifth Harmony.", "followers": 67000000},
    {"name": "Jackie Aina", "handle": "@jackieaina", "brief_bio": "Beauty influencer and advocate for diversity in the beauty industry.", "followers": 3700000},
    {"name": "Lilly Singh", "handle": "@lilly", "brief_bio": "Comedian and talk show host, known for her YouTube channel Superwoman.", "followers": 9600000},
    {"name": "Nash Grier", "handle": "@nashgrier", "brief_bio": "Social media personality and actor, gained fame on Vine.", "followers": 11000000},
    {"name": "Ellen DeGeneres", "handle": "@theellenshow", "brief_bio": "Comedian and former talk show host.", "followers": 100000000},
]

# Game state variables
incorrect_guesses = 0
max_incorrect_guesses = 5
used_influencers = set()  # Keeps track of influencers who have lost


def pick_random_influencers():
    """Pick two random influencers who have not been used (lost) yet."""
    #If Any influencer who is not used then a list is created of influencers who were not used
    remaining_influencers = [inf for inf in influencers if inf["name"] not in used_influencers]
    return random.sample(remaining_influencers, 2)


def display_influencer_info(inf1, inf2):
    """Display the information of two influencers."""
    print(f"\nInfluencer 1: {inf1['name']} ({inf1['handle']} ({inf1['brief_bio']} )")
    print(f"Influencer 2: {inf2['name']} ({inf2['handle']} ({inf2['brief_bio']})")


def get_user_guess():
    """Prompt the user to guess which influencer has more followers."""
    try:
        guess = input("\nWho has more followers? Type 1 for Influencer 1 or 2 for Influencer 2: ")
        while guess not in ['1', '2']:
            guess = input("Invalid input. Type 1 for Influencer 1 or 2 for Influencer 2: ")
        return int(guess)
    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting.")
        exit(0)  # Gracefully exit the game


def check_guess(inf1, inf2, guess):
    """Check if the guess is correct."""
    if (guess == 1 and inf1['followers'] > inf2['followers']) or (guess == 2 and inf2['followers'] > inf1['followers']):
        return True
    return False


def reset_game():
    """Reset game variables to their initial state."""
    global incorrect_guesses, used_influencers
    incorrect_guesses = 0
    used_influencers = set()

def play_again():
    """Ask the user if they want to play again."""
    while True:
        play_again_choice = input("\nDo you want to play again? (yes/no): ")
        if play_again_choice in ['yes', 'no']:
            return play_again_choice == 'yes'
        else:
            print("Please answer with 'yes' or 'no'.")

def game_loop():
    global incorrect_guesses
    correct_guesses = 0

    try:
        # Initial random influencers
        inf1, inf2 = pick_random_influencers()

        while incorrect_guesses < max_incorrect_guesses:
            lives_left = max_incorrect_guesses - incorrect_guesses
            print(f"\nYou have {lives_left} lives remaining.")
            # Display the current round's influencers
            display_influencer_info(inf1, inf2)

            # Get the user's guess
            guess = get_user_guess()

            # Check if the guess is correct
            if check_guess(inf1, inf2, guess):
                print("Correct!")
                correct_guesses += 1

                # The winner stays, pick a new influencer to compare against the winner
                winner = inf1 if guess == 1 else inf2
                used_influencers.add(inf2['name'] if guess == 1 else inf1['name'])  # Mark the loser as used

                remaining_influencers = [inf for inf in influencers if
                                         inf["name"] not in used_influencers and inf != winner]

                if remaining_influencers:
                    inf2 = random.choice(remaining_influencers)
                    inf1 = winner
                else:
                    print("No more influencers to choose from.")
                    break
            else:
                print("Incorrect!")
                incorrect_guesses += 1

                winner = inf1 if inf1['followers'] > inf2['followers'] else inf2
                used_influencers.add(inf1['name'] if inf1 != winner else inf2['name'])  # Mark the loser as used

                remaining_influencers = [inf for inf in influencers if
                                         inf["name"] not in used_influencers and inf != winner]

                if remaining_influencers:
                    inf2 = random.choice(remaining_influencers)
                    inf1 = winner
                else:
                    print("No more influencers to choose from.")
                    break

        # End of game message
        print(f"\nGame over! You made {correct_guesses} correct guesses and {incorrect_guesses} incorrect guesses.")

        # Ask if the user wants to play again
        if play_again():
            reset_game()  # Reset the game state
            game_loop()  # Start a new game
        else:
            print("Thanks for playing!")

    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting.")
        exit(0)

# Start the game
if __name__ == "__main__":
        reset_game()  # Initialize game state
        game_loop()  # Start the game loop



