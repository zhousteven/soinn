import unittest
import numpy as np
from soinn import Soinn


class TestSoinn(unittest.TestCase):
    def setUp(self):
        self.soinn = Soinn()

    def test_input_signal(self):
        pass

    def test_check_signal(self):
        signal = [0, 1, 2]
        self.assertRaises(TypeError, self.soinn._Soinn__check_signal, signal)
        signal = np.arange(6).reshape(2, 3)
        self.assertRaises(TypeError, self.soinn._Soinn__check_signal, signal)
        d = 6
        signal = np.arange(d)
        self.soinn._Soinn__check_signal(signal)
        self.assertTrue(hasattr(self.soinn, 'dim'))
        self.assertEqual(self.soinn.dim, d)
        signal = np.arange(d + 1)
        self.assertRaises(TypeError, self.soinn._Soinn__check_signal, signal)

    def test_add_node(self):
        self.soinn.dim = 2  # dim have to be set before calling __add_node()
        signal_array = [[0, 0], [1, 0], [1, 1], [0, 1]]
        for n in range(len(signal_array)):
            signal = np.array(signal_array[n])
            self.soinn._Soinn__add_node(signal)
            self.assertEqual(len(self.soinn.winning_times), n + 1)
            self.assertEqual(self.soinn.nodes.shape, (n + 1, self.soinn.dim))
            for i in range(len(signal)):
                self.assertEqual(self.soinn.nodes[n, i], signal[i], '[' + str(n) + ', ' + str(i) + ']')
            self.assertEqual(self.soinn.adjacent_mat.shape, (n + 1, n + 1))
            self.assertEqual(self.soinn.adjacent_mat.nnz, 0)

if __name__ == '__main__':
    unittest.main()
