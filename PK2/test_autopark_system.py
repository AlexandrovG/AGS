import unittest
from autopark_system import AutoparkSystem

class TestAutoparkSystem(unittest.TestCase):
    
    def setUp(self):
        self.system = AutoparkSystem()
    
    def test_task_g1_autoparks_starting_with_A(self):
        result = self.system.task_g1()
        
        self.assertIsInstance(result, dict)
        
        expected_parks = ['Автопарк Северный', 'Аэропортный автопарк']
        for park in expected_parks:
            self.assertIn(park, result)
        
        self.assertEqual(result['Автопарк Северный'], ['Иванов'])
        self.assertEqual(result['Аэропортный автопарк'], ['Антонов'])
        
        self.assertNotIn('Таксопарк Центральный', result)
        self.assertNotIn('Грузовой парк', result)
    
    def test_task_g2_max_salary_per_autopark(self):
        result = self.system.task_g2()
        
        self.assertIsInstance(result, list)
        
        for item in result:
            self.assertIsInstance(item, tuple)
            self.assertEqual(len(item), 2)
            self.assertIsInstance(item[0], str)
            self.assertIsInstance(item[1], int)
        
        salaries = [item[1] for item in result]
        self.assertEqual(salaries, sorted(salaries, reverse=True))
        
        result_dict = dict(result)
        self.assertEqual(result_dict['Таксопарк Центральный'], 55000)
        self.assertEqual(result_dict['Аэропортный автопарк'], 52000)
        self.assertEqual(result_dict['Грузовой парк'], 47000)
    
    def test_task_g3_all_connections_sorted(self):
        result = self.system.task_g3()
        
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        
        for item in result:
            self.assertIsInstance(item, tuple)
            self.assertEqual(len(item), 3)
            self.assertIsInstance(item[0], str)
            self.assertIsInstance(item[1], int)
            self.assertIsInstance(item[2], str)
        
        autopark_names = [item[2] for item in result]
        self.assertEqual(autopark_names, sorted(autopark_names))
        
        drivers_by_park = {}
        for driver, salary, park in result:
            if park not in drivers_by_park:
                drivers_by_park[park] = []
            drivers_by_park[park].append(driver)
        
        self.assertIn('Иванов', drivers_by_park.get('Автобусный парк', []))
        self.assertIn('Сидоров', drivers_by_park.get('Автопарк Северный', []))
        self.assertIn('Алексеев', drivers_by_park.get('Автобусный парк', []))
    
    def test_get_one_to_many_connections(self):
        connections = self.system.get_one_to_many()
        
        self.assertIsInstance(connections, list)
        self.assertGreater(len(connections), 0)
        
        for connection in connections:
            self.assertEqual(len(connection), 3)
            self.assertIsInstance(connection[0], str)
            self.assertIsInstance(connection[1], int)
            self.assertIsInstance(connection[2], str)
    
    def test_get_many_to_many_connections(self):
        connections = self.system.get_many_to_many()
        
        self.assertIsInstance(connections, list)
        self.assertGreater(len(connections), 0)
        
        for connection in connections:
            self.assertEqual(len(connection), 3)
            self.assertIsInstance(connection[0], str)
            self.assertIsInstance(connection[1], int)
            self.assertIsInstance(connection[2], str)

if __name__ == '__main__':
    unittest.main()