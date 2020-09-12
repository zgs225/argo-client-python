# coding: utf-8

"""
    Argo

    Python client for Argo Workflows  # noqa: E501

    The version of the OpenAPI document: 2.10.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from argo.workflows.client.configuration import Configuration


class V1alpha1WorkflowCreateRequest(object):
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
        'create_options': 'V1CreateOptions',
        'instance_id': 'str',
        'namespace': 'str',
        'server_dry_run': 'bool',
        'workflow': 'V1alpha1Workflow'
    }

    attribute_map = {
        'create_options': 'createOptions',
        'instance_id': 'instanceID',
        'namespace': 'namespace',
        'server_dry_run': 'serverDryRun',
        'workflow': 'workflow'
    }

    def __init__(self, create_options=None, instance_id=None, namespace=None, server_dry_run=None, workflow=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1WorkflowCreateRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._create_options = None
        self._instance_id = None
        self._namespace = None
        self._server_dry_run = None
        self._workflow = None
        self.discriminator = None

        if create_options is not None:
            self.create_options = create_options
        if instance_id is not None:
            self.instance_id = instance_id
        if namespace is not None:
            self.namespace = namespace
        if server_dry_run is not None:
            self.server_dry_run = server_dry_run
        if workflow is not None:
            self.workflow = workflow

    @property
    def create_options(self):
        """Gets the create_options of this V1alpha1WorkflowCreateRequest.  # noqa: E501


        :return: The create_options of this V1alpha1WorkflowCreateRequest.  # noqa: E501
        :rtype: V1CreateOptions
        """
        return self._create_options

    @create_options.setter
    def create_options(self, create_options):
        """Sets the create_options of this V1alpha1WorkflowCreateRequest.


        :param create_options: The create_options of this V1alpha1WorkflowCreateRequest.  # noqa: E501
        :type create_options: V1CreateOptions
        """

        self._create_options = create_options

    @property
    def instance_id(self):
        """Gets the instance_id of this V1alpha1WorkflowCreateRequest.  # noqa: E501

        This field is no longer used.  # noqa: E501

        :return: The instance_id of this V1alpha1WorkflowCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this V1alpha1WorkflowCreateRequest.

        This field is no longer used.  # noqa: E501

        :param instance_id: The instance_id of this V1alpha1WorkflowCreateRequest.  # noqa: E501
        :type instance_id: str
        """

        self._instance_id = instance_id

    @property
    def namespace(self):
        """Gets the namespace of this V1alpha1WorkflowCreateRequest.  # noqa: E501


        :return: The namespace of this V1alpha1WorkflowCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this V1alpha1WorkflowCreateRequest.


        :param namespace: The namespace of this V1alpha1WorkflowCreateRequest.  # noqa: E501
        :type namespace: str
        """

        self._namespace = namespace

    @property
    def server_dry_run(self):
        """Gets the server_dry_run of this V1alpha1WorkflowCreateRequest.  # noqa: E501


        :return: The server_dry_run of this V1alpha1WorkflowCreateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._server_dry_run

    @server_dry_run.setter
    def server_dry_run(self, server_dry_run):
        """Sets the server_dry_run of this V1alpha1WorkflowCreateRequest.


        :param server_dry_run: The server_dry_run of this V1alpha1WorkflowCreateRequest.  # noqa: E501
        :type server_dry_run: bool
        """

        self._server_dry_run = server_dry_run

    @property
    def workflow(self):
        """Gets the workflow of this V1alpha1WorkflowCreateRequest.  # noqa: E501


        :return: The workflow of this V1alpha1WorkflowCreateRequest.  # noqa: E501
        :rtype: V1alpha1Workflow
        """
        return self._workflow

    @workflow.setter
    def workflow(self, workflow):
        """Sets the workflow of this V1alpha1WorkflowCreateRequest.


        :param workflow: The workflow of this V1alpha1WorkflowCreateRequest.  # noqa: E501
        :type workflow: V1alpha1Workflow
        """

        self._workflow = workflow

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
        if not isinstance(other, V1alpha1WorkflowCreateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1WorkflowCreateRequest):
            return True

        return self.to_dict() != other.to_dict()
