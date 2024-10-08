from tests_.common_.suites_.testSuites import TestSuites
from common_.reporters_.reporters import Reporters

if __name__ == '__main__':
    testSuites = TestSuites()
    suite = testSuites.get_performance_tests_suite()
    reporter = Reporters()
    runner = reporter.get_html_test_runner("Performance Suite", "Performance Suite Description")
    runner.run(suite)
