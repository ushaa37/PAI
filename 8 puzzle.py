from queue import PriorityQueue

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()

def find_blank(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

def is_valid_move(i, j):
    return 0 <= i < 3 and 0 <= j < 3

def apply_move(board, move):
    i, j = find_blank(board)
    new_i, new_j = i + move[0], j + move[1]
    board[i][j], board[new_i][new_j] = board[new_i][new_j], board[i][j]

def is_goal(board):
    return board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def manhattan_distance(board):
    distance = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                target_i, target_j = divmod(board[i][j] - 1, 3)
                distance += abs(i - target_i) + abs(j - target_j)
    return distance

def solve_puzzle(initial_board):
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_board = [list(row) for row in initial_board]

    pq = PriorityQueue()
    pq.put((0, current_board))

    while not pq.empty():
        _, current_board = pq.get()

        if is_goal(current_board):
            print("Puzzle Solved:")
            print_board(current_board)
            return

        blank_i, blank_j = find_blank(current_board)

        for move in moves:
            new_i, new_j = blank_i + move[0], blank_j + move[1]
            if is_valid_move(new_i, new_j):
                next_board = [row[:] for row in current_board]
                apply_move(next_board, move)
                priority = manhattan_distance(next_board)
                pq.put((priority, next_board))

initial_board = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
solve_puzzle(initial_board)