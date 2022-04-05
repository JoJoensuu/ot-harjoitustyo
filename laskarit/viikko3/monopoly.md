```mermaid
classDiagram
	Dice "*" --> "1" Game
	Board "*" --> "1" Game
	Player "*" --> "1" Game
	Square "*" --> "1" Board
	Token "*" --> "1" Player
	Token "*" --> "1" Square
	class Game{
		player Player
		board Board
		numberOfPlayers integer
		numberOfDice integer	
	class Dice{
		rolldice()
	}
	class Player{
		integer id
	}
		class Board{
	}
	class Square{
		integer id
		nextSquare Square
	}
	class Token{
		owner Player
		location Square
	}

	
