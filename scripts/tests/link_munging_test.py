import unittest
import re

# Useful for testing:
#   https://regex101.com
#   https://regexr.com

def convert_github_url(v1):
    # https://github.com/isiahmeadows/github-limits
    whole_pattern = r"""\[(?:GitHub - )?([A-Za-z-\d)]+)/([a-z\d\-_.]+)(: [^]]+){0,1}]\(https://github.com/\1/\2/?\)"""
    github_repo_hyperlink = re.compile(whole_pattern)
    # [$1/**$2**](https://github.com/$1/$2)$3 on PyCharm
    return github_repo_hyperlink.sub(r'[\1/**\2**](https://github.com/\1/\2)\3', v1)


class LinkMungingTestCase(unittest.TestCase):
    def test_github_link_with_description(self):
        v1 = r'[GitHub - UserName/sample-repo-name: Sample:,_()- Description](https://github.com/UserName/sample-repo-name)'
        v2 = r'[UserName/**sample-repo-name**](https://github.com/UserName/sample-repo-name): Sample:,_()- Description'
        self.check_conversion(v1, v2)

    def test_github_link_with_description_but_no_github_prefix(self):
        v1 = r'[UserName/sample-repo-name: Sample:,_()- Description](https://github.com/UserName/sample-repo-name)'
        v2 = r'[UserName/**sample-repo-name**](https://github.com/UserName/sample-repo-name): Sample:,_()- Description'
        self.check_conversion(v1, v2)

    def test_github_link_with_dot_in_repo_name(self):
        v1 = r'[GitHub - chubin/cheat.sh: the only cheat sheet you need](https://github.com/chubin/cheat.sh)'
        v2 = r'[chubin/**cheat.sh**](https://github.com/chubin/cheat.sh): the only cheat sheet you need'
        self.check_conversion(v1, v2)

    def test_github_link_without_description(self):
        v1 = r'[GitHub - copperspice/doxypress](https://github.com/copperspice/doxypress)'
        v2 = r'[copperspice/**doxypress**](https://github.com/copperspice/doxypress)'
        self.check_conversion(v1, v2)

    def test_github_failing_link(self):
        v1 = r'[GitHub - maskiran/lightroom_collection_tree: Mirror the collection/collection sets in Lightroom onto the file system](https://github.com/maskiran/lightroom_collection_tree)'
        v2 = r'[maskiran/**lightroom_collection_tree**](https://github.com/maskiran/lightroom_collection_tree): Mirror the collection/collection sets in Lightroom onto the file system'
        self.check_conversion(v1, v2)

    def test_github_failing_link2(self):
        v1 = r'[GitHub - Dmitriy-Shulha/obsidian-css-snippets: Most common appearance solutions for Obsidian now in a single place. Initially collected by Klaas: https://forum.obsidian.md/t/how-to-achieve-css-code-snippets/8474](https://github.com/Dmitriy-Shulha/obsidian-css-snippets)'
        v2 = r'[Dmitriy-Shulha/**obsidian-css-snippets**](https://github.com/Dmitriy-Shulha/obsidian-css-snippets): Most common appearance solutions for Obsidian now in a single place. Initially collected by Klaas: https://forum.obsidian.md/t/how-to-achieve-css-code-snippets/8474'
        self.check_conversion(v1, v2)

    def test_github_with_trailing_slash(self):
        v1 = r'[pimoroni/flotilla-rockpool: The Flotilla web dashboard](https://github.com/pimoroni/flotilla-rockpool/)'
        v2 = r'[pimoroni/**flotilla-rockpool**](https://github.com/pimoroni/flotilla-rockpool): The Flotilla web dashboard'
        self.check_conversion(v1, v2)

    def test_github_with_yet_another_unrecognised_character_in_description(self):
        v1 = r'[GitHub - arnemertz/commandline-videostore-cpp: C++ port of https://github.com/rickjanda/commandline-videostore](https://github.com/arnemertz/commandline-videostore-cpp)'
        v2 = r'[arnemertz/**commandline-videostore-cpp**](https://github.com/arnemertz/commandline-videostore-cpp): C++ port of https://github.com/rickjanda/commandline-videostore'
        self.check_conversion(v1, v2)

    def check_conversion(self, v1, v2):
        self.assertEqual(v2, convert_github_url(v1))


if __name__ == '__main__':
    unittest.main()
