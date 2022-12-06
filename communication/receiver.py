from collections import deque

PACKET_MARKER_LENGTH = 4
MESSAGE_MARKER_LENGTH = 14


class Receiver:
    def __init__(self, marker_length):
        self.position = 0
        self.buffer = deque(maxlen=marker_length)

    def read_next_character(self, data_stream):
        self.buffer.append(data_stream[self.position])
        self.position = self.position + 1

    def contains_marker(self, buffer):
        return len(set(buffer)) == self.buffer.maxlen

    def find_next_marker(self, data_stream):
        while self.position < len(data_stream):
            self.read_next_character(data_stream)
            if self.contains_marker(self.buffer):
                return self.position

        return None


def create_packet_receiver():
    return Receiver(PACKET_MARKER_LENGTH)


def create_message_receiver():
    return Receiver(MESSAGE_MARKER_LENGTH)
