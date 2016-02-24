# Off Centers
An exploration of the geographic balance of counties

In an area where the population is evenly and symmetrically distributed, the geographic center and the center of population will be close together. In an area where people live clustered on one corner or edge, these points will be far apart. This visualization uses the linear distance between these two points to explore the most balanced and the least balanced counties (and county-like units) in the United States.

## Explanation

See the [blog post](http://viewshed.matinic.us/2016/02/24/997/) which explains more about this project's concept.

## Data sources

The population centroid data comes from the Census Bureau's [Mean Centers of Population, 2010](https://www.census.gov/geo/reference/centersofpop.html).

Geographic centroids were computed using QGIS on the Census Bureau's [20m County Boundaries](https://www.census.gov/geo/maps-data/data/cbf/cbf_counties.html) shapefile.

Raw distance is calculated in meters by `data/calculator.py` using the Vincenty distance algorithm in [`geopy`](https://pypi.python.org/pypi/geopy). Weighted distance is the raw distance divided by the square root of area.

This data was massaged and combined into `data/output-data.csv`, and an `id` field in the format SSCCC was generated, where SS = State FIP; CCC = County FIP.

The 20m County Boundaries shapefile was then transformed into a TopoJSON using `ogr2ogr` and `topojson`, again generating an `id` field in the SSCCC format.

## Known issues

* The Aleutians West unit causes all sorts of headaches for QGIS, d3, and Leaflet alike due to the fact that it crosses -180 latitude. It's been removed for now.
* Need to implement a rank-number in the list
