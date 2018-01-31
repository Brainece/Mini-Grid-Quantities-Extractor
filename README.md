# Mini-Grid-Quantities-Extractor

This program is meant to take in a GIS Mini-grid Deign in kml format as input and 
provide as its output the mini-grid components which are to be used in the mini-grid cost estimation.

The mini-grid components are:

		Distribution Poles,
		Distribution Anchors - Normal, Flag and Fly
		Service Poles		
		Service Anchors - Normal
		Cable lengths - distribution and service lengths

Usage: 

Required:- python and fastkml library installed in host machine.

The GIS Mini-grid kml design should take the following structure and naming convention :-

		> GIS Design Site Outer Folder
			 > GIS Design Inner Folder
				  King
				> Queen(s)
					> Distribution Lines
						> Poles
						> Anchors
							> Normal 
							> Flag
							> Fly
						> Lengths
					> Service Lines
						> Poles
						> Anchors 
						> Lengths

Go to terminal and use :- python ./Scriptse/quantities_extractor.py /path_to_GIS_Design_site.kml



						
 
			

		


