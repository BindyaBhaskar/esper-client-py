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



import pprint
import re  # noqa: F401

import six

from esperclient.models.device_custom_group import DeviceCustomGroup  # noqa: F401,E501


class DeviceCustom(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'id': 'str',
        'state': 'int',
        'suid': 'str',
        'created_on': 'datetime',
        'updated_on': 'datetime',
        'is_active': 'bool',
        'groups': 'list[DeviceCustomGroup]',
        'device_name': 'str',
        'provisioned_on': 'datetime'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'state': 'state',
        'suid': 'suid',
        'created_on': 'created_on',
        'updated_on': 'updated_on',
        'is_active': 'is_active',
        'groups': 'groups',
        'device_name': 'device_name',
        'provisioned_on': 'provisioned_on'
    }

    def __init__(self, name=None, id=None, state=None, suid=None, created_on=None, updated_on=None, is_active=None, groups=None, device_name=None, provisioned_on=None):  # noqa: E501
        """DeviceCustom - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._id = None
        self._state = None
        self._suid = None
        self._created_on = None
        self._updated_on = None
        self._is_active = None
        self._groups = None
        self._device_name = None
        self._provisioned_on = None
        self.discriminator = None

        self.name = name
        if id is not None:
            self.id = id
        if state is not None:
            self.state = state
        if suid is not None:
            self.suid = suid
        if created_on is not None:
            self.created_on = created_on
        if updated_on is not None:
            self.updated_on = updated_on
        if is_active is not None:
            self.is_active = is_active
        self.groups = groups
        if device_name is not None:
            self.device_name = device_name
        if provisioned_on is not None:
            self.provisioned_on = provisioned_on

    @property
    def name(self):
        """Gets the name of this DeviceCustom.  # noqa: E501


        :return: The name of this DeviceCustom.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceCustom.


        :param name: The name of this DeviceCustom.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this DeviceCustom.  # noqa: E501


        :return: The id of this DeviceCustom.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceCustom.


        :param id: The id of this DeviceCustom.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def state(self):
        """Gets the state of this DeviceCustom.  # noqa: E501


        :return: The state of this DeviceCustom.  # noqa: E501
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DeviceCustom.


        :param state: The state of this DeviceCustom.  # noqa: E501
        :type: int
        """

        self._state = state

    @property
    def suid(self):
        """Gets the suid of this DeviceCustom.  # noqa: E501

        Esper unique device id  # noqa: E501

        :return: The suid of this DeviceCustom.  # noqa: E501
        :rtype: str
        """
        return self._suid

    @suid.setter
    def suid(self, suid):
        """Sets the suid of this DeviceCustom.

        Esper unique device id  # noqa: E501

        :param suid: The suid of this DeviceCustom.  # noqa: E501
        :type: str
        """
        if suid is not None and len(suid) > 255:
            raise ValueError("Invalid value for `suid`, length must be less than or equal to `255`")  # noqa: E501
        if suid is not None and len(suid) < 1:
            raise ValueError("Invalid value for `suid`, length must be greater than or equal to `1`")  # noqa: E501

        self._suid = suid

    @property
    def created_on(self):
        """Gets the created_on of this DeviceCustom.  # noqa: E501


        :return: The created_on of this DeviceCustom.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this DeviceCustom.


        :param created_on: The created_on of this DeviceCustom.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def updated_on(self):
        """Gets the updated_on of this DeviceCustom.  # noqa: E501


        :return: The updated_on of this DeviceCustom.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this DeviceCustom.


        :param updated_on: The updated_on of this DeviceCustom.  # noqa: E501
        :type: datetime
        """

        self._updated_on = updated_on

    @property
    def is_active(self):
        """Gets the is_active of this DeviceCustom.  # noqa: E501


        :return: The is_active of this DeviceCustom.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this DeviceCustom.


        :param is_active: The is_active of this DeviceCustom.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def groups(self):
        """Gets the groups of this DeviceCustom.  # noqa: E501


        :return: The groups of this DeviceCustom.  # noqa: E501
        :rtype: list[DeviceCustomGroup]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this DeviceCustom.


        :param groups: The groups of this DeviceCustom.  # noqa: E501
        :type: list[DeviceCustomGroup]
        """
        if groups is None:
            raise ValueError("Invalid value for `groups`, must not be `None`")  # noqa: E501

        self._groups = groups

    @property
    def device_name(self):
        """Gets the device_name of this DeviceCustom.  # noqa: E501


        :return: The device_name of this DeviceCustom.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this DeviceCustom.


        :param device_name: The device_name of this DeviceCustom.  # noqa: E501
        :type: str
        """
        if device_name is not None and len(device_name) < 1:
            raise ValueError("Invalid value for `device_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._device_name = device_name

    @property
    def provisioned_on(self):
        """Gets the provisioned_on of this DeviceCustom.  # noqa: E501


        :return: The provisioned_on of this DeviceCustom.  # noqa: E501
        :rtype: datetime
        """
        return self._provisioned_on

    @provisioned_on.setter
    def provisioned_on(self, provisioned_on):
        """Sets the provisioned_on of this DeviceCustom.


        :param provisioned_on: The provisioned_on of this DeviceCustom.  # noqa: E501
        :type: datetime
        """

        self._provisioned_on = provisioned_on

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DeviceCustom, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeviceCustom):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other