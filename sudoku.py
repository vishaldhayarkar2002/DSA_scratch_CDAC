def isValidSudoku(board):
    # Sets for each row, column, and box
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            val = board[r][c]

            # Skip empty cells
            if val == '.':
                continue

            # Which 3×3 box does this cell belong to?
            box_index = (r // 3) * 3 + (c // 3)

            # Check if digit already exists in row, col, or box
            if val in rows[r] or val in cols[c] or val in boxes[box_index]:
                return False

            # Mark digit as seen
            rows[r].add(val)
            cols[c].add(val)
            boxes[box_index].add(val)

    return True


# box_index = (r // 3) * 3 + (c // 3)
# Maps (r, c) to box 0–8.
# Example: (4, 7) → (1)*3 + 2 = 5.
# Box layout:

# text
# 0 1 2
# 3 4 5
# 6 7 8