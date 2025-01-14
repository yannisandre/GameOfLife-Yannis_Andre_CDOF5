import os
import time
import random

def clear_console():
    """Efface la console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def create_grid(rows, cols):
    """Crée une grille de cellules avec des valeurs aléatoires (0 ou 1)."""
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

def display_grid(grid):
    """Affiche la grille dans la console."""
    for row in grid:
        print("".join("■" if cell else " " for cell in row))

def count_neighbors(grid, row, col):
    """Compte les voisins vivants autour d'une cellule."""
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    rows, cols = len(grid), len(grid[0])
    count = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < rows and 0 <= c < cols and (r != row or c != col):
            count += grid[r][c]
    return count

def next_generation(grid):
    """Calcule la prochaine génération de la grille."""
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            live_neighbors = count_neighbors(grid, r, c)
            if grid[r][c] == 1 and live_neighbors in [2, 3]:
                new_grid[r][c] = 1  # Reste vivante
            elif grid[r][c] == 0 and live_neighbors == 3:
                new_grid[r][c] = 1  # Devient vivante
    return new_grid

def game_of_life(rows=20, cols=40, generations=100, interval=0.2):
    """Exécute le Jeu de la vie."""
    grid = create_grid(rows, cols)
    for gen in range(generations):
        clear_console()
        print(f"Generation {gen + 1}")
        display_grid(grid)
        grid = next_generation(grid)
        time.sleep(interval)

if __name__ == "__main__":
    game_of_life()
