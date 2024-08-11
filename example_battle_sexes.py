import grm

game = grm.Game()

game.player_join(grm.Player(2))
game.player_join(grm.Player(2))

game.player_init_mixed_strategies()

"""
Battle of sexes

Bimatrix:
    [7, 0],
    [0, 3]

    [3, 0],
    [0, 7],
"""

# player 1
game.player_assign_payoff(1, "11", 7)
game.player_assign_payoff(1, "12", 0)
game.player_assign_payoff(1, "21", 0)
game.player_assign_payoff(1, "22", 3)

# player 2
game.player_assign_payoff(2, "11", 3)
game.player_assign_payoff(2, "12", 0)
game.player_assign_payoff(2, "21", 0)
game.player_assign_payoff(2, "22", 7)

# run the iterations to approximate Nash equilibrium
game.run()

# visulize the game evolution for `grm.Player(3)`
game.plot_2()
