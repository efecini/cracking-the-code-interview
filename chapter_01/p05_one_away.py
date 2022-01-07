# O(N)
import time
import unittest


def are_one_edit_different(s1, s2):
    if len(s1)==len(s2):
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return s2[i+1:len(s2)] == s1[i+1:len(s1)]
        return True
    elif len(s1)+1 == len(s2):
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return s2[i+1:len(s2)] == s1[i:len(s1)]
            elif i+1 == len(s1):
                return True
        return True
    elif len(s1) == len(s2)+1:
        for i in range(len(s2)):
            if s2[i] != s1[i]:
                return s1[i+1:len(s1)] == s2[i:len(s2)]
            elif i+1 == len(s2):
                return True
        return True
    else:
        return False

class Test(unittest.TestCase):
    test_cases = [
        # no changes
        ("pale", "pale", True),
        # one insert
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pales", "pale", True),
        ("ples", "pales", True),
        ("pale", "pkle", True),
        ("paleabc", "pleabc", True),
        ("", "d", True),
        ("d", "de", True),
        # one replace
        ("pale", "bale", True),
        ("a", "b", True),
        ("pale", "ble", False),
        # multiple replace
        ("pale", "bake", False),
        # insert and replace
        ("pale", "pse", False),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
        # permutation with insert shouldn't match
        ("ale", "elas", False),
    ]

    testable_functions = [are_one_edit_different]

    def test_one_away(self):

        for f in self.testable_functions:
            start = time.perf_counter()
            for _ in range(100):
                for [text_a, text_b, expected] in self.test_cases:
                    assert f(text_a, text_b) == expected
            duration = time.perf_counter() - start
            print(f"{f.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    unittest.main()
