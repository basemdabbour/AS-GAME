# Tic Tac Toe – Game Project 



# 1.	Introduction 



Tic Tac Toe is a game against a simple artificial intelligence. An artificial intelligence (or AI) is a computer program that can intelligently respond to the player’s moves. This game doesn’t introduce any complicated new concepts. The artificial intelligence that plays Tic Tac Toe is really just a few lines of code..
Back when we were a kids , two children’s used to play Tic Tac Toe with paper and pencil when one of them is “X“ and the other is “O“ and if one of the players get three of the their marks on the board in row or column or one of the two diagonals , they WIN 
And when the board fills up with neither player winning the game break even.








# 2.	Simple run for Tic Tac Toe Game 


 
![image](https://user-images.githubusercontent.com/32684082/35981692-31c510c8-0cee-11e8-91c0-ec9cf6b94e93.png)
 ![image](https://user-images.githubusercontent.com/32684082/35982079-29b32504-0cef-11e8-80b7-b3c02d82bbd2.png)








# 3.	The Tic Tac Toe source code



Please copy the below code to your shell and run it:


[source code]( https://github.com/basemdabbour/AS-GAME/blob/master/tictactoe-DS-AS-2018.py)







# 4.	Game design


The below figure shows how the Flowchart for this Tic Tac Toe looks like, in this game the player (you) will choose between "X" and "O" and who take the first turn will be randomly chosen by using random module in python “ import random ”


![image](https://user-images.githubusercontent.com/32684082/35982148-5a052e5a-0cef-11e8-891e-e793189dffb4.png)



>Note: the board is numbered as keyboard number pad as per the following sample:

 
 ![image](https://user-images.githubusercontent.com/32684082/35982237-94c08dc8-0cef-11e8-864a-6ec0f75482b2.png)




 
 
 

# 5.	Game in details with functions


In this program, the Tic Tac Toe board is simply represented as a list of strings. Each string will represent one of the nine spaces on the board (either be 'X' for the X player, 'O' for the O player, or a single space ' ' for a blank space.). To make it easier to remember which index in the list is for which space, same as the numbers on a keyboard’s number keypad, as per the Figure 4 we can also agree that list of 10 strings stored in variable board will make board [5] in center, board [1] in bottom left and board [6] in the right side and so on so forth 




**Functions:**


•	**GameBoard()** function to draw the board of strings (1 till 9).


•	**inputPlayerletter()** function so the player can choose which letter will start with “X” or “O” , and the computer will get the second letter.


•	**whoGoesFirst()** function to randomly choose the player who will go first in the game , in this case player or computer 


•	**playAgain()** function to repeat the game again by using “random.randint(0, 1) == 0” , if (0) the computer will have the first move , (1) the player will have the first move.


•	**MakeAMove():** function to pass the parameter for the borad[ ] with chosen letter by player or computer.


•	**isWinner()** function with long return line to check if there is three spaces in board filled with same letter horizontally , vertically or diagonally.


•	**getboardCopy()** function to make copy of the board of TTT in the game , making append to the board with new copy of it without changing the original board and moves has been played before.


•	**FreeSpace()** function to check if the entire board filled with sting or not , make sure to choose the right empty slot to make a move, otherwise a message will pop up to ask for available move.


•	**getPlayerMove()** function to ask the player to enter the number of the space that wants to move on , the (while) loop here makes sure that the player is choosing the empty space each move and check if the space is already taken before or not by calling FreeSpace() , and finally return the move as integer from string.


•	 **chooseRandomMoveFromList()** function will first check that the space is valid to make a move on , and returns a valid move from the passed list on the passed board and None in case of no valid/true move made.


•	**getComputerMove()** function, the algorithm which has been used in TTT game is simple algorithm to compute the results , this algorithm is implemented and used in the getComputerMove() function.


•	**isboardFull() ** Function that returns True in case all moves(10 strings 1-9, index 0 not used) has already passed through with “X” or “O” , and False in case of any spaces found not filled yet , in other words , isbordFull() invert function of FreeSpace().




# 6.	**UML Diagrams**


•	Class Diagram


  ![image](https://user-images.githubusercontent.com/32684082/35982366-ebdcec96-0cef-11e8-9f3b-fd4dcd2a09e6.png)
  
  
  
•	Use Case Diagram

 
![image](https://user-images.githubusercontent.com/32684082/35982396-fefbcbf8-0cef-11e8-9bc1-ff4015bc3325.png)







# 7.	SonarQube – Metrics


With SonarQube we can check how much the code is clean from bugs and vulnrability 
By creating new project with token name either existing one or generate new which is linked to new project for testing and analysing by applying one of the metrics (bugs test , line of cods ... e :



![image](https://user-images.githubusercontent.com/32684082/35982469-31cd12e4-0cf0-11e8-913e-22dd2df0283a.png)




The following command will scan the code and do the test


` sonar-scanner.bat -Dsonar.projectKey=AS-GAME -Dsonar.organization=basemdabbour-github -Dsonar.sources=. -Dsonar.host.url=https://sonarcloud.io -Dsonar.login=ca8628234e17b3cb7011afc999c047e0226ac2d7 `



And the result will be like this



 ![image](https://user-images.githubusercontent.com/32684082/35982446-1f994f34-0cf0-11e8-9a4a-365f5d6bc25d.png)








# 8.	**Clean Code Development**

Writing any software is the most complicated endeavors for human, as Bidan Kernigan the co-author of the AWK PL who summed up the true nature of software development in his book, said
"Controlling complexity is the essence of software development. The harsh reality of real world software development is that software is often created with intentional, or unintentional, complexity and a disregard for maintainability, testability, and quality. The end result of this unfortunate reality is software that can become increasingly difficult and expensive to maintain and that fails sporadically and even spectacularly.".


**8.1.	Always use Class-functions approach**

Using function is a block of reusable line of codes that is used to perform a specific action and its one of the important steps when writing software code in any programing language. 
List of advantages :
•	Reducing duplication of code.
•	Decomposing complex problems into simpler pieces.
•	Improving clarity of the code.
•	Reuse of code.
•	Information hiding.
You can see all TicTacToy functions previouslly in section 5 - Game In Details.



**8.2.	Use modeul carefully**

A module can contain executable statements as well as function definitions. 
These statements are intended to initialize the module. They are executed only the first time the module name is encountered in an import statement.
Each module has its own private symbol table, which is used as the global symbol table by all functions defined in the module.
Advantages: 
•	No global namespace for objects 
•	Python Modules are very easy to import and use 

In Tic Tac Toe game, a "random" module is imported not just to reduce the lines of code, but also contain useful commands:
•	random.randint(x,y) : to return random integer from interverl 
if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'
•	random.choice(seq): to return random element from non empty sequance or list ,otherwise return None
if len(possibLMoves) != 0:
        return random.choice(possibLMoves)
    else:
        return None
	
	
	
**8.3.	Organize your code**

Don‘t make your code messy especially if you are writing thousands of lines of code, organize your python code by listing all functions first in the body and then the main



**8.4.	Use #Comments**

Always use #comments in your project to describe what this lines of code do?, not just for your future reference, but also for other people who might end up reading your project and evaluating it.


**8.5.	 A clean code hypothetical test**

Always make hypnosis to check if there is any problem and solution for it: run tests on your code multiple times with different approach to insure and prove that your software can continuously works without breaking down so bad such as the following snippets code:




    #Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = getboardCopy(board)
        if FreeSpace(copy, i):
            MakeAMove(copy, playerletter, i)
            if isWinner(copy, playerletter):
                return i

    #Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [ 1, 3, 7, 9 ])
    if move != None:
        return move

    #Try to take the center, if it is free.
    if FreeSpace(board, 5):
        return 5

    #Move on one of the sides.
    return chooseRandomMoveFromList(board, [ 2, 4, 6, 8 ])









# 9.	Continuous Delivery


With the help of the Git plugin Jenkins can easily pull source code from any Git repository that the Jenkins build node can access.

 
 
![image](https://user-images.githubusercontent.com/32684082/35982831-06fbca5a-0cf1-11e8-95b0-9fb917371e8e.png)








# 10.	AOP jointpoints

The below figure shows Separate deferent concerns of implementing the Observer pattern in the context of TicTacToe a board game of Two or more players each modify the board game and need to be notified whenever some of the other players has changed the board, this is one of the powerful illustration of the AOP technique.


The big picture was broken into smaller pieces of concern which improve the programming style.



 ![image](https://user-images.githubusercontent.com/32684082/35988205-1c794a4e-0cfe-11e8-8a35-ec0f0e8e2936.png)
 
 

In this figure, we can consider the component based approach for implementing an observer pattern. The board game and players are components, which means that in the board game, each player is an observer who needs to be notified whenever the board game is changed by another player. However it’s connecting the board and the player by a notification bus as shown in (a) which describe the connectors between the components. 


The connector represents communication channels between board game and player, whenever a change happened, it will update the player about that change.  






# 11.	 DSL Demo example

Domain Specific Languages can serve all sort of purposes. They can be used in different contexts and by different kinds of users. Some DSLs are intended to be used by programmers, and therefore are more technical, while others are intended to be used by someone who is not a programmer and therefore they use less geeky concepts and syntax.


There are several examples of public DSL which are used a lot:

•	DOT – A DSL to define graphs
•	Sed – A DSL to define text transformation
•	Gawk – A DSL to print and process text
•	Website-spec – A DSL for functional web testing
•	SQL – databases
•	HTML – web layout
•	UML – visual modeling
•	PlantUML – A DSL to draw UML diagrams: PlantUML Can be used to define UML diagrams of different kinds.

For example using PlantUML, we can define a sequence diagram as per the following DSL Demo example snippet:

`@startuml`
`actor Customer1`
`actor customer2`
`database database` 
`Customer 1 -> Supplier : Request a refund`
`Supplier -> database: Verify data`
`Supplier -> Customer1`
`Supplier -> Customer2`
`@enduml`



From that code, we will get the following sequence diagram
 

![image](https://user-images.githubusercontent.com/32684082/35988305-5db0813a-0cfe-11e8-80ac-37fe8044866e.png)






# 12.	Logic Solver







# 13.	Scala Code





