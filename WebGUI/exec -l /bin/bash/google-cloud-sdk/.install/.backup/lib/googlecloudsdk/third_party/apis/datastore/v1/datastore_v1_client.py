"""Generated client library for datastore version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.datastore.v1 import datastore_v1_messages as messages


class DatastoreV1(base_api.BaseApiClient):
  """Generated client library for service datastore version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://datastore.googleapis.com/'

  _PACKAGE = u'datastore'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/datastore']
  _VERSION = u'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'DatastoreV1'
  _URL_VERSION = u'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new datastore handle."""
    url = url or self.BASE_URL
    super(DatastoreV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.projects_operations = self.ProjectsOperationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsOperationsService(base_api.BaseApiService):
    """Service class for the projects_operations resource."""

    _NAME = u'projects_operations'

    def __init__(self, client):
      super(DatastoreV1.ProjectsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      """Starts asynchronous cancellation on a long-running operation.  The server.
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
        request: (DatastoreProjectsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/operations/{operationsId}:cancel',
        http_method=u'POST',
        method_id=u'datastore.projects.operations.cancel',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}:cancel',
        request_field='',
        request_type_name=u'DatastoreProjectsOperationsCancelRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes a long-running operation. This method indicates that the client is.
no longer interested in the operation result. It does not cancel the
operation. If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (DatastoreProjectsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/operations/{operationsId}',
        http_method=u'DELETE',
        method_id=u'datastore.projects.operations.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'DatastoreProjectsOperationsDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (DatastoreProjectsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/operations/{operationsId}',
        http_method=u'GET',
        method_id=u'datastore.projects.operations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'DatastoreProjectsOperationsGetRequest',
        response_type_name=u'GoogleLongrunningOperation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists operations that match the specified filter in the request. If the.
server doesn't support this method, it returns `UNIMPLEMENTED`.

NOTE: the `name` binding allows API services to override the binding
to use different resource name schemes, such as `users/*/operations`. To
override the binding, API services can add a binding such as
`"/v1/{name=users/*}/operations"` to their service configuration.
For backwards compatibility, the default name includes the operations
collection id, however overriding users must ensure the name binding
is the parent resource, without the operations collection id.

      Args:
        request: (DatastoreProjectsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/operations',
        http_method=u'GET',
        method_id=u'datastore.projects.operations.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1/{+name}/operations',
        request_field='',
        request_type_name=u'DatastoreProjectsOperationsListRequest',
        response_type_name=u'GoogleLongrunningListOperationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(DatastoreV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }

    def AllocateIds(self, request, global_params=None):
      """Allocates IDs for the given keys, which is useful for referencing an entity.
before it is inserted.

      Args:
        request: (DatastoreProjectsAllocateIdsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AllocateIdsResponse) The response message.
      """
      config = self.GetMethodConfig('AllocateIds')
      return self._RunMethod(
          config, request, global_params=global_params)

    AllocateIds.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'datastore.projects.allocateIds',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}:allocateIds',
        request_field=u'allocateIdsRequest',
        request_type_name=u'DatastoreProjectsAllocateIdsRequest',
        response_type_name=u'AllocateIdsResponse',
        supports_download=False,
    )

    def BeginTransaction(self, request, global_params=None):
      """Begins a new transaction.

      Args:
        request: (DatastoreProjectsBeginTransactionRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BeginTransactionResponse) The response message.
      """
      config = self.GetMethodConfig('BeginTransaction')
      return self._RunMethod(
          config, request, global_params=global_params)

    BeginTransaction.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'datastore.projects.beginTransaction',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}:beginTransaction',
        request_field=u'beginTransactionRequest',
        request_type_name=u'DatastoreProjectsBeginTransactionRequest',
        response_type_name=u'BeginTransactionResponse',
        supports_download=False,
    )

    def Commit(self, request, global_params=None):
      """Commits a transaction, optionally creating, deleting or modifying some.
entities.

      Args:
        request: (DatastoreProjectsCommitRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CommitResponse) The response message.
      """
      config = self.GetMethodConfig('Commit')
      return self._RunMethod(
          config, request, global_params=global_params)

    Commit.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'datastore.projects.commit',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}:commit',
        request_field=u'commitRequest',
        request_type_name=u'DatastoreProjectsCommitRequest',
        response_type_name=u'CommitResponse',
        supports_download=False,
    )

    def Lookup(self, request, global_params=None):
      """Looks up entities by key.

      Args:
        request: (DatastoreProjectsLookupRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LookupResponse) The response message.
      """
      config = self.GetMethodConfig('Lookup')
      return self._RunMethod(
          config, request, global_params=global_params)

    Lookup.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'datastore.projects.lookup',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}:lookup',
        request_field=u'lookupRequest',
        request_type_name=u'DatastoreProjectsLookupRequest',
        response_type_name=u'LookupResponse',
        supports_download=False,
    )

    def Rollback(self, request, global_params=None):
      """Rolls back a transaction.

      Args:
        request: (DatastoreProjectsRollbackRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (RollbackResponse) The response message.
      """
      config = self.GetMethodConfig('Rollback')
      return self._RunMethod(
          config, request, global_params=global_params)

    Rollback.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'datastore.projects.rollback',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}:rollback',
        request_field=u'rollbackRequest',
        request_type_name=u'DatastoreProjectsRollbackRequest',
        response_type_name=u'RollbackResponse',
        supports_download=False,
    )

    def RunQuery(self, request, global_params=None):
      """Queries for entities.

      Args:
        request: (DatastoreProjectsRunQueryRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (RunQueryResponse) The response message.
      """
      config = self.GetMethodConfig('RunQuery')
      return self._RunMethod(
          config, request, global_params=global_params)

    RunQuery.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'datastore.projects.runQuery',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}:runQuery',
        request_field=u'runQueryRequest',
        request_type_name=u'DatastoreProjectsRunQueryRequest',
        response_type_name=u'RunQueryResponse',
        supports_download=False,
    )
