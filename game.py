from game_data import TITLE, display_line, Hangman
print(TITLE)
display_line()
player = input("Please Enter your name:")
display_line()
hangman = Hangman(player)
hangman.play()


