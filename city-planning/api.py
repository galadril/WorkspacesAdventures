from flask import Flask, request, jsonify
from maps import get_location, plan_route, get_all_locations

app = Flask(__name__)

@app.route("/api/location", methods=["GET"])
def location_lookup():
    """
    Get the coordinates of a location by name.
    """
    location_name = request.args.get("name")
    if not location_name:
        return jsonify({"error": "Missing 'name' parameter"}), 400
    
    coords = get_location(location_name)
    if coords:
        return jsonify({"name": location_name, "coordinates": coords})
    return jsonify({"error": "Location not found"}), 404


@app.route("/api/locations", methods=["GET"])
def all_locations():
    """
    Get a list of all available locations.
    """
    locations = get_all_locations()
    return jsonify({"locations": locations})


@app.route("/api/route", methods=["GET"])
def route_planner():
    """
    Plan a route between two locations.
    """
    start = request.args.get("start")
    end = request.args.get("end")
    if not start or not end:
        return jsonify({"error": "Missing 'start' or 'end' parameter"}), 400
    
    try:
        route = plan_route(start, end)
        return jsonify({"route": route})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True, port=5001)
