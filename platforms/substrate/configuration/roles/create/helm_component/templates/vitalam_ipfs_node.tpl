apiVersion: helm.fluxcd.io/v1
kind: HelmRelease
metadata:
  name: {{ component_name }}
  namespace: {{ component_ns }}
  annotations:
    fluxcd.io/automated: "false"
spec:
  releaseName: {{ component_name }}
  chart:
    git: {{ org.gitops.git_url }}
    ref: {{ org.gitops.branch }}
    path: {{ charts_dir }}/vitalam-ipfs-node
  values:
    fullnameOverride: {{ peer.name }}-ipfs
    config:
      healthCheckPort: 80
      nodeHost: {{ nodeHost }}
      logLevel: info
      ipfsApiPort: {{ peer.api.port }}
      ipfsSwarmPort: {{ peer.swarm.port }}
      ipfsDataPath: "/ipfs"
      ipfsCommand: "/usr/local/bin/ipfs"
      ipfsArgs:
        - daemon
      ipfsLogLevel: fatal
{% if ipfs_bootnode is defined %}
      ipfsBootNodeAddress: {{ ipfs_bootnode[1:] | join(',') }}
{% endif %}      
      enableLivenessProbe: true
    image:
      repository: {{ docker_url }}/digicatapult/vitalam-ipfs
      pullPolicy: IfNotPresent
      tag: 'v1.2.12'
    storage:
      storageClass: "{{ storageclass_name }}"
      dataVolumeSize: 20  # in Gigabytes
    vitalamNode:
      enabled: false
