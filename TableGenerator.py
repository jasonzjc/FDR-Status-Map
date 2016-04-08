# generate list of online units, offline units, returned units, and to be deployed units

# get ID, longitude, latitude from online unit list
FileOnline = open('onlineunits20160407.csv')
delimiter = ','
FDRonID = list()
FDRonLongitude = list()
FDRonLatitude = list()
for line in FileOnline:
	line = line.rstrip()
	contents = line.split(delimiter)
	FDRonID.append(contents[0])
	FDRonLongitude.append(contents[1])
	FDRonLatitude.append(contents[2])
#print Latitude
FileOnline.close

# get ID, name, location, deployment status from deployment list
FileFDRdeploy = open('FDRdeploy.csv')
FDRIDAll = list()
FDRNameAll = list()
FDRLocationAll = list()
FDRDeployStatAll = list()
for line in FileFDRdeploy:
	line = line.rstrip()
	contents = line.split(delimiter)
	#print contents
	FDRIDAll.append(contents[0])
	FDRNameAll.append(contents[1])
	l = (contents[2:-1])
# 	print l
	add = ' '.join(l)
# 	print l
	FDRLocationAll.append(add)
	FDRDeployStatAll.append(contents[-1])
# print FDRDeployStatAll
FileFDRdeploy.close

# generate online unit table for mapping, including ID, name, longitude, and latitude
FDRonName = list()
FileOnlineOut = open('Onlinemap.csv','w')
count = 0
OnlineOutHead = 'ID,Name,Latitude,Longitude\r\n'
FileOnlineOut.write(OnlineOutHead)
for ID in FDRonID:
	IDNo = FDRIDAll.index(ID)
	FDRonName.append(FDRNameAll[IDNo])
	line = FDRonID[count] + "," + FDRonName[count] + "," + FDRonLongitude[count] + "," + FDRonLatitude[count] + "\r"
	count = count + 1
	FileOnlineOut.write(line)
	#print line

FileOnlineOut.close

# generate offline unit table for mapping, including ID, name, and location
FileOfflineOut = open('Offlinemap.csv','w')
count = 0
OfflineOutHead = 'ID,Name,Location\r\n'
FileOfflineOut.write(OfflineOutHead)
for ID in FDRIDAll:
	if FDRDeployStatAll[count] == '0':
		count = count + 1
		continue
	if FDRDeployStatAll[count] == '2':
		count = count + 1
		continue
	if ID in FDRonID:
		count = count + 1
		continue
	
	line = FDRIDAll[count] + "," + FDRNameAll[count] + "," + FDRLocationAll[count] + "\r\n"
	count = count + 1
	FileOfflineOut.write(line)
# 	print count, ID, FDRDeployStatAll[count-1]

FileOfflineOut.close

# generate to be deployed unit table for mapping, including ID, name, and location
FileToDeployOut = open('ToDeploymap.csv','w')
count = 0
ToDeployOutHead = 'ID,Name,Location\r\n'
FileToDeployOut.write(ToDeployOutHead)
for ID in FDRIDAll:
	if FDRDeployStatAll[count] == '2':
		line = FDRIDAll[count] + "," + FDRNameAll[count] + "," + FDRLocationAll[count] + "\r\n"
		FileToDeployOut.write(line)
	count = count + 1
	
# 	print count, ID, FDRDeployStatAll[count-1]

FileToDeployOut.close

# generate returned unit table for mapping, including ID, name, and location
FileReturnedOut = open('Returnedmap.csv','w')
count = 0
ReturnedOutHead = 'ID,Name,Location\r\n'
FileReturnedOut.write(ReturnedOutHead)
for ID in FDRIDAll:
	if FDRDeployStatAll[count] == '0':
		line = FDRIDAll[count] + "," + FDRNameAll[count] + "," + FDRLocationAll[count] + "\r\n"
		FileReturnedOut.write(line)
	count = count + 1
	
# 	print count, ID, FDRDeployStatAll[count-1]

FileReturnedOut.close