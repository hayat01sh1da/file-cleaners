import unittest
import os
import glob
import shutil
import sys
sys.path.append('./src')
from application import Application

class TestApplication(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.join('.', 'test', 'tmp')
        if not os.path.isdir(self.dirname):
            os.makedirs(self.dirname)
        for i in range(1, 101):
            with open(os.path.join(self.dirname, 'test_file_{i:03}.txt'.format(i = i)), 'w') as f:
                f.write('')
        self.pattern = '*.txt'

    def test_run_in_dry_run_mode_1(self):
      Application(self.dirname, self.pattern).run()
      self.assertEqual(len(glob.glob(os.path.join(self.dirname, '**', self.pattern), recursive = True)), 100)

    def test_run_in_dry_run_mode_2(self):
      Application(self.dirname, self.pattern, '-d').run()
      self.assertEqual(len(glob.glob(os.path.join(self.dirname, '**', self.pattern), recursive = True)), 100)

    def test_run_in_exec_mode(self):
      Application(self.dirname, self.pattern, '-e').run()
      self.assertEqual(len(glob.glob(os.path.join(self.dirname, '**', self.pattern), recursive = True)), 0)

    def tearDown(self):
        shutil.rmtree(self.dirname)

if __name__ == '__main__':
    unittest.main()
