import unittest
import json
import sys

## rename record_gpu_usage to record_gpu_usage.py to run tests
import record_gpu_usage
from unittest.mock import patch
import os

if sys.version_info[0] < 3:
    import ConfigParser
else:
    import configparser as ConfigParser

class TestStringMethods(unittest.TestCase):

    def test_to_json(self):
        rows = [["a", "b", "c", "d", "e", "f", "g"]]
        actual = json.loads(record_gpu_usage.to_json(rows))
        self.assertEqual('a', actual[0]['serial'])
        self.assertEqual('b', actual[0]['pid'])
        self.assertEqual('c', actual[0]['gpuUtilization'])
        self.assertEqual('d', actual[0]['memoryUtilization'])
        self.assertEqual('e', actual[0]['maxMemoryUsage'])
        self.assertEqual('f', actual[0]['time'])
        self.assertEqual('g', actual[0]['startTime'])

    def test_get_config(self):
        config = ConfigParser.ConfigParser()
        config.add_section('CLUSTER')
        config.add_section('DATABASE')
        config.set('CLUSTER', 'name', 'test_cluster')
        config.set('DATABASE', 'user', 'bob')
        config.set('DATABASE', 'password', 'secret')
        cluster, db = record_gpu_usage.get_config(config)
        self.assertEqual(cluster, 'test_cluster')
        self.assertEqual(db, {'user':'bob', 'password':'secret'})

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    @patch("record_gpu_usage.nvmlDeviceGetHandleByIndex")
    @patch("record_gpu_usage.nvmlDeviceClearAccountingPids")
    def test_ClearAccounting(self, b, gethandle):
        os.environ['CUDA_VISIBLE_DEVICES'] = "1,3,5"
        record_gpu_usage.ClearAccounting()
        actual = [x[0][0] for x in gethandle.call_args_list]
        self.assertEqual(actual, [1, 3, 5])

    def test_available_devices(self):
        os.environ['CUDA_VISIBLE_DEVICES'] = "1,3,5"
        self.assertEqual([1, 3, 5], list(record_gpu_usage.available_devices()))

if __name__ == "__main__":
    unittest.main()

