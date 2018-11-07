def get_line(path):
    try:
        fp = open(path, 'r')
    except FileNotFoundError:
        print('Cannot open {}'.format(path))
    else:
        with fp:
            for line in fp:
                yield line


def csv_reader(path, fields, sep=',', header=False):
    for line in list(get_line(path)):
        line = line.rstrip('\n')
        if header is True:
            if len(header) != fields:
                raise ValueError('Expected {} fields, but the header only has {}.'.format(fields, len(header)))
            header = False
            continue
        # print(line)
        lst = line.split(sep)
        # print(lst)
        if len(lst) != fields:
            raise ValueError('Expected {} fields, but it is {}.'.format(fields, len(lst)))
        yield tuple(lst)
