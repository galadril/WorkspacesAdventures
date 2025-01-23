# test_maps.py

import unittest
from maps import get_location, plan_route

class TestMaps(unittest.TestCase):
    def test_get_location_valid(self):
        self.assertEqual(get_location("City Hall"), (40.7128, -74.0060))
    
    def test_get_location_invalid(self):
        self.assertIsNone(get_location("Atlantis"))
    
    def test_plan_route_valid(self):
        route = plan_route("City Hall", "Codetropolis Park")
        self.assertIn("Route planned from City Hall to Codetropolis Park", route)
    
    def test_plan_route_invalid(self):
        with self.assertRaises(ValueError):
            plan_route("City Hall", "Atlantis")


if __name__ == "__main__":
    unittest.main()
