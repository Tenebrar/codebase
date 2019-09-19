from util.combinatorics.amounts import lattice_paths


def problem_0015(grid_height: int, grid_width: int) -> int:
    return lattice_paths(grid_height, grid_width)


if __name__ == '__main__':
    GRID_HEIGHT = 20
    GRID_WIDTH = 20

    print(problem_0015(GRID_HEIGHT, GRID_WIDTH))
    # Expected: 137846528820
