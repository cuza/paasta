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


class TronJobMonitoring:
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
        "alert_after": "str",
        "check_that_every_day_has_a_successful_run": "bool",
        "component": "AnyOfstringarray",
        "dependencies": "list[str]",
        "description": "str",
        "irc_channels": "list[str]",
        "notification_email": "AnyOfstringbooleannull",
        "page": "bool",
        "page_for_expected_runtime": "bool",
        "priority": "str",
        "project": "str",
        "realert_every": "int",
        "runbook": "str",
        "slack_channels": "list[str]",
        "tags": "list[str]",
        "team": "str",
        "ticket": "bool",
        "tip": "str",
    }

    attribute_map = {
        "alert_after": "alert_after",
        "check_that_every_day_has_a_successful_run": "check_that_every_day_has_a_successful_run",
        "component": "component",
        "dependencies": "dependencies",
        "description": "description",
        "irc_channels": "irc_channels",
        "notification_email": "notification_email",
        "page": "page",
        "page_for_expected_runtime": "page_for_expected_runtime",
        "priority": "priority",
        "project": "project",
        "realert_every": "realert_every",
        "runbook": "runbook",
        "slack_channels": "slack_channels",
        "tags": "tags",
        "team": "team",
        "ticket": "ticket",
        "tip": "tip",
    }

    def __init__(
        self,
        alert_after=None,
        check_that_every_day_has_a_successful_run=None,
        component=None,
        dependencies=None,
        description=None,
        irc_channels=None,
        notification_email=None,
        page=None,
        page_for_expected_runtime=None,
        priority=None,
        project=None,
        realert_every=None,
        runbook=None,
        slack_channels=None,
        tags=None,
        team=None,
        ticket=None,
        tip=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """TronJobMonitoring - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._alert_after = None
        self._check_that_every_day_has_a_successful_run = None
        self._component = None
        self._dependencies = None
        self._description = None
        self._irc_channels = None
        self._notification_email = None
        self._page = None
        self._page_for_expected_runtime = None
        self._priority = None
        self._project = None
        self._realert_every = None
        self._runbook = None
        self._slack_channels = None
        self._tags = None
        self._team = None
        self._ticket = None
        self._tip = None
        self.discriminator = None

        if alert_after is not None:
            self.alert_after = alert_after
        if check_that_every_day_has_a_successful_run is not None:
            self.check_that_every_day_has_a_successful_run = (
                check_that_every_day_has_a_successful_run
            )
        if component is not None:
            self.component = component
        if dependencies is not None:
            self.dependencies = dependencies
        if description is not None:
            self.description = description
        if irc_channels is not None:
            self.irc_channels = irc_channels
        if notification_email is not None:
            self.notification_email = notification_email
        if page is not None:
            self.page = page
        if page_for_expected_runtime is not None:
            self.page_for_expected_runtime = page_for_expected_runtime
        if priority is not None:
            self.priority = priority
        if project is not None:
            self.project = project
        if realert_every is not None:
            self.realert_every = realert_every
        if runbook is not None:
            self.runbook = runbook
        if slack_channels is not None:
            self.slack_channels = slack_channels
        if tags is not None:
            self.tags = tags
        if team is not None:
            self.team = team
        if ticket is not None:
            self.ticket = ticket
        if tip is not None:
            self.tip = tip

    @property
    def alert_after(self):
        """Gets the alert_after of this TronJobMonitoring.  # noqa: E501


        :return: The alert_after of this TronJobMonitoring.  # noqa: E501
        :rtype: str
        """
        return self._alert_after

    @alert_after.setter
    def alert_after(self, alert_after):
        """Sets the alert_after of this TronJobMonitoring.


        :param alert_after: The alert_after of this TronJobMonitoring.  # noqa: E501
        :type: str
        """

        self._alert_after = alert_after

    @property
    def check_that_every_day_has_a_successful_run(self):
        """Gets the check_that_every_day_has_a_successful_run of this TronJobMonitoring.  # noqa: E501


        :return: The check_that_every_day_has_a_successful_run of this TronJobMonitoring.  # noqa: E501
        :rtype: bool
        """
        return self._check_that_every_day_has_a_successful_run

    @check_that_every_day_has_a_successful_run.setter
    def check_that_every_day_has_a_successful_run(
        self, check_that_every_day_has_a_successful_run
    ):
        """Sets the check_that_every_day_has_a_successful_run of this TronJobMonitoring.


        :param check_that_every_day_has_a_successful_run: The check_that_every_day_has_a_successful_run of this TronJobMonitoring.  # noqa: E501
        :type: bool
        """

        self._check_that_every_day_has_a_successful_run = (
            check_that_every_day_has_a_successful_run
        )

    @property
    def component(self):
        """Gets the component of this TronJobMonitoring.  # noqa: E501


        :return: The component of this TronJobMonitoring.  # noqa: E501
        :rtype: AnyOfstringarray
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this TronJobMonitoring.


        :param component: The component of this TronJobMonitoring.  # noqa: E501
        :type: AnyOfstringarray
        """

        self._component = component

    @property
    def dependencies(self):
        """Gets the dependencies of this TronJobMonitoring.  # noqa: E501


        :return: The dependencies of this TronJobMonitoring.  # noqa: E501
        :rtype: list[str]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this TronJobMonitoring.


        :param dependencies: The dependencies of this TronJobMonitoring.  # noqa: E501
        :type: list[str]
        """

        self._dependencies = dependencies

    @property
    def description(self):
        """Gets the description of this TronJobMonitoring.  # noqa: E501


        :return: The description of this TronJobMonitoring.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TronJobMonitoring.


        :param description: The description of this TronJobMonitoring.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def irc_channels(self):
        """Gets the irc_channels of this TronJobMonitoring.  # noqa: E501


        :return: The irc_channels of this TronJobMonitoring.  # noqa: E501
        :rtype: list[str]
        """
        return self._irc_channels

    @irc_channels.setter
    def irc_channels(self, irc_channels):
        """Sets the irc_channels of this TronJobMonitoring.


        :param irc_channels: The irc_channels of this TronJobMonitoring.  # noqa: E501
        :type: list[str]
        """

        self._irc_channels = irc_channels

    @property
    def notification_email(self):
        """Gets the notification_email of this TronJobMonitoring.  # noqa: E501


        :return: The notification_email of this TronJobMonitoring.  # noqa: E501
        :rtype: AnyOfstringbooleannull
        """
        return self._notification_email

    @notification_email.setter
    def notification_email(self, notification_email):
        """Sets the notification_email of this TronJobMonitoring.


        :param notification_email: The notification_email of this TronJobMonitoring.  # noqa: E501
        :type: AnyOfstringbooleannull
        """

        self._notification_email = notification_email

    @property
    def page(self):
        """Gets the page of this TronJobMonitoring.  # noqa: E501


        :return: The page of this TronJobMonitoring.  # noqa: E501
        :rtype: bool
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this TronJobMonitoring.


        :param page: The page of this TronJobMonitoring.  # noqa: E501
        :type: bool
        """

        self._page = page

    @property
    def page_for_expected_runtime(self):
        """Gets the page_for_expected_runtime of this TronJobMonitoring.  # noqa: E501


        :return: The page_for_expected_runtime of this TronJobMonitoring.  # noqa: E501
        :rtype: bool
        """
        return self._page_for_expected_runtime

    @page_for_expected_runtime.setter
    def page_for_expected_runtime(self, page_for_expected_runtime):
        """Sets the page_for_expected_runtime of this TronJobMonitoring.


        :param page_for_expected_runtime: The page_for_expected_runtime of this TronJobMonitoring.  # noqa: E501
        :type: bool
        """

        self._page_for_expected_runtime = page_for_expected_runtime

    @property
    def priority(self):
        """Gets the priority of this TronJobMonitoring.  # noqa: E501


        :return: The priority of this TronJobMonitoring.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this TronJobMonitoring.


        :param priority: The priority of this TronJobMonitoring.  # noqa: E501
        :type: str
        """

        self._priority = priority

    @property
    def project(self):
        """Gets the project of this TronJobMonitoring.  # noqa: E501


        :return: The project of this TronJobMonitoring.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this TronJobMonitoring.


        :param project: The project of this TronJobMonitoring.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def realert_every(self):
        """Gets the realert_every of this TronJobMonitoring.  # noqa: E501


        :return: The realert_every of this TronJobMonitoring.  # noqa: E501
        :rtype: int
        """
        return self._realert_every

    @realert_every.setter
    def realert_every(self, realert_every):
        """Sets the realert_every of this TronJobMonitoring.


        :param realert_every: The realert_every of this TronJobMonitoring.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and realert_every is not None
            and realert_every < -1
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `realert_every`, must be a value greater than or equal to `-1`"
            )  # noqa: E501

        self._realert_every = realert_every

    @property
    def runbook(self):
        """Gets the runbook of this TronJobMonitoring.  # noqa: E501


        :return: The runbook of this TronJobMonitoring.  # noqa: E501
        :rtype: str
        """
        return self._runbook

    @runbook.setter
    def runbook(self, runbook):
        """Sets the runbook of this TronJobMonitoring.


        :param runbook: The runbook of this TronJobMonitoring.  # noqa: E501
        :type: str
        """

        self._runbook = runbook

    @property
    def slack_channels(self):
        """Gets the slack_channels of this TronJobMonitoring.  # noqa: E501


        :return: The slack_channels of this TronJobMonitoring.  # noqa: E501
        :rtype: list[str]
        """
        return self._slack_channels

    @slack_channels.setter
    def slack_channels(self, slack_channels):
        """Sets the slack_channels of this TronJobMonitoring.


        :param slack_channels: The slack_channels of this TronJobMonitoring.  # noqa: E501
        :type: list[str]
        """

        self._slack_channels = slack_channels

    @property
    def tags(self):
        """Gets the tags of this TronJobMonitoring.  # noqa: E501


        :return: The tags of this TronJobMonitoring.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TronJobMonitoring.


        :param tags: The tags of this TronJobMonitoring.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def team(self):
        """Gets the team of this TronJobMonitoring.  # noqa: E501


        :return: The team of this TronJobMonitoring.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this TronJobMonitoring.


        :param team: The team of this TronJobMonitoring.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def ticket(self):
        """Gets the ticket of this TronJobMonitoring.  # noqa: E501


        :return: The ticket of this TronJobMonitoring.  # noqa: E501
        :rtype: bool
        """
        return self._ticket

    @ticket.setter
    def ticket(self, ticket):
        """Sets the ticket of this TronJobMonitoring.


        :param ticket: The ticket of this TronJobMonitoring.  # noqa: E501
        :type: bool
        """

        self._ticket = ticket

    @property
    def tip(self):
        """Gets the tip of this TronJobMonitoring.  # noqa: E501


        :return: The tip of this TronJobMonitoring.  # noqa: E501
        :rtype: str
        """
        return self._tip

    @tip.setter
    def tip(self, tip):
        """Sets the tip of this TronJobMonitoring.


        :param tip: The tip of this TronJobMonitoring.  # noqa: E501
        :type: str
        """

        self._tip = tip

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
        if not isinstance(other, TronJobMonitoring):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TronJobMonitoring):
            return True

        return self.to_dict() != other.to_dict()