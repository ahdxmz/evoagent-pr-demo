import subprocess
import sys
import unittest

from runner import run_command


class RunnerTests(unittest.TestCase):
    def test_run_command_executes_argument_list_and_captures_output(self):
        result = run_command([sys.executable, "-c", "print('hello')"])

        self.assertEqual(0, result.returncode)
        self.assertEqual("hello", result.stdout.strip())

    def test_run_command_raises_when_command_fails(self):
        with self.assertRaises(subprocess.CalledProcessError):
            run_command([sys.executable, "-c", "raise SystemExit(3)"])


if __name__ == "__main__":
    unittest.main()
