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


class V1alpha1WorkflowStep(object):
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
        'arguments': 'V1alpha1Arguments',
        'continue_on': 'V1alpha1ContinueOn',
        'name': 'str',
        'on_exit': 'str',
        'template': 'str',
        'template_ref': 'V1alpha1TemplateRef',
        'when': 'str',
        'with_items': 'list[object]',
        'with_param': 'str',
        'with_sequence': 'V1alpha1Sequence'
    }

    attribute_map = {
        'arguments': 'arguments',
        'continue_on': 'continueOn',
        'name': 'name',
        'on_exit': 'onExit',
        'template': 'template',
        'template_ref': 'templateRef',
        'when': 'when',
        'with_items': 'withItems',
        'with_param': 'withParam',
        'with_sequence': 'withSequence'
    }

    def __init__(self, arguments=None, continue_on=None, name=None, on_exit=None, template=None, template_ref=None, when=None, with_items=None, with_param=None, with_sequence=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1WorkflowStep - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._arguments = None
        self._continue_on = None
        self._name = None
        self._on_exit = None
        self._template = None
        self._template_ref = None
        self._when = None
        self._with_items = None
        self._with_param = None
        self._with_sequence = None
        self.discriminator = None

        if arguments is not None:
            self.arguments = arguments
        if continue_on is not None:
            self.continue_on = continue_on
        if name is not None:
            self.name = name
        if on_exit is not None:
            self.on_exit = on_exit
        if template is not None:
            self.template = template
        if template_ref is not None:
            self.template_ref = template_ref
        if when is not None:
            self.when = when
        if with_items is not None:
            self.with_items = with_items
        if with_param is not None:
            self.with_param = with_param
        if with_sequence is not None:
            self.with_sequence = with_sequence

    @property
    def arguments(self):
        """Gets the arguments of this V1alpha1WorkflowStep.  # noqa: E501


        :return: The arguments of this V1alpha1WorkflowStep.  # noqa: E501
        :rtype: V1alpha1Arguments
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this V1alpha1WorkflowStep.


        :param arguments: The arguments of this V1alpha1WorkflowStep.  # noqa: E501
        :type: V1alpha1Arguments
        """

        self._arguments = arguments

    @property
    def continue_on(self):
        """Gets the continue_on of this V1alpha1WorkflowStep.  # noqa: E501


        :return: The continue_on of this V1alpha1WorkflowStep.  # noqa: E501
        :rtype: V1alpha1ContinueOn
        """
        return self._continue_on

    @continue_on.setter
    def continue_on(self, continue_on):
        """Sets the continue_on of this V1alpha1WorkflowStep.


        :param continue_on: The continue_on of this V1alpha1WorkflowStep.  # noqa: E501
        :type: V1alpha1ContinueOn
        """

        self._continue_on = continue_on

    @property
    def name(self):
        """Gets the name of this V1alpha1WorkflowStep.  # noqa: E501

        Name of the step  # noqa: E501

        :return: The name of this V1alpha1WorkflowStep.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1alpha1WorkflowStep.

        Name of the step  # noqa: E501

        :param name: The name of this V1alpha1WorkflowStep.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def on_exit(self):
        """Gets the on_exit of this V1alpha1WorkflowStep.  # noqa: E501

        OnExit is a template reference which is invoked at the end of the template, irrespective of the success, failure, or error of the primary template.  # noqa: E501

        :return: The on_exit of this V1alpha1WorkflowStep.  # noqa: E501
        :rtype: str
        """
        return self._on_exit

    @on_exit.setter
    def on_exit(self, on_exit):
        """Sets the on_exit of this V1alpha1WorkflowStep.

        OnExit is a template reference which is invoked at the end of the template, irrespective of the success, failure, or error of the primary template.  # noqa: E501

        :param on_exit: The on_exit of this V1alpha1WorkflowStep.  # noqa: E501
        :type: str
        """

        self._on_exit = on_exit

    @property
    def template(self):
        """Gets the template of this V1alpha1WorkflowStep.  # noqa: E501

        Template is the name of the template to execute as the step  # noqa: E501

        :return: The template of this V1alpha1WorkflowStep.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this V1alpha1WorkflowStep.

        Template is the name of the template to execute as the step  # noqa: E501

        :param template: The template of this V1alpha1WorkflowStep.  # noqa: E501
        :type: str
        """

        self._template = template

    @property
    def template_ref(self):
        """Gets the template_ref of this V1alpha1WorkflowStep.  # noqa: E501


        :return: The template_ref of this V1alpha1WorkflowStep.  # noqa: E501
        :rtype: V1alpha1TemplateRef
        """
        return self._template_ref

    @template_ref.setter
    def template_ref(self, template_ref):
        """Sets the template_ref of this V1alpha1WorkflowStep.


        :param template_ref: The template_ref of this V1alpha1WorkflowStep.  # noqa: E501
        :type: V1alpha1TemplateRef
        """

        self._template_ref = template_ref

    @property
    def when(self):
        """Gets the when of this V1alpha1WorkflowStep.  # noqa: E501

        When is an expression in which the step should conditionally execute  # noqa: E501

        :return: The when of this V1alpha1WorkflowStep.  # noqa: E501
        :rtype: str
        """
        return self._when

    @when.setter
    def when(self, when):
        """Sets the when of this V1alpha1WorkflowStep.

        When is an expression in which the step should conditionally execute  # noqa: E501

        :param when: The when of this V1alpha1WorkflowStep.  # noqa: E501
        :type: str
        """

        self._when = when

    @property
    def with_items(self):
        """Gets the with_items of this V1alpha1WorkflowStep.  # noqa: E501

        WithItems expands a step into multiple parallel steps from the items in the list  # noqa: E501

        :return: The with_items of this V1alpha1WorkflowStep.  # noqa: E501
        :rtype: list[object]
        """
        return self._with_items

    @with_items.setter
    def with_items(self, with_items):
        """Sets the with_items of this V1alpha1WorkflowStep.

        WithItems expands a step into multiple parallel steps from the items in the list  # noqa: E501

        :param with_items: The with_items of this V1alpha1WorkflowStep.  # noqa: E501
        :type: list[object]
        """

        self._with_items = with_items

    @property
    def with_param(self):
        """Gets the with_param of this V1alpha1WorkflowStep.  # noqa: E501

        WithParam expands a step into multiple parallel steps from the value in the parameter, which is expected to be a JSON list.  # noqa: E501

        :return: The with_param of this V1alpha1WorkflowStep.  # noqa: E501
        :rtype: str
        """
        return self._with_param

    @with_param.setter
    def with_param(self, with_param):
        """Sets the with_param of this V1alpha1WorkflowStep.

        WithParam expands a step into multiple parallel steps from the value in the parameter, which is expected to be a JSON list.  # noqa: E501

        :param with_param: The with_param of this V1alpha1WorkflowStep.  # noqa: E501
        :type: str
        """

        self._with_param = with_param

    @property
    def with_sequence(self):
        """Gets the with_sequence of this V1alpha1WorkflowStep.  # noqa: E501


        :return: The with_sequence of this V1alpha1WorkflowStep.  # noqa: E501
        :rtype: V1alpha1Sequence
        """
        return self._with_sequence

    @with_sequence.setter
    def with_sequence(self, with_sequence):
        """Sets the with_sequence of this V1alpha1WorkflowStep.


        :param with_sequence: The with_sequence of this V1alpha1WorkflowStep.  # noqa: E501
        :type: V1alpha1Sequence
        """

        self._with_sequence = with_sequence

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
        if not isinstance(other, V1alpha1WorkflowStep):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1WorkflowStep):
            return True

        return self.to_dict() != other.to_dict()
