import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 500, 500
ROWS, COLS = 5, 5
SQUARE_SIZE = WIDTH // COLS

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Fill Puzzle")


board = [[-1 for _ in range(COLS)] for _ in range(ROWS)]


def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if board[row][col] == -1 else COLORS[board[row][col]]
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.rect(screen, GRAY, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 2)


def is_valid_color(row, col, color_index):

    neighbors = [
        (row - 1, col),
        (row + 1, col),
        (row, col - 1),
        (row, col + 1)
    ]
    for r, c in neighbors:
        if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == color_index:
            return False
    return True


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                col, row = x // SQUARE_SIZE, y // SQUARE_SIZE

                current_color = board[row][col]
                next_color = (current_color + 1) % len(COLORS) if current_color != -1 else 0

                if is_valid_color(row, col, next_color):
                    board[row][col] = next_color

        screen.fill(WHITE)
        draw_board()
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
