+++
title = "Kubeflow on Google Cloud v1.6.0"
description = "A new minor release of Kubeflow 1.6"
weight = 40
+++

A new version of Kubeflow on Google Cloud has been released! See the updated instructions on how to [deploy](https://googlecloudplatform.github.io/kubeflow-gke-docs/docs/deploy/) to a new cluster and [upgrade](https://googlecloudplatform.github.io/kubeflow-gke-docs/docs/deploy/upgrade/) an existing deployment.

### Changes:

- 🔼 Upgraded upstream `Manifests` to `v1.6.0`.
- 🔼 Upgraded `ASM` to `v1.14` ([#385](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/385)).
- 🔼 Upgraded `Knative` to `v1.2` ([#373](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/373)).
- 🔼 Upgraded `cert-manager` to `v1.5` ([#372](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/372)).
- 🔼 Upgraded `pipelines` to `v2.0.0-alpha.4`.
- 🔼 Upgraded APIs to support `GKE 1.22` ([#349](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/349)).
- 🔨 Improved deployment stability ([#371](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/371), [#376](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/376), [#384](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/384), [#386](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/386)).
- 🚚 Removed deprecated `kfserving`, `cloud-endpoints`, and `application` manifests ([#375](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/375), [#377](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/377)).
- 🧪 Validated deployment using `GKE 1.21` and `GKE 1.22`.
