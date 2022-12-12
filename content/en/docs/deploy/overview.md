+++
title = "Overview"
description = "Full fledged Kubeflow deployment on Google Cloud"
weight = 1
+++

This guide describes how to deploy Kubeflow and a series of Kubeflow components on Google Kubernetes Engine (GKE).
<!-- If you want to use Kubeflow Pipelines only, refer to [Installation Options for Kubeflow Pipelines](https://www.kubeflow.org/docs/components/pipelines/installation/overview/) for choosing an installation option.
-->

## Features

Kubeflow deployed on Google Cloud includes the following:

1. Full-fledged multi-user Kubeflow running on Google Kubernetes Engine.
1. [Cluster Autoscaler](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler)
    with automatic resizing of the node pool.
1. [Cloud Endpoint](https://cloud.google.com/endpoints/docs) integrated with [Identity-aware Proxy (IAP)](https://cloud.google.com/iap).
1. GPU and [Cloud TPU](https://cloud.google.com/tpu/) accelerated nodes available for your Machine Learning (ML) workloads.
1. [Cloud Logging](https://cloud.google.com/logging/docs/) for easy debugging and troubleshooting.
1. Other managed services offered by Google Cloud, such as [Cloud Storage](https://cloud.google.com/storage), [Cloud SQL](https://cloud.google.com/sql), [Anthos Service Mesh](https://cloud.google.com/anthos/service-mesh), [Identity and Access Management (IAM)](https://cloud.google.com/iam), [Config Controller](https://cloud.google.com/anthos-config-management/docs/concepts/config-controller-overview), and so on.

![Kubeflow on Google Cloud: central dashboard](../../images/gke/full-kf-home.png)
**Figure 1.** User interface of full-fledged Kubeflow deployment on Google Cloud.

## Management cluster

Kubeflow on Google Cloud employs a management cluster, which lets you manage Google Cloud resources via [Config Controller](https://cloud.google.com/anthos-config-management/docs/concepts/config-controller-overview). The management cluster is independent from the Kubeflow cluster and manages Kubeflow clusters. You can also use a management cluster from a different Google Cloud project, by assigning owner permissions to the associated service account.

![Kubeflow on Google Cloud: clusters hierarchy](../../images/gke/full-deployment-structure.png)
**Figure 2.** Example of Kubeflow on Google Cloud deployment.

## Deployment process

To set up a Kubeflow environment on Google Cloud, complete these steps:

1. [Set up Google Cloud project](../project-setup/).
2. [Set up OAuth client](../oauth-setup/).
3. [Deploy Management cluster](../management-setup/).
4. [Deploy Kubeflow cluster](../deploy-cli/).

For debugging approaches to common issues encountered during these deployment steps, see [troubleshooting deployments](../../troubleshooting/) to find common issues
and debugging approaches. If the issue isn’t included in the list of commonly encountered issues, report a bug at [GoogleCloudPlatform/kubeflow-distribution](https://github.com/GoogleCloudPlatform/kubeflow-distribution).

## Next steps

- [Deploy Kubeflow Cluster](../deploy-cli/).
- Run a full ML workflow on Kubeflow by using the [end-to-end MNIST notebook](https://github.com/kubeflow/pipelines/blob/e42d9d2609369b96973c821dca11fe5b2565e705/samples/contrib/kubeflow-e2e-mnist/kubeflow-e2e-mnist.ipynb).
