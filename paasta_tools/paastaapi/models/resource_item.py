"""
    Paasta API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""
import pprint
import re  # noqa: F401

import six

from paasta_tools.paastaapi.configuration import Configuration


class ResourceItem:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "cpus": "ResourceValue",
        "disk": "ResourceValue",
        "groupings": "object",
        "mem": "ResourceValue",
    }

    attribute_map = {
        "cpus": "cpus",
        "disk": "disk",
        "groupings": "groupings",
        "mem": "mem",
    }

    def __init__(
        self,
        cpus=None,
        disk=None,
        groupings=None,
        mem=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """ResourceItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cpus = None
        self._disk = None
        self._groupings = None
        self._mem = None
        self.discriminator = None

        if cpus is not None:
            self.cpus = cpus
        if disk is not None:
            self.disk = disk
        if groupings is not None:
            self.groupings = groupings
        if mem is not None:
            self.mem = mem

    @property
    def cpus(self):
        """Gets the cpus of this ResourceItem.  # noqa: E501


        :return: The cpus of this ResourceItem.  # noqa: E501
        :rtype: ResourceValue
        """
        return self._cpus

    @cpus.setter
    def cpus(self, cpus):
        """Sets the cpus of this ResourceItem.


        :param cpus: The cpus of this ResourceItem.  # noqa: E501
        :type: ResourceValue
        """

        self._cpus = cpus

    @property
    def disk(self):
        """Gets the disk of this ResourceItem.  # noqa: E501


        :return: The disk of this ResourceItem.  # noqa: E501
        :rtype: ResourceValue
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        """Sets the disk of this ResourceItem.


        :param disk: The disk of this ResourceItem.  # noqa: E501
        :type: ResourceValue
        """

        self._disk = disk

    @property
    def groupings(self):
        """Gets the groupings of this ResourceItem.  # noqa: E501


        :return: The groupings of this ResourceItem.  # noqa: E501
        :rtype: object
        """
        return self._groupings

    @groupings.setter
    def groupings(self, groupings):
        """Sets the groupings of this ResourceItem.


        :param groupings: The groupings of this ResourceItem.  # noqa: E501
        :type: object
        """

        self._groupings = groupings

    @property
    def mem(self):
        """Gets the mem of this ResourceItem.  # noqa: E501


        :return: The mem of this ResourceItem.  # noqa: E501
        :rtype: ResourceValue
        """
        return self._mem

    @mem.setter
    def mem(self, mem):
        """Sets the mem of this ResourceItem.


        :param mem: The mem of this ResourceItem.  # noqa: E501
        :type: ResourceValue
        """

        self._mem = mem

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResourceItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResourceItem):
            return True

        return self.to_dict() != other.to_dict()