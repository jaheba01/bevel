"""Generated client library for anthosevents version v1alpha1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.anthosevents.v1alpha1 import anthosevents_v1alpha1_messages as messages


class AnthoseventsV1alpha1(base_api.BaseApiClient):
  """Generated client library for service anthosevents version v1alpha1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://anthosevents.googleapis.com/'
  MTLS_BASE_URL = 'https://anthosevents.mtls.googleapis.com/'

  _PACKAGE = 'anthosevents'
  _SCOPES = ['https://www.googleapis.com/auth/userinfo.email']
  _VERSION = 'v1alpha1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'AnthoseventsV1alpha1'
  _URL_VERSION = 'v1alpha1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new anthosevents handle."""
    url = url or self.BASE_URL
    super(AnthoseventsV1alpha1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.namespaces_cloudruns = self.NamespacesCloudrunsService(self)
    self.namespaces = self.NamespacesService(self)

  class NamespacesCloudrunsService(base_api.BaseApiService):
    """Service class for the namespaces_cloudruns resource."""

    _NAME = 'namespaces_cloudruns'

    def __init__(self, client):
      super(AnthoseventsV1alpha1.NamespacesCloudrunsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new CloudRun resource.

      Args:
        request: (AnthoseventsNamespacesCloudrunsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CloudRun) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='apis/addons.sigs.k8s.io/v1alpha1/namespaces/{namespacesId}/cloudruns',
        http_method='POST',
        method_id='anthosevents.namespaces.cloudruns.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='apis/addons.sigs.k8s.io/v1alpha1/{+parent}/cloudruns',
        request_field='cloudRun',
        request_type_name='AnthoseventsNamespacesCloudrunsCreateRequest',
        response_type_name='CloudRun',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Rpc to delete a CloudRun.

      Args:
        request: (AnthoseventsNamespacesCloudrunsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='apis/addons.sigs.k8s.io/v1alpha1/namespaces/{namespacesId}/cloudruns/{cloudrunsId}',
        http_method='DELETE',
        method_id='anthosevents.namespaces.cloudruns.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='apis/addons.sigs.k8s.io/v1alpha1/{+name}',
        request_field='',
        request_type_name='AnthoseventsNamespacesCloudrunsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Rpc to get information about a CloudRun resource.

      Args:
        request: (AnthoseventsNamespacesCloudrunsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CloudRun) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='apis/addons.sigs.k8s.io/v1alpha1/namespaces/{namespacesId}/cloudruns/{cloudrunsId}',
        http_method='GET',
        method_id='anthosevents.namespaces.cloudruns.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='apis/addons.sigs.k8s.io/v1alpha1/{+name}',
        request_field='',
        request_type_name='AnthoseventsNamespacesCloudrunsGetRequest',
        response_type_name='CloudRun',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Rpc to list CloudRun resources.

      Args:
        request: (AnthoseventsNamespacesCloudrunsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListCloudRunsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='apis/addons.sigs.k8s.io/v1alpha1/namespaces/{namespacesId}/cloudruns',
        http_method='GET',
        method_id='anthosevents.namespaces.cloudruns.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['continue_', 'fieldSelector', 'labelSelector', 'limit', 'resourceVersion', 'watch'],
        relative_path='apis/addons.sigs.k8s.io/v1alpha1/{+parent}/cloudruns',
        request_field='',
        request_type_name='AnthoseventsNamespacesCloudrunsListRequest',
        response_type_name='ListCloudRunsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Rpc to update a CloudRun resource.

      Args:
        request: (AnthoseventsNamespacesCloudrunsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CloudRun) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='apis/addons.sigs.k8s.io/v1alpha1/namespaces/{namespacesId}/cloudruns/{cloudrunsId}',
        http_method='PATCH',
        method_id='anthosevents.namespaces.cloudruns.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='apis/addons.sigs.k8s.io/v1alpha1/{+name}',
        request_field='cloudRun',
        request_type_name='AnthoseventsNamespacesCloudrunsPatchRequest',
        response_type_name='CloudRun',
        supports_download=False,
    )

    def ReplaceCloudRun(self, request, global_params=None):
      r"""Rpc to replace a CloudRun resource.

Only the spec and metadata labels and annotations are modifiable. After
the Update request, Cloud Run will work to make the 'status'
match the requested 'spec'.

May provide metadata.resourceVersion to enforce update from last read for
optimistic concurrency control.

      Args:
        request: (AnthoseventsNamespacesCloudrunsReplaceCloudRunRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CloudRun) The response message.
      """
      config = self.GetMethodConfig('ReplaceCloudRun')
      return self._RunMethod(
          config, request, global_params=global_params)

    ReplaceCloudRun.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='apis/addons.sigs.k8s.io/v1alpha1/namespaces/{namespacesId}/cloudruns/{cloudrunsId}',
        http_method='PUT',
        method_id='anthosevents.namespaces.cloudruns.replaceCloudRun',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='apis/addons.sigs.k8s.io/v1alpha1/{+name}',
        request_field='cloudRun',
        request_type_name='AnthoseventsNamespacesCloudrunsReplaceCloudRunRequest',
        response_type_name='CloudRun',
        supports_download=False,
    )

  class NamespacesService(base_api.BaseApiService):
    """Service class for the namespaces resource."""

    _NAME = 'namespaces'

    def __init__(self, client):
      super(AnthoseventsV1alpha1.NamespacesService, self).__init__(client)
      self._upload_configs = {
          }
