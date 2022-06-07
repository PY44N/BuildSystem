#include <iostream>

#include "Board.h"
#include "Engine/Terminal.h"

Board::Board() {
	board = {
		{0, 0, 0},
		{0, 0, 0},
		{0, 0, 0},
	};
}

void Board::print()
{
	Terminal::clearScreen();

	for (int y = 0; y < board.size(); y++) {
		for (int x = 0; x < board[y].size(); x++) {
			int value = board[y][x];
			const char* display = (value == 1 ? "X" : value == 2 ? "O" : " ");
			std::cout << display << (x != 2 ? " | " : "");
		}
		std::cout << std::endl << (y != 2 ? "----------" : "") << std::endl;
	}
}

void Board::setValue(int x, int y, int value)
{
	board[y][x] = value;
}

void Board::setValue(Vector2 position, int value)
{
	setValue(position.x, position.y, value);
}

std::vector<int> Board::getX(int x)
{
	std::vector<int> xValues = {};

	for (int y = 0; y < board.size(); y++) {
		xValues.push_back(board[y][x]);
	}

	return xValues;
}

std::vector<int> Board::getY(int y)
{
	return board[y];
}

std::vector<int> Board::getDiag(int startY, int slope)
{
	std::vector<int> diag = {};

	int y = startY;
	for (int x = 0; x < 3; x++) {
		diag.push_back(board[y][x]);
		y += slope;
	}

	return diag;
}

bool Board::hasWinner(const std::vector<int>& list)
{
	int first = list[0];

	if (first == 0) {
		return false;
	}

	for (int i = 0; i < list.size(); i++) {
		if (list[i] != first) {
			return false;
		}
	}

	return true;
}

int Board::getWinner()
{
	for (int y = 0; y < board.size(); y++) {
		if (hasWinner(getY(y))) {
			return board[y][0];
		}
	}

	for (int x = 0; x < 3; x++) {
		if (hasWinner(getX(x))) {
			return board[0][x];
		}
	}

	if (hasWinner(getDiag(0, 1))) {
		return board[0][0];
	}

	if (hasWinner(getDiag(2, -1))) {
		return board[2][0];
	}

	return 0;
}

bool Board::isBoardFull()
{
	for (int y = 0; y < board.size(); y++) {
		for (int x = 0; x < board[y].size(); x++) {
			if (board[y][x] == 0) {
				return false;
			}
		}
	}

	return true;
}

bool Board::isValidPosition(const Vector2& position)
{
	return (board[position.y][position.x] == 0);
}
