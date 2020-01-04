from projecteuler.settings import inputfile


def problem_0079(filename: str) -> None:
    with open(inputfile(filename), 'r') as file:
        for line in file.readlines():
            print(line)


if __name__ == '__main__':
    print(problem_0079('p079_keylog.txt'))
    # Expected:
