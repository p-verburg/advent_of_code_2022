def get_item_priority(item_code):
    if 'a' <= item_code <= 'z':
        return ord(item_code) - ord('a') + 1
    if 'A' <= item_code <= 'Z':
        return ord(item_code) - ord('A') + 27

    return None


def get_total_item_priority(item_codes):
    total = 0
    for item_code in item_codes:
        total += get_item_priority(item_code)

    return total
