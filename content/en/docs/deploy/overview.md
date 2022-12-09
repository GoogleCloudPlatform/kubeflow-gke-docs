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

1. Full-fledged multi-user Kubeflow running on GKE.
1. [Cluster Autoscaler](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler)
    with automatic resizing of the node pool.
1. [Cloud Endpoint](https://cloud.google.com/endpoints/docs) integrated with [Identity-aware Proxy (IAP)](https://cloud.google.com/iap).
1. GPU and [Cloud TPU](https://cloud.google.com/tpu/) accelerated nodes available for your Machine Learning (ML) workloads.
1. [Cloud Logging](https://cloud.google.com/logging/docs/) for easy debugging and troubleshooting.
1. Other managed services offered by Google Cloud, such as [Cloud Storage](https://cloud.google.com/storage), [Cloud SQL](https://cloud.google.com/sql), [Anthos Service Mesh](https://cloud.google.com/anthos/service-mesh), [Identity and Access Management (IAM)](https://cloud.google.com/iam), [Config Controller](https://cloud.google.com/anthos-config-management/docs/concepts/config-controller-overview), and so on.

<img src=".{{ .Site.Params.version_url_prefix }}/docs/images/gke/full-kf-home.png" 
    alt="Full Kubeflow Central Dashboard"
    class="mt-3 mb-3 border border-info rounded">


## Management cluster

Kubeflow on GCP employs management cluster, which allows you to manage Google Cloud resources via [Config Connector](https://cloud.google.com/config-connector/docs/overview). The management cluster is independent from Kubeflow cluster. Its purpose is to manage Kubeflow clusters (see figure below). The management cluster can live in a different Google Cloud project by assigning owner permission to the associated service account.

<img src="../images/logos/gcp.png"
    alt="Full Kubeflow deployment structure"
    class="mt-3 mb-3 border border-info rounded">

## Deployment process

Follow the steps below to set up Kubeflow environment on Google Cloud. Some of these steps are one-time only, for example: OAuth Client can be shared by multiple Kubeflow clusters in the same Google Cloud project.

1. [Set up Google Cloud project](/{{ .Site.Params.version_url_prefix }}docs/deploy/project-setup/).
2. [Set up OAuth Client](/{{ .Site.Params.version_url_prefix }}docs/deploy/oauth-setup/).
3. [Deploy Management Cluster](/{{ .Site.Params.version_url_prefix }}docs/deploy/management-setup/).
4. [Deploy Kubeflow Cluster](/{{ .Site.Params.version_url_prefix }}docs/deploy/deploy-cli/).

If you encounter any issues during the deployment steps, refer to [Troubleshooting deployments](/{{ .Site.Params.version_url_prefix }}docs/troubleshooting/) to find common issues
and debugging approaches. If this issue is new, file a bug to [GoogleCloudPlatform/kubeflow-distribution](https://github.com/GoogleCloudPlatform/kubeflow-distribution).

## Next steps

- Repeat [Deploy Kubeflow Cluster](/{{ .Site.Params.version_url_prefix }}docs/deploy/deploy-cli/) if you want to deploy another Kubeflow cluster.
- Run a full ML workflow on Kubeflow, using the [end-to-end MNIST notebook](https://github.com/kubeflow/pipelines/blob/e42d9d2609369b96973c821dca11fe5b2565e705/samples/contrib/kubeflow-e2e-mnist/kubeflow-e2e-mnist.ipynb).
