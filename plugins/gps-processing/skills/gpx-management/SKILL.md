---
name: gpx-management
description: 'Analyze GPX files: calculate total distance (km, miles, nautical miles), count trackpoints, extract metadata. Use for GPS track analysis, route statistics, GPX file inspection.'
argument-hint: Path to GPX file(s) to analyze
---

# GPX File Management & Analysis

## When to Use

- User asks to analyze a GPX file (distance, points, stats)
- User wants distance in km, miles, or nautical miles
- User asks about a GPS track, route, or waypoints
- User provides a `.gpx` file attachment or path

## Procedure


### Step 1 — Run the analysis script

Execute the analysis script on the target GPX file:

```sh
python3 ./scripts/gpx_analyze.py <path-to-gpx-file>
```

The [analysis script](./scripts/gpx_analyze.py) computes:

- **Total trackpoints** across all segments
- **Total distance** using the Haversine formula
- **Distance in km, miles, and nautical miles**
- **Track name and type** from metadata
- **Start/end times** if timestamps are present


### Step 2 — Present results

Display a summary table:

| Metric | Value |
|--------|-------|
| Track Name | ... |
| Activity Type | ... |
| Total Points | ... |
| Distance (km) | ... |
| Distance (miles) | ... |
| Distance (nautical miles) | ... |
| Start Time | ... |
| End Time | ... |

## Distance Conversion Reference

- 1 km = 0.621371 miles
- 1 km = 0.539957 nautical miles
- Haversine formula uses Earth radius = 6,371 km

## Notes

- GPX files may contain multiple `<trk>` elements and `<trkseg>` segments — sum all segments
- Namespace-aware XML parsing is required (default namespace: `http://www.topografix.com/GPX/1/1`)
- The script handles GPX 1.1 and 1.1 namespaces
