import requests
import json
import types


urlDict = {
    'configurations': 'https://api.itglue.com/configurations',
    'Configurations': 'https://api.itglue.com/configurations',
    'config_interfaces': 'https://api.itglue.com/configuration_interfaces',
    'configuration_statuses': 'https://api.itglue.com/configuration_statuses',
    'configuration_types': 'https://api.itglue.com/configuration_types',
    'contacts': 'https://api.itglue.com/contacts',
    'Contacts': 'https://api.itglue.com/contacts',
    'contact_types': 'https://api.itglue.com/contact_types',
    'countries': 'https://api.itglue.com/countries',
    'flexible_asset': 'https://api.itglue.com/flexible_assets',
    'Flexible Assets': 'https://api.itglue.com/flexible_assets',
    'flexible_asset_fields': 'https://api.itglue.com/flexible_assets_fields',
    'flexible_asset_types': 'https://api.itglue.com/flexible_asset_types',
    'locations': 'https://api.itglue.com/locations',
    'manufacturers': 'https://api.itglue.com/manufacturers',
    'models': 'https://api.itglue.com/models',
    'operating_systems': 'https://api.itglue.com/operating_systems',
    'organizations': 'https://api.itglue.com/organizations',
    'Organizations': 'https://api.itglue.com/organizations',
    'organization_statuses': 'https://api.itglue.com/organization_statuses',
    'organization_types': 'https://api.itglue.com/organization_types',
    'password': 'https://api.itglue.com/passwords',
    'password_categories': 'https://api.itglue.com/password_categories',
    'platforms': 'https://api.itglue.com/platforms',
    'regions': 'https://api.itglue.com/regions',
    }

filterDict = {
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
    'FlexibleAssetType': 'filter[flexible_asset_type_id]=',
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

includeDict = {
    'interfaces': 'include=configuration_interfaces',
    'rmmRecord': 'include=rmm_records',
    'password': 'include=passwords',
    'attachments': 'include=attachments',
    'related_items': 'include=related_items',
    'updated': 'include=updater',
    'location': 'include=location'
}

showDict = {
    'show_password': 'show_password=',
}

sortDict = {
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

pageDict = {
    'page': 'page=',
    'page-num': 'page[number]=',
    'page-size': 'page[size]=',
}


class pytglue:
    def __init__(self, apikey, load_id=True):
        self.self = self

        self.Connect(apikey, load_id=True)

        self.Configurations = self.Configurations(
            self.common_load_data, self.common_merge_data,
            self.common_convert_to_id, self.common_patch_request,
            self.common_format_update, self.common_print,
            self.common_select_next, self.common_clear, self.common_print_all,
            self.common_append_data, self.common_search, self.Create,
            self.common_post_request, self.common_select)

        self.FlexibleAsset = self.FlexibleAsset(
            self.common_load_data, self.common_merge_data,
            self.common_convert_to_id, self.common_patch_request,
            self.common_print, self.common_select_next, self.common_clear,
            self.common_print_all, self.common_append_data, self.common_search)

        self.Contacts = self.Contacts(
            self.common_load_data, self.common_merge_data,
            self.common_convert_to_id, self.common_patch_request,
            self.common_format_update, self.common_print,
            self.common_select_next, self.common_clear, self.common_print_all,
            self.common_append_data, self.common_search,
            self.common_select)

        self.Organizations = self.Organizations(
            self.common_load_data, self.common_merge_data,
            self.common_convert_to_id, self.common_patch_request,
            self.common_format_update, self.common_print,
            self.common_select_next, self.common_clear, self.common_print_all,
            self.common_append_data, self.common_search,
            self.common_select)

    def Connect(self, apikey, load_id=True):
        self.getheader = {'x-api-key': apikey}
        self.postheader = {
            'x-api-key': apikey, 'Content-Type': 'application/vnd.api+json'}

        if load_id:
            self.idlist = {
                'manufacturers': {}, 'organizations': {},
                'configuration_statuses': {}, 'configuration_types': {},
                'contact_types': {}, 'countries': {},
                'flexible_asset_types': {}, 'operating_systems': {},
                'organization_types': {}, 'organization_statuses': {},
                'password_categories': {}, 'regions': {},
                'models': {'None': {}}}

            query = ''
            query = self.common_make_query(query, 'sort-name')
            query = self.common_make_query(
                query, 'page-size', 1000, final=True)
            for cat in self.idlist:
                response = self.common_get_request(urlDict[cat], query)
                if cat != 'models':
                    for x in response['data']:
                        key = x['attributes']['name']
                        value = x['id']
                        self.idlist[cat][key] = value
                else:
                    for key in self.idlist['manufacturers']:
                        self.idlist['models'][key] = {}
                    for x in response['data']:
                        key = x['attributes']['manufacturer-name']
                        if key is None:
                            key = 'None'
                        subkey = x['attributes']['name']
                        value = x['id']
                        self.idlist['models'][key][subkey] = value

    def Get(self):
        if self.query == '':
            self.query = None
            self.filter_by_id = False
        if not self.filter_by_id:
            url = urlDict[self.query_type]
        else:
            url = urlDict[self.query_type] + "/" + str(self.filter_by_ip)

        if self.query_type == 'Configurations':
            self.rawdata = self.common_get_request(url, self.query)
            self.Configurations.appendData(self.rawdata)
        elif self.query_type == 'Flexible Assets':
            self.rawdata = self.common_get_request(url, self.query)
            self.FlexibleAsset.appendData(self.rawdata)
        elif self.query_type == 'Organizations':
            self.rawdata = self.common_get_request(url, self.query)
            self.Organizations.appendData(self.rawdata)
        elif self.query_type == 'Contacts':
            self.rawdata = self.common_get_request(url, self.query)
            self.Contacts.appendData(self.rawdata)

    def Query(self, query_type):
        self.query_type = query_type
        if self.query_type == 'Configurations':
            self.query = ''
            self.FilterList = [
                'id', 'name', 'org', 'configType', 'configStatus', 'contactID',
                'serial', 'rmmID', 'rmm']
            self.IncludeList = [
                'interfaces', 'rmmRecord', 'password', 'attachments',
                'relatedItems', 'updated', 'location']
            self.canConvert = ['org', 'configType', 'configStatus']

        if self.query_type == 'Flexible Assets':
            self.query = ''
            self.FilterList = ['FlexibleAssetType', 'name', 'org']
            self.canConvert = ['FlexibleAssetType', 'org']
            self.IncludeList = ['password']

        if self.query_type == 'Organizations':
            self.query = ''
            self.FilterList = [
                'id', 'name', 'orgType', 'orgStatus', 'created', 'updated',
                'excludeID', 'excludeName', 'excludeOrgType',
                'excludeOrgStatus']
            self.canConvert = [
                'orgType', 'orgStatus', 'excludeOrgType', 'excludeOrgStatus']
            self.IncludeList = []

        if self.query_type == 'Contacts':
            self.query = ''
            self.FilterList = [
                'org', 'firstName', 'lastName', 'title', 'contactType',
                'important', 'primaryEmail']
            self.canConvert = ['org', 'contactType']
            self.IncludeList = ['location', 'password']

    def Filter(self, **kwargs):
        if kwargs is not None:
            filter = {}
            include = {}
            for key in kwargs:
                if key in self.FilterList:
                    filter[key] = kwargs[key]
                elif key in self.IncludeList:
                    include[key] = kwargs[key]
                else:
                    error = 'Invalid Variable: '+key
                    raise RuntimeError(error)

            for key in filter:
                if 'id' in filter.keys():
                    self.filter_by_id = filter[key]
                    break
                else:
                    self.filter_by_id = False
                    value = include[key]
                    if isinstance(value, str):
                        try:
                            value = int(value)
                        except ValueError:
                            if key in self.canConvert:
                                value = self.common_convert_to_id(key, value)
                        self.query = self.common_make_query(
                                                        self.query, key, value)

            for key in include:
                value = filter[key]
                if isinstance(value, bool):
                    self.query = self.common_make_query(self.query, key, value)
                else:
                    error = ('Invalid Variable: '
                             + key
                             + ', value for Included items must be Boolian.')
                    raise RuntimeError(error)

            self.query = self.common_make_query(
                                    self.query, 'page-size', 1000, final=True)

    def common_make_query(
            self, query, param=None, param_value=None, final=False):

        if param_value is not None:
            param_value = str(param_value)
        if param in filterDict.keys():
            query = query + filterDict[param] + param_value + '&'
        elif param in includeDict.keys():
            query = query + includeDict[param] + '&'
        elif param in sortDict.keys():
            query = query + sortDict[param] + '&'
        elif param in pageDict.keys():
            query = query + pageDict[param] + param_value + '&'
        elif param in showDict.keys():
            query = query + showDict[param] + param_value + '&'
        if final:
            query = query.rstrip('&')
        return query

    def common_get_request(self, url, query=None, return_all=True):
            response = requests.get(url, params=query, headers=self.getheader)
            if response.status_code < 199 or response.status_code < 299:
                response = json.loads(response.text)
                if not return_all:
                    return response
                else:
                    try:
                        links = response['links']
                        while 'next' in links:
                            nextpage = response['links']['next']
                            response_alt = requests.get(nextpage,
                                                        headers=self.getheader)
                            response_alt = json.loads(response_alt.text)
                            for key in response.keys():
                                if key == 'links':
                                    response[key] = response_alt[key]
                                elif isinstance(response[key], list):
                                    response[key] = (response[key]
                                                     + response_alt[key])
                            links = response['links']
                    except KeyError:
                        pass
                    return response
            else:
                error = ('Status Code: ', response.status_code,
                         '\nResponse Text: ', response.text, '\nRequest URL: ',
                         url, '\nRequest Header: ', self.getheader,
                         '\nRequest Query: ', query)
                raise RuntimeError(error)

    def common_patch_request(self, url, data):
        data = json.dumps(data)
        response = requests.patch(url, data=data, headers=self.postheader)
        if response.status_code < 199 or response.status_code < 299:
            response = json.loads(response.text)
        else:
            error = ('Status Code: ', response.status_code,
                     '\nResponse Text: ', response.text, '\nRequest URL: ',
                     url, '\nRequest Header: ', self.postheader,
                     '\nRequest Data: ', query)
            raise RuntimeError(error)

    def common_post_request(self, url, data):
        data = json.dumps(data)
        response = requests.post(url, data=data, headers=self.postheader)
        if response.status_code < 199 or response.status_code < 299:
            response = json.loads(response.text)
        else:
            error = ('Status Code: ', response.status_code,
                     '\nResponse Text: ', response.text, '\nRequest URL: ',
                     url, '\nRequest Header: ', self.postheader,
                     '\nRequest Data: ', query)
            raise RuntimeError(error)

    def common_convert_to_id(self, key, value):
        organization_aliases = ['org', 'organization-name']
        configType_aliases = ['configType', 'configuration-type-name']
        configStatus_aliases = ['configStatus', 'configuration-status-name']
        FlexibleAssetType_aliases = ['FlexibleAssetType']
        orgType_aliases = ['orgType', 'excludeOrgType']
        orgStatus_aliases = ['orgStatus', 'excludeOrgStatus']
        contactType_aliases = ['contactType']

        try:
            if key in organization_aliases:
                value = int(self.idlist['organizations'][value])
            elif key in configType_aliases:
                value = int(self.idlist['configuration_types'][value])
            elif key in configStatus_aliases:
                value = int(self.idlist['configuration_statuses'][value])
            elif key in FlexibleAssetType_aliases:
                value = int(self.idlist['flexible_asset_types'][value])
            elif key in orgType_aliases:
                value = int(self.idlist['organization_types'][value])
            elif key in orgStatus_aliases:
                value = int(self.idlist['organization_statuses'][value])
            elif key in contactType_aliases:
                value = int(self.idlist['contact_types'][value])
            return value
        except KeyError:
            error = 'Invalid '+key+' choice: ' + value
            raise RuntimeError(error)

    def PrintPretty(self, cat, manufacturer=None):
        catlist = [
            'manufacturers', 'organizations', 'configuration_statuses',
            'configuration_types', 'contact_types', 'countries',
            'flexible_asset_types', 'operating_systems', 'organization_types',
            'password_categories', 'regions']
        if cat == 'models':
            models = self.idlist['models']
            if manufacturer is None:
                for key in models:
                    print(key)
                    for subkey in models[key]:
                        print(subkey, ': ', models[key][subkey])
                    print('')
            else:
                for subkey in models[manufacturer]:
                    print(subkey, ': ', models[manufacturer][subkey])
        elif cat in catlist:
            for key in self.idlist[cat]:
                print(key, ': ', self.idlist[cat][key])
        else:
            error = 'Invalid Category Selection: ' + cat
            raise RuntimeError(error)

    def common_merge_data(self, newdata, data):
        for x in newdata:
            if data is None:
                data.append(x)
            else:
                if x in data:
                    continue
                for y in data:
                    if x['id'] == y['id']:
                        key = list(x['relationships'].keys())
                        key = key[0]
                        data[y]['relationships'][key] = x['relationships'][key]
                        continue
                data.append(x)
        return data

    def common_load_data(self, singledata, alldata):
        def loop(result, key_1, singledata, alldata):
            if isinstance(singledata[key_1], str):
                result[key_1] = singledata[key_1]

            elif isinstance(singledata[key_1], dict):
                for key_2 in singledata[key_1]:

                    if isinstance(singledata[key_1][key_2], dict):
                        if key_2 == 'traits' or key_2 == 'location':
                            for key_6 in singledata[key_1][key_2]:
                                result[key_6] = singledata[key_1][key_2][key_6]
                        else:
                            key_5 = list(singledata[key_1][key_2].keys())
                            key_5 = key_5[0]
                            if isinstance(
                                        singledata[key_1][key_2][key_5], list):

                                for list_1 in singledata[key_1][key_2][key_5]:

                                    included_id = list_1['id']

                                    for list_2 in alldata['included']:
                                        if list_2['id'] == included_id:
                                            for key_3 in list_2:
                                                if isinstance(
                                                        list_2[key_3], dict):

                                                    for key_4 in list_2[key_3]:
                                                        result_key = (
                                                                list_2['type']
                                                                + '-'
                                                                + key_4)
                                                        result_value = (
                                                          list_2[key_3][key_4])

                                                        try:
                                                            result[result_key].append(result_value)
                                                        except (NameError, KeyError):
                                                            result[result_key] = [result_value]
                                                else:
                                                    result_key = (list_2['type']
                                                                  + '-'
                                                                  + key_3)
                                                    result_value = list_2[key_3]
                                                    try:
                                                        result[result_key].append(result_value)
                                                    except (NameError, KeyError):
                                                        result[result_key] = [result_value]
                            else:
                                continue
                    else:
                        result[key_2] = singledata[key_1][key_2]
            return result
        result = {}
        for key_1 in singledata:
            result = loop(result, key_1, singledata, alldata)
        return result

    def common_format_update(self, subclass, url):
        subclass.Select()
        update = {'data': []}
        for x in subclass.updates:
            updatequeue = {'type': x.pop('type'), 'attributes': {}}
            for y in x:
                updatequeue['attributes'][y] = x[y]
            update['data'].append(updatequeue)
        self.common_patch_request(url, update)

    def common_print(self, subclass):
        for x in subclass.item:
            print(x, ': ', subclass.item[x])

    def common_select_next(self, subclass):
        subclass.counter = subclass.counter+1
        try:
            subclass.Select()
            return False
        except IndexError:
            subclass.counter = 0
            subclass.Select()
            return True

    def common_clear(self, subclass):
        subclass.rawdata = {'data': [], 'included': []}
        subclass.counter = 0
        subclass.updates = []

    def common_print_all(self, subclass):
        counterholder = subclass.counter
        subclass.counter = 0
        subclass.Select()
        for x in subclass.rawdata['data']:
            subclass.Print()
            print('')
            subclass.SelectNext()
        subclass.counter = counterholder
        subclass.Select()

    def common_append_data(self, subclass, newdata):
        subclass.rawdata['data'] = subclass.common_merge_data(
                                    newdata['data'], subclass.rawdata['data'])
        try:
            subclass.rawdata['included'] = subclass.common_merge_data(
                                                newdata['included'],
                                                subclass.rawdata['included'])
        except KeyError:
            pass
        subclass.Select()

    def common_search(self, subclass, **kwargs):
        # Will only return value of last kwarg
        # Can search on any key, but will only return the first value.
        subclass.counter = 0
        subclass.Select()
        for key in kwargs:
            value = kwargs[key]
            end = False
            while not end:
                if subclass.item[key] == value:
                    break
                else:
                    end = subclass.SelectNext()
            if end is True:
                error = str(value) + " was not found in " + key
                raise RuntimeError(error)

    def common_select(self, subclass, editable, canconvert):
        changes = {}
        update = False
        try:
            for x in editable:
                if subclass.item[x] != subclass.control[x]:
                    changes[x] = subclass.item[x]
                    update = True
            for x in canconvert:
                if subclass.item[x] != subclass.control[x]:
                    converted = subclass.common_convert_to_id(
                                                        x, subclass.item[x])
                    if x == 'organization-name':
                        changes['organization-id'] = converted
                    elif x == 'configuration-type-name':
                        changes['configuration-type-id'] = converted
                    elif x == 'configuration-status-name':
                        changes['configuration-status-id'] = converted
                    elif x == 'organization-type-name':
                        changes['organization-type-id'] = converted
                    elif x == 'organization-status-name':
                        changes['organization-status-id'] = converted

                    update = True
        except (AttributeError, TypeError):
            pass

        if update:
            changes['id'] = subclass.control['id']
            changes['type'] = subclass.control['type']
            subclass.updates.append(changes)
        subclass.item = subclass.common_load_data(
                                    subclass.rawdata['data'][subclass.counter],
                                    subclass.rawdata)
        subclass.control = dict(subclass.item)

    class Create:
        def __init__(
                self, subclass, create_items, create_required, create_convert,
                common_convert_to_id, Post, Print, PrintAll):
            self.self = subclass
            self.new_create = create_items
            self.item = dict(self.new_create)
            self.required = create_required
            self.create_list = []
            self.create_convert = create_convert
            self.common_convert_to_id = common_convert_to_id
            self.Post = Post
            self.Print = Print
            self.PrintAll = PrintAll

        def Next(self):
            self.requirement_check()
            self.create_list.append(self.item)
            self.item = dict(self.new_create)

        def requirement_check(self):
            for x in self.create_convert:
                if self.item[x] is not None:
                    id = self.common_convert_to_id(x, self.item[x])
                    self.item[self.create_convert[x]] = id
            missing = False
            missing_fields = []
            for x in self.required:
                if self.item[x] is None:
                    missing_fields.append(x)
                    missing = True

            if missing:
                error = 'Missing Required Field: '+key
                raise RuntimeError(error)

    class Configurations:
        def __init__(self, common_load_data, common_merge_data,
                     common_convert_to_id, common_patch_request,
                     common_format_update, common_print, common_select_next,
                     common_clear, common_print_all, common_append_data,
                     common_search, Create, common_post_request,
                     common_select):

            self.self = self
            self.rawdata = {'data': [], 'included': []}
            self.counter = 0
            self.common_load_data = common_load_data
            self.common_merge_data = common_merge_data
            self.common_convert_to_id = common_convert_to_id
            self.updates = []
            self.common_patch_request = common_patch_request
            self.common_format_update = common_format_update
            self.common_print = common_print
            self.common_select_next = common_select_next
            self.common_clear = common_clear
            self.common_print_all = common_print_all
            self.common_append_data = common_append_data
            self.common_post_request = common_post_request
            self.common_select = common_select
            self.common_search = common_search
            create_items = {
                'organization-id': None, 'organization-name': None,
                'configuration-type-id': None, 'configuration-type-name': None,
                'configuration-status-id': None,
                'configuration-status-name': None, 'location-id': None,
                'contact-id': None, 'manufacturer-id': None, 'model-id': None,
                'operating-system-id': None, 'operating-system-notes': None,
                'name': None, 'notes': None, 'hostname': None,
                'primary-ip': None, 'mac-address': None, 'serial-number': None,
                'default-gateway': None, 'asset-tag': None, 'position': None,
                'installed-by': None, 'purchased-by': None,
                'purchased-at': None, 'warranty-expires-at': None,
                'installed-at': None, 'configuration-interfaces-name': None,
                'configuration-interfaces-ip-address': None,
                'configuration-interfaces-primary': None,
                'configuration-interfaces-notes': None
                }
            create_required = [
                'organization-id', 'configuration-type-id', 'name']
            create_convert = {
                'organization-name': 'organization-id',
                'configuration-type-name': 'configuration-type-id',
                'configuration-status-name': 'configuration-status-id'
            }

            self.Create = Create(
                self, create_items, create_required, create_convert,
                self.common_convert_to_id, self.Post, self.Print, self.PrintAll)

        def appendData(self, newdata):
            self.common_append_data(self, newdata)

        def Clear(self):
            self.common_clear(self)

        def Print(self):
            self.common_print(self)

        def PrintAll(self):
            self.common_print_all(self)

        def Update(self):
            self.common_format_update(self, urlDict['Configuration'])

        def Search(self, **kwargs):
            self.common_search(self, **kwargs)

        def SelectNext(self):
            self.common_select_next(self)

        def Select(self):
            editable = [
                'organization-id', 'configuration-type-id', 'location-id',
                'configuration-status-id', 'contact-id', 'manufacturer-id',
                'model-id', 'operating-system-id', 'operating-system-notes',
                'name', 'notes', 'hostname', 'primary-ip', 'mac-address',
                'default-gateway', 'serial-number', 'asset-tag', 'position',
                'installed-by', 'purchased-by', 'purchased-at',
                'warranty-expires-at', 'installed-at']
            canconvert = [
                'organization-name', 'configuration-type-name',
                'configuration-status-name', 'manufacturer-name', 'model-name']

            self.common_select(self, editable, canconvert)

        def Post(self):
            self.Create.Next()
            config_items = []
            for item in self.Create.create_list:
                config_interface_items = []
                config_interface = {}
                y = 0
                for x in item['configuration-interfaces-ip-address']:
                    try:
                        name = item['configuration-interfaces-name'][y]
                    except (IndexError, TypeError):
                        name = None
                    try:
                        primary = item['configuration-interfaces-primary'][y]
                    except (IndexError, TypeError):
                        primary = None
                    try:
                        notes = item['configuration-interfaces-notes'][y]
                    except (IndexError, TypeError):
                        notes = None
                    config_interface[y] = {
                        'ip': x, 'name': name, 'primary': primary,
                        'notes': notes}
                    y = y + 1
                for x in config_interface:
                    interface = {
                        'type': 'configuration_interfaces',
                        'attributes': {
                            'name': config_interface[x]['name'],
                            'ip-address': config_interface[x]['ip'],
                            'primary': config_interface[x]['primary'],
                            'notes': config_interface[x]['notes']}}
                    for y in dict(interface['attributes']):
                        if interface['attributes'][y] is None:
                            interface['attributes'].pop(y)
                    config_interface_items.append(interface)
                configuration = {
                    'type': 'configurations',
                    'attributes': {
                        'name': item['name'],
                        'configuration-type-id': item['configuration-type-id'],
                        'organization-id': item['organization-id'],
                        'configuration-status-id': item['configuration-status-id'],
                        'location-id': item['location-id'],
                        'contact-id': item['contact-id'],
                        'manufacturer-id': item['manufacturer-id'],
                        'model-id': item['model-id'],
                        'operating-system-id': item['operating-system-id'],
                        'operating-system-notes': item['operating-system-notes'],
                        'notes': item['notes'],
                        'hostname': item['hostname'],
                        'primary-ip': item['primary-ip'],
                        'mac-address': item['mac-address'],
                        'default-gateway': item['default-gateway'],
                        'serial-number': item['serial-number'],
                        'asset-tag': item['asset-tag'],
                        'position': item['position'],
                        'installed-by': item['installed-by'],
                        'purchased-by': item['purchased-by'],
                        'purchased-at': item['purchased-at'],
                        'warranty-expires-at': item['warranty-expires-at'],
                        'installed-at': item['installed-at']}}
                for y in dict(configuration['attributes']):
                    if configuration['attributes'][y] is None:
                        configuration['attributes'].pop(y)

                if config_interface_items != []:
                    configuration['relationships'] = {
                                        'configuration_interfaces': {
                                            'data': config_interface_items}}
                # config_items.append(configuration)
                data = {'data': configuration}
                self.common_post_request(urlDict['Configuration'], data)

    class FlexibleAsset:
        def __init__(self, common_load_data, common_merge_data,
                     common_convert_to_id, common_patch_request,
                     common_print, common_select_next, common_clear,
                     common_print_all, common_append_data, common_search):
            self.self = self
            self.rawdata = {'data': [], 'included': []}
            self.counter = 0
            self.common_load_data = common_load_data
            self.common_merge_data = common_merge_data
            self.common_convert_to_id = common_convert_to_id
            self.updates = []
            self.common_patch_request = common_patch_request
            self.common_print = common_print
            self.common_select_next = common_select_next
            self.common_clear = common_clear
            self.common_print_all = common_print_all
            self.common_append_data = common_append_data
            self.common_search = common_search

        def appendData(self, newdata):
            seld.common_append_data(self, newdata)

        def Clear(self):
            self.common_clear(self)

        def Print(self):
            self.common_print(self)

        def PrintAll(self):
            self.common_print_all(self)

        def Search(self, **kwargs):
            self.common_search(self, **kwargs)

        def SelectNext(self):
            self.common_select_next(self)

        def Select(self):
            noneditable = [
                'id', 'name', 'type', 'resource-url', 'restricted', 'my-glue',
                'flexible-asset-type-id', 'flexible-asset-type-name',
                'created-at', 'updated-at']
            self.update = {}
            update = False
            try:
                for x in self.item:
                    if x not in noneditable:
                        if self.item[x] != self.control[x]:
                            update = True
                            if x == 'organization-name':
                                organization_id = self.common_convert_to_id(
                                                    'org', self.item[x])
                                self.update['organization-id'] = organization_id
                            elif isinstance(self.control[x], dict):
                                if isinstance(self.item[x], list):
                                    self.update[x] = self.item[x]
                                else:
                                    error = (
                                     """Tagged Items in Flexible Assets\
                                        must be updated as a list of\
                                        ITGlue IDs.""")
                                    raise RuntimeError(error)
                            else:
                                self.update[x] = self.item[x]

            except AttributeError:
                pass

            if update:
                self.update['id'] = self.control['id']
                self.update['type'] = self.control['type']
                updatekeys = list(self.update.keys())
                itemkeys = list(self.item.keys())
                for x in list(itemkeys):
                    if x in noneditable:
                        itemkeys.remove(x)
                    elif x in updatekeys:
                        itemkeys.remove(x)
                for x in itemkeys:
                    if isinstance(self.control[x], dict):
                        idlist = []
                        for y in self.control[x]['values']:
                            idlist.append(y['id'])
                        self.update[x] = idlist
                    else:
                        self.update[x] = self.control[x]
                self.update.pop('organization-name')
                self.updates.append(self.update)

            self.item = self.common_load_data(
                                            self.rawdata['data'][self.counter],
                                            self.rawdata)
            self.control = dict(self.item)

        def Update(self):
            url = urlDict['Flexible Asset']
            self.Select()
            update = {'data': []}
            for x in self.updates:
                updatequeue = {
                    'type': x.pop('type'),
                    'attributes': {'id': x.pop('id'),
                                   'organization-id': x.pop('organization-id'),
                                   'traits': {}}}
                for y in x:
                    updatequeue['attributes']['traits'][y] = x[y]
                if len(self.updates) == 1:
                    id = updatequeue['attributes'].pop('id')
                    url = url+'/'+id
                    update['data'] = updatequeue
                else:
                    update['data'].append(updatequeue)
            self.updatetest = update
            self.updates = []

            self.common_patch_request(url, update)

# There is something wrong with the Contacts query with org ids.
# It queries with 'filter[organization_id]=' but it needs
# to be 'organization_id=' for contacts.

    class Contacts:
        def __init__(self, common_load_data, common_merge_data,
                     common_convert_to_id, common_patch_request,
                     common_format_update, common_print, common_select_next,
                     common_clear, common_print_all, common_append_data,
                     common_search, common_select):

            self.self = self
            self.rawdata = {'data': [], 'included': []}
            self.counter = 0
            self.common_load_data = common_load_data
            self.common_merge_data = common_merge_data
            self.common_convert_to_id = common_convert_to_id
            self.updates = []
            self.common_patch_request = common_patch_request
            self.common_format_update = common_format_update
            self.common_print = common_print
            self.common_select_next = common_select_next
            self.common_clear = common_clear
            self.common_print_all = common_print_all
            self.common_append_data = common_append_data
            self.common_search = common_search
            self.common_select = common_select

        def appendData(self, newdata):
            self.common_append_data(self, newdata)

        def Clear(self):
            self.common_clear(self)

        def Print(self):
            self.common_print(self)

        def PrintAll(self):
            self.common_print_all(self)

        def Search(self, **kwargs):
            self.common_search(self, **kwargs)

        def SelectNext(self):
            self.common_select_next(self)

        # Need to add support for editing email/phone numbers
        def Select(self):
            editable = [
                'organization-id', 'contact-type-id', 'location-id',
                'first-name', 'last-name', 'title', 'important', 'notes'
                ]
            canconvert = [
                'organization-name', 'contact-type-name']

            self.common_select(self, editable, canconvert)

    class Organizations:
        def __init__(self, common_load_data, common_merge_data,
                     common_convert_to_id, common_patch_request,
                     common_format_update, common_print, common_select_next,
                     common_clear, common_print_all, common_append_data,
                     common_search, common_select):

            self.self = self
            self.rawdata = {'data': [], 'included': []}
            self.counter = 0
            self.common_load_data = common_load_data
            self.common_merge_data = common_merge_data
            self.common_convert_to_id = common_convert_to_id
            self.updates = []
            self.common_patch_request = common_patch_request
            self.common_format_update = common_format_update
            self.common_print = common_print
            self.common_select_next = common_select_next
            self.common_clear = common_clear
            self.common_print_all = common_print_all
            self.common_append_data = common_append_data
            self.common_search = common_search
            self.common_select = common_select

        def appendData(self, newdata):
            self.common_append_data(self, newdata)

        def Clear(self):
            self.common_clear(self)

        def Print(self):
            self.common_print(self)

        def PrintAll(self):
            self.common_print_all(self)

        def Search(self, **kwargs):
            self.common_search(self, **kwargs)

        def SelectNext(self):
            self.common_select_next(self)

        def Select(self):
            editable = [
                'name', 'alert', 'description', 'organization-type-id',
                'organization-status-id', 'quick-notes', 'quick-notes',
                'short-name']
            canconvert = [
                'organization-type-name', 'organization-status-name']

            self.common_select(self, editable, canconvert)
