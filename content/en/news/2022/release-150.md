+++
title = "Kubeflow on Google Cloud v1.5.0"
description = "A new minor release of Kubeflow 1.5"
weight = 5
+++

A new version of Kubeflow on Google Cloud has been released! See the updated instructions on how to [deploy](https://googlecloudplatform.github.io/kubeflow-gke-docs/docs/deploy/) to a new cluster and [upgrade](https://googlecloudplatform.github.io/kubeflow-gke-docs/docs/deploy/upgrade/) an existing deployment.

### Changes:

- 🔼 Upgrade Kubeflow components versions as listed in components versions table
- 🚀 Integrated with `Config Controller`, simplified management cluster maintenance cost, there is no need to manually upgrade `Config Connector` CRD.
- 🚚 Switch from `kfserving` to `KServe` as default serving component, you can switch back to `kfserving` in `config.yaml`.
- 🔨 Fixed `cloudsqlproxy` issue with `livenessProbe` configuration.
- 🧪 Validated deployment using `GKE 1.20.12`.
