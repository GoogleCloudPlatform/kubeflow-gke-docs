+++
title = "Kubeflow on Google Cloud v1.5.1"
description = "A new patch release of Kubeflow 1.5"
weight = 4
+++

A new version of Kubeflow on Google Cloud has been released! See the updated instructions on how to [deploy](https://googlecloudplatform.github.io/kubeflow-gke-docs/docs/deploy/) to a new cluster and [upgrade](https://googlecloudplatform.github.io/kubeflow-gke-docs/docs/deploy/upgrade/) an existing deployment.

### Changes:

- 🔼 Upgraded `ASM` to `v1.13`.
- 🔨 Fixed `KServe` issues with dashboard ([#362]((https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/362)) and directory([#361]((https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/361)).
- 🚚 Increased the maximum length of Kubeflow cluster name ([#359]((https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/359)).
- 🚚 Moved RequestAuthentication policy creation to `iap-enabler` to improve GitOps friendliness ([#364]((https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/364)).
- 🧪 Validated deployment using `GKE 1.21.11`.
