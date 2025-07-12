import pygame
import sys
import chess
import math

pygame.init()
WIDTH, HEIGHT = 640, 640
SQUARE_SIZE = WIDTH // 8
FONT = pygame.font.SysFont("segoeuisymbol", 48)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess - Player vs Computer (Minimax AI)")

WHITE_COLOR = (240, 217, 181)
BROWN = (181, 136, 99)
HIGHLIGHT = (255, 255, 0)
MOVE_HINT = (100, 255, 100)

symbols = {
    "r": "♜", "n": "♞", "b": "♝", "q": "♛", "k": "♚", "p": "♟",
    "R": "♖", "N": "♘", "B": "♗", "Q": "♕", "K": "♔", "P": "♙"
}

piece_values = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0
}

def draw_board(board, selected_square=None, legal_moves=[]):
    for row in range(8):
        for col in range(8):
            rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            color = BROWN if (row + col) % 2 else WHITE_COLOR
            pygame.draw.rect(screen, color, rect)
            square = chess.square(col, 7 - row)
            if square == selected_square:
                pygame.draw.rect(screen, HIGHLIGHT, rect, 4)
            elif square in legal_moves:
                pygame.draw.circle(screen, MOVE_HINT, rect.center, 10)
            piece = board.piece_at(square)
            if piece:
                text = FONT.render(symbols[piece.symbol()], True, (0, 0, 0))
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)
    pygame.display.flip()

def get_square_under_mouse(pos):
    x, y = pos
    col = x // SQUARE_SIZE
    row = y // SQUARE_SIZE
    return chess.square(col, 7 - row)

def evaluate_board(board):
    if board.is_checkmate():
        return -9999 if board.turn else 9999
    elif board.is_stalemate() or board.is_insufficient_material():
        return 0
    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            value = piece_values[piece.piece_type]
            score += value if piece.color == chess.WHITE else -value
    return score

def minimax(board, depth, alpha, beta, maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    best_move = None
    if maximizing:
        max_eval = -math.inf
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = math.inf
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def ai_move(board):
    _, move = minimax(board, 2, -math.inf, math.inf, False)
    if move:
        board.push(move)

def promote_pawn(board, move):
    if board.is_legal(move):
        board.push(move)
    else:
        for promo in [chess.QUEEN, chess.ROOK, chess.BISHOP, chess.KNIGHT]:
            promo_move = chess.Move(move.from_square, move.to_square, promotion=promo)
            if promo_move in board.legal_moves:
                board.push(promo_move)
                break

def display_result(board):
    screen.fill((0, 0, 0))
    result = board.result()

    if board.is_checkmate():
        winner = "Player Wins!" if not board.turn else "Computer Wins!"
    elif board.is_stalemate():
        winner = "Draw (Stalemate)"
    elif board.is_insufficient_material():
        winner = "Draw (Insufficient Material)"
    elif board.is_seventyfive_moves():
        winner = "Draw (75-move rule)"
    elif board.is_fivefold_repetition():
        winner = "Draw (Fivefold repetition)"
    else:
        winner = f"Game Over: {result}"

    result_font = pygame.font.SysFont("arial", 48)
    result_text = result_font.render(winner, True, (255, 255, 255))
    text_rect = result_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(result_text, text_rect)
    pygame.display.flip()
    pygame.time.wait(4000)

def main():
    board = chess.Board()
    selected_square = None
    running = True

    while running:
        legal_moves = []
        if selected_square is not None:
            legal_moves = [move.to_square for move in board.legal_moves if move.from_square == selected_square]

        draw_board(board, selected_square, legal_moves)

        if board.is_game_over():
            display_result(board)
            running = False
            continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and board.turn == chess.WHITE:
                square = get_square_under_mouse(pygame.mouse.get_pos())
                if selected_square is not None:
                    move = chess.Move(selected_square, square)
                    if move in board.legal_moves:
                        if board.piece_at(selected_square).piece_type == chess.PAWN and chess.square_rank(square) in [0, 7]:
                            promote_pawn(board, move)
                        else:
                            board.push(move)
                        selected_square = None
                    else:
                        selected_square = None
                elif board.piece_at(square) and board.piece_at(square).color == chess.WHITE:
                    selected_square = square

        if board.turn == chess.BLACK and not board.is_game_over():
            pygame.time.wait(300)
            ai_move(board)

    pygame.quit()
    sys.exit()

if __name__== "__main__":
    main()