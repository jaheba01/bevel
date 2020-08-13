"""Generated client library for cloudasset version v1beta1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.cloudasset.v1beta1 import cloudasset_v1beta1_messages as messages


class CloudassetV1beta1(base_api.BaseApiClient):
  """Generated client library for service cloudasset version v1beta1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://cloudasset.googleapis.com/'
  MTLS_BASE_URL = 'https://cloudasset.mtls.googleapis.com/'

  _PACKAGE = 'cloudasset'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1beta1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'CloudassetV1beta1'
  _URL_VERSION = 'v1beta1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new cloudasset handle."""
    url = url or self.BASE_URL
    super(CloudassetV1beta1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.folders_operations = self.FoldersOperationsService(self)
    self.folders = self.FoldersService(self)
    self.organizations_operations = self.OrganizationsOperationsService(self)
    self.organizations = self.OrganizationsService(self)
    self.projects_operations = self.ProjectsOperationsService(self)
    self.projects = self.ProjectsService(self)

  class FoldersOperationsService(base_api.BaseApiService):
    """Service class for the folders_operations resource."""

    _NAME = 'folders_operations'

    def __init__(self, client):
      super(CloudassetV1beta1.FoldersOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (CloudassetFoldersOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/folders/{foldersId}/operations/{operationsId}/{operationsId1}',
        http_method='GET',
        method_id='cloudasset.folders.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='CloudassetFoldersOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class FoldersService(base_api.BaseApiService):
    """Service class for the folders resource."""

    _NAME = 'folders'

    def __init__(self, client):
      super(CloudassetV1beta1.FoldersService, self).__init__(client)
      self._upload_configs = {
          }

    def ExportAssets(self, request, global_params=None):
      r"""Exports assets with time and resource types to a given Cloud Storage.
location. The output format is newline-delimited JSON.
This API implements the google.longrunning.Operation API allowing you
to keep track of the export. We recommend intervals of at least 2 seconds
with exponential retry to poll the export operation result. For
regular-size resource parent, the export operation usually finishes within
5 minutes.

      Args:
        request: (CloudassetFoldersExportAssetsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('ExportAssets')
      return self._RunMethod(
          config, request, global_params=global_params)

    ExportAssets.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/folders/{foldersId}:exportAssets',
        http_method='POST',
        method_id='cloudasset.folders.exportAssets',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1beta1/{+parent}:exportAssets',
        request_field='exportAssetsRequest',
        request_type_name='CloudassetFoldersExportAssetsRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class OrganizationsOperationsService(base_api.BaseApiService):
    """Service class for the organizations_operations resource."""

    _NAME = 'organizations_operations'

    def __init__(self, client):
      super(CloudassetV1beta1.OrganizationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (CloudassetOrganizationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/organizations/{organizationsId}/operations/{operationsId}/{operationsId1}',
        http_method='GET',
        method_id='cloudasset.organizations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='CloudassetOrganizationsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class OrganizationsService(base_api.BaseApiService):
    """Service class for the organizations resource."""

    _NAME = 'organizations'

    def __init__(self, client):
      super(CloudassetV1beta1.OrganizationsService, self).__init__(client)
      self._upload_configs = {
          }

    def BatchGetAssetsHistory(self, request, global_params=None):
      r"""Batch gets the update history of assets that overlap a time window.
For IAM_POLICY content, this API outputs history when the asset and its
attached IAM POLICY both exist. This can create gaps in the output history.
Otherwise, this API outputs history with asset in both non-delete or
deleted status.
If a specified asset does not exist, this API returns an INVALID_ARGUMENT
error.

      Args:
        request: (CloudassetOrganizationsBatchGetAssetsHistoryRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BatchGetAssetsHistoryResponse) The response message.
      """
      config = self.GetMethodConfig('BatchGetAssetsHistory')
      return self._RunMethod(
          config, request, global_params=global_params)

    BatchGetAssetsHistory.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/organizations/{organizationsId}:batchGetAssetsHistory',
        http_method='GET',
        method_id='cloudasset.organizations.batchGetAssetsHistory',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['assetNames', 'contentType', 'readTimeWindow_endTime', 'readTimeWindow_startTime'],
        relative_path='v1beta1/{+parent}:batchGetAssetsHistory',
        request_field='',
        request_type_name='CloudassetOrganizationsBatchGetAssetsHistoryRequest',
        response_type_name='BatchGetAssetsHistoryResponse',
        supports_download=False,
    )

    def ExportAssets(self, request, global_params=None):
      r"""Exports assets with time and resource types to a given Cloud Storage.
location. The output format is newline-delimited JSON.
This API implements the google.longrunning.Operation API allowing you
to keep track of the export. We recommend intervals of at least 2 seconds
with exponential retry to poll the export operation result. For
regular-size resource parent, the export operation usually finishes within
5 minutes.

      Args:
        request: (CloudassetOrganizationsExportAssetsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('ExportAssets')
      return self._RunMethod(
          config, request, global_params=global_params)

    ExportAssets.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/organizations/{organizationsId}:exportAssets',
        http_method='POST',
        method_id='cloudasset.organizations.exportAssets',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1beta1/{+parent}:exportAssets',
        request_field='exportAssetsRequest',
        request_type_name='CloudassetOrganizationsExportAssetsRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsOperationsService(base_api.BaseApiService):
    """Service class for the projects_operations resource."""

    _NAME = 'projects_operations'

    def __init__(self, client):
      super(CloudassetV1beta1.ProjectsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (CloudassetProjectsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/operations/{operationsId}/{operationsId1}',
        http_method='GET',
        method_id='cloudasset.projects.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='CloudassetProjectsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(CloudassetV1beta1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }

    def BatchGetAssetsHistory(self, request, global_params=None):
      r"""Batch gets the update history of assets that overlap a time window.
For IAM_POLICY content, this API outputs history when the asset and its
attached IAM POLICY both exist. This can create gaps in the output history.
Otherwise, this API outputs history with asset in both non-delete or
deleted status.
If a specified asset does not exist, this API returns an INVALID_ARGUMENT
error.

      Args:
        request: (CloudassetProjectsBatchGetAssetsHistoryRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BatchGetAssetsHistoryResponse) The response message.
      """
      config = self.GetMethodConfig('BatchGetAssetsHistory')
      return self._RunMethod(
          config, request, global_params=global_params)

    BatchGetAssetsHistory.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}:batchGetAssetsHistory',
        http_method='GET',
        method_id='cloudasset.projects.batchGetAssetsHistory',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['assetNames', 'contentType', 'readTimeWindow_endTime', 'readTimeWindow_startTime'],
        relative_path='v1beta1/{+parent}:batchGetAssetsHistory',
        request_field='',
        request_type_name='CloudassetProjectsBatchGetAssetsHistoryRequest',
        response_type_name='BatchGetAssetsHistoryResponse',
        supports_download=False,
    )

    def ExportAssets(self, request, global_params=None):
      r"""Exports assets with time and resource types to a given Cloud Storage.
location. The output format is newline-delimited JSON.
This API implements the google.longrunning.Operation API allowing you
to keep track of the export. We recommend intervals of at least 2 seconds
with exponential retry to poll the export operation result. For
regular-size resource parent, the export operation usually finishes within
5 minutes.

      Args:
        request: (CloudassetProjectsExportAssetsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('ExportAssets')
      return self._RunMethod(
          config, request, global_params=global_params)

    ExportAssets.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}:exportAssets',
        http_method='POST',
        method_id='cloudasset.projects.exportAssets',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1beta1/{+parent}:exportAssets',
        request_field='exportAssetsRequest',
        request_type_name='CloudassetProjectsExportAssetsRequest',
        response_type_name='Operation',
        supports_download=False,
    )
