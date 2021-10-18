import unittest
import re



def convert_github_url(v1):
    # https://github.com/isiahmeadows/github-limits
    github_repo_hyperlink = re.compile(r"""\[GitHub\ -\ ([a-z\d)]+)/([a-z\d.-]+)(:\ [A-Za-z\d :.\-,_()]+){0,1}]\(https://github.com/\1/\2\)""")
    return github_repo_hyperlink.sub(r'[\1/**\2**](https://github.com/\1/\2)\3', v1)


class LinkMungingTestCase(unittest.TestCase):
    def test_github_link_with_description(self):
        v1 = r'[GitHub - username/sample-repo-name: Sample:,_()- Description](https://github.com/username/sample-repo-name)'
        v2 = r'[username/**sample-repo-name**](https://github.com/username/sample-repo-name): Sample:,_()- Description'
        self.assertEqual(v2, convert_github_url(v1))  # add assertion here

    def test_github_link_without_description(self):
        v1 = r'[GitHub - copperspice/doxypress](https://github.com/copperspice/doxypress)'
        v2 = r'[copperspice/**doxypress**](https://github.com/copperspice/doxypress)'
        self.assertEqual(v2, convert_github_url(v1))  # add assertion here


if __name__ == '__main__':
    unittest.main()
