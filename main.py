from game import start_game

if __name__ == "__main__":
    from menu import main_menu
    player1, player2 = main_menu()  # Get player names from menu
    start_game(player1, player2)    # Start the actual game
