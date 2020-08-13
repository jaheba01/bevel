"""Generated message classes for recaptchaenterprise version v1.

"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding


package = 'recaptchaenterprise'


class GoogleCloudRecaptchaenterpriseV1AndroidKeySettings(_messages.Message):
  r"""Settings specific to keys that can be used by Android apps.

  Fields:
    allowedPackageNames: Android package names of apps allowed to use the key.
      Example: 'com.companyname.appname'
  """

  allowedPackageNames = _messages.StringField(1, repeated=True)


class GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequest(_messages.Message):
  r"""The request message to annotate an Assessment.

  Enums:
    AnnotationValueValuesEnum: Required. The annotation that will be assigned
      to the Event.

  Fields:
    annotation: Required. The annotation that will be assigned to the Event.
  """

  class AnnotationValueValuesEnum(_messages.Enum):
    r"""Required. The annotation that will be assigned to the Event.

    Values:
      ANNOTATION_UNSPECIFIED: Default unspecified type.
      LEGITIMATE: Provides information that the event turned out to be
        legitimate.
      FRAUDULENT: Provides information that the event turned out to be
        fraudulent.
      PASSWORD_CORRECT: Provides information that the event was related to a
        login event in which the user typed the correct password.
      PASSWORD_INCORRECT: Provides information that the event was related to a
        login event in which the user typed the incorrect password.
    """
    ANNOTATION_UNSPECIFIED = 0
    LEGITIMATE = 1
    FRAUDULENT = 2
    PASSWORD_CORRECT = 3
    PASSWORD_INCORRECT = 4

  annotation = _messages.EnumField('AnnotationValueValuesEnum', 1)


class GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentResponse(_messages.Message):
  r"""Empty response for AnnotateAssessment."""


class GoogleCloudRecaptchaenterpriseV1Assessment(_messages.Message):
  r"""A recaptcha assessment resource.

  Fields:
    event: The event being assessed.
    name: Output only. The resource name for the Assessment in the format
      "projects/{project}/assessments/{assessment}".
    riskAnalysis: Output only. The risk analysis result for the event being
      assessed.
    tokenProperties: Output only. Properties of the provided event token.
  """

  event = _messages.MessageField('GoogleCloudRecaptchaenterpriseV1Event', 1)
  name = _messages.StringField(2)
  riskAnalysis = _messages.MessageField('GoogleCloudRecaptchaenterpriseV1RiskAnalysis', 3)
  tokenProperties = _messages.MessageField('GoogleCloudRecaptchaenterpriseV1TokenProperties', 4)


class GoogleCloudRecaptchaenterpriseV1ChallengeMetrics(_messages.Message):
  r"""Metrics related to challenges.

  Fields:
    failedCount: Count of submitted challenge solutions that were incorrect or
      otherwise deemed suspicious such that a subsequent challenge was
      triggered.
    nocaptchaCount: Count of nocaptchas (successful verification without a
      challenge) issued.
    pageloadCount: Count of reCAPTCHA checkboxes or badges rendered. This is
      mostly equivalent to a count of pageloads for pages that include
      reCAPTCHA.
    passedCount: Count of nocaptchas (successful verification without a
      challenge) plus submitted challenge solutions that were correct and
      resulted in verification.
  """

  failedCount = _messages.IntegerField(1)
  nocaptchaCount = _messages.IntegerField(2)
  pageloadCount = _messages.IntegerField(3)
  passedCount = _messages.IntegerField(4)


class GoogleCloudRecaptchaenterpriseV1Event(_messages.Message):
  r"""A GoogleCloudRecaptchaenterpriseV1Event object.

  Fields:
    expectedAction: Optional. The expected action for this type of event. This
      should be the same action provided at token generation time on client-
      side platforms already integrated with recaptcha enterprise.
    siteKey: Optional. The site key that was used to invoke reCAPTCHA on your
      site and generate the token.
    token: Optional. The user response token provided by the reCAPTCHA client-
      side integration on your site.
    userAgent: Optional. The user agent present in the request from the user's
      device related to this event.
    userIpAddress: Optional. The IP address in the request from the user's
      device related to this event.
  """

  expectedAction = _messages.StringField(1)
  siteKey = _messages.StringField(2)
  token = _messages.StringField(3)
  userAgent = _messages.StringField(4)
  userIpAddress = _messages.StringField(5)


class GoogleCloudRecaptchaenterpriseV1IOSKeySettings(_messages.Message):
  r"""Settings specific to keys that can be used by iOS apps.

  Fields:
    allowedBundleIds: iOS bundle ids of apps allowed to use the key. Example:
      'com.companyname.productname.appname'
  """

  allowedBundleIds = _messages.StringField(1, repeated=True)


class GoogleCloudRecaptchaenterpriseV1Key(_messages.Message):
  r"""A key used to identify and configure applications (web and/or mobile)
  that use reCAPTCHA Enterprise.

  Messages:
    LabelsValue: See <a href="https://cloud.google.com/recaptcha-
      enterprise/docs/labels"> Creating and managing labels</a>.

  Fields:
    androidSettings: Settings for keys that can be used by Android apps.
    createTime: The timestamp corresponding to the creation of this Key.
    displayName: Human-readable display name of this key. Modifiable by user.
    iosSettings: Settings for keys that can be used by iOS apps.
    labels: See <a href="https://cloud.google.com/recaptcha-
      enterprise/docs/labels"> Creating and managing labels</a>.
    name: The resource name for the Key in the format
      "projects/{project}/keys/{key}".
    webSettings: Settings for keys that can be used by websites.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""See <a href="https://cloud.google.com/recaptcha-
    enterprise/docs/labels"> Creating and managing labels</a>.

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  androidSettings = _messages.MessageField('GoogleCloudRecaptchaenterpriseV1AndroidKeySettings', 1)
  createTime = _messages.StringField(2)
  displayName = _messages.StringField(3)
  iosSettings = _messages.MessageField('GoogleCloudRecaptchaenterpriseV1IOSKeySettings', 4)
  labels = _messages.MessageField('LabelsValue', 5)
  name = _messages.StringField(6)
  webSettings = _messages.MessageField('GoogleCloudRecaptchaenterpriseV1WebKeySettings', 7)


class GoogleCloudRecaptchaenterpriseV1ListKeysResponse(_messages.Message):
  r"""Response to request to list keys in a project.

  Fields:
    keys: Key details.
    nextPageToken: Token to retrieve the next page of results. It is set to
      empty if no keys remain in results.
  """

  keys = _messages.MessageField('GoogleCloudRecaptchaenterpriseV1Key', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class GoogleCloudRecaptchaenterpriseV1Metrics(_messages.Message):
  r"""Metrics for a single Key.

  Fields:
    challengeMetrics: Metrics will be continuous and in order by dates, and in
      the granularity of day. Only challenge-based keys (CHECKBOX, INVISIBLE),
      will have challenge-based data.
    scoreMetrics: Metrics will be continuous and in order by dates, and in the
      granularity of day. All Key types should have score-based data.
    startTime: Inclusive start time aligned to a day (UTC).
  """

  challengeMetrics = _messages.MessageField('GoogleCloudRecaptchaenterpriseV1ChallengeMetrics', 1, repeated=True)
  scoreMetrics = _messages.MessageField('GoogleCloudRecaptchaenterpriseV1ScoreMetrics', 2, repeated=True)
  startTime = _messages.StringField(3)


class GoogleCloudRecaptchaenterpriseV1RiskAnalysis(_messages.Message):
  r"""Risk analysis result for an event.

  Enums:
    ReasonsValueListEntryValuesEnum:

  Fields:
    reasons: Reasons contributing to the risk analysis verdict.
    score: Legitimate event score from 0.0 to 1.0. (1.0 means very likely
      legitimate traffic while 0.0 means very likely non-legitimate traffic).
  """

  class ReasonsValueListEntryValuesEnum(_messages.Enum):
    r"""ReasonsValueListEntryValuesEnum enum type.

    Values:
      CLASSIFICATION_REASON_UNSPECIFIED: <no description>
      AUTOMATION: <no description>
      UNEXPECTED_ENVIRONMENT: <no description>
      TOO_MUCH_TRAFFIC: <no description>
      UNEXPECTED_USAGE_PATTERNS: <no description>
      LOW_CONFIDENCE_SCORE: <no description>
    """
    CLASSIFICATION_REASON_UNSPECIFIED = 0
    AUTOMATION = 1
    UNEXPECTED_ENVIRONMENT = 2
    TOO_MUCH_TRAFFIC = 3
    UNEXPECTED_USAGE_PATTERNS = 4
    LOW_CONFIDENCE_SCORE = 5

  reasons = _messages.EnumField('ReasonsValueListEntryValuesEnum', 1, repeated=True)
  score = _messages.FloatField(2, variant=_messages.Variant.FLOAT)


class GoogleCloudRecaptchaenterpriseV1ScoreDistribution(_messages.Message):
  r"""Score distribution.

  Messages:
    ScoreBucketsValue: Map key is score value multiplied by 100. The scores
      are discrete values between [0, 1]. The maximum number of buckets is on
      order of a few dozen, but typically much lower (ie. 10).

  Fields:
    scoreBuckets: Map key is score value multiplied by 100. The scores are
      discrete values between [0, 1]. The maximum number of buckets is on
      order of a few dozen, but typically much lower (ie. 10).
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ScoreBucketsValue(_messages.Message):
    r"""Map key is score value multiplied by 100. The scores are discrete
    values between [0, 1]. The maximum number of buckets is on order of a few
    dozen, but typically much lower (ie. 10).

    Messages:
      AdditionalProperty: An additional property for a ScoreBucketsValue
        object.

    Fields:
      additionalProperties: Additional properties of type ScoreBucketsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ScoreBucketsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.IntegerField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  scoreBuckets = _messages.MessageField('ScoreBucketsValue', 1)


class GoogleCloudRecaptchaenterpriseV1ScoreMetrics(_messages.Message):
  r"""Metrics related to scoring.

  Messages:
    ActionMetricsValue: Action-based metrics. The map key is the action name
      which specified by the site owners at time of the "execute" client-side
      call. Populated only for SCORE keys.

  Fields:
    actionMetrics: Action-based metrics. The map key is the action name which
      specified by the site owners at time of the "execute" client-side call.
      Populated only for SCORE keys.
    overallMetrics: Aggregated score metrics for all traffic.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ActionMetricsValue(_messages.Message):
    r"""Action-based metrics. The map key is the action name which specified
    by the site owners at time of the "execute" client-side call. Populated
    only for SCORE keys.

    Messages:
      AdditionalProperty: An additional property for a ActionMetricsValue
        object.

    Fields:
      additionalProperties: Additional properties of type ActionMetricsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ActionMetricsValue object.

      Fields:
        key: Name of the additional property.
        value: A GoogleCloudRecaptchaenterpriseV1ScoreDistribution attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('GoogleCloudRecaptchaenterpriseV1ScoreDistribution', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  actionMetrics = _messages.MessageField('ActionMetricsValue', 1)
  overallMetrics = _messages.MessageField('GoogleCloudRecaptchaenterpriseV1ScoreDistribution', 2)


class GoogleCloudRecaptchaenterpriseV1TokenProperties(_messages.Message):
  r"""A GoogleCloudRecaptchaenterpriseV1TokenProperties object.

  Enums:
    InvalidReasonValueValuesEnum: Reason associated with the response when
      valid = false.

  Fields:
    action: Action name provided at token generation.
    createTime: The timestamp corresponding to the generation of the token.
    hostname: The hostname of the page on which the token was generated.
    invalidReason: Reason associated with the response when valid = false.
    valid: Whether the provided user response token is valid. When valid =
      false, the reason could be specified in invalid_reason or it could also
      be due to a user failing to solve a challenge or a sitekey mismatch (i.e
      the sitekey used to generate the token was different than the one
      specified in the assessment).
  """

  class InvalidReasonValueValuesEnum(_messages.Enum):
    r"""Reason associated with the response when valid = false.

    Values:
      INVALID_REASON_UNSPECIFIED: Default unspecified type.
      UNKNOWN_INVALID_REASON: If the failure reason was not accounted for.
      MALFORMED: The provided user verification token was malformed.
      EXPIRED: The user verification token had expired.
      DUPE: The user verification had already been seen.
      MISSING: The user verification token was not present.
    """
    INVALID_REASON_UNSPECIFIED = 0
    UNKNOWN_INVALID_REASON = 1
    MALFORMED = 2
    EXPIRED = 3
    DUPE = 4
    MISSING = 5

  action = _messages.StringField(1)
  createTime = _messages.StringField(2)
  hostname = _messages.StringField(3)
  invalidReason = _messages.EnumField('InvalidReasonValueValuesEnum', 4)
  valid = _messages.BooleanField(5)


class GoogleCloudRecaptchaenterpriseV1WebKeySettings(_messages.Message):
  r"""Settings specific to keys that can be used by websites.

  Enums:
    ChallengeSecurityPreferenceValueValuesEnum: Settings for the frequency and
      difficulty at which this key triggers captcha challenges. This should
      only be specified for IntegrationTypes CHECKBOX and INVISIBLE.
    IntegrationTypeValueValuesEnum: Required. Describes how this key is
      integrated with the website.

  Fields:
    allowAllDomains: If set to true, it means allowed_domains will not be
      enforced.
    allowAmpTraffic: Required. Whether this key can be used on AMP
      (Accelerated Mobile Pages) websites. This can only be set for the SCORE
      integration type.
    allowedDomains: Domains or subdomains of websites allowed to use the key.
      All subdomains of an allowed domain are automatically allowed. A valid
      domain requires a host and must not include any path, port, query or
      fragment. Examples: 'example.com' or 'subdomain.example.com'
    challengeSecurityPreference: Settings for the frequency and difficulty at
      which this key triggers captcha challenges. This should only be
      specified for IntegrationTypes CHECKBOX and INVISIBLE.
    integrationType: Required. Describes how this key is integrated with the
      website.
  """

  class ChallengeSecurityPreferenceValueValuesEnum(_messages.Enum):
    r"""Settings for the frequency and difficulty at which this key triggers
    captcha challenges. This should only be specified for IntegrationTypes
    CHECKBOX and INVISIBLE.

    Values:
      CHALLENGE_SECURITY_PREFERENCE_UNSPECIFIED: Default type that indicates
        this enum hasn't been specified.
      USABILITY: Key tends to show fewer and easier challenges.
      BALANCE: Key tends to show balanced (in amount and difficulty)
        challenges.
      SECURITY: Key tends to show more and harder challenges.
    """
    CHALLENGE_SECURITY_PREFERENCE_UNSPECIFIED = 0
    USABILITY = 1
    BALANCE = 2
    SECURITY = 3

  class IntegrationTypeValueValuesEnum(_messages.Enum):
    r"""Required. Describes how this key is integrated with the website.

    Values:
      INTEGRATION_TYPE_UNSPECIFIED: Default type that indicates this enum
        hasn't been specified. This is not a valid IntegrationType, one of the
        other types must be specified instead.
      SCORE: Only used to produce scores. It doesn't display the "I'm not a
        robot" checkbox and never shows captcha challenges.
      CHECKBOX: Displays the "I'm not a robot" checkbox and may show captcha
        challenges after it is checked.
      INVISIBLE: Doesn't display the "I'm not a robot" checkbox, but may show
        captcha challenges after risk analysis.
    """
    INTEGRATION_TYPE_UNSPECIFIED = 0
    SCORE = 1
    CHECKBOX = 2
    INVISIBLE = 3

  allowAllDomains = _messages.BooleanField(1)
  allowAmpTraffic = _messages.BooleanField(2)
  allowedDomains = _messages.StringField(3, repeated=True)
  challengeSecurityPreference = _messages.EnumField('ChallengeSecurityPreferenceValueValuesEnum', 4)
  integrationType = _messages.EnumField('IntegrationTypeValueValuesEnum', 5)


class GoogleProtobufEmpty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance:      service Foo {
  rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);     }  The
  JSON representation for `Empty` is empty JSON object `{}`.
  """



class RecaptchaenterpriseProjectsAssessmentsAnnotateRequest(_messages.Message):
  r"""A RecaptchaenterpriseProjectsAssessmentsAnnotateRequest object.

  Fields:
    googleCloudRecaptchaenterpriseV1AnnotateAssessmentRequest: A
      GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequest resource to be
      passed as the request body.
    name: Required. The resource name of the Assessment, in the format
      "projects/{project}/assessments/{assessment}".
  """

  googleCloudRecaptchaenterpriseV1AnnotateAssessmentRequest = _messages.MessageField('GoogleCloudRecaptchaenterpriseV1AnnotateAssessmentRequest', 1)
  name = _messages.StringField(2, required=True)


class RecaptchaenterpriseProjectsAssessmentsCreateRequest(_messages.Message):
  r"""A RecaptchaenterpriseProjectsAssessmentsCreateRequest object.

  Fields:
    googleCloudRecaptchaenterpriseV1Assessment: A
      GoogleCloudRecaptchaenterpriseV1Assessment resource to be passed as the
      request body.
    parent: Required. The name of the project in which the assessment will be
      created, in the format "projects/{project}".
  """

  googleCloudRecaptchaenterpriseV1Assessment = _messages.MessageField('GoogleCloudRecaptchaenterpriseV1Assessment', 1)
  parent = _messages.StringField(2, required=True)


class RecaptchaenterpriseProjectsKeysCreateRequest(_messages.Message):
  r"""A RecaptchaenterpriseProjectsKeysCreateRequest object.

  Fields:
    googleCloudRecaptchaenterpriseV1Key: A GoogleCloudRecaptchaenterpriseV1Key
      resource to be passed as the request body.
    parent: Required. The name of the project in which the key will be
      created, in the format "projects/{project}".
  """

  googleCloudRecaptchaenterpriseV1Key = _messages.MessageField('GoogleCloudRecaptchaenterpriseV1Key', 1)
  parent = _messages.StringField(2, required=True)


class RecaptchaenterpriseProjectsKeysDeleteRequest(_messages.Message):
  r"""A RecaptchaenterpriseProjectsKeysDeleteRequest object.

  Fields:
    name: Required. The name of the key to be deleted, in the format
      "projects/{project}/keys/{key}".
  """

  name = _messages.StringField(1, required=True)


class RecaptchaenterpriseProjectsKeysGetMetricsRequest(_messages.Message):
  r"""A RecaptchaenterpriseProjectsKeysGetMetricsRequest object.

  Fields:
    name: Required. The name of the requested metrics, in the format
      "projects/{project}/keys/{key}/metrics".
  """

  name = _messages.StringField(1, required=True)


class RecaptchaenterpriseProjectsKeysGetRequest(_messages.Message):
  r"""A RecaptchaenterpriseProjectsKeysGetRequest object.

  Fields:
    name: Required. The name of the requested key, in the format
      "projects/{project}/keys/{key}".
  """

  name = _messages.StringField(1, required=True)


class RecaptchaenterpriseProjectsKeysListRequest(_messages.Message):
  r"""A RecaptchaenterpriseProjectsKeysListRequest object.

  Fields:
    pageSize: Optional. The maximum number of keys to return. Default is 10.
      Max limit is 1000.
    pageToken: Optional. The next_page_token value returned from a previous.
      ListKeysRequest, if any.
    parent: Required. The name of the project that contains the keys that will
      be listed, in the format "projects/{project}".
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class RecaptchaenterpriseProjectsKeysPatchRequest(_messages.Message):
  r"""A RecaptchaenterpriseProjectsKeysPatchRequest object.

  Fields:
    googleCloudRecaptchaenterpriseV1Key: A GoogleCloudRecaptchaenterpriseV1Key
      resource to be passed as the request body.
    name: The resource name for the Key in the format
      "projects/{project}/keys/{key}".
    updateMask: Optional. The mask to control which field of the key get
      updated. If the mask is not present, all fields will be updated.
  """

  googleCloudRecaptchaenterpriseV1Key = _messages.MessageField('GoogleCloudRecaptchaenterpriseV1Key', 1)
  name = _messages.StringField(2, required=True)
  updateMask = _messages.StringField(3)


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
