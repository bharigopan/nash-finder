import grm

game = grm.Game()

game.player_join(grm.Player(2))
game.player_join(grm.Player(2))

game.player_init_mixed_strategies()

"""
Prosoner's dilemma
Bimatrix:
    [-100000, -10000],
    [-250000, -30000]

    [-100000, -250000],
    [-10000, -30000],
the unique NE at (-100000, -100000)
"""

# player 1
game.player_assign_payoff(1, "11", -100000)
game.player_assign_payoff(1, "12", -10000)
game.player_assign_payoff(1, "21", -250000)
game.player_assign_payoff(1, "22", -30000)

# player 2
game.player_assign_payoff(2, "11", -100000)
game.player_assign_payoff(2, "12", -250000)
game.player_assign_payoff(2, "21", -10000)
game.player_assign_payoff(2, "22", -30000)

# run the iterations to approximate Nash equilibrium
game.run()

# visulize the game evolution for `grm.Player(3)`
game.plot_2()
