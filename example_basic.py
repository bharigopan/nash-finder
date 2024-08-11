import grm

game = grm.Game()

# two playeys, and each player uses THREE pure strategies
game.player_join(grm.Player(2))
game.player_join(grm.Player(2))

game.player_init_mixed_strategies()

# assign the payoff (define the payoff function)
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
game.run(iterations=10**4 * 6)

# visulize the game evolution for `grm.Player(2)`
game.plot_3()
