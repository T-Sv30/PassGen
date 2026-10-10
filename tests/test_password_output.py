import os
import tempfile
import unittest
from unittest.mock import patch

from passgen import writePasswordsToClipboard, writePasswordsToFile


class PasswordOutputTest(unittest.TestCase):
    passwords = ["password1", "password2", "password3"]
    password_data = "password1\npassword2\npassword3\n"

    def test_write_to_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            filename = os.path.join(tmp, "passwords.txt")
            writePasswordsToFile(filename, ["password1", "password2", "password3"])
            with open(filename, encoding="utf-8") as handle:
                self.assertEqual(handle.read(), "password1\npassword2\npassword3\n")

    def test_write_to_file_uses_utf8(self):
        with tempfile.TemporaryDirectory() as tmp:
            filename = os.path.join(tmp, "unicode.txt")
            writePasswordsToFile(filename, ["café"])
            with open(filename, encoding="utf-8") as handle:
                self.assertEqual(handle.read(), "café\n")

    @patch("passgen.pyperclip.copy")
    def test_write_to_clipboard(self, copy):
        writePasswordsToClipboard(self.passwords)
        copy.assert_called_once_with(self.password_data.rstrip("\n"))


if __name__ == "__main__":
    unittest.main()
