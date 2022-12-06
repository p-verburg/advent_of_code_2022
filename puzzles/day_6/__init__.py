from communication.receiver import create_packet_receiver, create_message_receiver

with open('data_stream.txt') as file:
    data_stream = file.read().strip()

receiver = create_packet_receiver()
first_packet_position = receiver.find_next_marker(data_stream)

print(first_packet_position)

receiver = create_message_receiver()
first_message_position = receiver.find_next_marker(data_stream)

print(first_message_position)
