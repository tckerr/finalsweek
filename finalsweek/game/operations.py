def max_seat_difference(object_set):
    if len(object_set) > 2:
        raise Exception("Improper use of 'seat_difference' operation: length of object_set is not 2, but {}".format(str(len(object_set))))
    elif len(object_set) == 1:
        print("WARNING, max_seat_difference called with one person... AI?")
        return 0
    seat0 = object_set[0].seat
    seat1 = object_set[1].seat
    col_diff = abs(seat0.column - seat1.column)
    row_diff = abs(seat0.row - seat1.row)
    return max(col_diff, row_diff) * 3