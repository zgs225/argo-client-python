# coding: utf-8

"""
    Argo

    Python client for Argo Workflows  # noqa: E501

    The version of the OpenAPI document: 2.10.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from argo.workflows.client.configuration import Configuration


class V1QuobyteVolumeSource(object):
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
        'group': 'str',
        'read_only': 'bool',
        'registry': 'str',
        'tenant': 'str',
        'user': 'str',
        'volume': 'str'
    }

    attribute_map = {
        'group': 'group',
        'read_only': 'readOnly',
        'registry': 'registry',
        'tenant': 'tenant',
        'user': 'user',
        'volume': 'volume'
    }

    def __init__(self, group=None, read_only=None, registry=None, tenant=None, user=None, volume=None, local_vars_configuration=None):  # noqa: E501
        """V1QuobyteVolumeSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._group = None
        self._read_only = None
        self._registry = None
        self._tenant = None
        self._user = None
        self._volume = None
        self.discriminator = None

        if group is not None:
            self.group = group
        if read_only is not None:
            self.read_only = read_only
        self.registry = registry
        if tenant is not None:
            self.tenant = tenant
        if user is not None:
            self.user = user
        self.volume = volume

    @property
    def group(self):
        """Gets the group of this V1QuobyteVolumeSource.  # noqa: E501

        Group to map volume access to Default is no group  # noqa: E501

        :return: The group of this V1QuobyteVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this V1QuobyteVolumeSource.

        Group to map volume access to Default is no group  # noqa: E501

        :param group: The group of this V1QuobyteVolumeSource.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def read_only(self):
        """Gets the read_only of this V1QuobyteVolumeSource.  # noqa: E501

        ReadOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false.  # noqa: E501

        :return: The read_only of this V1QuobyteVolumeSource.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this V1QuobyteVolumeSource.

        ReadOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false.  # noqa: E501

        :param read_only: The read_only of this V1QuobyteVolumeSource.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def registry(self):
        """Gets the registry of this V1QuobyteVolumeSource.  # noqa: E501

        Registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes  # noqa: E501

        :return: The registry of this V1QuobyteVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._registry

    @registry.setter
    def registry(self, registry):
        """Sets the registry of this V1QuobyteVolumeSource.

        Registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes  # noqa: E501

        :param registry: The registry of this V1QuobyteVolumeSource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and registry is None:  # noqa: E501
            raise ValueError("Invalid value for `registry`, must not be `None`")  # noqa: E501

        self._registry = registry

    @property
    def tenant(self):
        """Gets the tenant of this V1QuobyteVolumeSource.  # noqa: E501

        Tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin  # noqa: E501

        :return: The tenant of this V1QuobyteVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this V1QuobyteVolumeSource.

        Tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin  # noqa: E501

        :param tenant: The tenant of this V1QuobyteVolumeSource.  # noqa: E501
        :type: str
        """

        self._tenant = tenant

    @property
    def user(self):
        """Gets the user of this V1QuobyteVolumeSource.  # noqa: E501

        User to map volume access to Defaults to serivceaccount user  # noqa: E501

        :return: The user of this V1QuobyteVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this V1QuobyteVolumeSource.

        User to map volume access to Defaults to serivceaccount user  # noqa: E501

        :param user: The user of this V1QuobyteVolumeSource.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def volume(self):
        """Gets the volume of this V1QuobyteVolumeSource.  # noqa: E501

        Volume is a string that references an already created Quobyte volume by name.  # noqa: E501

        :return: The volume of this V1QuobyteVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this V1QuobyteVolumeSource.

        Volume is a string that references an already created Quobyte volume by name.  # noqa: E501

        :param volume: The volume of this V1QuobyteVolumeSource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and volume is None:  # noqa: E501
            raise ValueError("Invalid value for `volume`, must not be `None`")  # noqa: E501

        self._volume = volume

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1QuobyteVolumeSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1QuobyteVolumeSource):
            return True

        return self.to_dict() != other.to_dict()
