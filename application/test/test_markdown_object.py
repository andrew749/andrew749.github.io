import unittest
import os

from application import markdown_object

sample_markdown = \
"---\n" \
"title: Test title\n" \
"subtitle: Test subtitle\n" \
"date: Test date\n" \
"---\n" \
"#Title\n" \
"This is a test markdown file\n"

class MarkdownObjectTest(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_getMarkdownFrontMatter(self):
		data = markdown_object._getMarkdownFrontMatter(sample_markdown)
		self.assertEqual(data["title"], "Test title")
		self.assertEqual(data["subtitle"], "Test subtitle")
		self.assertEqual(data["date"], "Test date")

if __name__ == "__main__":
	unittest.main()