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

from .execution_activity import ExecutionActivity


class HDInsightSparkActivity(ExecutionActivity):
    """HDInsight Spark activity.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param name: Required. Activity name.
    :type name: str
    :param description: Activity description.
    :type description: str
    :param depends_on: Activity depends on condition.
    :type depends_on: list[~azure.mgmt.datafactory.models.ActivityDependency]
    :param type: Required. Constant filled by server.
    :type type: str
    :param linked_service_name: Linked service reference.
    :type linked_service_name:
     ~azure.mgmt.datafactory.models.LinkedServiceReference
    :param policy: Activity policy.
    :type policy: ~azure.mgmt.datafactory.models.ActivityPolicy
    :param root_path: Required. The root path in 'sparkJobLinkedService' for
     all the job’s files. Type: string (or Expression with resultType string).
    :type root_path: object
    :param entry_file_path: Required. The relative path to the root folder of
     the code/package to be executed. Type: string (or Expression with
     resultType string).
    :type entry_file_path: object
    :param arguments: The user-specified arguments to HDInsightSparkActivity.
    :type arguments: list[object]
    :param get_debug_info: Debug info option. Possible values include: 'None',
     'Always', 'Failure'
    :type get_debug_info: str or
     ~azure.mgmt.datafactory.models.HDInsightActivityDebugInfoOption
    :param spark_job_linked_service: The storage linked service for uploading
     the entry file and dependencies, and for receiving logs.
    :type spark_job_linked_service:
     ~azure.mgmt.datafactory.models.LinkedServiceReference
    :param class_name: The application's Java/Spark main class.
    :type class_name: str
    :param proxy_user: The user to impersonate that will execute the job.
     Type: string (or Expression with resultType string).
    :type proxy_user: object
    :param spark_config: Spark configuration property.
    :type spark_config: dict[str, object]
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
        'root_path': {'required': True},
        'entry_file_path': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'depends_on': {'key': 'dependsOn', 'type': '[ActivityDependency]'},
        'type': {'key': 'type', 'type': 'str'},
        'linked_service_name': {'key': 'linkedServiceName', 'type': 'LinkedServiceReference'},
        'policy': {'key': 'policy', 'type': 'ActivityPolicy'},
        'root_path': {'key': 'typeProperties.rootPath', 'type': 'object'},
        'entry_file_path': {'key': 'typeProperties.entryFilePath', 'type': 'object'},
        'arguments': {'key': 'typeProperties.arguments', 'type': '[object]'},
        'get_debug_info': {'key': 'typeProperties.getDebugInfo', 'type': 'str'},
        'spark_job_linked_service': {'key': 'typeProperties.sparkJobLinkedService', 'type': 'LinkedServiceReference'},
        'class_name': {'key': 'typeProperties.className', 'type': 'str'},
        'proxy_user': {'key': 'typeProperties.proxyUser', 'type': 'object'},
        'spark_config': {'key': 'typeProperties.sparkConfig', 'type': '{object}'},
    }

    def __init__(self, *, name: str, root_path, entry_file_path, additional_properties=None, description: str=None, depends_on=None, linked_service_name=None, policy=None, arguments=None, get_debug_info=None, spark_job_linked_service=None, class_name: str=None, proxy_user=None, spark_config=None, **kwargs) -> None:
        super(HDInsightSparkActivity, self).__init__(additional_properties=additional_properties, name=name, description=description, depends_on=depends_on, linked_service_name=linked_service_name, policy=policy, **kwargs)
        self.root_path = root_path
        self.entry_file_path = entry_file_path
        self.arguments = arguments
        self.get_debug_info = get_debug_info
        self.spark_job_linked_service = spark_job_linked_service
        self.class_name = class_name
        self.proxy_user = proxy_user
        self.spark_config = spark_config
        self.type = 'HDInsightSpark'
