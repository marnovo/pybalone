#
# Pybalone
#
# A Python implementation of the Abalone* board game
# Abalone is a registered trademark of Abalone S.A.
#

x = 9  # invalid spaces
b = 0  # empty board spaces
A = 1  # player 1/A/top
B = 2  # player 2/B/bottom

# Axial coordinates used as explained in:
# http://www.redblobgames.com/grids/hexagons/#coordinates-axial
# Stored as explained in:
# http://www.redblobgames.com/grids/hexagons/#map-storage

# Fix below with above

BOARD_ZERO = [
             [  x, x, 0, 0, 0, 0, 0, x, x],
             [x, x, 0, 0, 0, 0, 0, 0, x  ],
             [  x, 0, 0, 0, 0, 0, 0, 0, x],
             [x, 0, 0, 0, 0, 0, 0, 0, 0  ],
             [  0, 0, 0, 0, 0, 0, 0, 0, 0],
             [x, 0, 0, 0, 0, 0, 0, 0, 0  ],
             [  x, 0, 0, 0, 0, 0, 0, 0, x],
             [x, x, 0, 0, 0, 0, 0, 0, x  ],
             [  x, x, 0, 0, 0, 0, 0, x, x],
             ]

BOARD_INIT = [
             [  x, x, 1, 1, 1, 1, 1, x, x],
             [x, x, 1, 1, 1, 1, 1, 1, x  ],
             [  x, 0, 0, 1, 1, 1, 0, 0, x],
             [x, 0, 0, 0, 0, 0, 0, 0, 0  ],
             [  0, 0, 0, 0, 0, 0, 0, 0, 0],
             [x, 0, 0, 0, 0, 0, 0, 0, 0  ],
             [  x, 0, 0, 2, 2, 2, 0, 0, x],
             [x, x, 2, 2, 2, 2, 2, 2, x  ],
             [  x, x, 2, 2, 2, 2, 2, x, x],
             ]

board = BOARD_INIT

