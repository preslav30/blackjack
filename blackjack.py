# BLACKJACK
# The game does not include splitting cards.
# I made the game to practice using dictionaries and functions.

import random

deck_of_cards = {'Ace of Spades': 11, '2 of Spades': 2, '3 of Spades': 3, '4 of Spades': 4, '5 of Spades': 5,
                         '6 of Spades': 6, '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9, '10 of Spades': 10,
                         'Jack of Spades': 10, 'Queen of Spades': 10, 'King of Spades': 10, 'Ace of Diamonds': 11,
                         '2 of Diamonds': 2, '3 of Diamonds': 3, '4 of Diamonds': 4, '5 of Diamonds': 5, '6 of Diamonds': 6,
                         '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9, '10 of Diamonds': 10,
                         'Jack of Diamonds': 10, 'Queen of Diamonds': 10, 'King of Diamonds': 10, 'Ace of Hearts': 11,
                         '2 of Hearts': 2, '3 of Hearts': 3, '4 of Hearts': 4, '5 of Hearts': 5, '6 of Hearts': 6,
                         '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9, '10 of Hearts': 10, 'Jack of Hearts': 10,
                         'Queen of Hearts': 10, 'King of Hearts': 10, 'Ace of Clubs': 11, '2 of Clubs': 2, '3 of Clubs': 3,
                         '4 of Clubs': 4, '5 of Clubs': 5, '6 of Clubs': 6, '7 of Clubs': 7, '8 of Clubs': 8,
                         '9 of Clubs': 9, '10 of Clubs': 10, 'Jack of Clubs': 10, 'Queen of Clubs': 10, 'King of Clubs': 10}


def clear_screen(lines=100):
    print("\n" * lines)


def random_deal():
    random_card_key = random.choice(list(deck_of_cards.keys()))
    random_card_value = deck_of_cards[random_card_key]
    deck_of_cards.pop(random_card_key)
    return random_card_key, random_card_value


def blackjack_game():
    game_over = False
    while not game_over:

        player_total_hand_value = 0
        dealer_total_hand_value = 0
        dealer_hand_list = []
        player_hand_list = []

        player_first_random_card, player_first_random_card_value = random_deal()
        player_second_random_card, player_second_random_card_value = random_deal()
        if player_first_random_card_value == 11 and player_second_random_card_value == 11:
            player_second_random_card_value = 1
        player_hand_list.extend((player_first_random_card, player_second_random_card))
        player_total_hand_value = player_total_hand_value + player_first_random_card_value + player_second_random_card_value

        dealer_first_random_card, dealer_first_random_card_value = random_deal()
        dealer_hand_list.append(dealer_first_random_card)
        dealer_total_hand_value += dealer_first_random_card_value

        print("\nWelcome to Blackjack!")
        print(f"Your cards are {', '.join(player_hand_list)}. They add up to {player_total_hand_value}")
        print(f"Dealer's first card is: {dealer_first_random_card}. Dealer's score is currently {dealer_total_hand_value}")

        draw_another_card = True
        draw_choice = input("\nType 'y' to get another card, 'n' to pass and finish current game: ")
        while draw_another_card:
            if draw_choice != "y":
                draw_another_card = False
                clear_screen()
                break
            player_next_random_card, player_next_random_card_value = random_deal()
            if player_next_random_card_value == 11 and player_total_hand_value >= 11:
                player_next_random_card_value = 1
            player_hand_list.append(player_next_random_card)
            player_total_hand_value += player_next_random_card_value
            clear_screen()
            print(f"\nYour cards are {', '.join(player_hand_list)}. Total is {player_total_hand_value}")
            print(f"Dealer's score: {dealer_total_hand_value}")
            if player_total_hand_value > 21:
                print(f"You exceeded 21. You lose!")
                quit()
            draw_choice = input("\nType 'y' to get another card, 'n' to pass and finish current game: ")

        if not draw_another_card:
            dealer_limit_reached = False
            while not dealer_limit_reached:
                dealer_next_card, dealer_next_card_value = random_deal()
                dealer_hand_list.append(dealer_next_card)
                dealer_total_hand_value += dealer_next_card_value
                if dealer_total_hand_value > 17:
                    dealer_limit_reached = True
                    break

        if not draw_another_card and dealer_limit_reached:
            print(f"Your final hand is: {', '.join(player_hand_list)}. Final score is {player_total_hand_value}")
            print(f"Dealer's final hand is: {', '.join(dealer_hand_list)}. Dealer's final score is: {dealer_total_hand_value}")
            if dealer_total_hand_value > 21 and player_total_hand_value <= 21:
                print("\nYOU WIN!")
            elif dealer_total_hand_value <= 21 and dealer_total_hand_value > player_total_hand_value:
                print("\nDealer wins!")
            elif dealer_total_hand_value == player_total_hand_value:
                print("It's a draw! No one wins.")
            if input("\nDo you want to play another game? 'y' or 'n': ") == "y":
                clear_screen()
                blackjack_game()
            else:
                game_over = True
                quit()


blackjack_game()


