---
name: "Mission 2b: Fix Route Planner"  
about: "Restore and enhance the route planner functionality for Codetropolis navigation."  
title: "🔧 Fix and Complete the Route Planner"  
labels: ["bug", "enhancement"]
assignees: ""
---

# 🔧 Fix and Complete the Codetropolis Route Planner  

The citizens of Codetropolis are lost—literally! The city’s navigation system is down, leaving everyone unable to find their way. Your mission is to restore order by fixing and completing the route planner functionality.  

---

## 🗺️ Mission Objectives  

1. **Debug the `get_location` Function**:  
   - Ensure the function returns accurate coordinates for valid locations.  
   - Add clear error messages for invalid or missing locations.  

2. **Complete the `plan_route` Function**:  
   - Implement a method to calculate the distance between two locations.  
   - Hint: Use the **Haversine formula** for accurate distance calculations.  

---

## 🛠️ Known Issues  

- **Missing Location Lookup**: Some locations are not returning proper coordinates.  
- **Broken Route Planner**: The route planning function is incomplete and doesn’t calculate distances.  

---

## 💡 Implementation Example  

- **Debug `get_location`**: Return coordinates like `(40.7148, -74.0059)` or a meaningful error for missing locations.  
- **Plan Route**: Use the Haversine formula to calculate the distance in kilometers or miles.  
