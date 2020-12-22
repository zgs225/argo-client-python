# coding: utf-8

"""
    Argo Server API

    You can get examples of requests and responses by using the CLI with `--gloglevel=9`, e.g. `argo list --gloglevel=9`  # noqa: E501

    The version of the OpenAPI document: v2.12.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from argo.workflows.client.configuration import Configuration


class V1alpha1GetUserInfoResponse(object):
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
        'groups': 'list[str]',
        'issuer': 'str',
        'subject': 'str'
    }

    attribute_map = {
        'groups': 'groups',
        'issuer': 'issuer',
        'subject': 'subject'
    }

    def __init__(self, groups=None, issuer=None, subject=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1GetUserInfoResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._groups = None
        self._issuer = None
        self._subject = None
        self.discriminator = None

        if groups is not None:
            self.groups = groups
        if issuer is not None:
            self.issuer = issuer
        if subject is not None:
            self.subject = subject

    @property
    def groups(self):
        """Gets the groups of this V1alpha1GetUserInfoResponse.  # noqa: E501


        :return: The groups of this V1alpha1GetUserInfoResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this V1alpha1GetUserInfoResponse.


        :param groups: The groups of this V1alpha1GetUserInfoResponse.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def issuer(self):
        """Gets the issuer of this V1alpha1GetUserInfoResponse.  # noqa: E501


        :return: The issuer of this V1alpha1GetUserInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this V1alpha1GetUserInfoResponse.


        :param issuer: The issuer of this V1alpha1GetUserInfoResponse.  # noqa: E501
        :type: str
        """

        self._issuer = issuer

    @property
    def subject(self):
        """Gets the subject of this V1alpha1GetUserInfoResponse.  # noqa: E501


        :return: The subject of this V1alpha1GetUserInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this V1alpha1GetUserInfoResponse.


        :param subject: The subject of this V1alpha1GetUserInfoResponse.  # noqa: E501
        :type: str
        """

        self._subject = subject

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
        if not isinstance(other, V1alpha1GetUserInfoResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1GetUserInfoResponse):
            return True

        return self.to_dict() != other.to_dict()
