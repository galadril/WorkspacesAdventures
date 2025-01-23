# maps.py

MAP_DATA = {
    "locations": [
        {"name": "City Hall", "coordinates": (40.7128, -74.0060)},
        {"name": "Codetropolis Park", "coordinates": (40.7138, -74.0050)},
        {"name": "Hovercar Garage", "coordinates": (40.7120, -74.0045)},
    ]
}

def get_location(name):
    """
    Retrieve the coordinates of a location by name.
    """
    for location in MAP_DATA["locations"]:
        if location["name"].lower() == name.lower():
            return location["coordinates"]
    return None  # Intentional issue: Returns None without explanation


def plan_route(start, end):
    """
    Plan a route between two locations. Currently incomplete.
    """
    start_coords = get_location(start)
    end_coords = get_location(end)

    if not start_coords or not end_coords:
        raise ValueError(f"One or both locations not found: {start}, {end}")
    
    # TODO: Calculate distance between coordinates (use Haversine formula)
    return f"Route planned from {start} to {end}. Distance calculation coming soon!"


if __name__ == "__main__":
    try:
        print(plan_route("City Hall", "Codetropolis Park"))
    except Exception as e:
        print("Error planning route:", e)
