+++
title = "Kubeflow on Google Cloud v1.6.1"
description = "A new patch release of Kubeflow 1.6"
weight = 2
+++

A new version of Kubeflow on Google Cloud has been released! See the updated instructions on how to [deploy](https://googlecloudplatform.github.io/kubeflow-gke-docs/docs/deploy/) to a new cluster and [upgrade](https://googlecloudplatform.github.io/kubeflow-gke-docs/docs/deploy/upgrade/) an existing deployment.

### Changes:

- ๐ผ Upgraded upstream `Manifests` to `v1.6.1`.
- ๐ผ Upgraded `pipelines` to `v2.0.0-alpha.6` (fixes [#392](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/392)).
- ๐ผ Updated `MySQL` to `8.0` ([#391](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/391)).
- ๐จ Fixed `ASM` deployment issue ([#389](https://github.com/GoogleCloudPlatform/kubeflow-distribution/issues/389))
- ๐จ Minor improvements of deployment process.
- ๐งช Validated deployment using `GKE 1.22`.
