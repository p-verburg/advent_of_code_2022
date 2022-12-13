import unittest

from communication.packetorder import read_all_packets, PacketPair, are_in_right_order


class PacketOrderTests(unittest.TestCase):
    def test_read_all_packets(self):
        with open('test_distress_signal.txt') as file:
            packet_pairs = read_all_packets(file)

        self.assertEqual(8, len(packet_pairs))

        self.assertListEqual([1, 1, 3, 1, 1], packet_pairs[0].left)
        self.assertListEqual([1, 1, 5, 1, 1], packet_pairs[0].right)

        self.assertListEqual([[1], [2, 3, 4]], packet_pairs[1].left)
        self.assertListEqual([[1], 4], packet_pairs[1].right)

        # ...
        self.assertListEqual([1, [2, [3, [4, [5, 6, 0]]]], 8, 9], packet_pairs[-1].right)

    def packet_order_test(self, left, right, expected):
        are_in_order = are_in_right_order(left, right)

        self.assertEqual(expected, are_in_order)

    def test_are_in_right_order_1(self):
        self.packet_order_test([1, 1, 3, 1, 1],
                               [1, 1, 5, 1, 1],
                               True)

    def test_are_in_right_order_2(self):
        self.packet_order_test([[1], [2, 3, 4]],
                               [[1], 4],
                               True)

    def test_are_in_right_order_3(self):
        self.packet_order_test([9],
                               [[8, 7, 6]],
                               False)

    def test_are_in_right_order_4(self):
        self.packet_order_test([[4, 4], 4, 4],
                               [[4, 4], 4, 4, 4],
                               True)

    def test_are_in_right_order_5(self):
        self.packet_order_test([7, 7, 7, 7],
                               [7, 7, 7],
                               False)

    def test_are_in_right_order_6(self):
        self.packet_order_test([], [3], True)

    def test_are_in_right_order_7(self):
        self.packet_order_test([[[]]], [[]], False)

    def test_are_in_right_order_8(self):
        self.packet_order_test([1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
                               [1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
                               False)


if __name__ == '__main__':
    unittest.main()
