:- dynamic(game/1).
%:- dynamic((',')/2)


% Факты о настольных играх
game(chess).
game(monopoly).
game(scrabble).
game(risk).
game(checkers).
game(card_game).

% Факты о количестве игроков
players(chess, 2).
players(monopoly, 2-4).
players(scrabble, 2-4).
players(risk, 2-6).
players(checkers, 2).
players(card_game, 2-8).

% Факты о типе игры
type(chess, strategy).
type(monopoly, board).
type(scrabble, word).
type(risk, strategy).
type(checkers, board).
type(card_game, card).

% Факты о правилах игры
rules(chess, 'Move chess pieces strategically to checkmate your opponent.').
rules(monopoly, 'Buy properties and bankrupt your opponents in this classic board game.').
rules(scrabble, 'Create words and score points with letter tiles.').
rules(risk, 'Conquer the world with armies and strategic warfare.').
rules(checkers, 'Jump over and capture your opponent\'s pieces in this board game.').
rules(card_game, 'Play cards strategically to win the game.').

% Факты о некоторых игровых персонажах
character(chess, 'King').
character(chess, 'Queen').
character(chess, 'Rook').
character(chess, 'Bishop').
character(chess, 'Knight').
character(chess, 'Pawn').
character(monopoly, 'Mr. Monopoly').
character(scrabble, 'Tile Bag').
character(risk, 'General').
character(checkers, 'Red Checker').
character(checkers, 'Black Checker').

% Правило: Игра strategy подходит для взрослых
suitable_for_adults(Game) :- type(Game, strategy) ; type(Game, word).

% Правило: Игра board подходит для детей
suitable_for_children(Game) :- type(Game, board) ; type(Game, word).

% Правило: Игра, подходящая для взрослых и детей
suitable_for_family(Game) :- suitable_for_adults(Game), suitable_for_children(Game).

% Правило: Игра, которую можно сыграть вдвоем и подходит для взрослых
two_player_adult_game(Game) :- players(Game, 2), suitable_for_adults(Game).

% Правило: Игра с большим количеством игроков и подходит для детей
multiplayer_children_game(Game) :- players(Game, Players), Players > 4, suitable_for_children(Game).
