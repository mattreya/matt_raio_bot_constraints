import unittest
import os
import shutil
from unittest.mock import patch
from slash_commands import quiz_me, generate_gns3_config

class TestQuizMe(unittest.TestCase):
    def tearDown(self):
        if os.path.exists("gns3_configs"):
            shutil.rmtree("gns3_configs")

    def test_quiz_me_pass(self):
        with patch('builtins.input', side_effect=['C', 'A', 'A']):
            result = quiz_me('multiple choice', 'OSPF')
            self.assertIn("You scored 100.00%", result)

    def test_quiz_me_fail(self):
        with patch('builtins.input', side_effect=['A', 'B', 'C']):
            result = quiz_me('multiple choice', 'OSPF')
            self.assertIn("You scored 0.00%", result)
            self.assertIn("GNS3 configuration files have been generated", result)

    def test_generate_gns3_config(self):
        result = generate_gns3_config("OSPF")
        self.assertEqual(result, "GNS3 configuration files have been generated in the 'gns3_configs' directory.")
        self.assertTrue(os.path.exists("gns3_configs"))
        self.assertTrue(os.path.exists("gns3_configs/R1_config.txt"))
        self.assertTrue(os.path.exists("gns3_configs/R2_config.txt"))

        with open("gns3_configs/R1_config.txt", "r") as f:
            r1_config = f.read()
            self.assertIn("hostname R1", r1_config)
            self.assertIn("ip address 10.0.0.1 255.255.255.252", r1_config)
            self.assertIn("router ospf 1", r1_config)

        with open("gns3_configs/R2_config.txt", "r") as f:
            r2_config = f.read()
            self.assertIn("hostname R2", r2_config)
            self.assertIn("ip address 10.0.0.2 255.255.255.252", r2_config)
            self.assertIn("router ospf 1", r2_config)

if __name__ == '__main__':
    unittest.main()
