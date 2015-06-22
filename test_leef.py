import unittest
import leef


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.l = leef.LEEF_Logger("TestVendor", "TestName", leef.__version__)

    def test_delimeter_error(self):
        with self.assertRaises(ValueError) as cm:
            leef.LEEF_Logger("TestVendor", "TestName", leef.__version__,
                             delimiter="a")

    def testLogger(self):
        self.assertEqual(self.l.product_vendor, "TestVendor")
        self.assertEqual(self.l.product_name, "TestName")
        self.assertEqual(self.l.product_version, leef.__version__)

    def testEventString(self):
        keys = {"key1": "value1",
                "key2": "value2",
                "key3": "value3",
                }

        event_id = 1989

        # Proper Header
        header = "LEEF:1.0|TestVendor|TestName|{0}|{1}|". \
                 format(leef.__version__,
                        str(event_id))

        # Expected keys value string
        attributes = "key1=value1\tkey2=value2\tkey3=value3"

        expected = header + attributes

        test_string = self.l.logEvent("1989", keys)
        self.assertEqual(test_string, expected)


if __name__ == "__main__":
    unittest.main()
