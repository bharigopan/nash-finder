import grm

game = grm.Game()

game.player_join(grm.Player(2))
game.player_join(grm.Player(2))

game.player_init_mixed_strategies()

"""
Battle of sexes

Bimatrix:
    [900, 0],
    [0, 500]

    [500, 0],
    [0, 900],
"""

# player 1
game.player_assign_payoff(1, "11", 900)
game.player_assign_payoff(1, "12", 0)
game.player_assign_payoff(1, "21", 0)
game.player_assign_payoff(1, "22", 500)

# player 2
game.player_assign_payoff(2, "11", 500)
game.player_assign_payoff(2, "12", 0)
game.player_assign_payoff(2, "21", 0)
game.player_assign_payoff(2, "22", 900)

# run the iterations to approximate Nash equilibrium
game.run()

# visulize the game evolution for `grm.Player(3)`
game.plot_2()
