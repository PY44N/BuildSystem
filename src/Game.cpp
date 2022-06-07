#include <iostream>

#include "Game.h"
#include "Board.h"
#include "Engine/Util/Vector2.h"
#include "Engine/Input.h"

Game::Game() {
	moveCount = 0;
	loop();
}

void Game::loop() {
	board.print();

	Vector2 input = Input::getPosition(moveCount % 2);

	while (!board.isValidPosition(input)) {
		std::cout << "Invalid position, try again" << std::endl;
		input = Input::getPosition(moveCount % 2);
	}

	board.setValue(input, (moveCount % 2) + 1);

	int winner = board.getWinner();
	if (winner != 0) {
		board.print();
		std::cout << "Congratulations " << (winner == 1 ? "X" : winner == 2 ? "O" : " ") << " you won!" << std::endl;
		return;
	}

	if (board.isBoardFull()) {
		board.print();
		std::cout << "It is a tie!" << std::endl;
		return;
	}

	moveCount++;
	loop();
}