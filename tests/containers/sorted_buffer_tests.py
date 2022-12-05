import unittest
from containers.sorted_buffer import SortedBuffer


class TestObject:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'TestObject { ' + self.value + ' }'


class SortedBufferTests(unittest.TestCase):
    def test_submit_first(self):
        buffer = SortedBuffer(3)

        buffer.submit(2, TestObject('two'))

        self.assertEqual(len(buffer.values), 1)
        self.assertEqual(buffer.values[0].value, 'two')

    def test_submit_second_after(self):
        buffer = SortedBuffer(3)
        buffer.submit(5, TestObject('five'))

        buffer.submit(2, TestObject('two'))

        self.assertEqual(len(buffer.values), 2)
        self.assertEqual(buffer.values[0].value, 'five')
        self.assertEqual(buffer.values[1].value, 'two')

    def test_submit_second_before(self):
        buffer = SortedBuffer(3)
        buffer.submit(2, TestObject('two'))

        buffer.submit(5, TestObject('five'))

        self.assertEqual(len(buffer.values), 2)
        self.assertEqual(buffer.values[0].value, 'five')
        self.assertEqual(buffer.values[1].value, 'two')

    def test_reject_lower_than_last(self):
        buffer = SortedBuffer(3)
        buffer.submit(5, TestObject('five'))
        buffer.submit(4, TestObject('four'))
        buffer.submit(3, TestObject('three'))

        buffer.submit(2, TestObject('two'))

        self.assertEqual(len(buffer.values), 3)
        values = [o.value for o in buffer.values]
        self.assertNotIn('two', values)

    def test_truncate_lowest(self):
        buffer = SortedBuffer(3)
        buffer.submit(5, TestObject('five'))
        buffer.submit(4, TestObject('four'))
        buffer.submit(2, TestObject('two'))

        buffer.submit(3, TestObject('three'))

        self.assertEqual(len(buffer.values), 3)
        values = [o.value for o in buffer.values]
        self.assertNotIn('two', values)


if __name__ == '__main__':
    unittest.main()
