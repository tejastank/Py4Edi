import unittest

from Fixtures import FixtureReader, FixtureFiles


class TestParsingMultipleGroups(unittest.TestCase):
    def setUp(self):
        self.multiple_groups_doc = FixtureReader().read_edi_file(FixtureFiles.multiple_groups_file)

    def test_validity_of_parsed_document(self):
        """Ensure the document passes the validator"""
        self.assertTrue(self.multiple_groups_doc.validate().is_document_valid())

    def test_parsing_multiple_groups(self):
        """Test parsing multiple groups by ensuring we can get their control id"""
        self.assertEqual("987654321", self.multiple_groups_doc.interchange.groups[0].header.gs06.content)
        self.assertEqual("987654322", self.multiple_groups_doc.interchange.groups[1].header.gs06.content)

    def test_parsing_transactions_in_multiple_groups(self):
        """Test parsing transactions under multiple groups by ensuring we can get the transaction control number"""
        self.assertEqual("000000003",
                         self.multiple_groups_doc.interchange.groups[0].transaction_sets[2].header.st02.content)
        self.assertEqual("000000006",
                         self.multiple_groups_doc.interchange.groups[1].transaction_sets[2].header.st02.content)


if __name__ == '__main__':# pragma: no cover
    unittest.main()
