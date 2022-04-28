#!/usr/bin/env python
# coding: utf-8

import json

input_file_parent = "dsw_lifesciences_2.4.0.km"
input_file_fork = "elixir.no_lifesciences-elixir-norway_0.1.10.km"
output_file = "elixir.no_lifesciences-elixir-norway_0.2.0.km" 
new_version="0.2.0"
new_id="elixir.no:lifesciences-elixir-norway:"+new_version
newlog="### 0.2.0 " + "\n"+ "updated with Life Sciences DSW Knowledge Model 2.4.0" + '\n' + '\n'

with open(input_file_parent,"r") as file:
    km=json.load(file)

with open(input_file_fork,"r") as file:
    km_no=json.load(file)
    
km_no["packages"].append(km["packages"][-1])

km_no["version"]=new_version
km_no["id"]=new_id

for key in ["kmId","name","organizationId"]:
    km_no["packages"][-1][key]=km_no["packages"][-2][key]

km_no["packages"][-1]["version"]=new_version
km_no["packages"][-1]["id"]=new_id
km_no["packages"][-1]["mergeCheckpointPackageId"]= km_no["packages"][-1]["id"]
km_no["packages"][-1]["previousPackageId"] = km_no["packages"][-2]["id"]
km_no["packages"][-1]["forkOfPackageId"] = km_no["packages"][-2]["id"]
#km_no["packages"][-1]["readme"]=km_no["packages"][-2]["readme"]
newreadme=(km_no["packages"][-2]["readme"][0:214] + newlog + km_no["packages"][-2]["readme"][214:])
km_no["packages"][-1]["readme"]=newreadme

with open(output_file,"w") as outfile:
    json.dump(km_no,outfile)
