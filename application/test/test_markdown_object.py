import unittest
import os
import shutil

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
		# temporary folder to hold intermittent operations
		os.mkdir("tmp/")

	def tearDown(self):
		shutil.rmtree("tmp/")

	def test_getMarkdownFrontMatter(self):
		data = markdown_object._getMarkdownFrontMatter(sample_markdown)
		self.assertEqual(data["title"], "Test title")
		self.assertEqual(data["subtitle"], "Test subtitle")
		self.assertEqual(data["date"], "Test date")

	def test_generateHTMLFileFromMarkdown(self):
		markdown_object._generateHTMLFileFromMarkdown("projects/chordi.json", "tmp/chordi.html")
		self.assertGreater(os.path.getsize("tmp/chordi.html"), 0)
		self.assertTrue(os.path.exists("tmp/chordi.html"))

if __name__ == "__main__":
	unittest.main()