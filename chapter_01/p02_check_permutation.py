# O(N)
import unittest
from collections import Counter


def check_permutation(str1, str2):
    
    if len(str1) != len(str2):
        return False

    d = dict()
    for c in str1:
        if c not in d:
            d.update({c: 1})
        else:
            d[c]+=1

    for c in str2:
        if c not in d:
            return False
        else:
            d[c]-=1
            if d[c] < 0:
                return False
    return True
        
class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = check_permutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = check_permutation(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()