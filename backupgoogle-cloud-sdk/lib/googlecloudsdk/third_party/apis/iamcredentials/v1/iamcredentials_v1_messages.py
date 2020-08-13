"""Generated message classes for iamcredentials version v1.

Creates short-lived credentials for impersonating IAM service accounts.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding


package = 'iamcredentials'


class GenerateAccessTokenRequest(_messages.Message):
  r"""A GenerateAccessTokenRequest object.

  Fields:
    delegates: The sequence of service accounts in a delegation chain. Each
      service account must be granted the
      `roles/iam.serviceAccountTokenCreator` role on its next service account
      in the chain. The last service account in the chain must be granted the
      `roles/iam.serviceAccountTokenCreator` role on the service account that
      is specified in the `name` field of the request.  The delegates must
      have the following format:
      `projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}`. The `-`
      wildcard character is required; replacing it with a project ID is
      invalid.
    lifetime: The desired lifetime duration of the access token in seconds.
      Must be set to a value less than or equal to 3600 (1 hour). If a value
      is not specified, the token's lifetime will be set to a default value of
      one hour.
    scope: Required. Code to identify the scopes to be included in the OAuth
      2.0 access token. See
      https://developers.google.com/identity/protocols/googlescopes for more
      information. At least one value required.
  """

  delegates = _messages.StringField(1, repeated=True)
  lifetime = _messages.StringField(2)
  scope = _messages.StringField(3, repeated=True)


class GenerateAccessTokenResponse(_messages.Message):
  r"""A GenerateAccessTokenResponse object.

  Fields:
    accessToken: The OAuth 2.0 access token.
    expireTime: Token expiration time. The expiration time is always set.
  """

  accessToken = _messages.StringField(1)
  expireTime = _messages.StringField(2)


class GenerateIdTokenRequest(_messages.Message):
  r"""A GenerateIdTokenRequest object.

  Fields:
    audience: Required. The audience for the token, such as the API or account
      that this token grants access to.
    delegates: The sequence of service accounts in a delegation chain. Each
      service account must be granted the
      `roles/iam.serviceAccountTokenCreator` role on its next service account
      in the chain. The last service account in the chain must be granted the
      `roles/iam.serviceAccountTokenCreator` role on the service account that
      is specified in the `name` field of the request.  The delegates must
      have the following format:
      `projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}`. The `-`
      wildcard character is required; replacing it with a project ID is
      invalid.
    includeEmail: Include the service account email in the token. If set to
      `true`, the token will contain `email` and `email_verified` claims.
  """

  audience = _messages.StringField(1)
  delegates = _messages.StringField(2, repeated=True)
  includeEmail = _messages.BooleanField(3)


class GenerateIdTokenResponse(_messages.Message):
  r"""A GenerateIdTokenResponse object.

  Fields:
    token: The OpenId Connect ID token.
  """

  token = _messages.StringField(1)


class IamcredentialsProjectsServiceAccountsGenerateAccessTokenRequest(_messages.Message):
  r"""A IamcredentialsProjectsServiceAccountsGenerateAccessTokenRequest
  object.

  Fields:
    generateAccessTokenRequest: A GenerateAccessTokenRequest resource to be
      passed as the request body.
    name: Required. The resource name of the service account for which the
      credentials are requested, in the following format:
      `projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}`. The `-`
      wildcard character is required; replacing it with a project ID is
      invalid.
  """

  generateAccessTokenRequest = _messages.MessageField('GenerateAccessTokenRequest', 1)
  name = _messages.StringField(2, required=True)


class IamcredentialsProjectsServiceAccountsGenerateIdTokenRequest(_messages.Message):
  r"""A IamcredentialsProjectsServiceAccountsGenerateIdTokenRequest object.

  Fields:
    generateIdTokenRequest: A GenerateIdTokenRequest resource to be passed as
      the request body.
    name: Required. The resource name of the service account for which the
      credentials are requested, in the following format:
      `projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}`. The `-`
      wildcard character is required; replacing it with a project ID is
      invalid.
  """

  generateIdTokenRequest = _messages.MessageField('GenerateIdTokenRequest', 1)
  name = _messages.StringField(2, required=True)


class IamcredentialsProjectsServiceAccountsSignBlobRequest(_messages.Message):
  r"""A IamcredentialsProjectsServiceAccountsSignBlobRequest object.

  Fields:
    name: Required. The resource name of the service account for which the
      credentials are requested, in the following format:
      `projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}`. The `-`
      wildcard character is required; replacing it with a project ID is
      invalid.
    signBlobRequest: A SignBlobRequest resource to be passed as the request
      body.
  """

  name = _messages.StringField(1, required=True)
  signBlobRequest = _messages.MessageField('SignBlobRequest', 2)


class IamcredentialsProjectsServiceAccountsSignJwtRequest(_messages.Message):
  r"""A IamcredentialsProjectsServiceAccountsSignJwtRequest object.

  Fields:
    name: Required. The resource name of the service account for which the
      credentials are requested, in the following format:
      `projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}`. The `-`
      wildcard character is required; replacing it with a project ID is
      invalid.
    signJwtRequest: A SignJwtRequest resource to be passed as the request
      body.
  """

  name = _messages.StringField(1, required=True)
  signJwtRequest = _messages.MessageField('SignJwtRequest', 2)


class SignBlobRequest(_messages.Message):
  r"""A SignBlobRequest object.

  Fields:
    delegates: The sequence of service accounts in a delegation chain. Each
      service account must be granted the
      `roles/iam.serviceAccountTokenCreator` role on its next service account
      in the chain. The last service account in the chain must be granted the
      `roles/iam.serviceAccountTokenCreator` role on the service account that
      is specified in the `name` field of the request.  The delegates must
      have the following format:
      `projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}`. The `-`
      wildcard character is required; replacing it with a project ID is
      invalid.
    payload: Required. The bytes to sign.
  """

  delegates = _messages.StringField(1, repeated=True)
  payload = _messages.BytesField(2)


class SignBlobResponse(_messages.Message):
  r"""A SignBlobResponse object.

  Fields:
    keyId: The ID of the key used to sign the blob. The key used for signing
      will remain valid for at least 12 hours after the blob is signed. To
      verify the signature, you can retrieve the public key in several formats
      from the following endpoints:  - RSA public key wrapped in an X.509 v3
      certificate: `https://www.googleapis.com/service_accounts/v1/metadata/x5
      09/{ACCOUNT_EMAIL}` - Raw key in JSON format: `https://www.googleapis.co
      m/service_accounts/v1/metadata/raw/{ACCOUNT_EMAIL}` - JSON Web Key
      (JWK): `https://www.googleapis.com/service_accounts/v1/metadata/jwk/{ACC
      OUNT_EMAIL}`
    signedBlob: The signature for the blob. Does not include the original
      blob.  After the key pair referenced by the `key_id` response field
      expires, Google no longer exposes the public key that can be used to
      verify the blob. As a result, the receiver can no longer verify the
      signature.
  """

  keyId = _messages.StringField(1)
  signedBlob = _messages.BytesField(2)


class SignJwtRequest(_messages.Message):
  r"""A SignJwtRequest object.

  Fields:
    delegates: The sequence of service accounts in a delegation chain. Each
      service account must be granted the
      `roles/iam.serviceAccountTokenCreator` role on its next service account
      in the chain. The last service account in the chain must be granted the
      `roles/iam.serviceAccountTokenCreator` role on the service account that
      is specified in the `name` field of the request.  The delegates must
      have the following format:
      `projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}`. The `-`
      wildcard character is required; replacing it with a project ID is
      invalid.
    payload: Required. The JWT payload to sign. Must be a serialized JSON
      object that contains a JWT Claims Set. For example: `{"sub":
      "user@example.com", "iat": 313435}`  If the JWT Claims Set contains an
      expiration time (`exp`) claim, it must be an integer timestamp that is
      not in the past and no more than 12 hours in the future.
  """

  delegates = _messages.StringField(1, repeated=True)
  payload = _messages.StringField(2)


class SignJwtResponse(_messages.Message):
  r"""A SignJwtResponse object.

  Fields:
    keyId: The ID of the key used to sign the JWT. The key used for signing
      will remain valid for at least 12 hours after the JWT is signed. To
      verify the signature, you can retrieve the public key in several formats
      from the following endpoints:  - RSA public key wrapped in an X.509 v3
      certificate: `https://www.googleapis.com/service_accounts/v1/metadata/x5
      09/{ACCOUNT_EMAIL}` - Raw key in JSON format: `https://www.googleapis.co
      m/service_accounts/v1/metadata/raw/{ACCOUNT_EMAIL}` - JSON Web Key
      (JWK): `https://www.googleapis.com/service_accounts/v1/metadata/jwk/{ACC
      OUNT_EMAIL}`
    signedJwt: The signed JWT. Contains the automatically generated header;
      the client-supplied payload; and the signature, which is generated using
      the key referenced by the `kid` field in the header.  After the key pair
      referenced by the `key_id` response field expires, Google no longer
      exposes the public key that can be used to verify the JWT. As a result,
      the receiver can no longer verify the signature.
  """

  keyId = _messages.StringField(1)
  signedJwt = _messages.StringField(2)


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
