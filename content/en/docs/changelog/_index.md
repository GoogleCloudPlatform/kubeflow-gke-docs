+++
title = "Changelog"
description = "Kubeflow on Google Cloud Changelog"
weight = 300
+++
## 1.8.0

[Release notes](https://github.com/GoogleCloudPlatform/kubeflow-distribution/releases/tag/v1.8.0)

### Changes:

- 🔼 Upgraded upstream `Manifests` to `v1.8.0`.

## 1.7.1

[Release notes](https://github.com/GoogleCloudPlatform/kubeflow-distribution/releases/tag/v1.7.1)

### Changes:

- 🔨 Fixed `make apply` deployment issue ([#425](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/425), [#426](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/426), [#427](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/427)).
- 🧪 Validated deployment using `GKE 1.25.8`.

## 1.7.0

[Release notes](https://github.com/googlecloudplatform/kubeflow-distribution/releases/tag/v1.7.0)

### Changes:

- 🔼 Upgraded upstream `Manifests` to `v1.7.0`.
- 🔼 Upgraded `Kubeflow Pipelines` to `v2.0.0-alpha.7`.
- 🔼 Upgraded `KNative` to `v1.8.5` ([#404](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/404)).
- 🔼 Upgraded `cert-manager` to `v1.10.2` ([#405](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/405)).
- 🔼 Upgraded `ASM` to `v1.16.2` ([#406](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/406)).
- 🔼 Upgraded `KServe` to `v0.10` ([#408](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/408)).
- 🔨 Fixed `ASM` deployment issue ([#413](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/413), [#419](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/419))
- 🔨 Fixed user header issue in `KServe`  web-app ([#414](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/414))
- 🧪 Validated deployment using `GKE 1.23`, `GKE 1.24`, `GKE 1.25`, and `GKE 1.26`.

## 1.6.1

[Release notes](https://github.com/googlecloudplatform/kubeflow-distribution/releases/tag/v1.6.1)

### Changes:

- 🔼 Upgraded upstream `Manifests` to `v1.6.1`.
- 🔼 Upgraded `pipelines` to `v2.0.0-alpha.6` (fixes [#392](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/392)).
- 🔼 Updated `MySQL` to `8.0` ([#391](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/391)).
- 🔨 Fixed `ASM` deployment issue ([#389](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/389))
- 🔨 Minor improvements of deployment process.
- 🧪 Validated deployment using `GKE 1.22`.

## 1.6.0:

[Release notes](https://github.com/googlecloudplatform/kubeflow-distribution/releases/tag/v1.6.0)

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


## 1.5.1

[Release notes](https://github.com/googlecloudplatform/kubeflow-distribution/releases/tag/v1.5.1)

### Changes:

- 🔼 Upgraded `ASM` to `v1.13`.
- 🔨 Fixed `KServe` issues with dashboard ([#362](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/362)) and directory ([#361](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/361)).
- 🚚 Increased the maximum length of Kubeflow cluster name ([#359](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/359)).
- 🚚 Moved RequestAuthentication policy creation to `iap-enabler` to improve GitOps friendliness ([#364](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/364)).
- 🧪 Validated deployment using `GKE 1.21.11`.

## 1.5.0:

[Release notes](https://github.com/googlecloudplatform/kubeflow-distribution/releases/tag/v1.5.0)

### Changes:

- 🔼 Upgrade Kubeflow components versions as listed in components versions table
- 🚀 Integrated with `Config Controller`, simplified management cluster maintenance cost, there is no need to manually upgrade `Config Connector` CRD.
- 🚚 Switch from `kfserving` to `KServe` as default serving component, you can switch back to `kfserving` in `config.yaml`.
- 🔨 Fixed `cloudsqlproxy` issue with `livenessProbe` configuration.
- 🧪 Validated deployment using `GKE 1.20.12`.

## 1.4.1

[Release notes](https://github.com/googlecloudplatform/kubeflow-distribution/releases/tag/v1.4.1)

### Changes:

Changes on top of v1.4.0:

- 🔼 Upgrade: Integrate with Kubeflow `1.4.1` manifests ([kubeflow/manifests#2084](https://github.com/kubeflow/manifests/issues/2084))
- 🔨 Fix: Change cloud endpoint images destination ([#343](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/343))
- 🔨 Fix: Use `yq4` in `iap-ingress` Makefile.

## 1.4.0:

[Release notes](https://github.com/googlecloudplatform/kubeflow-distribution/releases/tag/v1.4.0)

### Changes:

- 🔼 Upgrade Kubeflow components versions as listed in components versions table
- 🚢 Removed `GKE 1.18` image version and k8s runtime pin, now GKE version is default to `STABLE` channel.
- 🌊 Set Emissary Executor as default Argo Workflow executor for Kubeflow Pipelines.
- 🔼 Upgraded `kpt` versions from `0.X.X` to `1.0.0-beta.6`.
- 🔼 Upgraded `yq` from `v3` to `v4`.
- 🔼 Upgraded `ASM` (Anthos Service Mesh) to `1.10.4-asm.6`.
- 🚀 Unblocked `KFSserving` usage by removing `commonLabels` from kustomization patch ([#298](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/298) and [#324](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/324)).
- 🔗 Integrated with `KFServing` Web App UI.
- 🔗 Integrated with unified operator: `training-operator`.
- 🪁 Simplified deployment: Removed requirement for independent installation of `yq`, `jq`, `kustomize`, `kpt`.
