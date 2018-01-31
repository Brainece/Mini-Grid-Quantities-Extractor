from fastkml import kml
import re
import argparse

#create an argparse object to accept the gis design (in kml format) input from the command line

parser = argparse.ArgumentParser()
parser.add_argument('inputFile', help='gis design that is in kml format')

args = parser.parse_args()

#Add a kml object to store the kml object

k = kml.KML()

#open the kml file and store it in a string variable
with open(args.inputFile) as file_object:
	contents = file_object.read()

#build a kml from the contents of the file that are stored as a string in the contents variable
k.from_string(contents)

#create a list variable to hold the outer doc folder
features = list(k.features())

#create a list to hold the inner doc folder
mainFolder = list(features[0].features())

contentsFolder = list(mainFolder[0].features())

#regex variable that holds the regex pattern object.(Searches for queens within the inner doc folder)
queenRegex = re.compile(r'^Queen\s\d+$')

#an empty list that will hold all the queen folders(objects) within the design
queens = []

#loop through the features in the main queen and work only with queen folders 
for feature in contentsFolder:
	name = feature.name
	if(queenRegex.search(name)):
		queens.append(feature)

    #loop through the distribution folder if the folder name == Distribution
	if(name == "Distribution Lines"):
		distributionFolders = list(feature.features())

		#loop through the folders in distribution folder to obatin the count for poles and anchors
		for folder in distributionFolders:
			if(folder.name == 'Poles'):
				distributionPoles = len(list(folder.features()))
				print("Distribution Poles: " + str(distributionPoles))
			elif (folder.name == 'Anchors'):
				Anchors = list(folder.features())
				for anchor in Anchors:
					if(anchor.name == 'Normal'):
						normalAnchors = len(list(anchor.features()))
						print('Normal Distribution Anchors: ' + str(normalAnchors))
					elif(anchor.name == 'Flag'):
						flagAnchors = len(list(anchor.features()))
						print('Flag Distribution Anchors:' + str(flagAnchors))
					elif(anchor.name == 'Fly'):
						flyAnchors = len(list(anchor.features()))
						print('Fly Distribution Anchors: ' + str(flyAnchors))
					else:
						print('Please rename your distribution anchor folders')

#loop through the queens in the queen list variable to obtain the count for the poles and the anchors

slPoles = 0
slAnchors = 0

for queen in queens:
	queenFolders = list(queen.features())
	
	for subFolder in queenFolders:
		if(subFolder.name == 'Service Lines'):
			serviceLineFolders = list(subFolder.features())

			for serviceFolder in serviceLineFolders:
				if(serviceFolder.name == ' Poles '):
					sPoles = list(serviceFolder.features())
					slPoles += len(sPoles)
					print(queen.name + " sl poles: " + str(len(sPoles)))

				elif(serviceFolder.name == 'Anchors'):
					sAnchors = list(serviceFolder.features())
					slAnchors += len(sAnchors)
					print(queen.name + " sl anchors : " + str(len(sAnchors)))

print('Total sl Poles : ' + str(slPoles) + '\n')
print('Total sl Anchors: ' + str(slAnchors) + '\n')











	
