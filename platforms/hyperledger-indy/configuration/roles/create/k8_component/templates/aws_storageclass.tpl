kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: {{ component_name }}
provisioner: kubernetes.io/aws-ebs
reclaimPolicy: Delete
volumeBindingMode: Immediate
parameters:
  encrypted: "true"
  {% if encryption_key %}
  kmsKeyId: {{ encryption_key }}
  {% endif %}
{% if zone %}
allowedTopologies:
  - matchLabelExpressions:
    - key: failure-domain.beta.kubernetes.io/zone
      values: {{ zone }}
{% endif %}