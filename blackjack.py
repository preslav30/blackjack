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


def random_deal(card_deck, hand_list, hand_value):
    random_card_key = random.choice(list(card_deck.keys()))
    random_card_value = card_deck[random_card_key]
    hand_list.append(random_card_key)
    hand_value += random_card_value
    del card_deck[random_card_key]
    return random_card_key, random_card_value, hand_list, hand_value


def game_result(hand_list1, hand_list2, hand_value1, hand_value2):
    print(f"Your final hand is: {', '.join(hand_list1)}. Final score is {hand_value1}")
    print(f"Dealer's final hand is: {', '.join(hand_list2)}. Dealer's final score is: {hand_value2}")
    if hand_value2 > 21 and hand_value1 <= 21:
        print("\nYOU WIN!")
    elif 21 >= hand_value2 > hand_value1:
        print("\nDealer wins!")
    elif hand_value2 == hand_value1:
        print("It's a draw! No one wins.")


def blackjack_game():
    game_over = False
    while not game_over:
        card_deck_copy = deck_of_cards.copy()  # make a copy of the card deck so we can remove items from it
        player_total_hand_value = 0
        dealer_total_hand_value = 0
        dealer_hand_list = []
        player_hand_list = []

        player_first_random_card, player_first_random_card_value, player_hand_list, player_total_hand_value = random_deal(card_deck_copy, player_hand_list, player_total_hand_value)
        player_second_random_card, player_second_random_card_value, player_hand_list, player_total_hand_value = random_deal(card_deck_copy, player_hand_list, player_total_hand_value)
        if player_total_hand_value == 22:
            player_total_hand_value = 12

        dealer_first_random_card, dealer_first_random_card_value, dealer_hand_list, dealer_total_hand_value = random_deal(card_deck_copy, dealer_hand_list, dealer_total_hand_value)

        print("\nWelcome to Blackjack!")
        print(f"Your initial cards are {', '.join(player_hand_list)}. They add up to {player_total_hand_value}")
        print(f"Dealer's first card is: {dealer_first_random_card}. Dealer's score is currently {dealer_total_hand_value}")

        draw_another_card = True
        draw_choice = input("\nType 'y' to get another card, 'n' to pass and finish current game: ")
        while draw_another_card:
            if draw_choice != "y":
                draw_another_card = False
                clear_screen()
                break
            player_next_random_card, player_next_random_card_value, player_hand_list, player_total_hand_value = random_deal(card_deck_copy, player_hand_list, player_total_hand_value)
            if player_next_random_card_value == 11 and player_total_hand_value >= 11:
                player_total_hand_value -= 10

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
                dealer_next_card, dealer_next_card_value, dealer_hand_list, dealer_total_hand_value = random_deal(card_deck_copy, dealer_hand_list, dealer_total_hand_value)
                if dealer_total_hand_value > 17:
                    dealer_limit_reached = True
                    break

        if not draw_another_card and dealer_limit_reached:
            game_result(player_hand_list, dealer_hand_list, player_total_hand_value, dealer_total_hand_value)

            if input("\nDo you want to play another game? 'y' or 'n': ") == "y":
                clear_screen()
                blackjack_game()
            else:
                game_over = True
                print("\nThank you for playing!")
                quit()


blackjack_game()


