import unittest

from runner import run_command

class RunnerTests(unittest.TestCase):
  def test_run_command_is_available(self):
    self.assertTrue(callable(run_command))

if __name__ == "__main__":
  unittest.main()
