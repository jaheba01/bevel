"""Generated message classes for cloudresourcesearch version v1.

An API for searching over Google Cloud Platform Resources.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'cloudresourcesearch'


class CloudresourcesearchResourcesSearchRequest(_messages.Message):
  r"""A CloudresourcesearchResourcesSearchRequest object.

  Fields:
    orderBy: Optional. A comma-separated list of string-valued fields for
      sorting the results.  If this field is omitted, then the order of
      results is not defined. You can use fields from the resource schemas as
      well as the built-in fields `resourceName` and `resourceType`. Field
      values are ordered by their UTF-8 encodings.  Fields are sorted in
      ascending order by default. To sort a field in descending order, append
      `" desc"` to the field name. For example, the `order_by` value
      `"resource_type desc,resource_name"` sorts results by resource type in
      descending order; resources with the same type are returned in ascending
      order of their names.
    pageSize: Optional. The maximum number of resources to return from this
      request.  The presence of `next_page_token` in the response indicates
      that more resources are available.  The default value of `page_size` is
      20 and the maximum value is 1000.
    pageToken: Optional. If present, then retrieve the next batch of results
      from the preceding call to this method.  `page_token` must be the value
      of `next_page_token` from the previous response.  The values of other
      method parameters, including the query and sort order, must be identical
      to those in the previous call.
    query: Optional. The query string. If the query is missing or empty, all
      accessible resources are returned.  Any field in a supported resource
      type's schema may be specified in the query. Additionally, every
      resource has a `@type` field whose value is the resource's type URL. See
      `SearchResult.resource_type` for more information.  Example: The
      following query searches for accessible Compute Engine VM instances
      (`@type:Instance`) that have an `env` label value of `prod` and that
      have a machine type that starts with `"n1-stand"`:      @type:Instance
      labels.env:prod machineType:n1-stand*  For more information, see [Search
      Queries](/resource-search/docs/search-queries) and [Resource
      Types](/resource-search/docs/reference/Resource.Types).
  """

  orderBy = _messages.StringField(1)
  pageSize = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(3)
  query = _messages.StringField(4)


class SearchResponse(_messages.Message):
  r"""Response message for `resources.search`.

  Fields:
    matchedCount: The approximate total number of resources that match the
      query.  It will never be less than the number of resources returned so
      far, but it can change as additional pages of results are returned.
    nextPageToken: If there are more results than those appearing in this
      response, then `next_page_token` is included.  To get the next set of
      results, call this method again using the value of `next_page_token` as
      `page_token`.
    results: A list of resources that match the search query.
  """

  matchedCount = _messages.IntegerField(1)
  nextPageToken = _messages.StringField(2)
  results = _messages.MessageField('SearchResult', 3, repeated=True)


class SearchResult(_messages.Message):
  r"""A single Google Cloud Platform resource.

  Messages:
    ResourceValue: The matched resource, expressed as a JSON object.

  Fields:
    discoveryType: The JSON schema name listed in the discovery document.
      Example: `Project`.
    discoveryUrl: The URL of the discovery document containing the resource's
      JSON schema. Example:
      `https://cloudresourcemanager.googleapis.com/$discovery/rest`.
    resource: The matched resource, expressed as a JSON object.
    resourceName: The RPC resource name: a scheme-less URI that includes the
      DNS-compatible API service name. The URI does not include an API version
      and does not support %-encoding. Example:
      `//cloudresourcemanager.googleapis.com/projects/my-project-123`.
    resourceType: A domain-scoped name that describes the protocol buffer
      message type. Example:
      `type.googleapis.com/google.cloud.resourcemanager.v1.Project`.
    resourceUrl: The REST URL for accessing the resource. An HTTP GET
      operation using this URL returns an object equivalent to the value in
      the `resource` field. Example:
      `https://cloudresourcemanager.googleapis.com/v1/projects/my-
      project-123`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResourceValue(_messages.Message):
    r"""The matched resource, expressed as a JSON object.

    Messages:
      AdditionalProperty: An additional property for a ResourceValue object.

    Fields:
      additionalProperties: Properties of the object.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ResourceValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  discoveryType = _messages.StringField(1)
  discoveryUrl = _messages.StringField(2)
  resource = _messages.MessageField('ResourceValue', 3)
  resourceName = _messages.StringField(4)
  resourceType = _messages.StringField(5)
  resourceUrl = _messages.StringField(6)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default='json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
