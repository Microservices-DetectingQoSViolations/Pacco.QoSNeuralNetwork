def generate_time(offset, data_length):
    start = offset - data_length
    return range(start, offset)
