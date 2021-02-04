#rain stats

def maxRain(rainfall):
	maxRainMonth = rainfall.index(max(rainfall)) + 1
	print("\nHighest rainfall was %d in month %d." % (max(rainfall), maxRainMonth))
	
def minRain(rainfall):
	minRainMonth = rainfall.index(min(rainfall)) + 1
	print("\nLeast rainfall was %d in month %d." % (min(rainfall), minRainMonth))
	

def main():

	rainfall = []
	totalRain = 0
	
	for i in range(0, 12):
		rainInMonth = int(input("Enter rainfall for month %d in mm: " % int(i + 1)))
		rainfall.append(rainInMonth)
		totalRain += rainInMonth
	
	maxRain(rainfall)
	minRain(rainfall)	
		
	#print(rainfall)
	
	print("\nTotal rainfall for the year was: %d mm." % totalRain)
	
	
	
	

main()