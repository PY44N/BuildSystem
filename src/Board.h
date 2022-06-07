#pragma once

#include <vector>

#include "Engine/Util/Vector2.h"

class Board
{
private:
	std::vector<int> getX(int x);
	std::vector<int> getY(int y);
	std::vector<int> getDiag(int startY, int slope);
	bool hasWinner(const std::vector<int>& list);
public:
	Board();
	std::vector<std::vector<int>> board;
	void print();
	void setValue(int x, int y, int value);
	void setValue(Vector2 position, int value);
	int getWinner();
	bool isBoardFull();
	bool isValidPosition(const Vector2& position);
};
