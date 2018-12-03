import requests
import json
import types

urlDict={
    'configurations': 'https://api.itglue.com/configurations',
    'Configuration': 'https://api.itglue.com/configurations',
    'configuration_interfaces': 'https://api.itglue.com/configuration_interfaces',
    'configuration_statuses': 'https://api.itglue.com/configuration_statuses',
    'configuration_types': 'https://api.itglue.com/configuration_types',
    'contacts': 'https://api.itglue.com/contacts',
    'Contact': 'https://api.itglue.com/contacts',
    'contact_types': 'https://api.itglue.com/contact_types',
    'countries': 'https://api.itglue.com/countries',
    'flexible_asset': 'https://api.itglue.com/flexible_assets',
    'Flexible Asset': 'https://api.itglue.com/flexible_assets',
    'flexible_asset_fields': 'https://api.itglue.com/flexible_assets_fields',
    'flexible_asset_types': 'https://api.itglue.com/flexible_asset_types',
    'locations': 'https://api.itglue.com/locations',
    'manufacturers': 'https://api.itglue.com/manufacturers',
    'models': 'https://api.itglue.com/models',
    'operating_systems': 'https://api.itglue.com/operating_systems',
    'organizations': 'https://api.itglue.com/organizations',
    'Organization': 'https://api.itglue.com/organizations',
    'organization_statuses': 'https://api.itglue.com/organization_statuses',
    'organization_types': 'https://api.itglue.com/organization_types',
    'password': 'https://api.itglue.com/passwords',
    'password_categories': 'https://api.itglue.com/password_categories',
    'platforms': 'https://api.itglue.com/platforms',
    'regions': 'https://api.itglue.com/regions',
    }

filterDict={
    'id': 'filter[id]=',
    'name': 'filter[name]=',
    'org': 'filter[organization_id]=',
    'configType': 'filter[configuration_type_id]=',
    'configStatus': 'filter[configuration_status_id]=',
    'contactID': 'filter[contact_id]=',
    'serial': 'filter[serial_number]=',
    'rmmID': 'filter[rmm_id]=',
    'rmm': 'filter[rmm_integration_type]=',
    'orgType': 'filer[organization_type_id]=',
    'orgStatus': 'filter[organization_status_id]=',
    'created': 'filter[created_at]=',
    'updated': 'filter[updated_at]=',
    'myglueAcctID': 'filter[my_glue_account_id]=',
    'passwordCategory': 'filter[password_category_id]=',
    'url': 'filter[url]=',
    'cached_resource_name': 'filter[cached_resource_name]=',
    'excludeID': 'filter[exclude][id]=',
    'excludeName': 'filter[exclude][name]=',
    'excludeOrgType': 'filter[exclude][organization_type_id]=',
    'excludeOrgStatus': 'filter[exclude][organization_status_id]=',
    'flexibleAssetType': 'filter[flexible_asset_type_id]=',
    'firstName': 'filter[first_name]=',
    'lastName': 'filter[last_name]=',
    'title': 'filter[title]=',
    'contactType': 'filter[contact_type_id]',
    'important': 'filter[important]',
    'primaryEmail': 'filter[primary_email]',
    'city': 'filter[city]',
    'region': 'filter[region_id]',
    'country': 'filter[country_id]',
}

includeDict={
    'interfaces': 'include=configuration_interfaces',
    'rmmRecord': 'include=rmm_records',
    'password': 'include=passwords',
    'attachments': 'include=attachments',
    'related_items': 'include=related_items',
    'updated': 'include=updater',
    'location': 'include=location'
}

showDict={
    'show_password': 'show_password=',
}

sortDict={
    'sort-name': 'sort=name',
    'sort-id': 'sort=id',
    'sort-created': 'sort=created_at',
    'sort-updated': 'sort=updated_at',
    'sort_organization_status_name': 'sort=organization_status_name',
    'sort_organization_type_name': 'sort=organization_type_name',
    'sort_short_name': 'sort=short_name',
    'sort_my_glue_account_id': 'sort=my_glue_account_id',
    'sort_username': 'sort=username',
    'sort_url': 'sort=url',
    'sort_first_name': 'sort=first_name',
    'sort_last_name': 'sort=last_name'
}

pageDict={
    'page': 'page=',
    'page-num': 'page[number]=',
    'page-size': 'page[size]=',
}

class pytglue:
    def __init__(self):
        self.self=self
        #self.Configurations=self.Configurations(self.parseData, self.loadData, self.appendData, self.Select, self.SelectNext, self.Print, self.PrintAll)
        self.Configurations=self.Configurations(self.loadData, self.append)
        self.FlexibleAsset=self.FlexibleAsset(self.loadData, self.append)
        self.Organizations=self.Organizations(self.loadData, self.append)
        self.Contacts=self.Contacts(self.loadData, self.append)

    def makeQuery(self, query, param=None, param_value=None, final=False):
        if param_value != None:
            param_value=str(param_value)
        if param in filterDict.keys():
            query=query+filterDict[param]+param_value+'&'
        elif param in includeDict.keys():
            query=query+includeDict[param]+'&'
        elif param in sortDict.keys():
            query=query+sortDict[param]+'&'
        elif param in pageDict.keys():
            query=query+pageDict[param]+param_value+'&'
        elif param in showDict.keys():
            query=query+showDict[param]+param_value+'&'
        if final:
            query = query.rstrip('&')
        return query

    def getRequest(self, url, query=None, return_all=True):
            response=requests.get(url, params=query, headers=self.getheader)
            if response.status_code < 199 or response.status_code < 299:
                response=json.loads(response.text)
                if return_all==False:
                    return response
                else:
                    try:
                        links=response['links']
                        while 'next' in links:
                            nextpage=response['links']['next']
                            response_alt=requests.get(nextpage, headers=self.getheader)
                            response_alt=json.loads(response_alt.text)
                            for key in response.keys():
                                if key=='links':
                                    response[key]=response_alt[key]
                                elif isinstance (response[key], list):
                                    response[key]=response[key]+response_alt[key]
                            links=response['links']
                    except KeyError:
                        pass
                    return response
            else:
                error=("Status Code: ", response.status_code, "\nResponse Text: ",
                response.text, "\nRequest URL: ", url, "\nRequest Header: ", self.getheader,
                "\nRequest Query: ", query)
                raise RuntimeError(error)

    def Get(self):
        if self.query=='':
            self.query=None
        if self.queryType=='Configuration':
            self.rawdata=self.getRequest(urlDict[self.queryType],self.query)
            self.Configurations.appendData(self.rawdata)
        if self.queryType=='Flexible Asset':
            self.rawdata=self.getRequest(urlDict[self.queryType],self.query)
            self.FlexibleAsset.appendData(self.rawdata)
        if self.queryType=='Organization':
            self.rawdata=self.getRequest(urlDict[self.queryType],self.query)
            self.Organizations.appendData(self.rawdata)
        if self.queryType=='Contact':
            self.rawdata=self.getRequest(urlDict[self.queryType],self.query)
            self.Contacts.appendData(self.rawdata)



    def Connect(self, apikey):
        self.getheader={'x-api-key': apikey}
        self.postheader={'x-api-key': apikey, 'Content-Type':'application/vnd.api+json'}

        self.idlist={'manufacturers':{}, 'organizations':{}, 'configuration_statuses':{},
        'configuration_types':{}, 'contact_types':{}, 'countries':{},
        'flexible_asset_types':{}, 'operating_systems':{}, 'organization_types':{},
        'organization_statuses':{}, 'password_categories':{}, 'regions':{},
        'models': {'None':{}}}

        query=''
        query=self.makeQuery(query, 'sort-name')
        query=self.makeQuery(query, 'page-size', 1000, final=True)
        for cat in self.idlist:
            response=self.getRequest(urlDict[cat], query)
            if cat != 'models':
                for x in response['data']:
                    key=x['attributes']['name']
                    value=x['id']
                    self.idlist[cat][key]=value
            else:
                for key in self.idlist['manufacturers']:
                    self.idlist['models'][key]={}
                for x in response['data']:
                    key=x['attributes']['manufacturer-name']
                    if key==None:
                        key='None'
                    subkey=x['attributes']['name']
                    value=x['id']
                    self.idlist['models'][key][subkey]=value

    def printPretty(self, cat, manufacturer=None):
        catlist=['manufacturers', 'organizations', 'configuration_statuses',
        'configuration_types', 'contact_types', 'countries', 'flexible_asset_types',
        'operating_systems', 'organization_types', 'password_categories',
        'regions']
        if cat=='models':
            if manufacturer==None:
                for key in self.idlist['models']:
                    print (key)
                    for subkey in self.idlist['models'][key]:
                        print (subkey, ": ", self.idlist['models'][key][subkey])
                    print('')
            else:
                for subkey in self.idlist['models'][manufacturer]:
                    print (subkey, ": ", self.idlist['models'][manufacturer][subkey])
        elif cat in catlist:
            for key in self.idlist[cat]:
                print (key, ": ", self.idlist[cat][key])
        else:
            error="Invalid Category Selection: "+cat
            raise RuntimeError(error)

    def convertToID(self, key, value):

        try:
            if key=='org':
                value=self.idlist['organizations'][value]
            elif key=='configType':
                value=self.idlist['configuration_types'][value]
            elif key=='configStatus':
                value=self.idlist['configuration_statuses'][value]
            elif key=='flexibleAssetType':
                value=self.idlist['flexible_asset_types'][value]
            elif key=='orgType':
                value=self.idlist['organization_types'][value]
            elif key=='orgStatus':
                value=self.idlist['organization_statuses'][value]
            elif key=='excludeOrgType':
                value=self.idlist['organization_types'][value]
            elif key=='excludeOrgStatus':
                value=self.idlist['organization_statuses'][value]
            elif key=='contactType':
                value=self.idlist['contact_types'][value]
            return value
        except KeyError:
            error = "Invalid "+key+" choice: "+ value
            raise RuntimeError(error)

    def Query(self, queryType):
        self.queryType=queryType
        if self.queryType=='Configuration':
            self.query=''
            self.FilterList=['id', 'name', 'org', 'configType', 'configStatus', 'contactID',
            'serial', 'rmmID', 'rmm']
            self.IncludeList=['interfaces', 'rmmRecord', 'password', 'attachments', 'relatedItems',
            'updated', 'location']
            self.canConvert=['org', 'configType', 'configStatus']
        if self.queryType=='Flexible Asset':
            self.query=''
            self.FilterList=['flexibleAssetType', 'name', 'org']
            self.canConvert=['flexibleAssetType', 'org']
            self.IncludeList=['password']
        if self.queryType=='Organization':
            self.query=''
            self.FilterList=['id', 'name', 'orgType', 'orgStatus', 'created', 'updated',
            'excludeID', 'excludeName', 'excludeOrgType', 'excludeOrgStatus']
            self.canConvert=['orgType', 'orgStatus', 'excludeOrgType', 'excludeOrgStatus']
            self.IncludeList=[]
        if self.queryType=='Contact':
            self.query=''
            self.FilterList=['org', 'firstName', 'lastName', 'title', 'contactType',
            'important', 'primaryEmail']
            self.canConvert=['org','contactType']
            self.IncludeList=['location', 'password']

        ##Add in other items

    def Filter(self, **kwargs):
        def clear(self):
            self.query=''
        if kwargs is not None:
            for key in kwargs:
                value=kwargs[key]
                if key in self.FilterList:
                    if isinstance (value, str):
                        try:
                            value=int(value)
                        except ValueError:
                            if key in self.canConvert:
                                value=self.convertToID(key, value)
                        self.query=self.makeQuery(self.query, key, value)
                ##Add in sort, show, and include
                elif key in self.IncludeList:
                    if isinstance(value, bool):
                        self.query=self.makeQuery(self.query, key, value)
                    else:
                        error = "Invalid Variable: "+key+", value for Included items must be Boolian."
                        raise RuntimeError(error)
                else:
                    error = "Invalid Variable: "+key
                    raise RuntimeError(error)

            self.query=self.makeQuery(self.query, final=True)
    def append(self, newdata, existingdata):
        for x in newdata:
            if existingdata==None:
                existingdata.append(x)
            else:
                if x in existingdata:
                    continue
                for y in existingdata:
                    if x['id']==y['id']:
                        key=list(x['relationships'].keys())
                        key=key[0]
                        existingdata[y]['relationships'][key]=x['relationships'][key]
                        continue
                existingdata.append(x)
        return existingdata
    def loadData(self, singledata, alldata):
        def loop (result, key_1, singledata, alldata):
            if isinstance(singledata[key_1], str):
                result[key_1]=singledata[key_1]

            elif isinstance(singledata[key_1], dict):
                for key_2 in singledata[key_1]:

                    if isinstance(singledata[key_1][key_2], dict):
                        if key_2 == 'traits' or key_2 =='location':
                            for key_6 in singledata[key_1][key_2]:
                                result[key_6]=singledata[key_1][key_2][key_6]
                        else:
                            key_5=list(singledata[key_1][key_2].keys())
                            key_5=key_5[0]
                            if isinstance(singledata[key_1][key_2][key_5], list):
                                for list_1 in singledata[key_1][key_2][key_5]:

                                    included_id=list_1['id']

                                    for list_2 in alldata['included']:
                                        if list_2['id']==included_id:
                                            for key_3 in list_2:
                                                if isinstance(list_2[key_3], dict):
                                                    for key_4 in list_2[key_3]:
                                                        result_key=list_2['type']+'-'+key_4
                                                        result_value=list_2[key_3][key_4]
                                                        try:
                                                            result[result_key].append(result_value)
                                                        except (NameError, KeyError):
                                                            result[result_key]=[result_value]
                                                else:
                                                    result_key=list_2['type']+'-'+key_3
                                                    result_value=list_2[key_3]
                                                    try:
                                                        result[result_key].append(result_value)
                                                    except (NameError, KeyError):
                                                        result[result_key]=[result_value]
                            else:
                                continue
                    else:
                        result[key_2]=singledata[key_1][key_2]
            return result
        result={}
        for key_1 in singledata:
            result=loop(result, key_1, singledata, alldata)
        return result
##Add Clear function

    class Configurations:
        def __init__(self, loadData, append):


            self.self=self
            self.rawdata={'data':[], 'included':[]}
            self.counter=0
            self.loadData=loadData
            self.append=append

        def appendData(self, newdata):
            self.rawdata['data']=self.append(newdata['data'], self.rawdata['data'])
            try:
                self.rawdata['included']=self.append(newdata['included'], self.rawdata['included'])
            except KeyError:
                pass
        def Select(self):
            self.item=self.loadData(self.rawdata['data'][self.counter], self.rawdata)
        def SelectNext(self):
            self.counter=self.counter+1
            try:
                self.Select()
            except IndexError:
                self.counter=0
                self.Select()
        def Print(self):
            for x in self.item:
                print(x,": ", self.item[x])
        def PrintAll(self):
            print (self)
            counterholder=self.counter
            self.counter=0
            self.Select()
            for x in self.rawdata['data']:
                self.Print()
                print('')
                self.SelectNext()
            self.counter=counterholder
            self.Select()

    class FlexibleAsset:
        def __init__(self, loadData, append):
            self.self=self
            self.rawdata={'data':[], 'included':[]}
            self.counter=0
            self.loadData=loadData
            self.append=append

        def appendData(self, newdata):
            self.rawdata['data']=self.append(newdata['data'], self.rawdata['data'])
            try:
                self.rawdata['included']=self.append(newdata['included'], self.rawdata['included'])
            except KeyError:
                pass
        def Select(self):
            self.item=self.loadData(self.rawdata['data'][self.counter], self.rawdata)
        def SelectNext(self):
            self.counter=self.counter+1
            try:
                self.Select()
            except IndexError:
                self.counter=0
                self.Select()
        def Print(self):
            for x in self.item:
                print(x,": ", self.item[x])
        def PrintAll(self):
            counterholder=self.counter
            self.counter=0
            self.Select()
            for x in self.rawdata['data']:
                self.Print()
                print('')
                print('')
                print('')
                self.SelectNext()
            self.counter=counterholder
            self.Select()
## There is something wrong with the Contacts query with org ids. the query gives
## 'filter[organization_id]=' but it needs to be 'organization_id=' for contacts
    class Contacts:
        def __init__(self, loadData, append):
            self.self=self
            self.rawdata={'data':[], 'included':[]}
            self.counter=0
            self.loadData=loadData
            self.append=append

        def appendData(self, newdata):
            self.rawdata['data']=self.append(newdata['data'], self.rawdata['data'])
            try:
                self.rawdata['included']=self.append(newdata['included'], self.rawdata['included'])
            except KeyError:
                pass
        def Select(self):
            self.item=self.loadData(self.rawdata['data'][self.counter], self.rawdata)
        def SelectNext(self):
            self.counter=self.counter+1
            try:
                self.Select()
            except IndexError:
                self.counter=0
                self.Select()
        def Print(self):
            for x in self.item:
                print(x,": ", self.item[x])
        def PrintAll(self):
            counterholder=self.counter
            self.counter=0
            self.Select()
            for x in self.rawdata['data']:
                self.Print()
                print('')
                print('')
                print('')
                self.SelectNext()
            self.counter=counterholder
            self.Select()

    class Organizations:
        def __init__(self, loadData, append):
            self.self=self
            self.rawdata={'data':[], 'included':[]}
            self.counter=0
            self.loadData=loadData
            self.append=append

        def appendData(self, newdata):
            self.rawdata['data']=self.append(newdata['data'], self.rawdata['data'])
            try:
                self.rawdata['included']=self.append(newdata['included'], self.rawdata['included'])
            except KeyError:
                pass
        def Select(self):
            self.item=self.loadData(self.rawdata['data'][self.counter], self.rawdata)
        def SelectNext(self):
            self.counter=self.counter+1
            try:
                self.Select()
            except IndexError:
                self.counter=0
                self.Select()
        def Print(self):
            for x in self.item:
                print(x,": ", self.item[x])
        def PrintAll(self):
            counterholder=self.counter
            self.counter=0
            self.Select()
            for x in self.rawdata['data']:
                self.Print()
                print('')
                print('')
                print('')
                self.SelectNext()
            self.counter=counterholder
            self.Select()
