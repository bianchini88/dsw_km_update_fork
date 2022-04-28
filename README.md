# dsw_km_update_fork
This repository currently contains a minimal python script for manipulation of Knowledge models (KM) exported from the Data Stewardship Wizard (DSW)
in form of json files. In particular, the said script is created for helping to maintain a KM that is a fork of another one. 
When the parent KM is updated to a new version, there is currently no automatised way of updating the fork to include the new content from the GUI. 
By standard manipulation of python dictionaries created from the KM in json form, 
this script fetches the content from the new version of the parent KM and appends it to the forked KM.
