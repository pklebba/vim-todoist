import unittest
import vim_todoist as sut


@unittest.skip("Don't forget to test!")
class VimTodoistTests(unittest.TestCase):

    def test_example_fail(self):
        result = sut.vim_todoist_example()
        self.assertEqual("Happy Hacking", result)
