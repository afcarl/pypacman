Board Class
This class takes care of printing the board on stdout, generating walls, coins, pacman.
It also keeps track of present level's score

Person Class
Base class for Packman class and Ghost class, implements methods like getpos, setpos, checkwall,etc.

Packman Class
Packman class takes care of position of packman and moving itself. It also keeps score (total coins collected till now)

    Ghost Class
    Keeps track of path of a particular ghost and sending it to random positions after every key down.
    Also it checks the position of the pacman with this instance of Ghost and exits the game if they collide.

    _Getch,_GetchUnix Class
    Since python does not a getchar function, these classes implement this so that at every key down pacman moves in respective positions

    Game:
    1.Number of ghosts is user input and these are placed at random positions and moved at random positions
    2.Coins are placed at random and also number of coins is not fixed
    3.Walls are fixed
    4.After coins are picked by packman next level is started with newly generated coins
    5.Game continues until ghost catches packman or input is 'q'

    Inheritance:
    Person inherits from board uses isWall method
    Packman and Ghost inherits from Person properties like position, checkWall etc

    Polymorphism:
    We have __init__ method in each class but the respective constructor is called

    Modularity:
    Game is divided into classes which are present in different files

    Encapsulation:
    Classes are instanciated with objects and these objects made encapsulate different properties of the class methods
