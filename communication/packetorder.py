class PacketPair:
    def __init__(self, left, right):
        self.left = left
        self.right = right


def read_all_packets(signal):
    pairs = []
    while True:
        try:
            left = eval(next(signal))
            right = eval(next(signal))

            pairs.append(PacketPair(left, right))

            next(signal)
        except StopIteration:
            break

    return pairs


def are_in_right_order(left, right):
    if isinstance(left, list) and isinstance(right, int):
        return are_in_right_order(left, [right])
    if isinstance(left, int) and isinstance(right, list):
        return are_in_right_order([left], right)
    if isinstance(left, list) and isinstance(right, list):
        left_size = len(left)
        right_size = len(right)

        for i in range(0, min(left_size, right_size)):
            result = are_in_right_order(left[i], right[i])
            if result:
                return True
            if result is not None:
                return False

        if left_size < right_size:
            return True
        if left_size > right_size:
            return False

        return None

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        if left > right:
            return False
        return None

    raise ValueError('Data of unsupported type')


def compare(left, right):
    result = are_in_right_order(left, right)
    if result is None:
        return 0
    if result:
        return -1
    return 1


def append_divider_packets(list):
    list.append([[2]])
    list.append([[6]])


def find_divider_packets(packets):
    indices = []
    for i in range(0, len(packets)):
        if packets[i] == [[2]] or packets[i] == [[6]]:
            indices.append(i + 1)
    return indices
