"""Generated client library for firestore version v1beta2."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.firestore.v1beta2 import firestore_v1beta2_messages as messages


class FirestoreV1beta2(base_api.BaseApiClient):
  """Generated client library for service firestore version v1beta2."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://firestore.googleapis.com/'
  MTLS_BASE_URL = 'https://firestore.mtls.googleapis.com/'

  _PACKAGE = 'firestore'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform', 'https://www.googleapis.com/auth/datastore']
  _VERSION = 'v1beta2'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'FirestoreV1beta2'
  _URL_VERSION = 'v1beta2'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new firestore handle."""
    url = url or self.BASE_URL
    super(FirestoreV1beta2, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_databases_collectionGroups_fields = self.ProjectsDatabasesCollectionGroupsFieldsService(self)
    self.projects_databases_collectionGroups_indexes = self.ProjectsDatabasesCollectionGroupsIndexesService(self)
    self.projects_databases_collectionGroups = self.ProjectsDatabasesCollectionGroupsService(self)
    self.projects_databases = self.ProjectsDatabasesService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsDatabasesCollectionGroupsFieldsService(base_api.BaseApiService):
    """Service class for the projects_databases_collectionGroups_fields resource."""

    _NAME = 'projects_databases_collectionGroups_fields'

    def __init__(self, client):
      super(FirestoreV1beta2.ProjectsDatabasesCollectionGroupsFieldsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the metadata and configuration for a Field.

      Args:
        request: (FirestoreProjectsDatabasesCollectionGroupsFieldsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleFirestoreAdminV1beta2Field) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta2/projects/{projectsId}/databases/{databasesId}/collectionGroups/{collectionGroupsId}/fields/{fieldsId}',
        http_method='GET',
        method_id='firestore.projects.databases.collectionGroups.fields.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta2/{+name}',
        request_field='',
        request_type_name='FirestoreProjectsDatabasesCollectionGroupsFieldsGetRequest',
        response_type_name='GoogleFirestoreAdminV1beta2Field',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists the field configuration and metadata for this database.

Currently, FirestoreAdmin.ListFields only supports listing fields
that have been explicitly overridden. To issue this query, call
FirestoreAdmin.ListFields with the filter set to
`indexConfig.usesAncestorConfig:false`.

      Args:
        request: (FirestoreProjectsDatabasesCollectionGroupsFieldsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleFirestoreAdminV1beta2ListFieldsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta2/projects/{projectsId}/databases/{databasesId}/collectionGroups/{collectionGroupsId}/fields',
        http_method='GET',
        method_id='firestore.projects.databases.collectionGroups.fields.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1beta2/{+parent}/fields',
        request_field='',
        request_type_name='FirestoreProjectsDatabasesCollectionGroupsFieldsListRequest',
        response_type_name='GoogleFirestoreAdminV1beta2ListFieldsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a field configuration. Currently, field updates apply only to.
single field index configuration. However, calls to
FirestoreAdmin.UpdateField should provide a field mask to avoid
changing any configuration that the caller isn't aware of. The field mask
should be specified as: `{ paths: "index_config" }`.

This call returns a google.longrunning.Operation which may be used to
track the status of the field update. The metadata for
the operation will be the type FieldOperationMetadata.

To configure the default field settings for the database, use
the special `Field` with resource name:
`projects/{project_id}/databases/{database_id}/collectionGroups/__default__/fields/*`.

      Args:
        request: (FirestoreProjectsDatabasesCollectionGroupsFieldsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta2/projects/{projectsId}/databases/{databasesId}/collectionGroups/{collectionGroupsId}/fields/{fieldsId}',
        http_method='PATCH',
        method_id='firestore.projects.databases.collectionGroups.fields.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1beta2/{+name}',
        request_field='googleFirestoreAdminV1beta2Field',
        request_type_name='FirestoreProjectsDatabasesCollectionGroupsFieldsPatchRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

  class ProjectsDatabasesCollectionGroupsIndexesService(base_api.BaseApiService):
    """Service class for the projects_databases_collectionGroups_indexes resource."""

    _NAME = 'projects_databases_collectionGroups_indexes'

    def __init__(self, client):
      super(FirestoreV1beta2.ProjectsDatabasesCollectionGroupsIndexesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a composite index. This returns a google.longrunning.Operation.
which may be used to track the status of the creation. The metadata for
the operation will be the type IndexOperationMetadata.

      Args:
        request: (FirestoreProjectsDatabasesCollectionGroupsIndexesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta2/projects/{projectsId}/databases/{databasesId}/collectionGroups/{collectionGroupsId}/indexes',
        http_method='POST',
        method_id='firestore.projects.databases.collectionGroups.indexes.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1beta2/{+parent}/indexes',
        request_field='googleFirestoreAdminV1beta2Index',
        request_type_name='FirestoreProjectsDatabasesCollectionGroupsIndexesCreateRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a composite index.

      Args:
        request: (FirestoreProjectsDatabasesCollectionGroupsIndexesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta2/projects/{projectsId}/databases/{databasesId}/collectionGroups/{collectionGroupsId}/indexes/{indexesId}',
        http_method='DELETE',
        method_id='firestore.projects.databases.collectionGroups.indexes.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta2/{+name}',
        request_field='',
        request_type_name='FirestoreProjectsDatabasesCollectionGroupsIndexesDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets a composite index.

      Args:
        request: (FirestoreProjectsDatabasesCollectionGroupsIndexesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleFirestoreAdminV1beta2Index) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta2/projects/{projectsId}/databases/{databasesId}/collectionGroups/{collectionGroupsId}/indexes/{indexesId}',
        http_method='GET',
        method_id='firestore.projects.databases.collectionGroups.indexes.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta2/{+name}',
        request_field='',
        request_type_name='FirestoreProjectsDatabasesCollectionGroupsIndexesGetRequest',
        response_type_name='GoogleFirestoreAdminV1beta2Index',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists composite indexes.

      Args:
        request: (FirestoreProjectsDatabasesCollectionGroupsIndexesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleFirestoreAdminV1beta2ListIndexesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta2/projects/{projectsId}/databases/{databasesId}/collectionGroups/{collectionGroupsId}/indexes',
        http_method='GET',
        method_id='firestore.projects.databases.collectionGroups.indexes.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1beta2/{+parent}/indexes',
        request_field='',
        request_type_name='FirestoreProjectsDatabasesCollectionGroupsIndexesListRequest',
        response_type_name='GoogleFirestoreAdminV1beta2ListIndexesResponse',
        supports_download=False,
    )

  class ProjectsDatabasesCollectionGroupsService(base_api.BaseApiService):
    """Service class for the projects_databases_collectionGroups resource."""

    _NAME = 'projects_databases_collectionGroups'

    def __init__(self, client):
      super(FirestoreV1beta2.ProjectsDatabasesCollectionGroupsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsDatabasesService(base_api.BaseApiService):
    """Service class for the projects_databases resource."""

    _NAME = 'projects_databases'

    def __init__(self, client):
      super(FirestoreV1beta2.ProjectsDatabasesService, self).__init__(client)
      self._upload_configs = {
          }

    def ExportDocuments(self, request, global_params=None):
      r"""Exports a copy of all or a subset of documents from Google Cloud Firestore.
to another storage system, such as Google Cloud Storage. Recent updates to
documents may not be reflected in the export. The export occurs in the
background and its progress can be monitored and managed via the
Operation resource that is created. The output of an export may only be
used once the associated operation is done. If an export operation is
cancelled before completion it may leave partial data behind in Google
Cloud Storage.

      Args:
        request: (FirestoreProjectsDatabasesExportDocumentsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('ExportDocuments')
      return self._RunMethod(
          config, request, global_params=global_params)

    ExportDocuments.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta2/projects/{projectsId}/databases/{databasesId}:exportDocuments',
        http_method='POST',
        method_id='firestore.projects.databases.exportDocuments',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta2/{+name}:exportDocuments',
        request_field='googleFirestoreAdminV1beta2ExportDocumentsRequest',
        request_type_name='FirestoreProjectsDatabasesExportDocumentsRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def ImportDocuments(self, request, global_params=None):
      r"""Imports documents into Google Cloud Firestore. Existing documents with the.
same name are overwritten. The import occurs in the background and its
progress can be monitored and managed via the Operation resource that is
created. If an ImportDocuments operation is cancelled, it is possible
that a subset of the data has already been imported to Cloud Firestore.

      Args:
        request: (FirestoreProjectsDatabasesImportDocumentsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('ImportDocuments')
      return self._RunMethod(
          config, request, global_params=global_params)

    ImportDocuments.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta2/projects/{projectsId}/databases/{databasesId}:importDocuments',
        http_method='POST',
        method_id='firestore.projects.databases.importDocuments',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta2/{+name}:importDocuments',
        request_field='googleFirestoreAdminV1beta2ImportDocumentsRequest',
        request_type_name='FirestoreProjectsDatabasesImportDocumentsRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(FirestoreV1beta2.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
