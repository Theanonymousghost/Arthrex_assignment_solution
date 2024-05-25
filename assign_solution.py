import unittest
from collections import deque

candidates = {
    'A': ['B', 'C', 'J'],
    'D': ['E', 'F', 'G'],
    'H': ['I', 'K', 'V'],
    'J': ['V'],
    'K': ['L', 'M', 'N', 'A'],
    'O': ['P', 'V', 'U'],
    'Q': ['S', 'T', 'D'],
    'U': ['H', 'J'],
    'V': ['W', 'X', 'Y', 'Z'],
}

contacted = []
current = deque()

def contacted_candidates(char):
    if char in candidates:
        current.append(char)
        current.extend(candidates[char])
    else:
        for key, value in candidates.items():
            if char in value:
                current.extend(candidates[key])
                current.append(key)

    while current:
        temp = current.popleft()
        if temp in contacted:
            continue
        else:
            contacted.append(temp)
            if temp in candidates:
                current.extend(candidates[temp])

"""
ins = input("Input char: ")
contacted_candidates(ins)
print(contacted)
"""

class TestContactedCandidates(unittest.TestCase):

    def setUp(self):
        global contacted, current
        contacted = []
        current = deque()

    def test_indirect_connection_m(self):
        contacted_candidates('M')
        self.assertEqual(contacted, ['L', 'M', 'N', 'A', 'K', 'B', 'C', 'J', 'V', 'W', 'X', 'Y', 'Z'])

    def test_direct_connection_a(self):
        contacted_candidates('A')
        self.assertEqual(contacted, ['A', 'B', 'C', 'J', 'V', 'W', 'X', 'Y', 'Z'])

    def test_direct_connection(self):
        contacted_candidates('K')
        self.assertEqual(contacted, ['K', 'L', 'M', 'N', 'A', 'B', 'C', 'J', 'V', 'W', 'X', 'Y', 'Z'])

    def test_indirect_connection_z(self):
        contacted_candidates('Z')
        self.assertEqual(contacted, ['W', 'X', 'Y', 'Z', 'V'])

    def test_no_connection_empty(self):
        contacted_candidates('')
        self.assertEqual(contacted, [])

    def test_key_in_value_v(self):
        contacted_candidates('V')
        self.assertIn('V', contacted)
        self.assertIn('W', contacted)
        self.assertIn('X', contacted)
        self.assertIn('Y', contacted)
        self.assertIn('Z', contacted)

if __name__ == '__main__':
    unittest.main()
