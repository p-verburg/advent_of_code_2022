import unittest
from communication.receiver import Receiver, create_packet_receiver, create_message_receiver


def find_first_packet_marker(data_stream):
    receiver = create_packet_receiver()
    return receiver.find_next_marker(data_stream)


def find_first_message_marker(data_stream):
    receiver = create_message_receiver()
    return receiver.find_next_marker(data_stream)


class ReceiverTests(unittest.TestCase):
    def test_identify_start_of_packet_marker(self):
        receiver = create_packet_receiver()

        marker_found = receiver.contains_marker("bvwb".strip())

        self.assertEqual(False, marker_found)

        marker_found = receiver.contains_marker("vwbj".strip())

        self.assertEqual(True, marker_found)

    def test_find_first_packet_1(self):
        data_stream = "bvwbjplbgvbhsrlpgdmjqwftvncz"

        marker_position = find_first_packet_marker(data_stream)

        self.assertEqual(5, marker_position)

    def test_find_first_packet_2(self):
        data_stream = "nppdvjthqldpwncqszvftbrmjlhg"

        marker_position = find_first_packet_marker(data_stream)

        self.assertEqual(6, marker_position)

    def test_find_first_packet_3(self):
        data_stream = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"

        marker_position = find_first_packet_marker(data_stream)

        self.assertEqual(10, marker_position)

    def test_find_first_packet_4(self):
        data_stream = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

        marker_position = find_first_packet_marker(data_stream)

        self.assertEqual(11, marker_position)

    def test_find_first_message_1(self):
        data_stream = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

        marker_position = find_first_message_marker(data_stream)

        self.assertEqual(19, marker_position)

    def test_find_first_message_2(self):
        data_stream = "bvwbjplbgvbhsrlpgdmjqwftvncz"

        marker_position = find_first_message_marker(data_stream)

        self.assertEqual(23, marker_position)

    def test_find_first_message_3(self):
        data_stream = "nppdvjthqldpwncqszvftbrmjlhg"

        marker_position = find_first_message_marker(data_stream)

        self.assertEqual(23, marker_position)

    def test_find_first_message_4(self):
        data_stream = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"

        marker_position = find_first_message_marker(data_stream)

        self.assertEqual(29, marker_position)

 
if __name__ == '__main__':
    unittest.main()
