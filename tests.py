import unittest
import gpu_accounting
import ConfigParser

class TestStringMethods(unittest.TestCase):

    def test_to_json(self):
        rows = [["a", "b", "c", "d", "e", "f"]]
        expected = """[{"pid": "b", "time": "f", "gpuUtilization": "c", "serial": "a", "maxMemoryUsage": "e", "memoryUtilization": "d"}]"""
        self.assertEqual(gpu_accounting.to_json(rows), expected)

    def test_get_config(self):
        config = ConfigParser.ConfigParser()
        config.add_section('CLUSTER')
        config.add_section('DATABASE')
        config.set('CLUSTER', 'name', 'test_cluster')
        config.set('DATABASE', 'user', 'bob')
        config.set('DATABASE', 'password', 'secret')
        cluster, db = gpu_accounting.get_config(config)
        self.assertEqual(cluster, 'test_cluster')
        self.assertEqual(db, {'user':'bob', 'password':'secret'})

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == "__main__":
    unittest.main()

