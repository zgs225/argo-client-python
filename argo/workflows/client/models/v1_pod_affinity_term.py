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


class V1PodAffinityTerm(object):
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
        'label_selector': 'V1LabelSelector',
        'namespaces': 'list[str]',
        'topology_key': 'str'
    }

    attribute_map = {
        'label_selector': 'labelSelector',
        'namespaces': 'namespaces',
        'topology_key': 'topologyKey'
    }

    def __init__(self, label_selector=None, namespaces=None, topology_key=None, local_vars_configuration=None):  # noqa: E501
        """V1PodAffinityTerm - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._label_selector = None
        self._namespaces = None
        self._topology_key = None
        self.discriminator = None

        if label_selector is not None:
            self.label_selector = label_selector
        if namespaces is not None:
            self.namespaces = namespaces
        self.topology_key = topology_key

    @property
    def label_selector(self):
        """Gets the label_selector of this V1PodAffinityTerm.  # noqa: E501


        :return: The label_selector of this V1PodAffinityTerm.  # noqa: E501
        :rtype: V1LabelSelector
        """
        return self._label_selector

    @label_selector.setter
    def label_selector(self, label_selector):
        """Sets the label_selector of this V1PodAffinityTerm.


        :param label_selector: The label_selector of this V1PodAffinityTerm.  # noqa: E501
        :type: V1LabelSelector
        """

        self._label_selector = label_selector

    @property
    def namespaces(self):
        """Gets the namespaces of this V1PodAffinityTerm.  # noqa: E501

        namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means \"this pod's namespace\"  # noqa: E501

        :return: The namespaces of this V1PodAffinityTerm.  # noqa: E501
        :rtype: list[str]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        """Sets the namespaces of this V1PodAffinityTerm.

        namespaces specifies which namespaces the labelSelector applies to (matches against); null or empty list means \"this pod's namespace\"  # noqa: E501

        :param namespaces: The namespaces of this V1PodAffinityTerm.  # noqa: E501
        :type: list[str]
        """

        self._namespaces = namespaces

    @property
    def topology_key(self):
        """Gets the topology_key of this V1PodAffinityTerm.  # noqa: E501

        This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.  # noqa: E501

        :return: The topology_key of this V1PodAffinityTerm.  # noqa: E501
        :rtype: str
        """
        return self._topology_key

    @topology_key.setter
    def topology_key(self, topology_key):
        """Sets the topology_key of this V1PodAffinityTerm.

        This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.  # noqa: E501

        :param topology_key: The topology_key of this V1PodAffinityTerm.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and topology_key is None:  # noqa: E501
            raise ValueError("Invalid value for `topology_key`, must not be `None`")  # noqa: E501

        self._topology_key = topology_key

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
        if not isinstance(other, V1PodAffinityTerm):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1PodAffinityTerm):
            return True

        return self.to_dict() != other.to_dict()
