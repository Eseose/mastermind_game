from src.controller import GameControl
from src.view import Display


# displays a view and gets player input based on current game state
def get_user_input(game_obj: GameControl, view_obj: Display):
    if game_obj.current_state == game_obj.on:
        return view_obj.display_main_menu()
    elif game_obj.current_state == game_obj.in_progress:
        return view_obj.get_user_guess(attempt=game_obj.game_model.attempt)
    elif game_obj.current_state == game_obj.finished:
        return view_obj.display_end_menu()


game = GameControl()
view = Display()

# while loop runs until game is turned off (state = game.off)
while game.current_state != game.off:
    user_choice = get_user_input(game, view)
    if user_choice == "Q":
        # quits from game sets game state to game.off
        if game.current_state == game.on:
            quit_choice = view.display_confirm_quit()
            game.quit_game(quit_choice)
        else:
            # exits to main menu
            game.exit_to_main_menu(user_choice)

    # main menu view
    if game.current_state == game.on:
        if user_choice == "S":
            view.get_user_name()
            game.initialize_game()
        elif user_choice == "A":
            user_choice = view.display_about()
        elif user_choice == "D":
            user_choice = view.display_choose_difficulty()
            if user_choice == "Q":
                quit_choice = view.display_confirm_exit_to_main_menu()
                game.exit_to_main_menu(quit_choice)
            else:
                game.choose_difficulty(user_choice)
        elif user_choice == "L":
            view.display_leader_board()
    # player is currently playing a game
    elif game.current_state == game.in_progress:
        game.make_attempt(user_choice)
    # player has completed the game
    elif game.current_state == game.finished:
        game.restart_game()
