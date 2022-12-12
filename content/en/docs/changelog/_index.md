+++
title = "Changelog"
description = "Kubeflow on Google Cloud Changelog"
weight = 300
+++

## 1.6.1

[Release notes](https://github.com/GoogleCloudPlatform/kubeflow-distribution/releases/tag/v1.6.1)

### Changes:

- 🔼 Upgraded upstream Manifests to v1.6.1.
- 🔼 Upgraded pipelines to v 2.0.0-alpha.6 (fixes #392).
- 🔼 Updated MySQL to 8.0 (#391).
- 🔨 Fixed ASM deployment issue (#389)
- 🔨 Minor improvements of deployment process.
- 🧪 Validated deployment using GKE 1.22.

## 1.6.0:

[Release notes](https://github.com/GoogleCloudPlatform/kubeflow-distribution/releases/tag/v1.6.0)

### Changes:

- 🔼 Upgraded upstream Manifests to v1.6.0
- 🔼 Upgraded ASM to v 1.14 (#385).
- 🔼 Upgraded Knative to v 1.2 (#373).
- 🔼 Upgraded cert-manager to v 1.5 (#372).
- 🔼 Upgraded pipelines to v 2.0.0-alpha.4.
- 🔼 Upgraded APIs to support GKE 1.22 (#349).
- 🔨 Improved deployment stability (#371, #376, #384, #386).
- 🚚 Removed deprecated kfserving, cloud-endpoints, and application manifests (#375, #377).
- 🧪 Validated deployment using GKE 1.21 and GKE 1.22.

## 1.5.1

[Release notes](https://github.com/GoogleCloudPlatform/kubeflow-distribution/releases/tag/v1.5.1)

### Changes:

- 🔼 Upgraded ASM to v 1.13.
- 🔨 Fixed KServe issues with dashboard (#362) and directory(#361).
- 🚚 Increased the maximum length of Kubeflow cluster name (#359).
- 🚚 Moved RequestAuthentication policy creation to iap-enabler to improve GitOps friendliness (#364).
- 🧪 Validated deployment using GKE 1.21.11.

## 1.5.0:

[Release notes](https://github.com/GoogleCloudPlatform/kubeflow-distribution/releases/tag/v1.5.0)

### Changes:

- 🔼 Upgrade Kubeflow components versions as listed in [components versions table](https://github.com/kubeflow/manifests/tree/v1.5.0#kubeflow-components-versions)
- 🚀 Integrated with Config Controller, simplified management cluster maintenance cost, there is no need to manually upgrade Config Connector CRD.
- 🚚 Switch from kfserving to KServe as default serving component, you can switch back to kfserving in `config.yaml`.
- 🔨 Fixed cloudsqlproxy issue with livenessProbe configuration.
- 🧪 Validated deployment using GKE 1.20.12.

## 1.4.1

[Release notes](https://github.com/GoogleCloudPlatform/kubeflow-distribution/releases/tag/v1.4.1)

### Changes:

Changes on top of v1.4.0:

- 🔼 Upgrade: Integrate with Kubeflow 1.4.1 manifests (kubeflow/manifests#2084)
- 🔨 Fix: Change cloud endpoint images destination (#343)
- 🔨 Fix: Use yq4 in iap-ingress Makefile.

## 1.4.0:

[Release notes](https://github.com/GoogleCloudPlatform/kubeflow-distribution/releases/tag/v1.4.0)

### Changes:

- 🔼 Upgrade Kubeflow components versions as listed in components versions table
- 🚢 Removed GKE 1.18 image version and k8s runtime pin, now GKE version is default to Stable channel.
- 🌊 Set Emissary Executor as default Argo Workflow executor for Kubeflow Pipelines.
- 🔼 Upgraded kpt versions from 0.X.X to 1.0.0-beta.6.
- 🔼 Upgraded yq from v3 to v4.
- 🔼 Upgraded ASM(Anthos Service Mesh) to 1.10.4-asm.6.
- 🚀 Unblocked KFSserving usage by removing commonLabels from kustomization patch #298 #324.
- 🔗 Integrated with KFServing Web App UI.
- 🔗 Integrated with unified operator: training-operator.
- 🪁 Simplified deployment: Removed requirement for independent installation of yq, jq, kustomize, kpt.
