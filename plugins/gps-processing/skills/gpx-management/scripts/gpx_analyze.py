#!/usr/bin/env python3
"""GPX file analyzer — computes distance (km, miles, nm), point count, and metadata."""

import sys
import xml.etree.ElementTree as ET
import math
import shutil
import subprocess
from datetime import datetime

# GPX namespaces
NS = {
    "gpx11": "http://www.topografix.com/GPX/1/1",
    "gpx10": "http://www.topografix.com/GPX/1/0",
}


def haversine(lat1, lon1, lat2, lon2):
    """Distance between two GPS points in km using the Haversine formula."""
    R = 6371.1  # Earth radius in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(math.radians(lat1))
        * math.cos(math.radians(lat2))
        * math.sin(dlon / 2) ** 2
    )
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def detect_namespace(root):
    """Return the namespace URI used in the GPX file."""
    tag = root.tag
    if tag.startswith("{"):
        return tag[1 : tag.index("}")]
    return ""


def parse_gpx(filepath):
    """Parse a GPX file and return analysis results."""
    tree = ET.parse(filepath)
    root = tree.getroot()
    ns_uri = detect_namespace(root)
    ns = {"g": ns_uri} if ns_uri else {}

    prefix = "g:" if ns else ""

    # Track name and type
    track_name = None
    track_type = None
    trk = root.find(f".//{prefix}trk", ns)
    if trk is not None:
        name_el = trk.find(f"{prefix}name", ns)
        type_el = trk.find(f"{prefix}type", ns)
        track_name = name_el.text if name_el is not None else None
        track_type = type_el.text if type_el is not None else None

    # Collect all trackpoints
    points = []
    for trkpt in root.iter(f"{{{ns_uri}}}trkpt" if ns_uri else "trkpt"):
        lat = float(trkpt.get("lat"))
        lon = float(trkpt.get("lon"))
        time_el = trkpt.find(f"{prefix}time", ns)
        timestamp = time_el.text if time_el is not None else None
        points.append((lat, lon, timestamp))

    # Compute total distance
    total_km = 0.0
    for i in range(1, len(points)):
        total_km += haversine(points[i - 1][0], points[i - 1][1], points[i][0], points[i][1])

    total_miles = total_km * 0.621371
    total_nm = total_km * 0.539957

    # Time range
    start_time = points[0][2] if points else None
    end_time = points[-1][2] if points else None

    return {
        "track_name": track_name,
        "track_type": track_type,
        "total_points": len(points),
        "distance_km": round(total_km, 3),
        "distance_miles": round(total_miles, 3),
        "distance_nm": round(total_nm, 3),
        "start_time": start_time,
        "end_time": end_time,
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: gpx_analyze.py <gpx-file>", file=sys.stderr)
        sys.exit(1)

    filepath = sys.argv[1]

    # Parse and analyze
    results = parse_gpx(filepath)

    # Output
    print(f"Track Name:              {results['track_name'] or 'N/A'}")
    print(f"Activity Type:           {results['track_type'] or 'N/A'}")
    print(f"Total Points:            {results['total_points']}")
    print(f"Distance (km):           {results['distance_km']}")
    print(f"Distance (miles):        {results['distance_miles']}")
    print(f"Distance (nautical mi):  {results['distance_nm']}")
    print(f"Start Time:              {results['start_time'] or 'N/A'}")
    print(f"End Time:                {results['end_time'] or 'N/A'}")


if __name__ == "__main__":
    main()
