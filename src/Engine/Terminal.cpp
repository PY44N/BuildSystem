#include <iostream>

#include "Terminal.h"

void Terminal::clearScreen()
{
	for (int i = 0; i < 100; i++) {
		std::cout << std::endl;
	}
}
