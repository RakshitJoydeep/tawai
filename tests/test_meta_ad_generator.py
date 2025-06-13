import csv
from io import StringIO
import unittest

from meta_ad_generator import generate_creatives


class TestMetaAdGenerator(unittest.TestCase):
    def test_generate_creatives_adds_column(self):
        csv_data = (
            "business,product,description,audience,offer,cta\n"
            "Acme,Widget,Bright and shiny,DIYers,20% off,Buy now\n"
        )
        reader = csv.DictReader(StringIO(csv_data))
        rows = list(reader)
        result = generate_creatives(rows)
        self.assertIn('creative', result[0])
        self.assertTrue(result[0]['creative'])


if __name__ == '__main__':
    unittest.main()
