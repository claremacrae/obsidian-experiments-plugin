import unittest
import re



def convert_github_url(v1):
    return r'[username/**sample-repo-name**](https://github.com/username/sample-repo-name): Sample:,- Description'


class LinkMungingTestCase(unittest.TestCase):
    def test_github_links(self):
        v1 = r'[GitHub - username/sample-repo-name: Sample:,- Description](https://github.com/username/sample-repo-name)'
        v2 = r'[username/**sample-repo-name**](https://github.com/username/sample-repo-name): Sample:,- Description'

        self.assertEqual(v2, convert_github_url(v1))  # add assertion here


if __name__ == '__main__':
    unittest.main()
