# pytglue
Unofficial Python Wrapper for IT Glue. 

It goes without saying, but you are responsible for your own environment. It is possible to cause major issues with your 
data while using the API if you are not careful. 

## Usage:

### Connecting to ITGlue:
An API key is required from ITGlue to connect. 

```
Pytglue = pytglue(apikey)
```
By default, the IDs for the following items are queried for use with the convert_to_id function. This allows you to update, filter, and create using the name of the item rather than the IT Glue ID. 

* <sub>Organization Names</sub>
* <sub>Organization Statuses</sub>
* <sub>Organization Types</sub>
* <sub>Configuration Types</sub>
* <sub>Configuration Statuses</sub>
* <sub>Flexible Asset Types</sub>
* <sub>Contact Types</sub>
* <sub>Manufacturers</sub>
* <sub>Models</sub>
* <sub>Password Categories</sub>
* <sub>Countries</sub>
* <sub>Regions</sub>



This does result in additional calls to ITGlue that may be unnecessary. To bypass this you can use use the following command. Anything that utilizes the convert_to_id function will result in errors. 
```
Pytglue = pytglue(apikey, load_id=False)
```

### Queries and Filters
Pytglue can query the following items:
* <sub>Configurations</sub>
* <sub>Flexible Assets</sub>
* <sub>Organizations<sub>
* <sub>Contacts</sub>

Argument must be one 'Configurations', 'Flexible Assets', 'Organizations', 'Contacts'
```
Pytglue.Query('Configurations')
```

Filtering can be done with either the specific ID or the exact name using the convert_to_id function. Currently the "Sort" and
"Page" functions from the IT Glue API are not supported, however all matching items are returned, not just the first 50. 

All Include values are boolian and IT Glue will only recognize one. 

Acceptable values for filtering are: 
##### Configurations 
<sub>Filter</sub>
* <sub>id</sub>
* <sub>name</sub>
* <sub>org (Can be the ID or exact name of an Organization)</sub>
* <sub>configType (Can be the ID or exact name of a Configuration Type)</sub>
* <sub>configStatus (Can be the ID or exact name of a Configuration Status)</sub>
* <sub>contactID</sub>
* <sub>serial</sub>
* <sub>rmmID</sub>
* <sub>rmm</sub>

<sub>Include</sub>
* <sub>interfaces</sub>
* <sub>rmmRecord</sub>
* <sub>password</sub>
* <sub>attachments</sub>
* <sub>relatedItems</sub>
* <sub>updated</sub>
* <sub>location</sub>
  
##### Flexible Assets
<sub>Filter</sub>
* <sub>FlexibleAssetType (Can be the ID or exact name of the Flexible Asset Type)</sub>
* <sub>name</sub>
* <sub>org (Can be the ID or exact name of an Organization)</sub>

<sub>Include</sub>
* <sub>password</sub>

##### Organizations
<sub>Filter</sub>
* <sub>id</sub>
* <sub>name</sub>
* <sub>orgType (Can be the ID or the exact name of the Organization Type)</sub>
* <sub>orgStatus (Can be the ID or the exact name of the Organization Status)</sub>
* <sub>created</sub>
* <sub>updated</sub>
* <sub>excludeID</sub>
* <sub>excludeName</sub>
* <sub>excludeOrgType (Can be the ID or the exact name of the Organization Type)</sub>
* <sub>excludeOrgStatus (Can be the ID or the exact name of the Organization Status)</sub>

##### Contacts
<sub>Filter</sub>
* <sub>org (Can be the ID or exact name of an Organization)</sub>
* <sub>firstName</sub>
* <sub>lastName</sub>
* <sub>title</sub>
* <sub>contactType (Can be the ID or exact name of a Contact Type)</sub>
* <sub>firstName</sub>
* <sub>important</sub>
* <sub>primaryEmail</sub>
<sub>Include</sub>
* <sub>location</sub>
* <sub>password</sub>

```
Pytglue.Filter(configType='Firewall', configStatus='Active', interfaces=True)
```

To Query the data, use the Get function. 

```
Pytglue.Get()
```

To return the latest Get data for use outside of the wrapper. 

```
data = Pytglue.rawdata
```

### CRUD

**At this time Creating is only supported for Configurations, and Deleting is not supported at all**

Working with data is done within the class specific to the for the type of data. 

```
Pytglue.Configurations.something
Pytglue.FlexibleAssets.something
Pytglue.Organizations.somethin
Pytglue.Contacts.Something
```

#### Printing
```
Pytglue.Configurations.Print()
Pytglue.Configurations.PrintAll()
```

#### Selecting
```
Pytglue.Configurations.SelectNext()
```

SelectNext() returns a true or false value dictating whether it is selecting the final item queried.
Once the final item is selected it resets back to the first item. 
To loop through all items you can use a while loop.

```
lastitem = False
while not lastitem: 
    Pytglue.Configurations.item['configuration-status-name'] = 'Active'
    lastitem = Pytglue.Configurations.SelectNext()
```

#### Searching
Searching can be performed on any single value returned. If multiple items meet the requirements of the search, 
only the first result is returned. After searching, the selected item is the item that was found. An error is returned if 
no matches are found. 

```
Pytglue.Configurations.Search(id=12345)
```

#### Clear
Clear() is used to reset the query results. This will need to be run to perform another query of the same type. 
Future versions will need allow queries to be stacked ex. filtering for Firewalls and the filtering for Routers
and then combining the results. That does not work yet so Clear() must be used to prevent errors. 

```
Pytglue.Configurations.Clear()
```


#### Modifying Data

The data is stored in a list of dictionaries, with the dictonary keys being the key returned from IT Glue. 
Data returned using 'Include' is has the include value appended to the key. 
To modify the selected item:

```
Pytglue.Configurations.item['name'] = 'A new name'
Pytglue.Configurations.item['configuration-interfaces-name'] = 'Another new name' 
```

Calling SelectNext() or Update() checks the item for any changes since it was initially selected. 
If there are any changes, they are queued to be updated. Calling Update() will update all modified 
items in the queue of that class. e.g. Calling Update() in Configurations will not update Flexible Assets. 
This can result in a large API call and cause a timeout error. In the future I would like to get Update()
to break it into smaller requests, but that does not happen at this time. 
```
Pytglue.Configurations.Update()
```

##### **A Few Notes About Flexible Assets**
* Because Flexible Assets keys can be any value and because in Flexible Assets an empty field returns no value, there 
  is no built in check to ensure you are entering a valid key. 
* Unlike the IT Glue API Documentation, you *can* modify a single value in a Flexible Asset without entering all fields.
  This is done by copying any unmodified fields to send in the update call. 
* Tagged fields are returned as dictionaries, but a list of IDs must be provided in order for them to be updated. 

#### Creating Data
At this time, only Configurations can be created. 
Create() uses an empty 'item' dictionary with all editable values empty. 
Print, PrintAll, and convert_to_id work within create. If convert_to_id is used, and an ID is given for the corresponding
field, the value from convert_to_id takes precedence. 

Post() is used to post the items to IT Glue.

Configuration Interfaces accepts lists of multiple values. 

```
Pytglue.Configurations.Create.item['organization-name'] = 'Happy Frog'
Pytglue.Configurations.Create.item['configuration-type-name'] = 'Managed Server'
Pytglue.Configurations.Create.item['name'] = 'HF-SF-CJ452JK'
Pytglue.Configurations.Create.item['hostname'] = 'HFSFCJ452JK'
Pytglue.Configurations.Create.item['configuration-status-name'] = 'Active'
Pytglue.Configurations.Create.item['configuration-interfaces-ip-address'] = ['192.168.1.200', '192.168.1.201']
Pytglue.Configurations.Create.item['configuration-interfaces-primary'] = [True, False]
Pytglue.Configurations.Create.item['configuration-interfaces-name'] = ['NIC1', 'NIC2']
Pytglue.Configurations.Create.Next()
Pytglue.Configurations.Create.item['organization-name'] = 'Happy Frog'
Pytglue.Configurations.Create.item['configuration-type-name'] = 'Managed Server'
Pytglue.Configurations.Create.item['name'] = 'HF-NY-CJ452JK'
Pytglue.Configurations.Create.item['hostname'] = 'HFNYCJ452JK'
Pytglue.Configurations.Create.item['configuration-status-name'] = 'Active'
Pytglue.Configurations.Create.item['configuration-interfaces-ip-address'] = ['192.168.2.200', '192.168.2.201']
Pytglue.Configurations.Create.item['configuration-interfaces-primary'] = [True, False]
Pytglue.Configurations.Create.item['configuration-interfaces-name'] = ['NIC1', 'NIC2']
Pytglue.Configurations.Post()
```
