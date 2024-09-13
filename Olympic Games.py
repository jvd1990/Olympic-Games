# Olympic Games
import random
# Names
player1 = input("What is your name player 1: ")
player2 = input("What is your name player 2: ")
player3 = input("What is your name player 3: ")
player4 = input("What is your name player 4: ")
# Nationality
country1 = input(f"Where are you from {player1}: ")
country2 = input(f"Where are you from {player2}: ")
country3 = input(f"Where are you from {player3}: ")
country4 = input(f"Where are you from {player4}: ")
# Rank
rank = random.randint(1,10)
if rank == 1:
    print(f"{player1} from {country1}, you are the first and you will recive a gold medal.")
    print(f"{player2} from {country2}, you are the second and you will recive a silver medal.")
    print(f"{player3} from {country3}, you are the third and you will recive a bronze medal.")
    print(f"{player4} from {country4}, you are the forth and you won't recive any medal.")
elif rank == 2:
    print(f"{player2} from {country2}, you are the first and you will recive a gold medal.")
    print(f"{player1} from {country1}, you are the second and you will recive a silver medal.")
    print(f"{player3} from {country3}, you are the third and you will recive a bronze medal.")
    print(f"{player4} from {country4}, you are the forth and you won't recive any medal.")
elif rank == 3:
    print(f"{player2} from {country2}, you are the first and you will recive a gold medal.")
    print(f"{player1} from {country1}, you are the second and you will recive a silver medal.")
    print(f"{player4} from {country4}, you are the third and you will recive a bronze medal.")
    print(f"{player3} from {country3}, you are the forth and you won't recive any medal.")
elif rank == 4:
    print(f"{player2} from {country2}, you are the first and you will recive a gold medal.")
    print(f"{player3} from {country3}, you are the second and you will recive a silver medal.")
    print(f"{player4} from {country4}, you are the third and you will recive a bronze medal.")
    print(f"{player1} from {country1}, you are the forth and you won't recive any medal.")
elif rank == 5:
    print(f"{player3} from {country3}, you are the first and you will recive a gold medal.")
    print(f"{player4} from {country4}, you are the second and you will recive a silver medal.")
    print(f"{player2} from {country2}, you are the third and you will recive a bronze medal.")
    print(f"{player1} from {country1}, you are the forth and you won't recive any medal.")
elif rank == 6:
    print(f"{player3} from {country3}, you are the first and you will recive a gold medal.")
    print(f"{player2} from {country2}, you are the second and you will recive a silver medal.")
    print(f"{player1} from {country1}, you are the third and you will recive a bronze medal.")
    print(f"{player4} from {country4}, you are the forth and you won't recive any medal.")
elif rank == 7:
    print(f"{player1} from {country1}, you are the first and you will recive a gold medal.")
    print(f"{player4} from {country4}, you are the second and you will recive a silver medal.")
    print(f"{player3} from {country3}, you are the third and you will recive a bronze medal.")
    print(f"{player2} from {country2}, you are the forth and you won't recive any medal.")
elif rank == 8:
    print(f"{player1} from {country1}, you are the first and you will recive a gold medal.")
    print(f"{player3} from {country3}, you are the second and you will recive a silver medal.")
    print(f"{player2} from {country2}, you are the third and you will recive a bronze medal.")
    print(f"{player4} from {country4}, you are the forth and you won't recive any medal.")
elif rank == 9:
    print(f"{player2} from {country2}, you are the first and you will recive a gold medal.")
    print(f"{player4} from {country4}, you are the second and you will recive a silver medal.")
    print(f"{player3} from {country3}, you are the third and you will recive a bronze medal.")
    print(f"{player1} from {country1}, you are the forth and you won't recive any medal.")
elif rank == 10:
    print(f"{player4} from {country4}, you are the first and you will recive a gold medal.")
    print(f"{player3} from {country3}, you are the second and you will recive a silver medal.")
    print(f"{player1} from {country1}, you are the third and you will recive a bronze medal.")
    print(f"{player2} from {country2}, you are the forth and you won't recive any medal.")