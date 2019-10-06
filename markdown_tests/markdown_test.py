import unittest
from my_markdown import markdown


class MyTestCase(unittest.TestCase):
    def test_markdown(self):
        mdFile = open('testFile.md',mode='r')
        md = mdFile.read()
        mdFile.close()
        out = markdown.markdown_to_html(md)
        print("Markdown: ")
        print(md)
        print("Html:")
        print(out)




if __name__ == '__main__':
    unittest.main()
