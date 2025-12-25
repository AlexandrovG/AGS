import unittest
from unittest.mock import Mock, patch
from main import *

class TestCafeSystem(unittest.TestCase):
    def setUp(self):
        self.cafe = CafeOrderSystem()
        self.test_order = Order()
        self.pizza = Pizza("Тестовая", 100, "small")
        self.drink = Drink("Тестовый", 50, 0.5)
    
    def test_pizza_creation(self):
        self.assertEqual(self.pizza.name, "Тестовая")
        self.assertEqual(self.pizza.price, 100)
        self.assertEqual(self.pizza.size, "small")
    
    def test_order_add_item(self):
        self.test_order.add_item(self.pizza)
        self.assertEqual(len(self.test_order.items), 1)
        self.assertEqual(self.test_order.items[0].name, "Тестовая")
    
    def test_order_total_price(self):
        self.test_order.add_item(self.pizza)
        self.test_order.add_item(self.drink)
        self.assertEqual(self.test_order.total_price, 150)
    
    def test_observer_addition(self):
        observer = Mock()
        self.test_order.add_observer(observer)
        self.assertEqual(len(self.test_order._observers), 1)
    
    def test_observer_notification(self):
        observer = Mock()
        self.test_order.add_observer(observer)
        self.test_order.change_status("готовится")
        observer.update.assert_called_once_with(self.test_order)
    
    def test_factory_method_pizza(self):
        factory = PizzaFactory()
        pizza = factory.create_item("Тест", 200, "large")
        self.assertIsInstance(pizza, Pizza)
        self.assertEqual(pizza.size, "large")
    
    def test_facade_combo_order(self):
        order = self.cafe.create_combo_order("Тестовый Клиент")
        self.assertEqual(order.status, "выдан")
        self.assertEqual(len(order.items), 3)
    
    @patch('main.KitchenObserver')
    def test_mock_kitchen_in_facade(self, MockKitchen):
        mock_kitchen = MockKitchen.return_value
        self.cafe.kitchen = mock_kitchen
        order = self.cafe.create_combo_order("Тест")
        self.assertTrue(mock_kitchen.update.called)
    
    def test_menu_item_preparation(self):
        result = self.pizza.prepare()
        self.assertIn("готов", result.lower())

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCafeSystem)
    runner = unittest.TextTestRunner(verbosity=2)
    
    print("=" * 60)
    print("ЗАПУСК МОДУЛЬНЫХ ТЕСТОВ")
    print("=" * 60)
    
    result = runner.run(suite)
    
    print(f"\nРезультаты тестов:")
    print(f"Всего тестов: {result.testsRun}")
    print(f"Пройдено: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Провалено: {len(result.failures)}")
    print(f"Ошибок: {len(result.errors)}")
    
    return result

if __name__ == "__main__":
    run_tests()