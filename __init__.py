import requests
import json
import types

urlDict={
    'configurations': 'https://api.itglue.com/configurations',
    'configuration_interfaces': 'https://api.itglue.com/configuration_interfaces',
    'configuration_statuses': 'https://api.itglue.com/configuration_statuses',
    'configuration_types': 'https://api.itglue.com/configuration_types',
    'contacts': 'https://api.itglue.com/contacts',
    'contact_types': 'https://api.itglue.com/contact_types',
    'countries': 'https://api.itglue.com/countries',
    'flexible_asset': 'https://api.itglue.com/flexible_assets',
    'flexible_asset_fields': 'https://api.itglue.com/flexible_assets_fields',
    'flexible_asset_types': 'https://api.itglue.com/flexible_asset_types',
    'locations': 'https://api.itglue.com/locations',
    'manufacturers': 'https://api.itglue.com/manufacturers',
    'models': 'https://api.itglue.com/models',
    'operating_systems': 'https://api.itglue.com/operating_systems',
    'organizations': 'https://api.itglue.com/organizations',
    'organization_status': 'https://api.itglue.com/organization_status',
    'organization_types': 'https://api.itglue.com/organization_types',
    'password': 'https://api.itglue.com/passwords',
    'password_categories': 'https://api.itglue.com/password_categories',
    'platforms': 'https://api.itglue.com/platforms',
    'regions': 'https://api.itglue.com/regions',
    }

filterDict={
    'id': 'filter[id]=',
    'name': 'filter[name]=',
    'org-id': 'filter[organization_id]=',
    'config-type': 'filter[configuration_type_id]=',
    'config-status': 'filter[configuration_status_id]=',
    'contact-id': 'filter[contact_id]=',
    'serial-num': 'filter[serial_number]=',
    'rmm-id': 'filter[rmm_id]=',
    'rmm': 'filter[rmm_integration_type]=',
    'organization_type_id': 'filer[organization_type_id]=',
    'organization_status_id': 'filter[organization_status_id]=',
    'created_at': 'filter[created_at]=',
    'updated_at': 'filter[updated_at]=',
    'my_glue_account_id': 'filter[my_glue_account_id]=',
    'password_category_id': 'filter[password_category_id]=',
    'url': 'filter[url]=',
    'cached_resource_name': 'filter[cached_resource_name]=',
    'exclude_id': 'filter[exclude][id]=',
    'exclude_name': 'filter[exclude][name]=',
    'exclude_organization_type_id': 'filter[exclude][organization_type_id]=',
    'exclude_organization_status_id': 'filter[exclude][organization_status_id]=',
    'flexible_asset_type_id': 'filter[flexible_asset_type_id]=',
    'first_name': 'filter[first_name]=',
    'last_name': 'filter[last_name]=',
    'title': 'filter[title]=',
    'contact_type_id': 'filter[contact_type_id]',
    'important': 'filter[important]',
    'primary_email': 'filter[primary_email]',
    'city': 'filter[city]',
    'region_id': 'filter[region_id]',
    'country_id': 'filter[country_id]',
}

includeDict={
    'configuration_interfaces': 'include=configuration_interfaces',
    'rmm_record': 'include=rmm_records',
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
