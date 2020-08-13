"""Generated client library for artifactregistry version v1alpha1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.artifactregistry.v1alpha1 import artifactregistry_v1alpha1_messages as messages


class ArtifactregistryV1alpha1(base_api.BaseApiClient):
  """Generated client library for service artifactregistry version v1alpha1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://artifactregistry.googleapis.com/'
  MTLS_BASE_URL = 'https://artifactregistry.mtls.googleapis.com/'

  _PACKAGE = 'artifactregistry'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1alpha1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'ArtifactregistryV1alpha1'
  _URL_VERSION = 'v1alpha1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new artifactregistry handle."""
    url = url or self.BASE_URL
    super(ArtifactregistryV1alpha1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_repositories = self.ProjectsLocationsRepositoriesService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsRepositoriesService(base_api.BaseApiService):
    """Service class for the projects_locations_repositories resource."""

    _NAME = 'projects_locations_repositories'

    def __init__(self, client):
      super(ArtifactregistryV1alpha1.ProjectsLocationsRepositoriesService, self).__init__(client)
      self._upload_configs = {
          }

    def Import(self, request, global_params=None):
      r"""Imports artifacts. The returned Operation will complete once the resources.
are imported. Package, Version, and File resources are created based on the
imported artifacts. Imported artifacts that conflict with existing
resources are ignored.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesImportRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Import')
      return self._RunMethod(
          config, request, global_params=global_params)

    Import.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}:import',
        http_method='POST',
        method_id='artifactregistry.projects.locations.repositories.import',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1alpha1/{+parent}:import',
        request_field='googleDevtoolsArtifactregistryV1alpha1ImportArtifactsRequest',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesImportRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(ArtifactregistryV1alpha1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(ArtifactregistryV1alpha1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
