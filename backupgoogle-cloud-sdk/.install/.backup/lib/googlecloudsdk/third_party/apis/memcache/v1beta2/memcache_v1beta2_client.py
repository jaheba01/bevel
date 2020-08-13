"""Generated client library for memcache version v1beta2."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.memcache.v1beta2 import memcache_v1beta2_messages as messages


class MemcacheV1beta2(base_api.BaseApiClient):
  """Generated client library for service memcache version v1beta2."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://memcache.googleapis.com/'
  MTLS_BASE_URL = 'https://memcache.mtls.googleapis.com/'

  _PACKAGE = 'memcache'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1beta2'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'MemcacheV1beta2'
  _URL_VERSION = 'v1beta2'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new memcache handle."""
    url = url or self.BASE_URL
    super(MemcacheV1beta2, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_instances = self.ProjectsLocationsInstancesService(self)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsInstancesService(base_api.BaseApiService):
    """Service class for the projects_locations_instances resource."""

    _NAME = 'projects_locations_instances'

    def __init__(self, client):
      super(MemcacheV1beta2.ProjectsLocationsInstancesService, self).__init__(client)
      self._upload_configs = {
          }

    def ApplyParameters(self, request, global_params=None):
      r"""ApplyParameters will update current set of Parameters to the set of.
specified nodes of the Memcached Instance.

      Args:
        request: (MemcacheProjectsLocationsInstancesApplyParametersRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('ApplyParameters')
      return self._RunMethod(
          config, request, global_params=global_params)

    ApplyParameters.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta2/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}:applyParameters',
        http_method='POST',
        method_id='memcache.projects.locations.instances.applyParameters',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta2/{+name}:applyParameters',
        request_field='applyParametersRequest',
        request_type_name='MemcacheProjectsLocationsInstancesApplyParametersRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Create(self, request, global_params=None):
      r"""Creates a new Instance in a given project and location.

      Args:
        request: (MemcacheProjectsLocationsInstancesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta2/projects/{projectsId}/locations/{locationsId}/instances',
        http_method='POST',
        method_id='memcache.projects.locations.instances.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['instanceId'],
        relative_path='v1beta2/{+parent}/instances',
        request_field='instance',
        request_type_name='MemcacheProjectsLocationsInstancesCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single Instance.

      Args:
        request: (MemcacheProjectsLocationsInstancesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta2/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}',
        http_method='DELETE',
        method_id='memcache.projects.locations.instances.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta2/{+name}',
        request_field='',
        request_type_name='MemcacheProjectsLocationsInstancesDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single Instance.

      Args:
        request: (MemcacheProjectsLocationsInstancesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Instance) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta2/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}',
        http_method='GET',
        method_id='memcache.projects.locations.instances.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta2/{+name}',
        request_field='',
        request_type_name='MemcacheProjectsLocationsInstancesGetRequest',
        response_type_name='Instance',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists Instances in a given project and location.

      Args:
        request: (MemcacheProjectsLocationsInstancesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListInstancesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta2/projects/{projectsId}/locations/{locationsId}/instances',
        http_method='GET',
        method_id='memcache.projects.locations.instances.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1beta2/{+parent}/instances',
        request_field='',
        request_type_name='MemcacheProjectsLocationsInstancesListRequest',
        response_type_name='ListInstancesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates an existing Instance in a given project and location.

      Args:
        request: (MemcacheProjectsLocationsInstancesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta2/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}',
        http_method='PATCH',
        method_id='memcache.projects.locations.instances.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1beta2/{+name}',
        request_field='instance',
        request_type_name='MemcacheProjectsLocationsInstancesPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def UpdateParameters(self, request, global_params=None):
      r"""Updates the defined Memcached Parameters for an existing Instance.
This method only stages the parameters, it must be followed by
ApplyParameters to apply the parameters to nodes of the Memcached Instance.

      Args:
        request: (MemcacheProjectsLocationsInstancesUpdateParametersRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('UpdateParameters')
      return self._RunMethod(
          config, request, global_params=global_params)

    UpdateParameters.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta2/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}:updateParameters',
        http_method='PATCH',
        method_id='memcache.projects.locations.instances.updateParameters',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta2/{+name}:updateParameters',
        request_field='updateParametersRequest',
        request_type_name='MemcacheProjectsLocationsInstancesUpdateParametersRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = 'projects_locations_operations'

    def __init__(self, client):
      super(MemcacheV1beta2.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation.  The server.
makes a best effort to cancel the operation, but success is not
guaranteed.  If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.  Clients can use
Operations.GetOperation or
other methods to check whether the cancellation succeeded or whether the
operation completed despite cancellation. On successful cancellation,
the operation is not deleted; instead, it becomes an operation with
an Operation.error value with a google.rpc.Status.code of 1,
corresponding to `Code.CANCELLED`.

      Args:
        request: (MemcacheProjectsLocationsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta2/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='memcache.projects.locations.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta2/{+name}:cancel',
        request_field='cancelOperationRequest',
        request_type_name='MemcacheProjectsLocationsOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is.
no longer interested in the operation result. It does not cancel the
operation. If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (MemcacheProjectsLocationsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta2/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='DELETE',
        method_id='memcache.projects.locations.operations.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta2/{+name}',
        request_field='',
        request_type_name='MemcacheProjectsLocationsOperationsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (MemcacheProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta2/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='GET',
        method_id='memcache.projects.locations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta2/{+name}',
        request_field='',
        request_type_name='MemcacheProjectsLocationsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the.
server doesn't support this method, it returns `UNIMPLEMENTED`.

NOTE: the `name` binding allows API services to override the binding
to use different resource name schemes, such as `users/*/operations`. To
override the binding, API services can add a binding such as
`"/v1/{name=users/*}/operations"` to their service configuration.
For backwards compatibility, the default name includes the operations
collection id, however overriding users must ensure the name binding
is the parent resource, without the operations collection id.

      Args:
        request: (MemcacheProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta2/projects/{projectsId}/locations/{locationsId}/operations',
        http_method='GET',
        method_id='memcache.projects.locations.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1beta2/{+name}/operations',
        request_field='',
        request_type_name='MemcacheProjectsLocationsOperationsListRequest',
        response_type_name='ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(MemcacheV1beta2.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (MemcacheProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta2/projects/{projectsId}/locations/{locationsId}',
        http_method='GET',
        method_id='memcache.projects.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta2/{+name}',
        request_field='',
        request_type_name='MemcacheProjectsLocationsGetRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (MemcacheProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta2/projects/{projectsId}/locations',
        http_method='GET',
        method_id='memcache.projects.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1beta2/{+name}/locations',
        request_field='',
        request_type_name='MemcacheProjectsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(MemcacheV1beta2.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
