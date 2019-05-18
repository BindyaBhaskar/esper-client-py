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


class EnterpriseDetail(object):
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
        'id': 'str',
        'registered_name': 'str',
        'registered_address': 'str',
        'location': 'str',
        'zipcode': 'str',
        'contact_person': 'str',
        'contact_number': 'str',
        'contact_email': 'str',
        'created_on': 'datetime',
        'updated_on': 'datetime',
        'is_active': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'registered_name': 'registered_name',
        'registered_address': 'registered_address',
        'location': 'location',
        'zipcode': 'zipcode',
        'contact_person': 'contact_person',
        'contact_number': 'contact_number',
        'contact_email': 'contact_email',
        'created_on': 'created_on',
        'updated_on': 'updated_on',
        'is_active': 'is_active'
    }

    def __init__(self, id=None, registered_name=None, registered_address=None, location=None, zipcode=None, contact_person=None, contact_number=None, contact_email=None, created_on=None, updated_on=None, is_active=None):
        """EnterpriseDetail - a model defined in Swagger"""

        self._id = None
        self._registered_name = None
        self._registered_address = None
        self._location = None
        self._zipcode = None
        self._contact_person = None
        self._contact_number = None
        self._contact_email = None
        self._created_on = None
        self._updated_on = None
        self._is_active = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.registered_name = registered_name
        self.registered_address = registered_address
        self.location = location
        self.zipcode = zipcode
        if contact_person is not None:
            self.contact_person = contact_person
        if contact_number is not None:
            self.contact_number = contact_number
        self.contact_email = contact_email
        if created_on is not None:
            self.created_on = created_on
        if updated_on is not None:
            self.updated_on = updated_on
        if is_active is not None:
            self.is_active = is_active

    @property
    def id(self):
        """Gets the id of this EnterpriseDetail.


        :return: The id of this EnterpriseDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EnterpriseDetail.


        :param id: The id of this EnterpriseDetail.
        :type: str
        """

        self._id = id

    @property
    def registered_name(self):
        """Gets the registered_name of this EnterpriseDetail.


        :return: The registered_name of this EnterpriseDetail.
        :rtype: str
        """
        return self._registered_name

    @registered_name.setter
    def registered_name(self, registered_name):
        """Sets the registered_name of this EnterpriseDetail.


        :param registered_name: The registered_name of this EnterpriseDetail.
        :type: str
        """
        if registered_name is None:
            raise ValueError("Invalid value for `registered_name`, must not be `None`")
        if registered_name is not None and len(registered_name) > 255:
            raise ValueError("Invalid value for `registered_name`, length must be less than or equal to `255`")
        if registered_name is not None and len(registered_name) < 1:
            raise ValueError("Invalid value for `registered_name`, length must be greater than or equal to `1`")

        self._registered_name = registered_name

    @property
    def registered_address(self):
        """Gets the registered_address of this EnterpriseDetail.


        :return: The registered_address of this EnterpriseDetail.
        :rtype: str
        """
        return self._registered_address

    @registered_address.setter
    def registered_address(self, registered_address):
        """Sets the registered_address of this EnterpriseDetail.


        :param registered_address: The registered_address of this EnterpriseDetail.
        :type: str
        """
        if registered_address is None:
            raise ValueError("Invalid value for `registered_address`, must not be `None`")
        if registered_address is not None and len(registered_address) < 1:
            raise ValueError("Invalid value for `registered_address`, length must be greater than or equal to `1`")

        self._registered_address = registered_address

    @property
    def location(self):
        """Gets the location of this EnterpriseDetail.


        :return: The location of this EnterpriseDetail.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this EnterpriseDetail.


        :param location: The location of this EnterpriseDetail.
        :type: str
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")
        if location is not None and len(location) > 255:
            raise ValueError("Invalid value for `location`, length must be less than or equal to `255`")
        if location is not None and len(location) < 1:
            raise ValueError("Invalid value for `location`, length must be greater than or equal to `1`")

        self._location = location

    @property
    def zipcode(self):
        """Gets the zipcode of this EnterpriseDetail.


        :return: The zipcode of this EnterpriseDetail.
        :rtype: str
        """
        return self._zipcode

    @zipcode.setter
    def zipcode(self, zipcode):
        """Sets the zipcode of this EnterpriseDetail.


        :param zipcode: The zipcode of this EnterpriseDetail.
        :type: str
        """
        if zipcode is None:
            raise ValueError("Invalid value for `zipcode`, must not be `None`")
        if zipcode is not None and len(zipcode) > 8:
            raise ValueError("Invalid value for `zipcode`, length must be less than or equal to `8`")
        if zipcode is not None and len(zipcode) < 1:
            raise ValueError("Invalid value for `zipcode`, length must be greater than or equal to `1`")

        self._zipcode = zipcode

    @property
    def contact_person(self):
        """Gets the contact_person of this EnterpriseDetail.


        :return: The contact_person of this EnterpriseDetail.
        :rtype: str
        """
        return self._contact_person

    @contact_person.setter
    def contact_person(self, contact_person):
        """Sets the contact_person of this EnterpriseDetail.


        :param contact_person: The contact_person of this EnterpriseDetail.
        :type: str
        """
        if contact_person is not None and len(contact_person) > 255:
            raise ValueError("Invalid value for `contact_person`, length must be less than or equal to `255`")
        if contact_person is not None and len(contact_person) < 1:
            raise ValueError("Invalid value for `contact_person`, length must be greater than or equal to `1`")

        self._contact_person = contact_person

    @property
    def contact_number(self):
        """Gets the contact_number of this EnterpriseDetail.


        :return: The contact_number of this EnterpriseDetail.
        :rtype: str
        """
        return self._contact_number

    @contact_number.setter
    def contact_number(self, contact_number):
        """Sets the contact_number of this EnterpriseDetail.


        :param contact_number: The contact_number of this EnterpriseDetail.
        :type: str
        """
        if contact_number is not None and len(contact_number) > 20:
            raise ValueError("Invalid value for `contact_number`, length must be less than or equal to `20`")
        if contact_number is not None and len(contact_number) < 1:
            raise ValueError("Invalid value for `contact_number`, length must be greater than or equal to `1`")

        self._contact_number = contact_number

    @property
    def contact_email(self):
        """Gets the contact_email of this EnterpriseDetail.


        :return: The contact_email of this EnterpriseDetail.
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this EnterpriseDetail.


        :param contact_email: The contact_email of this EnterpriseDetail.
        :type: str
        """
        if contact_email is None:
            raise ValueError("Invalid value for `contact_email`, must not be `None`")
        if contact_email is not None and len(contact_email) > 254:
            raise ValueError("Invalid value for `contact_email`, length must be less than or equal to `254`")
        if contact_email is not None and len(contact_email) < 1:
            raise ValueError("Invalid value for `contact_email`, length must be greater than or equal to `1`")

        self._contact_email = contact_email

    @property
    def created_on(self):
        """Gets the created_on of this EnterpriseDetail.


        :return: The created_on of this EnterpriseDetail.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this EnterpriseDetail.


        :param created_on: The created_on of this EnterpriseDetail.
        :type: datetime
        """

        self._created_on = created_on

    @property
    def updated_on(self):
        """Gets the updated_on of this EnterpriseDetail.


        :return: The updated_on of this EnterpriseDetail.
        :rtype: datetime
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this EnterpriseDetail.


        :param updated_on: The updated_on of this EnterpriseDetail.
        :type: datetime
        """

        self._updated_on = updated_on

    @property
    def is_active(self):
        """Gets the is_active of this EnterpriseDetail.


        :return: The is_active of this EnterpriseDetail.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this EnterpriseDetail.


        :param is_active: The is_active of this EnterpriseDetail.
        :type: bool
        """

        self._is_active = is_active

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
        if issubclass(EnterpriseDetail, dict):
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
        if not isinstance(other, EnterpriseDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
