# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Schedule(Model):
    """Definition of the schedule.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Gets the id of the resource.
    :vartype id: str
    :ivar name: Gets name of the schedule.
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param start_time: Gets or sets the start time of the schedule.
    :type start_time: datetime
    :ivar start_time_offset_minutes: Gets the start time's offset in minutes.
    :vartype start_time_offset_minutes: float
    :param expiry_time: Gets or sets the end time of the schedule.
    :type expiry_time: datetime
    :param expiry_time_offset_minutes: Gets or sets the expiry time's offset
     in minutes.
    :type expiry_time_offset_minutes: float
    :param is_enabled: Gets or sets a value indicating whether this schedule
     is enabled. Default value: False .
    :type is_enabled: bool
    :param next_run: Gets or sets the next run time of the schedule.
    :type next_run: datetime
    :param next_run_offset_minutes: Gets or sets the next run time's offset in
     minutes.
    :type next_run_offset_minutes: float
    :param interval: Gets or sets the interval of the schedule.
    :type interval: bytearray
    :param frequency: Gets or sets the frequency of the schedule. Possible
     values include: 'OneTime', 'Day', 'Hour', 'Week', 'Month'
    :type frequency: str or ~azure.mgmt.automation.models.ScheduleFrequency
    :param time_zone: Gets or sets the time zone of the schedule.
    :type time_zone: str
    :param advanced_schedule: Gets or sets the advanced schedule.
    :type advanced_schedule: ~azure.mgmt.automation.models.AdvancedSchedule
    :param creation_time: Gets or sets the creation time.
    :type creation_time: datetime
    :param last_modified_time: Gets or sets the last modified time.
    :type last_modified_time: datetime
    :param description: Gets or sets the description.
    :type description: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'start_time_offset_minutes': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'start_time': {'key': 'properties.startTime', 'type': 'iso-8601'},
        'start_time_offset_minutes': {'key': 'properties.startTimeOffsetMinutes', 'type': 'float'},
        'expiry_time': {'key': 'properties.expiryTime', 'type': 'iso-8601'},
        'expiry_time_offset_minutes': {'key': 'properties.expiryTimeOffsetMinutes', 'type': 'float'},
        'is_enabled': {'key': 'properties.isEnabled', 'type': 'bool'},
        'next_run': {'key': 'properties.nextRun', 'type': 'iso-8601'},
        'next_run_offset_minutes': {'key': 'properties.nextRunOffsetMinutes', 'type': 'float'},
        'interval': {'key': 'properties.interval', 'type': 'bytearray'},
        'frequency': {'key': 'properties.frequency', 'type': 'str'},
        'time_zone': {'key': 'properties.timeZone', 'type': 'str'},
        'advanced_schedule': {'key': 'properties.advancedSchedule', 'type': 'AdvancedSchedule'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'last_modified_time': {'key': 'properties.lastModifiedTime', 'type': 'iso-8601'},
        'description': {'key': 'properties.description', 'type': 'str'},
    }

    def __init__(self, start_time=None, expiry_time=None, expiry_time_offset_minutes=None, is_enabled=False, next_run=None, next_run_offset_minutes=None, interval=None, frequency=None, time_zone=None, advanced_schedule=None, creation_time=None, last_modified_time=None, description=None):
        super(Schedule, self).__init__()
        self.id = None
        self.name = None
        self.type = None
        self.start_time = start_time
        self.start_time_offset_minutes = None
        self.expiry_time = expiry_time
        self.expiry_time_offset_minutes = expiry_time_offset_minutes
        self.is_enabled = is_enabled
        self.next_run = next_run
        self.next_run_offset_minutes = next_run_offset_minutes
        self.interval = interval
        self.frequency = frequency
        self.time_zone = time_zone
        self.advanced_schedule = advanced_schedule
        self.creation_time = creation_time
        self.last_modified_time = last_modified_time
        self.description = description
