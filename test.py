import pytest
from morra_cinese import isrock, ispaper, isscissor, end_game

def test_isrock():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    isrock()
    assert player_score in [0, 1]
    assert computer_score in [0, 1]
    
def test_ispaper():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    ispaper()
    assert player_score in [0, 1]
    assert computer_score in [0, 1]

def test_isscissor():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    isscissor()
    assert player_score in [0, 1]
    assert computer_score in [0, 1]
    
def test_end_game_player_wins():
    global player_score, computer_score
    player_score = 3
    computer_score = 1
    result = end_game()
    assert result == "Player Wins"

def test_end_game_computer_wins():
    global player_score, computer_score
    player_score = 1
    computer_score = 3
    result = end_game()
    assert result == "Computer Wins"

def test_end_game_draw():
    global player_score, computer_score
    player_score = 2
    computer_score = 2
    result = end_game()
    assert result == "Match Draw"