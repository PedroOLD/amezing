import sys
from utils import read_configuration, Solution
from dataclasses import dataclass
from algorithm import MazeGenerator
import random

"""
Add Decorator DataClasss on a Class. He help us add the propieties Class for
the use with the batter usebility
Ex: Before DataClass
    values_config["<NameProp>"]
after DataClass
    values_config.<nameProp>
"""


@dataclass
class ValuesConfg:
    width: int
    height: int
    path: str
    perfect: bool
    entry: tuple
    exit: tuple
    seed: str
    """
    Data container for maze configuration values.

    Attributes:
        width (int): Maze width (logical units).
        height (int): Maze height (logical units).
        path (str): Output file path.
        perfect (bool): Whether to generate a perfect maze.
        entry (tuple): Entry coordinates (row, col).
        exit (tuple): Exit coordinates (row, col).
        seed (str): Random seed for reproducibility.
    """


def entry_tuples(value: str) -> tuple[int, int]:
    """
    Convert a string representation of coordinates into a tuple.

    Args:
        value (str): Coordinate string in the format "(y,x)".

    Returns:
        tuple[int, int]: Parsed (y, x) coordinates.
    """
    return tuple(int(x) for x in value.replace('(', '').split(','))


def parse_bool(value: str) -> bool:
    """
    Convert a string to a boolean value.

    Args:
        value (str): Input string.

    Returns:
        bool: True if value represents a truthy string ("true", "1", "yes"),
        False otherwise.
    """
    return value.strip().lower() in ("true", "1", "yes")


def main() -> None:
    """
    Main entry point for maze generation and solving.

    Workflow:
        1. Read configuration file from command-line argument.
        2. Parse configuration into a structured dataclass.
        3. Validate dimensions and seed randomness.
        4. Generate the maze.
        5. Solve the maze using BFS.
        6. Mark the solution path in the maze.
        7. Print the colored maze.
        8. Append movement directions (N, S, E, W) to the output file.

    Notes:
        - Entry and exit positions are given in logical coordinates.
        - The solution path is written as directional steps.
    """
    # create the variable for to receiver values the file config
    if (len(sys.argv) != 2):
        print("Error need the file for generate")
        return
    # This function get and return a Dict with the configs
    values_config = read_configuration(sys.argv[1])
    # Use the ValueConfig class
    valuesReceiver = ValuesConfg(
        width=int(values_config["WIDTH"]),
        height=int(values_config["HEIGHT"]),
        path=str(values_config["OUTPUT_FILE"]),
        perfect=parse_bool(values_config['PERFECT']),
        entry=entry_tuples(values_config['ENTRY']),
        exit=entry_tuples(values_config['EXIT']),
        seed=str(values_config['SEED'])
    )
    if (valuesReceiver.height < 6 and valuesReceiver.width < 7):
        print("ERROR: Map Too Small. Min is 6 x 7.")
        sys.exit()

    if (valuesReceiver.seed == ""):
        random.seed()
    else:
        random.seed(valuesReceiver.seed)
    test = MazeGenerator(valuesReceiver.width,
                         valuesReceiver.height,
                         valuesReceiver.path,
                         valuesReceiver.entry,
                         valuesReceiver.exit,
                         valuesReceiver.perfect)

    test.create_maze()
    solution = Solution(valuesReceiver.entry, valuesReceiver.exit, test.maze)

    # esta printando a solucao mas esta passando por cima do 42

    resolution = solution.bfs_resolver()

    for i, (y, x) in enumerate(resolution):
        test.maze[y, x] = 3
        if i + 1 < len(resolution):
            ny, nx = resolution[i + 1]
            my, mx = resolution[i]
            test.maze[(y + ny) // 2, (x + nx) // 2] = 3
            test.maze[(y + my) // 2, (x + mx) // 2] = 3

    # imprime
    for line in test.generate_final_maze():
        print(line)

    resolution = solution.bfs_resolver()
    with open(valuesReceiver.path, "a") as f:
        for (cy, cx), (ncy, ncx) in zip(resolution, resolution[1:]):
            if (ncy > cy and ncx == cx):
                f.write("S")
            elif (ncy < cy and ncx == cx):
                f.write("N")
            elif (ncy == cy and ncx > cx):
                f.write("E")
            elif (ncy == cy and ncx < cx):
                f.write("W")


if __name__ == "__main__":
    main()
