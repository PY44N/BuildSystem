#include <iostream>

#include "Game.h"

int main() {
	Game game;

	char playAgain;
	std::cout << "Would you like to play again? [y/n]" << std::endl;
	std::cin >> playAgain;

	if (playAgain == 'y') {
		main();
	}

	return 0;
}