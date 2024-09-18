import unittest
from tests_.functionalTests import FunctionalTests
from tests_.performanceTests import PerformanceTests
from tests_.boundaryTests import BoundaryTests


class TestSuites:
    """
        This class provides methods to create test suites for various testing scenarios, allowing for organized and
        purpose-driven test case grouping.
    """
    def get_functional_tests_suite(self):
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(FunctionalTests))
        return suite

    def get_performance_tests_suite(self):
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(PerformanceTests))
        return suite

    def get_boundary_tests_suite(self):
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(BoundaryTests))
        return suite

    def get_regression_suite(self):
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(FunctionalTests))
        suite.addTest(unittest.makeSuite(PerformanceTests))
        suite.addTest(unittest.makeSuite(BoundaryTests))
        return suite
