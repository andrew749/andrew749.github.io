import markdown
import frontmatter

def _generateHTMLFromMarkdown(text):
    """
    Args:
        text: the plaintext data in markdown format

    Return:
        generated html code
    """
    html = markdown.markdown(text)
    return html

def _generateHTMLFileFromMarkdown(input_file, output_file_name):
    """
    Args:
        input_file = path of file to generate markdown from
        output_file_name = filename for generated html
    Return:
        generated html
    """
    input_file = codecs.open(input_file, mode="r", encoding="utf-8")
    text = input_file.read()
    html = _generateHTMLFromMarkdown(text)
    output_file = codecs.open("generated_content/{}.html".format(output_file_name),
                              "w",
                              encoding="utf-8",
                              errors="xmlcharrefreplace"
    )
    output_file.write(html)
    return html

def _getMarkdownFrontMatter(text):
    """
    Args:
        text: string of markdown

    Return:
        frontmatter in json format
    """
    data = frontmatter.loads(text)
    return data

class MarkdownObject(object):
    """
    Markdown object.

    Facilitates the creation of an in memory object with all the data encapsulated in a markdown file

    """
    def __init__(self, text):
        frontmatter =  _getMarkdownFrontMatter(text)
        self.metadata = frontmatter
        self.content = _generateHTMLFromMarkdown(frontmatter.content)

    @classmethod
    def markdownObjectFromFile(cls, file_path):
        """
        Args:
            file_path: path of a file to parse

        Return:
            MarkdownObject of the parsed file
        """
        file = open(file_path, 'r')
        md_object = MarkdownObject(file.readlines())
        file.close()
        return md_object

