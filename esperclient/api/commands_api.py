# coding: utf-8

"""
Esper Manage API

OpenAPI spec version: 1.0.0
Contact: developer@esper.io
---------------------------------------------------------

Copyright 2019 Shoonya Enterprises Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""



from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six

from esperclient.api_client import ApiClient


class CommandsApi(object):
    """NOTE: This class is auto generated.

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def run_command(self, enterprise_id, device_id, command, **kwargs):
        """Run commands on device

        Fire commands on device like lock, ping etc
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.run_command(enterprise_id, device_id, command, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: ID of the enterprise (required)
        :param str device_id: ID of the device (required)
        :param CommandRequest command: command name to fire (required)
        :return: DeviceCommand
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.run_command_with_http_info(enterprise_id, device_id, command, **kwargs)
        else:
            (data) = self.run_command_with_http_info(enterprise_id, device_id, command, **kwargs)
            return data

    def run_command_with_http_info(self, enterprise_id, device_id, command, **kwargs):
        """Run commands on device

        Fire commands on device like lock, ping etc
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.run_command_with_http_info(enterprise_id, device_id, command, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: ID of the enterprise (required)
        :param str device_id: ID of the device (required)
        :param CommandRequest command: command name to fire (required)
        :return: DeviceCommand
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['enterprise_id', 'device_id', 'command']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method run_command" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `run_command`")
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `run_command`")
        # verify the required parameter 'command' is set
        if ('command' not in params or
                params['command'] is None):
            raise ValueError("Missing the required parameter `command` when calling `run_command`")

        collection_formats = {}

        path_params = {}
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']
        if 'device_id' in params:
            path_params['device_id'] = params['device_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'command' in params:
            body_params = params['command']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # Authentication setting
        auth_settings = ['apiKey']

        return self.api_client.call_api(
            '/enterprise/{enterprise_id}/device/{device_id}/command/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceCommand',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)