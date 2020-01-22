class State:
  board[][]
  currentPlayer

  isFinished():boolean
  play(Move):State -> nouvel objet state
  getMoves(Player): Moves[]
  getScore(Player): float




class Move:
  start:(x,y)
  end: (x,y)
  type-action:boolean



Main :

s <- State(M,N)
while ! S.isFinished():
  p <- s.getCurrentPlayer()
  l <- s.getMoves(p)
  m <- random.choice(l)
  s <- s.play(m)

////
play(Move):
  newState
  newState.board <-> self.board (itération de chaque element veers le newState)

-----------------------------------------------------------------------------------
Class IA

Player
depth
cut

-> on peut inclure le souvenir du best move dans l'algo; en sauvegardent en plus des valeurs des etats le coup à jouer
ou
-> sous function qui au premier etage choisi un move
