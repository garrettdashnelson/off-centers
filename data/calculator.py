from geopy.distance import vincenty
import csv
from math import sqrt


filename = 'input-data.csv'
outfile = 'output-data.csv'

fieldnames = ['StateFIP','CountyFIP','CountyName','StateName','geocentroid','popcentroid','difference','area','population','WeightedDifference']

writer = csv.DictWriter( open(outfile,'w'), fieldnames )
writer.writeheader()

with open(filename,'r') as csvSrc:
	reader = csv.DictReader(csvSrc)
	for row in reader:
		geocentroid = ( float(row['geoy']), float(row['geox']) )
		popcentroid = ( float(row['popy']), float(row['popx']) )
		
		difference = vincenty(geocentroid, popcentroid).meters

		metricArea = float(row['censusarea']) * 2.589988
		weightedDifference = difference / sqrt(metricArea)

		thisLine = { 'StateFIP': row['state'], 'CountyFIP': row['county'], 'CountyName': row['name'], 'StateName': row['statename'], 'geocentroid': geocentroid, 'popcentroid': popcentroid, 'difference': difference, 'area': metricArea, 'population': row['pop'], 'WeightedDifference': weightedDifference }
		writer.writerow(thisLine)