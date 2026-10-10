import unittest
from substitute import fullSub, basicSub, appendNumbers

class RegressionTests(unittest.TestCase):
    def test_empty_input_rejected(self):
        for generator in (fullSub, basicSub, appendNumbers):
            with self.subTest(generator=generator.__name__):
                with self.assertRaises(ValueError):
                    generator("")

    def test_non_string_input_rejected(self):
        for generator in (fullSub, basicSub, appendNumbers):
            with self.subTest(generator=generator.__name__):
                with self.assertRaises(ValueError):
                    generator(123)

    def test_uppercase_and_nonletters(self):
        self.assertIn("Password1", basicSub("Password"))
        self.assertTrue(all(item.startswith("1") for item in basicSub("123test")))
        self.assertTrue(all(item.startswith("@") for item in basicSub("@test")))

    def test_basic_candidates_are_unique(self):
        values = basicSub("password")
        self.assertEqual(len(values), len(set(values)))

    def test_full_substitution_cap(self):
        with self.assertRaisesRegex(ValueError, "shorter input"):
            fullSub("abcdefghijklmno")

    def test_numeric_suffixes(self):
        values = appendNumbers("x")
        self.assertEqual(33330, len(values))
        self.assertEqual("x1", values[0])
        self.assertEqual("+0000", values[-1])

if __name__ == "__main__":
    unittest.main()
