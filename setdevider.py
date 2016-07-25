import numpy

def devide(feature, label, testSetPercent=0.2):
	if(testSetPercent >= 1):
		print "devide(feature, label, testSetPercent(<1)"

	totalLength = len(feature)
	testLength = int(round(totalLength * testSetPercent))
	trainLength = totalLength - testLength

	return feature[:trainLength], label[:trainLength], \
			feature[trainLength:], label[trainLength:]
