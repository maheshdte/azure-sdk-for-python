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

try:
    from .compute_operation_value_py3 import ComputeOperationValue
    from .instance_view_status_py3 import InstanceViewStatus
    from .sub_resource_py3 import SubResource
    from .sku_py3 import Sku
    from .availability_set_py3 import AvailabilitySet
    from .availability_set_update_py3 import AvailabilitySetUpdate
    from .virtual_machine_size_py3 import VirtualMachineSize
    from .virtual_machine_extension_image_py3 import VirtualMachineExtensionImage
    from .virtual_machine_image_resource_py3 import VirtualMachineImageResource
    from .virtual_machine_extension_instance_view_py3 import VirtualMachineExtensionInstanceView
    from .virtual_machine_extension_py3 import VirtualMachineExtension
    from .purchase_plan_py3 import PurchasePlan
    from .os_disk_image_py3 import OSDiskImage
    from .data_disk_image_py3 import DataDiskImage
    from .virtual_machine_image_py3 import VirtualMachineImage
    from .usage_name_py3 import UsageName
    from .usage_py3 import Usage
    from .virtual_machine_capture_parameters_py3 import VirtualMachineCaptureParameters
    from .virtual_machine_capture_result_py3 import VirtualMachineCaptureResult
    from .plan_py3 import Plan
    from .hardware_profile_py3 import HardwareProfile
    from .image_reference_py3 import ImageReference
    from .key_vault_secret_reference_py3 import KeyVaultSecretReference
    from .key_vault_key_reference_py3 import KeyVaultKeyReference
    from .disk_encryption_settings_py3 import DiskEncryptionSettings
    from .virtual_hard_disk_py3 import VirtualHardDisk
    from .managed_disk_parameters_py3 import ManagedDiskParameters
    from .os_disk_py3 import OSDisk
    from .data_disk_py3 import DataDisk
    from .storage_profile_py3 import StorageProfile
    from .additional_unattend_content_py3 import AdditionalUnattendContent
    from .win_rm_listener_py3 import WinRMListener
    from .win_rm_configuration_py3 import WinRMConfiguration
    from .windows_configuration_py3 import WindowsConfiguration
    from .ssh_public_key_py3 import SshPublicKey
    from .ssh_configuration_py3 import SshConfiguration
    from .linux_configuration_py3 import LinuxConfiguration
    from .vault_certificate_py3 import VaultCertificate
    from .vault_secret_group_py3 import VaultSecretGroup
    from .os_profile_py3 import OSProfile
    from .network_interface_reference_py3 import NetworkInterfaceReference
    from .network_profile_py3 import NetworkProfile
    from .boot_diagnostics_py3 import BootDiagnostics
    from .diagnostics_profile_py3 import DiagnosticsProfile
    from .virtual_machine_extension_handler_instance_view_py3 import VirtualMachineExtensionHandlerInstanceView
    from .virtual_machine_agent_instance_view_py3 import VirtualMachineAgentInstanceView
    from .disk_instance_view_py3 import DiskInstanceView
    from .boot_diagnostics_instance_view_py3 import BootDiagnosticsInstanceView
    from .virtual_machine_identity_py3 import VirtualMachineIdentity
    from .maintenance_redeploy_status_py3 import MaintenanceRedeployStatus
    from .virtual_machine_instance_view_py3 import VirtualMachineInstanceView
    from .virtual_machine_py3 import VirtualMachine
    from .virtual_machine_update_py3 import VirtualMachineUpdate
    from .rolling_upgrade_policy_py3 import RollingUpgradePolicy
    from .upgrade_policy_py3 import UpgradePolicy
    from .image_os_disk_py3 import ImageOSDisk
    from .image_data_disk_py3 import ImageDataDisk
    from .image_storage_profile_py3 import ImageStorageProfile
    from .image_py3 import Image
    from .image_update_py3 import ImageUpdate
    from .virtual_machine_scale_set_identity_py3 import VirtualMachineScaleSetIdentity
    from .virtual_machine_scale_set_os_profile_py3 import VirtualMachineScaleSetOSProfile
    from .virtual_machine_scale_set_update_os_profile_py3 import VirtualMachineScaleSetUpdateOSProfile
    from .virtual_machine_scale_set_managed_disk_parameters_py3 import VirtualMachineScaleSetManagedDiskParameters
    from .virtual_machine_scale_set_os_disk_py3 import VirtualMachineScaleSetOSDisk
    from .virtual_machine_scale_set_update_os_disk_py3 import VirtualMachineScaleSetUpdateOSDisk
    from .virtual_machine_scale_set_data_disk_py3 import VirtualMachineScaleSetDataDisk
    from .virtual_machine_scale_set_storage_profile_py3 import VirtualMachineScaleSetStorageProfile
    from .virtual_machine_scale_set_update_storage_profile_py3 import VirtualMachineScaleSetUpdateStorageProfile
    from .api_entity_reference_py3 import ApiEntityReference
    from .virtual_machine_scale_set_public_ip_address_configuration_dns_settings_py3 import VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettings
    from .virtual_machine_scale_set_public_ip_address_configuration_py3 import VirtualMachineScaleSetPublicIPAddressConfiguration
    from .virtual_machine_scale_set_update_public_ip_address_configuration_py3 import VirtualMachineScaleSetUpdatePublicIPAddressConfiguration
    from .virtual_machine_scale_set_ip_configuration_py3 import VirtualMachineScaleSetIPConfiguration
    from .virtual_machine_scale_set_update_ip_configuration_py3 import VirtualMachineScaleSetUpdateIPConfiguration
    from .virtual_machine_scale_set_network_configuration_dns_settings_py3 import VirtualMachineScaleSetNetworkConfigurationDnsSettings
    from .virtual_machine_scale_set_network_configuration_py3 import VirtualMachineScaleSetNetworkConfiguration
    from .virtual_machine_scale_set_update_network_configuration_py3 import VirtualMachineScaleSetUpdateNetworkConfiguration
    from .virtual_machine_scale_set_network_profile_py3 import VirtualMachineScaleSetNetworkProfile
    from .virtual_machine_scale_set_update_network_profile_py3 import VirtualMachineScaleSetUpdateNetworkProfile
    from .virtual_machine_scale_set_extension_py3 import VirtualMachineScaleSetExtension
    from .virtual_machine_scale_set_extension_profile_py3 import VirtualMachineScaleSetExtensionProfile
    from .virtual_machine_scale_set_vm_profile_py3 import VirtualMachineScaleSetVMProfile
    from .virtual_machine_scale_set_update_vm_profile_py3 import VirtualMachineScaleSetUpdateVMProfile
    from .virtual_machine_scale_set_py3 import VirtualMachineScaleSet
    from .virtual_machine_scale_set_update_py3 import VirtualMachineScaleSetUpdate
    from .virtual_machine_scale_set_vm_instance_ids_py3 import VirtualMachineScaleSetVMInstanceIDs
    from .virtual_machine_scale_set_vm_instance_required_ids_py3 import VirtualMachineScaleSetVMInstanceRequiredIDs
    from .virtual_machine_status_code_count_py3 import VirtualMachineStatusCodeCount
    from .virtual_machine_scale_set_instance_view_statuses_summary_py3 import VirtualMachineScaleSetInstanceViewStatusesSummary
    from .virtual_machine_scale_set_vm_extensions_summary_py3 import VirtualMachineScaleSetVMExtensionsSummary
    from .virtual_machine_scale_set_instance_view_py3 import VirtualMachineScaleSetInstanceView
    from .virtual_machine_scale_set_sku_capacity_py3 import VirtualMachineScaleSetSkuCapacity
    from .virtual_machine_scale_set_sku_py3 import VirtualMachineScaleSetSku
    from .platform_image_reference_py3 import PlatformImageReference
    from .rolling_upgrade_running_status_py3 import RollingUpgradeRunningStatus
    from .rolling_upgrade_progress_info_py3 import RollingUpgradeProgressInfo
    from .api_error_base_py3 import ApiErrorBase
    from .inner_error_py3 import InnerError
    from .api_error_py3 import ApiError
    from .virtual_machine_scale_set_os_upgrade_history_py3 import VirtualMachineScaleSetOSUpgradeHistory
    from .virtual_machine_scale_set_vm_py3 import VirtualMachineScaleSetVM
    from .virtual_machine_health_status_py3 import VirtualMachineHealthStatus
    from .virtual_machine_scale_set_vm_instance_view_py3 import VirtualMachineScaleSetVMInstanceView
    from .rolling_upgrade_status_info_py3 import RollingUpgradeStatusInfo
    from .compute_long_running_operation_properties_py3 import ComputeLongRunningOperationProperties
    from .resource_py3 import Resource
    from .update_resource_py3 import UpdateResource
    from .sub_resource_read_only_py3 import SubResourceReadOnly
    from .recovery_walk_response_py3 import RecoveryWalkResponse
    from .operation_status_response_py3 import OperationStatusResponse
    from .request_rate_by_interval_input_py3 import RequestRateByIntervalInput
    from .throttled_requests_input_py3 import ThrottledRequestsInput
    from .log_analytics_input_base_py3 import LogAnalyticsInputBase
    from .log_analytics_output_py3 import LogAnalyticsOutput
    from .log_analytics_operation_result_py3 import LogAnalyticsOperationResult
    from .run_command_input_parameter_py3 import RunCommandInputParameter
    from .run_command_input_py3 import RunCommandInput
    from .run_command_parameter_definition_py3 import RunCommandParameterDefinition
    from .run_command_document_base_py3 import RunCommandDocumentBase
    from .run_command_document_py3 import RunCommandDocument
    from .run_command_result_py3 import RunCommandResult
except (SyntaxError, ImportError):
    from .compute_operation_value import ComputeOperationValue
    from .instance_view_status import InstanceViewStatus
    from .sub_resource import SubResource
    from .sku import Sku
    from .availability_set import AvailabilitySet
    from .availability_set_update import AvailabilitySetUpdate
    from .virtual_machine_size import VirtualMachineSize
    from .virtual_machine_extension_image import VirtualMachineExtensionImage
    from .virtual_machine_image_resource import VirtualMachineImageResource
    from .virtual_machine_extension_instance_view import VirtualMachineExtensionInstanceView
    from .virtual_machine_extension import VirtualMachineExtension
    from .purchase_plan import PurchasePlan
    from .os_disk_image import OSDiskImage
    from .data_disk_image import DataDiskImage
    from .virtual_machine_image import VirtualMachineImage
    from .usage_name import UsageName
    from .usage import Usage
    from .virtual_machine_capture_parameters import VirtualMachineCaptureParameters
    from .virtual_machine_capture_result import VirtualMachineCaptureResult
    from .plan import Plan
    from .hardware_profile import HardwareProfile
    from .image_reference import ImageReference
    from .key_vault_secret_reference import KeyVaultSecretReference
    from .key_vault_key_reference import KeyVaultKeyReference
    from .disk_encryption_settings import DiskEncryptionSettings
    from .virtual_hard_disk import VirtualHardDisk
    from .managed_disk_parameters import ManagedDiskParameters
    from .os_disk import OSDisk
    from .data_disk import DataDisk
    from .storage_profile import StorageProfile
    from .additional_unattend_content import AdditionalUnattendContent
    from .win_rm_listener import WinRMListener
    from .win_rm_configuration import WinRMConfiguration
    from .windows_configuration import WindowsConfiguration
    from .ssh_public_key import SshPublicKey
    from .ssh_configuration import SshConfiguration
    from .linux_configuration import LinuxConfiguration
    from .vault_certificate import VaultCertificate
    from .vault_secret_group import VaultSecretGroup
    from .os_profile import OSProfile
    from .network_interface_reference import NetworkInterfaceReference
    from .network_profile import NetworkProfile
    from .boot_diagnostics import BootDiagnostics
    from .diagnostics_profile import DiagnosticsProfile
    from .virtual_machine_extension_handler_instance_view import VirtualMachineExtensionHandlerInstanceView
    from .virtual_machine_agent_instance_view import VirtualMachineAgentInstanceView
    from .disk_instance_view import DiskInstanceView
    from .boot_diagnostics_instance_view import BootDiagnosticsInstanceView
    from .virtual_machine_identity import VirtualMachineIdentity
    from .maintenance_redeploy_status import MaintenanceRedeployStatus
    from .virtual_machine_instance_view import VirtualMachineInstanceView
    from .virtual_machine import VirtualMachine
    from .virtual_machine_update import VirtualMachineUpdate
    from .rolling_upgrade_policy import RollingUpgradePolicy
    from .upgrade_policy import UpgradePolicy
    from .image_os_disk import ImageOSDisk
    from .image_data_disk import ImageDataDisk
    from .image_storage_profile import ImageStorageProfile
    from .image import Image
    from .image_update import ImageUpdate
    from .virtual_machine_scale_set_identity import VirtualMachineScaleSetIdentity
    from .virtual_machine_scale_set_os_profile import VirtualMachineScaleSetOSProfile
    from .virtual_machine_scale_set_update_os_profile import VirtualMachineScaleSetUpdateOSProfile
    from .virtual_machine_scale_set_managed_disk_parameters import VirtualMachineScaleSetManagedDiskParameters
    from .virtual_machine_scale_set_os_disk import VirtualMachineScaleSetOSDisk
    from .virtual_machine_scale_set_update_os_disk import VirtualMachineScaleSetUpdateOSDisk
    from .virtual_machine_scale_set_data_disk import VirtualMachineScaleSetDataDisk
    from .virtual_machine_scale_set_storage_profile import VirtualMachineScaleSetStorageProfile
    from .virtual_machine_scale_set_update_storage_profile import VirtualMachineScaleSetUpdateStorageProfile
    from .api_entity_reference import ApiEntityReference
    from .virtual_machine_scale_set_public_ip_address_configuration_dns_settings import VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettings
    from .virtual_machine_scale_set_public_ip_address_configuration import VirtualMachineScaleSetPublicIPAddressConfiguration
    from .virtual_machine_scale_set_update_public_ip_address_configuration import VirtualMachineScaleSetUpdatePublicIPAddressConfiguration
    from .virtual_machine_scale_set_ip_configuration import VirtualMachineScaleSetIPConfiguration
    from .virtual_machine_scale_set_update_ip_configuration import VirtualMachineScaleSetUpdateIPConfiguration
    from .virtual_machine_scale_set_network_configuration_dns_settings import VirtualMachineScaleSetNetworkConfigurationDnsSettings
    from .virtual_machine_scale_set_network_configuration import VirtualMachineScaleSetNetworkConfiguration
    from .virtual_machine_scale_set_update_network_configuration import VirtualMachineScaleSetUpdateNetworkConfiguration
    from .virtual_machine_scale_set_network_profile import VirtualMachineScaleSetNetworkProfile
    from .virtual_machine_scale_set_update_network_profile import VirtualMachineScaleSetUpdateNetworkProfile
    from .virtual_machine_scale_set_extension import VirtualMachineScaleSetExtension
    from .virtual_machine_scale_set_extension_profile import VirtualMachineScaleSetExtensionProfile
    from .virtual_machine_scale_set_vm_profile import VirtualMachineScaleSetVMProfile
    from .virtual_machine_scale_set_update_vm_profile import VirtualMachineScaleSetUpdateVMProfile
    from .virtual_machine_scale_set import VirtualMachineScaleSet
    from .virtual_machine_scale_set_update import VirtualMachineScaleSetUpdate
    from .virtual_machine_scale_set_vm_instance_ids import VirtualMachineScaleSetVMInstanceIDs
    from .virtual_machine_scale_set_vm_instance_required_ids import VirtualMachineScaleSetVMInstanceRequiredIDs
    from .virtual_machine_status_code_count import VirtualMachineStatusCodeCount
    from .virtual_machine_scale_set_instance_view_statuses_summary import VirtualMachineScaleSetInstanceViewStatusesSummary
    from .virtual_machine_scale_set_vm_extensions_summary import VirtualMachineScaleSetVMExtensionsSummary
    from .virtual_machine_scale_set_instance_view import VirtualMachineScaleSetInstanceView
    from .virtual_machine_scale_set_sku_capacity import VirtualMachineScaleSetSkuCapacity
    from .virtual_machine_scale_set_sku import VirtualMachineScaleSetSku
    from .platform_image_reference import PlatformImageReference
    from .rolling_upgrade_running_status import RollingUpgradeRunningStatus
    from .rolling_upgrade_progress_info import RollingUpgradeProgressInfo
    from .api_error_base import ApiErrorBase
    from .inner_error import InnerError
    from .api_error import ApiError
    from .virtual_machine_scale_set_os_upgrade_history import VirtualMachineScaleSetOSUpgradeHistory
    from .virtual_machine_scale_set_vm import VirtualMachineScaleSetVM
    from .virtual_machine_health_status import VirtualMachineHealthStatus
    from .virtual_machine_scale_set_vm_instance_view import VirtualMachineScaleSetVMInstanceView
    from .rolling_upgrade_status_info import RollingUpgradeStatusInfo
    from .compute_long_running_operation_properties import ComputeLongRunningOperationProperties
    from .resource import Resource
    from .update_resource import UpdateResource
    from .sub_resource_read_only import SubResourceReadOnly
    from .recovery_walk_response import RecoveryWalkResponse
    from .operation_status_response import OperationStatusResponse
    from .request_rate_by_interval_input import RequestRateByIntervalInput
    from .throttled_requests_input import ThrottledRequestsInput
    from .log_analytics_input_base import LogAnalyticsInputBase
    from .log_analytics_output import LogAnalyticsOutput
    from .log_analytics_operation_result import LogAnalyticsOperationResult
    from .run_command_input_parameter import RunCommandInputParameter
    from .run_command_input import RunCommandInput
    from .run_command_parameter_definition import RunCommandParameterDefinition
    from .run_command_document_base import RunCommandDocumentBase
    from .run_command_document import RunCommandDocument
    from .run_command_result import RunCommandResult
from .compute_operation_value_paged import ComputeOperationValuePaged
from .availability_set_paged import AvailabilitySetPaged
from .virtual_machine_size_paged import VirtualMachineSizePaged
from .usage_paged import UsagePaged
from .image_paged import ImagePaged
from .virtual_machine_paged import VirtualMachinePaged
from .virtual_machine_scale_set_paged import VirtualMachineScaleSetPaged
from .virtual_machine_scale_set_sku_paged import VirtualMachineScaleSetSkuPaged
from .virtual_machine_scale_set_os_upgrade_history_paged import VirtualMachineScaleSetOSUpgradeHistoryPaged
from .virtual_machine_scale_set_extension_paged import VirtualMachineScaleSetExtensionPaged
from .virtual_machine_scale_set_vm_paged import VirtualMachineScaleSetVMPaged
from .run_command_document_base_paged import RunCommandDocumentBasePaged
from .compute_management_client_enums import (
    StatusLevelTypes,
    OperatingSystemTypes,
    VirtualMachineSizeTypes,
    CachingTypes,
    DiskCreateOptionTypes,
    StorageAccountTypes,
    PassNames,
    ComponentNames,
    SettingNames,
    ProtocolTypes,
    ResourceIdentityType,
    MaintenanceOperationResultCodeTypes,
    UpgradeMode,
    OperatingSystemStateTypes,
    IPVersion,
    VirtualMachinePriorityTypes,
    VirtualMachineScaleSetSkuScaleType,
    RollingUpgradeStatusCode,
    RollingUpgradeActionType,
    IntervalInMins,
    InstanceViewTypes,
)

__all__ = [
    'ComputeOperationValue',
    'InstanceViewStatus',
    'SubResource',
    'Sku',
    'AvailabilitySet',
    'AvailabilitySetUpdate',
    'VirtualMachineSize',
    'VirtualMachineExtensionImage',
    'VirtualMachineImageResource',
    'VirtualMachineExtensionInstanceView',
    'VirtualMachineExtension',
    'PurchasePlan',
    'OSDiskImage',
    'DataDiskImage',
    'VirtualMachineImage',
    'UsageName',
    'Usage',
    'VirtualMachineCaptureParameters',
    'VirtualMachineCaptureResult',
    'Plan',
    'HardwareProfile',
    'ImageReference',
    'KeyVaultSecretReference',
    'KeyVaultKeyReference',
    'DiskEncryptionSettings',
    'VirtualHardDisk',
    'ManagedDiskParameters',
    'OSDisk',
    'DataDisk',
    'StorageProfile',
    'AdditionalUnattendContent',
    'WinRMListener',
    'WinRMConfiguration',
    'WindowsConfiguration',
    'SshPublicKey',
    'SshConfiguration',
    'LinuxConfiguration',
    'VaultCertificate',
    'VaultSecretGroup',
    'OSProfile',
    'NetworkInterfaceReference',
    'NetworkProfile',
    'BootDiagnostics',
    'DiagnosticsProfile',
    'VirtualMachineExtensionHandlerInstanceView',
    'VirtualMachineAgentInstanceView',
    'DiskInstanceView',
    'BootDiagnosticsInstanceView',
    'VirtualMachineIdentity',
    'MaintenanceRedeployStatus',
    'VirtualMachineInstanceView',
    'VirtualMachine',
    'VirtualMachineUpdate',
    'RollingUpgradePolicy',
    'UpgradePolicy',
    'ImageOSDisk',
    'ImageDataDisk',
    'ImageStorageProfile',
    'Image',
    'ImageUpdate',
    'VirtualMachineScaleSetIdentity',
    'VirtualMachineScaleSetOSProfile',
    'VirtualMachineScaleSetUpdateOSProfile',
    'VirtualMachineScaleSetManagedDiskParameters',
    'VirtualMachineScaleSetOSDisk',
    'VirtualMachineScaleSetUpdateOSDisk',
    'VirtualMachineScaleSetDataDisk',
    'VirtualMachineScaleSetStorageProfile',
    'VirtualMachineScaleSetUpdateStorageProfile',
    'ApiEntityReference',
    'VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettings',
    'VirtualMachineScaleSetPublicIPAddressConfiguration',
    'VirtualMachineScaleSetUpdatePublicIPAddressConfiguration',
    'VirtualMachineScaleSetIPConfiguration',
    'VirtualMachineScaleSetUpdateIPConfiguration',
    'VirtualMachineScaleSetNetworkConfigurationDnsSettings',
    'VirtualMachineScaleSetNetworkConfiguration',
    'VirtualMachineScaleSetUpdateNetworkConfiguration',
    'VirtualMachineScaleSetNetworkProfile',
    'VirtualMachineScaleSetUpdateNetworkProfile',
    'VirtualMachineScaleSetExtension',
    'VirtualMachineScaleSetExtensionProfile',
    'VirtualMachineScaleSetVMProfile',
    'VirtualMachineScaleSetUpdateVMProfile',
    'VirtualMachineScaleSet',
    'VirtualMachineScaleSetUpdate',
    'VirtualMachineScaleSetVMInstanceIDs',
    'VirtualMachineScaleSetVMInstanceRequiredIDs',
    'VirtualMachineStatusCodeCount',
    'VirtualMachineScaleSetInstanceViewStatusesSummary',
    'VirtualMachineScaleSetVMExtensionsSummary',
    'VirtualMachineScaleSetInstanceView',
    'VirtualMachineScaleSetSkuCapacity',
    'VirtualMachineScaleSetSku',
    'PlatformImageReference',
    'RollingUpgradeRunningStatus',
    'RollingUpgradeProgressInfo',
    'ApiErrorBase',
    'InnerError',
    'ApiError',
    'VirtualMachineScaleSetOSUpgradeHistory',
    'VirtualMachineScaleSetVM',
    'VirtualMachineHealthStatus',
    'VirtualMachineScaleSetVMInstanceView',
    'RollingUpgradeStatusInfo',
    'ComputeLongRunningOperationProperties',
    'Resource',
    'UpdateResource',
    'SubResourceReadOnly',
    'RecoveryWalkResponse',
    'OperationStatusResponse',
    'RequestRateByIntervalInput',
    'ThrottledRequestsInput',
    'LogAnalyticsInputBase',
    'LogAnalyticsOutput',
    'LogAnalyticsOperationResult',
    'RunCommandInputParameter',
    'RunCommandInput',
    'RunCommandParameterDefinition',
    'RunCommandDocumentBase',
    'RunCommandDocument',
    'RunCommandResult',
    'ComputeOperationValuePaged',
    'AvailabilitySetPaged',
    'VirtualMachineSizePaged',
    'UsagePaged',
    'ImagePaged',
    'VirtualMachinePaged',
    'VirtualMachineScaleSetPaged',
    'VirtualMachineScaleSetSkuPaged',
    'VirtualMachineScaleSetOSUpgradeHistoryPaged',
    'VirtualMachineScaleSetExtensionPaged',
    'VirtualMachineScaleSetVMPaged',
    'RunCommandDocumentBasePaged',
    'StatusLevelTypes',
    'OperatingSystemTypes',
    'VirtualMachineSizeTypes',
    'CachingTypes',
    'DiskCreateOptionTypes',
    'StorageAccountTypes',
    'PassNames',
    'ComponentNames',
    'SettingNames',
    'ProtocolTypes',
    'ResourceIdentityType',
    'MaintenanceOperationResultCodeTypes',
    'UpgradeMode',
    'OperatingSystemStateTypes',
    'IPVersion',
    'VirtualMachinePriorityTypes',
    'VirtualMachineScaleSetSkuScaleType',
    'RollingUpgradeStatusCode',
    'RollingUpgradeActionType',
    'IntervalInMins',
    'InstanceViewTypes',
]
