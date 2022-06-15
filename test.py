import unittest


class TestStringMethods(unittest.TestCase):
    """
    Class docstring
    """
    # def setUp(self) -> None:
    #     pass

    def test_string_a(self) -> None:
        """
        Check  string
        """
        self.assertEqual("a"*4, "aaaa")

    def test_upper(self) -> None:
        """
        Check Uppercase
        """
        self.assertEqual("qwe".upper(), "QWE")

    def test_isupper(self) -> None:
        """
        Check Is upper
        """
        self.assertTrue("FOO".isupper())
        self.assertFalse("FOO".isupper())

    def test_strip(self, name: str="abc") -> None:
        """
        Q
        """
        self.assertEqual(name.strip("a"), "bc")

    def test_split(self):
        """
        Q
        """
        word_hello = "hello world"
        self.assertEqual(word_hello.split(), ["hello", "word"])
        with self.assertRaises(TypeError):
            word_hello.split(2)


if __name__ == "__main__":
    unittest.main()
