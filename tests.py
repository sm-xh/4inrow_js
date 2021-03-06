from gameLogic import *
from gameExceptions import ColumnFullException

def test_init_move():
    test_game = Game()

    test_game.player_move((100, 0))
    test_game.changeTurn()
    test_game.player_move((200, 0))
    test_game.changeTurn()
    test_game.player_move((300, 0))
    test_game.changeTurn()
    test_game.player_move((400, 0))

    assert list(test_game._board[-1]).count(0) == 3


def test_winning_horizontally():
    test_game = Game()
    column = (200, 0)
    test_game.player_move(column)
    column = (300, 0)
    test_game.player_move(column)
    column = (400, 0)
    test_game.player_move(column)
    column = (500, 0)
    test_game.player_move(column)
    test_game.isGameOver()
    assert test_game._winner == "CZERWONY"


def test_winning_vertically():
    test_game = Game()
    test_game.changeTurn()
    column = (200, 0)
    test_game.player_move(column)
    test_game.player_move(column)
    test_game.player_move(column)
    test_game.player_move(column)
    test_game.isGameOver()
    assert test_game._winner == "ŻÓŁTY"


def test_winning_plus4_in_row():
    test_game = Game()

    # ustawianie kolejnych zetonow na sobie
    test_game.player_move((100, 0))
    test_game.changeTurn()
    test_game.player_move((100, 0))

    test_game.changeTurn()
    test_game.player_move((200, 0))
    test_game.changeTurn()
    test_game.player_move((200, 0))

    test_game.changeTurn()
    test_game.player_move((300, 0))
    test_game.changeTurn()
    test_game.player_move((300, 0))

    test_game.changeTurn()
    test_game.player_move((500, 0))
    test_game.changeTurn()
    test_game.player_move((500, 0))

    test_game.changeTurn()
    test_game.player_move((600, 0))
    test_game.changeTurn()
    test_game.player_move((600, 0))

    test_game.changeTurn()
    test_game.player_move((700, 0))
    test_game.changeTurn()
    test_game.player_move((700, 0))

    test_game.changeTurn()
    test_game.player_move((400, 0))
    test_game.isGameOver()
    assert test_game._winner == "CZERWONY"


def test_winning_cross():
    test_game = Game()
    # 1sza kolumna
    test_game.player_move((100, 0))
    test_game.changeTurn()
    test_game.player_move((100, 0))
    test_game.changeTurn()
    test_game.player_move((100, 0))
    test_game.changeTurn()
    test_game.player_move((100, 0))

    # 2ga kolumna
    test_game.player_move((200, 0))
    test_game.changeTurn()
    test_game.player_move((200, 0))
    test_game.changeTurn()
    test_game.player_move((200, 0))

    test_game.changeTurn()
    test_game.player_move((300, 0))
    test_game.changeTurn()
    test_game.player_move((300, 0))

    test_game.player_move((400, 0))
    test_game.isGameOver()
    assert test_game._winner == "ŻÓŁTY"


def test_draw():
    test_game = Game()

    #1szy rzad
    test_game.changeTurn()
    test_game.player_move((100, 0))
    test_game.player_move((200, 0))
    test_game.changeTurn()
    test_game.player_move((300, 0))
    test_game.player_move((400, 0))
    test_game.changeTurn()
    test_game.player_move((500, 0))
    test_game.player_move((700, 0))
    test_game.changeTurn()
    test_game.player_move((600, 0))

    # 2gi rzad
    test_game.changeTurn()
    test_game.player_move((100, 0))
    test_game.player_move((200, 0))
    test_game.player_move((500, 0))
    test_game.player_move((600, 0))
    test_game.changeTurn()
    test_game.player_move((300, 0))
    test_game.player_move((400, 0))
    test_game.player_move((700, 0))

    # 3ci rzad
    test_game.player_move((100, 0))
    test_game.player_move((200, 0))
    test_game.player_move((500, 0))
    test_game.player_move((600, 0))
    test_game.changeTurn()
    test_game.player_move((300, 0))
    test_game.player_move((400, 0))
    test_game.player_move((700, 0))

    # 4ty rzad
    test_game.player_move((100, 0))
    test_game.player_move((200, 0))
    test_game.player_move((600, 0))
    test_game.changeTurn()
    test_game.player_move((300, 0))
    test_game.player_move((400, 0))
    test_game.player_move((500, 0))
    test_game.player_move((700, 0))

    # 5ty rzad
    test_game.player_move((100, 0))
    test_game.player_move((200, 0))
    test_game.player_move((300, 0))
    test_game.player_move((500, 0))
    test_game.player_move((600, 0))
    test_game.player_move((700, 0))
    test_game.changeTurn()
    test_game.player_move((400, 0))

    # 6ty rzad
    test_game.player_move((100, 0))
    test_game.player_move((200, 0))
    test_game.player_move((300, 0))
    test_game.player_move((500, 0))
    test_game.player_move((600, 0))
    test_game.player_move((700, 0))
    test_game.changeTurn()
    test_game.player_move((400, 0))

    test_game.isGameOver()
    assert test_game._winner == "REMIS"


def test_full_column():
    test_game = Game()

    #zapelnieie kolumny
    test_game.changeTurn()
    test_game.player_move((100, 0))
    test_game.changeTurn()
    test_game.player_move((100, 0))
    test_game.changeTurn()
    test_game.player_move((100, 0))
    test_game.changeTurn()
    test_game.player_move((100, 0))
    test_game.changeTurn()
    test_game.player_move((100, 0))
    test_game.changeTurn()
    test_game.player_move((100, 0))
    test_game.changeTurn()
    assert test_game.player_move((100,0)) == (-1, -1)  #funkcja zwraca (-1,-1) jako obsługę wyjątku