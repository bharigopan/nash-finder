import grm

game = grm.Game()

game.player_join(grm.Player(2))
game.player_join(grm.Player(2))

game.player_init_mixed_strategies()

"""
Prosoner's dilemma
Bimatrix:
    [-10, -1],
    [-25, -3]

    [-10, -25],
    [-1, -3],
the unique NE at (-10, -10)
"""

# player 1
game.player_assign_payoff(1, "11", -10)
game.player_assign_payoff(1, "12", -1)
game.player_assign_payoff(1, "21", -25)
game.player_assign_payoff(1, "22", -3)

# player 2
game.player_assign_payoff(2, "11", -10)
game.player_assign_payoff(2, "12", -25)
game.player_assign_payoff(2, "21", -1)
game.player_assign_payoff(2, "22", -3)

# run the iterations to approximate Nash equilibrium
game.run()

# visulize the game evolution for `grm.Player(3)`
game.plot_2()
