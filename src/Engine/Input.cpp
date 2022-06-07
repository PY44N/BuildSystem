#include <iostream>

#include "Input.h"
#include "../Game.h"

Vector2 Input::getPosition(const int player)
{
    int x, y;
    
    std::cout << "Player " << (player == 0 ? "X" : player == 1 ? "O" : " ") << " is up next" << std::endl;

    std::cout << "What x position would you like?" << std::endl;
    std::cin >> x;

    std::cout << "What y position would you like?" << std::endl;
    std::cin >> y;

    return Vector2(x, y);
}
