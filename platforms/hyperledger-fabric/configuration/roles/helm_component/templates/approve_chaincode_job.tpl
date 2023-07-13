apiVersion: helm.toolkit.fluxcd.io/v2beta1
kind: HelmRelease
metadata:
  name: {{ component_name }}
  namespace: {{ namespace }}
  annotations:
    fluxcd.io/automated: "false"
spec:
  interval: 1m
  releaseName: {{ component_name }}
  chart:
    spec:
      interval: 1m
      sourceRef:
        kind: GitRepository
        name: flux-{{ network.env.type }}
        namespace: flux-{{ network.env.type }}
      chart: {{ charts_dir }}/approve_chaincode
  values:
    metadata:
      namespace: {{ namespace }}
      images:
        fabrictools: {{ fabrictools_image }}
        alpineutils: {{ alpine_image }}
    peer:
      name: {{ peer_name }}
      address: {{ peer_address }}
      localmspid: {{ name }}MSP
      loglevel: debug
      tlsstatus: true
    vault:
      role: vault-role
      address: {{ vault.url }}
      authpath: {{ network.env.type }}{{ namespace | e }}-auth
      adminsecretprefix: {{ vault.secret_path | default('secretsv2') }}/data/crypto/peerOrganizations/{{ namespace }}/users/admin 
      orderersecretprefix: {{ vault.secret_path | default('secretsv2') }}/data/crypto/peerOrganizations/{{ namespace }}/orderer
      serviceaccountname: vault-auth
{% if network.docker.username is defined and network.docker.password is defined %}
      imagesecretname: regcred
{% else %}
      imagesecretname: ""
{% endif %}
      tls: false
    orderer:
      address: {{ participant.ordererAddress }}
    chaincode:
      builder: hyperledger/fabric-ccenv:{{ network.version }}
      name: {{ component_chaincode.name | lower | e }}
      version: {{ component_chaincode.version | default('1') }}
      sequence: {{ component_chaincode.sequence | default('1') }}
      lang: {{ component_chaincode.lang | default('golang') }}
      commitarguments: {{ component_chaincode.arguments | default('') | quote }}
      endorsementpolicies:  {{ component_chaincode.endorsements | default('') | quote }}
{% if component_chaincode.repository is defined %}
      repository:
        hostname: "{{ component_chaincode.repository.url.split('/')[0] | lower }}"
        git_username: "{{ component_chaincode.repository.username}}"
        url: {{ component_chaincode.repository.url }}
        branch: {{ component_chaincode.repository.branch }}
        path: {{ component_chaincode.repository.path }}
{% endif %}
{% if peer.chaincode.pdc is defined and peer.chaincode.pdc.enabled %}
      pdc:
        enabled: true
        collectionsconfig: "{{ lookup('file', '{{ peer.chaincode.pdc.collections_config }}') | b64encode }}"
{% else %}
      pdc:
        enabled: false
{% if component_chaincode.repository.collections_config is defined %}
        collectionsconfig:  {{ component_chaincode.repository.collections_config }} 
{% else %}
        collectionsconfig:  ""
{% endif %}
{% endif %}
    channel:
      name: {{ item.channel_name | lower }}
