import unittest
import re



def convert_github_url(v1):
    # username: https://github.com/shinnn/github-username-regex
    p = re.compile(r'\[GitHub - ([a-z\d)]+)\/([a-z\d.-]+)(: [A-Za-z\d :\.\-,]+)]\(https:\/\/github.com\/\1\/\2\)')
    return p.sub(r'[\1/**\2**](https://github.com/\1/\2)\3', v1)


class LinkMungingTestCase(unittest.TestCase):
    def test_github_links(self):
        v1 = r'[GitHub - username/sample-repo-name: Sample:,- Description](https://github.com/username/sample-repo-name)'
        v2 = r'[username/**sample-repo-name**](https://github.com/username/sample-repo-name): Sample:,- Description'

        self.assertEqual(v2, convert_github_url(v1))  # add assertion here


if __name__ == '__main__':
    unittest.main()
