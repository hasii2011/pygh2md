
from unittest import TestSuite
from unittest import main as unitTestMain

from codeallybasic.UnitTestBase import UnitTestBase

from pygh2md.GitHubAdapter import GHIssues
from pygh2md.GitHubAdapter import GitHubAdapter
from pygh2md.exceptions.InvalidDateFormatException import InvalidDateFormatException


class TestGitHubAdapter(UnitTestBase):
    """
    Auto generated by the one and only:
        Gato Malo – Humberto A. Sanchez II
        Generated: 14 March 2024
    """
    """
        I don't care about:

            DeprecationWarning: Argument login_or_token is deprecated, please use auth=github.Auth.Token(...) instead
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        super().setUp()
        import warnings

        warnings.filterwarnings(action="ignore", message="Argument", category=DeprecationWarning)

    def tearDown(self):
        super().tearDown()

    def testConstruction(self):
        gitHubAdapter: GitHubAdapter = GitHubAdapter()

        self.assertIsNotNone(gitHubAdapter, '')

    def testAPI(self):

        gitHubAdapter: GitHubAdapter = GitHubAdapter()
        ghIssues: GHIssues = gitHubAdapter.getClosedIssues(repositorySlug='hasii2011/TestRepository', sinceDate='2024-03-15')

        self.assertEqual(1, len(ghIssues), 'There can be only 1')

    def testInvalidDateFormat(self):
        gitHubAdapter: GitHubAdapter = GitHubAdapter()

        with self.assertRaises(InvalidDateFormatException):
            gitHubAdapter.getClosedIssues(repositorySlug='hasii2011/TestRepository', sinceDate='66-03-15')


def suite() -> TestSuite:
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestGitHubAdapter))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
