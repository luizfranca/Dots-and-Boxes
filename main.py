import sys
import DotsAndBoxes as dab
import DotsAndBoxesAI as ai


if __name__ == "__main__":
    if (len(sys.argv) > 2):
        player = sys.argv[1] == "B"
        board = sys.argv[2]

        game = dab.DotsAndBoxes()
        game.input_board(board)
    else:
        game = dab.DotsAndBoxes(4, 4)
        player = True

    if (len(sys.argv) > 3):
        print "%d %d" % ai.alphabeta(game, int(sys.argv[3]), player = player)[0]
    else:
        print "%d %d" % ai.alphabeta(game, 7, player = player)[0]