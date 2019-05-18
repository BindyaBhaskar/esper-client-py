# coding: utf-8

"""
Esper APIs

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
import re

import six

from esperclient.models.emm_enterprise_state_enum import EMMEnterpriseStateEnum


class GoogleEnterprise(object):
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
        'id': 'int',
        'google_enterprise_id': 'str',
        'name': 'str',
        'state': 'EMMEnterpriseStateEnum',
        'callback_url': 'str',
        'signup_url': 'str',
        'completion_token': 'str',
        'enterprise_token': 'str',
        'is_active': 'bool',
        'created_on': 'datetime',
        'updated_on': 'datetime',
        'enterprise': 'str'
    }

    attribute_map = {
        'id': 'id',
        'google_enterprise_id': 'google_enterprise_id',
        'name': 'name',
        'state': 'state',
        'callback_url': 'callback_url',
        'signup_url': 'signup_url',
        'completion_token': 'completion_token',
        'enterprise_token': 'enterprise_token',
        'is_active': 'is_active',
        'created_on': 'created_on',
        'updated_on': 'updated_on',
        'enterprise': 'enterprise'
    }

    def __init__(self, id=None, google_enterprise_id=None, name=None, state=None, callback_url=None, signup_url=None, completion_token=None, enterprise_token=None, is_active=None, created_on=None, updated_on=None, enterprise=None):
        """GoogleEnterprise - a model defined in Swagger"""

        self._id = None
        self._google_enterprise_id = None
        self._name = None
        self._state = None
        self._callback_url = None
        self._signup_url = None
        self._completion_token = None
        self._enterprise_token = None
        self._is_active = None
        self._created_on = None
        self._updated_on = None
        self._enterprise = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if google_enterprise_id is not None:
            self.google_enterprise_id = google_enterprise_id
        self.name = name
        if state is not None:
            self.state = state
        if callback_url is not None:
            self.callback_url = callback_url
        if signup_url is not None:
            self.signup_url = signup_url
        if completion_token is not None:
            self.completion_token = completion_token
        if enterprise_token is not None:
            self.enterprise_token = enterprise_token
        if is_active is not None:
            self.is_active = is_active
        if created_on is not None:
            self.created_on = created_on
        if updated_on is not None:
            self.updated_on = updated_on
        if enterprise is not None:
            self.enterprise = enterprise

    @property
    def id(self):
        """Gets the id of this GoogleEnterprise.


        :return: The id of this GoogleEnterprise.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GoogleEnterprise.


        :param id: The id of this GoogleEnterprise.
        :type: int
        """

        self._id = id

    @property
    def google_enterprise_id(self):
        """Gets the google_enterprise_id of this GoogleEnterprise.


        :return: The google_enterprise_id of this GoogleEnterprise.
        :rtype: str
        """
        return self._google_enterprise_id

    @google_enterprise_id.setter
    def google_enterprise_id(self, google_enterprise_id):
        """Sets the google_enterprise_id of this GoogleEnterprise.


        :param google_enterprise_id: The google_enterprise_id of this GoogleEnterprise.
        :type: str
        """
        if google_enterprise_id is not None and len(google_enterprise_id) > 50:
            raise ValueError("Invalid value for `google_enterprise_id`, length must be less than or equal to `50`")
        if google_enterprise_id is not None and len(google_enterprise_id) < 1:
            raise ValueError("Invalid value for `google_enterprise_id`, length must be greater than or equal to `1`")

        self._google_enterprise_id = google_enterprise_id

    @property
    def name(self):
        """Gets the name of this GoogleEnterprise.


        :return: The name of this GoogleEnterprise.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GoogleEnterprise.


        :param name: The name of this GoogleEnterprise.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def state(self):
        """Gets the state of this GoogleEnterprise.


        :return: The state of this GoogleEnterprise.
        :rtype: EMMEnterpriseStateEnum
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this GoogleEnterprise.


        :param state: The state of this GoogleEnterprise.
        :type: EMMEnterpriseStateEnum
        """

        self._state = state

    @property
    def callback_url(self):
        """Gets the callback_url of this GoogleEnterprise.


        :return: The callback_url of this GoogleEnterprise.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        """Sets the callback_url of this GoogleEnterprise.


        :param callback_url: The callback_url of this GoogleEnterprise.
        :type: str
        """
        if callback_url is not None and len(callback_url) < 1:
            raise ValueError("Invalid value for `callback_url`, length must be greater than or equal to `1`")

        self._callback_url = callback_url

    @property
    def signup_url(self):
        """Gets the signup_url of this GoogleEnterprise.


        :return: The signup_url of this GoogleEnterprise.
        :rtype: str
        """
        return self._signup_url

    @signup_url.setter
    def signup_url(self, signup_url):
        """Sets the signup_url of this GoogleEnterprise.


        :param signup_url: The signup_url of this GoogleEnterprise.
        :type: str
        """
        if signup_url is not None and len(signup_url) < 1:
            raise ValueError("Invalid value for `signup_url`, length must be greater than or equal to `1`")

        self._signup_url = signup_url

    @property
    def completion_token(self):
        """Gets the completion_token of this GoogleEnterprise.


        :return: The completion_token of this GoogleEnterprise.
        :rtype: str
        """
        return self._completion_token

    @completion_token.setter
    def completion_token(self, completion_token):
        """Sets the completion_token of this GoogleEnterprise.


        :param completion_token: The completion_token of this GoogleEnterprise.
        :type: str
        """
        if completion_token is not None and len(completion_token) > 255:
            raise ValueError("Invalid value for `completion_token`, length must be less than or equal to `255`")
        if completion_token is not None and len(completion_token) < 1:
            raise ValueError("Invalid value for `completion_token`, length must be greater than or equal to `1`")

        self._completion_token = completion_token

    @property
    def enterprise_token(self):
        """Gets the enterprise_token of this GoogleEnterprise.


        :return: The enterprise_token of this GoogleEnterprise.
        :rtype: str
        """
        return self._enterprise_token

    @enterprise_token.setter
    def enterprise_token(self, enterprise_token):
        """Sets the enterprise_token of this GoogleEnterprise.


        :param enterprise_token: The enterprise_token of this GoogleEnterprise.
        :type: str
        """
        if enterprise_token is not None and len(enterprise_token) > 255:
            raise ValueError("Invalid value for `enterprise_token`, length must be less than or equal to `255`")
        if enterprise_token is not None and len(enterprise_token) < 1:
            raise ValueError("Invalid value for `enterprise_token`, length must be greater than or equal to `1`")

        self._enterprise_token = enterprise_token

    @property
    def is_active(self):
        """Gets the is_active of this GoogleEnterprise.


        :return: The is_active of this GoogleEnterprise.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this GoogleEnterprise.


        :param is_active: The is_active of this GoogleEnterprise.
        :type: bool
        """

        self._is_active = is_active

    @property
    def created_on(self):
        """Gets the created_on of this GoogleEnterprise.


        :return: The created_on of this GoogleEnterprise.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this GoogleEnterprise.


        :param created_on: The created_on of this GoogleEnterprise.
        :type: datetime
        """

        self._created_on = created_on

    @property
    def updated_on(self):
        """Gets the updated_on of this GoogleEnterprise.


        :return: The updated_on of this GoogleEnterprise.
        :rtype: datetime
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this GoogleEnterprise.


        :param updated_on: The updated_on of this GoogleEnterprise.
        :type: datetime
        """

        self._updated_on = updated_on

    @property
    def enterprise(self):
        """Gets the enterprise of this GoogleEnterprise.


        :return: The enterprise of this GoogleEnterprise.
        :rtype: str
        """
        return self._enterprise

    @enterprise.setter
    def enterprise(self, enterprise):
        """Sets the enterprise of this GoogleEnterprise.


        :param enterprise: The enterprise of this GoogleEnterprise.
        :type: str
        """

        self._enterprise = enterprise

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
        if issubclass(GoogleEnterprise, dict):
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
        if not isinstance(other, GoogleEnterprise):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
