from controller import GameControl
from view import Display

game = GameControl()
view = Display()

while game.current_state != game.off:
    # can input and quit be here???

    if game.current_state == game.on:
        user_choice = view.display_main_menu()
        if user_choice == "Q":
            quit_choice = view.display_confirm_quit()
            # game.quit_game_menu(quit_choice)
            game.quit_game(quit_choice)
        elif user_choice == "S":
            game.initialize_game()
        elif user_choice == "A":
            # print about and and main menu
            user_choice = view.display_about()
            if user_choice == "Q":
                quit_choice = view.display_confirm_quit()
                # game.quit_game_menu(quit_choice)
                game.quit_game(quit_choice)
            else:
                game.about(user_choice)
        elif user_choice == "D":
            # difficulty transition function
            user_choice = view.display_choose_difficulty()
            if user_choice == "Q":
                quit_choice = view.display_confirm_quit()
                # game.quit_game_menu(quit_choice)
                game.quit_game(quit_choice)
            else:
                game.choose_difficulty(user_choice)
    elif game.current_state == game.in_progress:
        user_choice = view.get_user_guess(
            attempts=game.attempts, attempt=game.attempt)
        if user_choice == "Q":
            quit_choice = view.display_confirm_quit()
            # game.quit_game_playing(quit_choice)
            game.quit_game(quit_choice)
        else:
            game.make_attempt(user_choice)
    elif game.current_state == game.finished:
        user_choice = view.display_end_menu()
        if user_choice == "R":
            game.restart_game()
        elif user_choice == "Q":
            quit_choice = view.display_confirm_quit()
            # game.quit_game_finished(quit_choice)
            game.quit_game(quit_choice)
