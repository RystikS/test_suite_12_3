from pickle import FALSE

from runner import Runner
from runner_and_tournament import *
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(False,'')
    def test_walk(self):
        walker1 = Runner('blade_walker')
        for i in range(10):
            walker1.walk()
        self.assertEqual(walker1.distance,50)

    @unittest.skipIf(False,'')
    def test_run(self):
        runner2 = Runner('blade_runner')
        for i in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    @unittest.skipIf(False,'')
    def test_challenge(self):
        walker = Runner('walker_1')
        runner = Runner('runner_2')
        for i in range(10):
            walker.run()
        for i in range(10):
            runner.walk()
        self.assertNotEqual(walker.distance, runner.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True
    all_results = {}
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner("Усэйн", 10)
        self.runner_2 = Runner("Андрей", 9)
        self.runner_3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        pass

    @unittest.skipUnless(False, 'Тесты в этом кейсе заморожены')
    def test_tour_1(self):
        tournament = Tournament(90, self.runner_1, self.runner_3)
        results = tournament.start()
        for runner_position in results.keys():
            winner_name = results[runner_position].name
            self.all_results[runner_position] = winner_name
        print(self.all_results)
        self.assertTrue(self.all_results[max(results.keys())] == "Ник")

    @unittest.skipUnless(False, 'Тесты в этом кейсе заморожены')
    def test_tour_2(self):
        tournament = Tournament(90, self.runner_2, self.runner_3)
        results = tournament.start()
        for runner_position in results.keys():
            winner_name = results[runner_position].name
            self.all_results[runner_position] = winner_name
        print(self.all_results)
        self.assertTrue(self.all_results[max(results.keys())] == "Ник")

    @unittest.skipUnless(False, 'Тесты в этом кейсе заморожены')
    def test_tour_3(self):
        tournament = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        results = tournament.start()
        for runner_position in results.keys():
            winner_name = results[runner_position].name
            self.all_results[runner_position] = winner_name
        print(self.all_results)
        self.assertTrue(self.all_results[max(results.keys())] == "Ник")

if __name__ == "__main__":
    unittest.main()
