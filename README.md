# FDR-Status-Map

Version 1.0

04/08/2016

This is a script to create tables to show FDR status and locations on the map


##Preliminary##

Online unit: The data record from FDRs are checked by the server operator from time to time. Each check covers the dates since a specific time, saying one month ago. Any FDR units, as long as it has sent any data to the database, will be defined as an online unit.

Offline unit: The FDR which is deployed but not qualified as the online unit is an offline unit. The deployed FDR has a status of 1 in the FDRdeploy file.

Returned unit: The FDR had been once deployed but returned afterwards. The returned FDR has a status of 1 in the FDRdeploy file.

To be deployed unit: The FDR either will be sent out or have just been sent out but waiting to be checked before adding to the database.


##Input##

The input files include two .csv files. Neither has the head.
One is named "onlineunits+date.csv", which includes the ID, latitude and longitude of the online FDRs. Usually checked by the server operator. Database is checked since a specific date, saying one month ago. Any FDR units, as long as it has sent any data to the database, will be shown in this list. Be aware that the data from some units are too less that no coordinator is included. In that case, the related coordinator will be (0,0). They should be manually corrected according to their address in the deployment file. 


The other is named "FDRdeploy.csv", which includes the ID, name, address (city, state, contoury), and deployment status of all FDRs. It is generated from the deployment achive file. The meaning of status:

0: returned unit

1: deployed unit

2: to be deployed unit (to be sent or sent but not added to the database yet)


##Output##

The program collect information from the two files, and generate four .csv files with head.

Onlinemap.csv: include the ID, name, latitude and longitude of all online units.

Offlinemap.csv: include the ID, name, address of all offline units.

Returnedmap.csv: include the ID, name, address of all returned units.

ToDeploymap.csv: include the ID, name, address of all to be deployed units.


All the output files can than be uploaded to Googlemap to generate the FDR status map.
