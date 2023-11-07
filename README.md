# MASTERMIND_GAME
Mastermind game is a strategy game in which you have 10 attempts to guess a randomly generated 4-digit number. 

## Thought Process
My approach to building this game involved a wholistic analysis of the game requirements and final output. Then, breaking down this big picture into bite size pieces that could be implemented. That is, writing down the various features, data requirements and what implementing them would look like.  

Although a traditional procedural approach was easy to implement and would meet the functional requirements, considering the non-functional requirements (gamer experience) and the possibility of scaling, led me to an extensive research into modern backend game technologies. This led to an event-driven approach to implementation. This approach promises to optimize user experience and scalability. I tried to follow the MVC architecture as it allows for easy decoupling of frontend and backend as the build scales. 

I hope you enjoy the game😊. My personal best in medium difficulty is guessing the 4 digit number on my 6th attempt! I dare you to beat that!😁 

## Prequisite
This game was built using Python 3.10.2. 
To run the setup for this game you will need to have Python 3 installed on your computer. Ignore the "$" and type the command that follows.

### Clone Repository
Open Command Prompt(windows) or Terminal(linux/mac) and navigate to your chosen folder location, <workspace directory>.

```
$ cd [workspace directory]
```
```
$ git clone https://github.com/Eseose/mastermind_game.git
```

### Setup/Run Program
```
$ cd mastermind_game
```

#### Windows:
```
$ setup_windows.bat
```
```
$ mastermind_venv\Scripts\activate
```
```
$ python main.py
```
#### Linux/Mac:
```
$ setup_linux_mac.sh
```
```
$ source mastermind_venv/bin/activate
```
```
$ python3 main.py  
```
## Extensions Implemented
- [x] **Difficulty levels:** This varies the range of numbers that can be guessed from.  
- [x] **About:** This gives a brief summary of the game and how it is played.
- [x] **Timer:** This is implemented to time each game and stored.
- [x] **Leaderboard:** This gives a list of three (3) best players in the selected difficulty level. 

## Extensions to Add/Improve
- [ ] Extend to multi-players  
- [ ] Extend timer to each attempt  
- [ ] Scoring  
- [ ] Hints  

## Built With
- [Python-State Machine](https://python-statemachine.readthedocs.io/en/latest/readme.html) - Python Game State Manager
- [SQLAlchemy](https://docs.sqlalchemy.org/en/20/) - SQL Database
- [RANDOM.ORG](https://www.random.org/clients/http/api/) - Random Number Generator API

## Author
### [*__Eseose Okiti__*](https://github.com/Eseose/)
