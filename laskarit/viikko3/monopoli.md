```mermaid
classDiagram
	Token "*"  --> "1"  Player
	Square "*" --> "1" Board
	Token "*" --> "1" Square
	Prison "*" --> "1" Board
	Prison "*" --> "1" Square
	StartSquare "*" --> "1" Board
	StartSquare "*" --> "1" Square
	NamedStreet "*" --> "1" Square
	ChanceCard "*" --> "1" Card
	CommunityChest "*" --> "1" Card
	class ChanceCard{
		Card card
	}
	class CommunityChest{
		Card card
	}
	class Player{
		int id
		int money
	}
	class Board{
		int prison
		int start
	}
	class Square{
		int id
		nextSquare
	}
	class StartSquare{
		Square
	}
	class Prison{
		Square
	}
	class NamedStreet{
		Square id
		int houses
		int hotels
		Player owner
	}
	class Token{
		Player owner
	}
	class Dice{
	}
	class Card{
		action
	}
