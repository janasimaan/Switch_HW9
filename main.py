from board import Board
from Game import game

if __name__ == "__main__":
    board_size = 4
    board = Board(board_size)
    gaming = game(board)
    gaming.play()