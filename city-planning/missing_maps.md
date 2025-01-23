# Missing Maps: Codetropolis Navigation System

The citizens of Codetropolis are lost—literally! The navigation system is down, and people can’t find their way. 

---

## Known Issues
1. **Missing location lookup**: Some locations are not returning proper coordinates.
2. **Broken route planner**: The route planning function is incomplete and doesn’t calculate distances.
3. **Outdated map data**: The current map only contains three locations. New landmarks are needed!

---

## Your Mission
1. Debug the `get_location` function to ensure it returns clear errors when a location isn’t found.
2. Complete the `plan_route` function by calculating the distance between two locations (hint: Use the Haversine formula).
3. Add at least two new locations to the `MAP_DATA` dictionary.

---

### Bonus Challenge
- Build a fun Easter egg: If someone searches for "Atlantis," return a random underwater location!
