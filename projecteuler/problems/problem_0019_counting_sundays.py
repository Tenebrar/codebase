from datetime import date

SUNDAY = 6


def problem_0019(start_year: int, end_year: int) -> int:
    return sum(date(year, month, 1).weekday() == SUNDAY for month in range(1, 13) for year in range(start_year, end_year + 1))


if __name__ == '__main__':
    START_YEAR = 1901
    END_YEAR = 2000

    print(problem_0019(START_YEAR, END_YEAR))
    # Expected: 171
