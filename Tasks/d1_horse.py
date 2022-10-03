def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """

    rows = shape[0]
    cols = shape[1]

    def get_step(i, j):
        if i == 0 and j == 0:  # попали в начальн точку
            return 1
        if not 0 <= i < rows:  # левый угол
            return 0
        if not 0 <= j <= cols:  # выпали из строки
            return 0

        return sum([get_step(i-2, j+1),
                    get_step(i-2, j-1),
                    get_step(i-1, j-2),
                    get_step(i+1, j-2)])

    return get_step(i=point[0], j=point[1])


if __name__ == '__main__':
    assert 2 == calculate_paths((4, 4), (3, 3))
    assert 13309 == calculate_paths((7, 15), (6, 14))
