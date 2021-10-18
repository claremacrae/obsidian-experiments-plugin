import unittest
import re



def convert_github_url(v1):
    # https://github.com/isiahmeadows/github-limits
    github_repo_hyperlink = re.compile(r"""
                        \[ # Open a markdown link
                        GitHub\ -\                          # GitHub prefix to page title
                        ([a-z\d)]+)                         # User/organisation name
                        /
                        ([a-z\d.-]+)                        # Repo name
                        (:\ [A-Za-z\d :.\-,]+)]            # Description of repo
                       \(https://github.com/\1/\2\)""",     # Repo URL
                       re.VERBOSE)
    return github_repo_hyperlink.sub(r'[\1/**\2**](https://github.com/\1/\2)\3', v1)


class LinkMungingTestCase(unittest.TestCase):
    def test_github_links(self):
        v1 = r'[GitHub - username/sample-repo-name: Sample:,- Description](https://github.com/username/sample-repo-name)'
        v2 = r'[username/**sample-repo-name**](https://github.com/username/sample-repo-name): Sample:,- Description'

        self.assertEqual(v2, convert_github_url(v1))  # add assertion here


if __name__ == '__main__':
    unittest.main()
