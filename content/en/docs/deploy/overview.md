+++
title = "Overview"
description = "Full fledged Kubeflow deployment on Google Cloud"
weight = 1
+++

This guide describes how to deploy Kubeflow and a series of Kubeflow components on GKE (Google Kubernetes Engine).
If you want to use Kubeflow Pipelines only, refer to [Installation Options for Kubeflow Pipelines](https://www.kubeflow.org/docs/components/pipelines/installation/overview/)
for choosing an installation option.

## Features

Once deployed, Kubeflow of GCP includes:

    1. Full-fledge multi-user Kubeflow running on GKE.
    1. [Cluster Autoscaler](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler)
        with automatic resizing of the node pool.
    1. [Cloud Endpoint](https://cloud.google.com/endpoints/docs) integrated with [IAP (Identity-aware Proxy)](https://cloud.google.com/iap).
    1. GPU and [Cloud TPU](https://cloud.google.com/tpu/) accelerated nodes available for your ML workloads.
    1. [Cloud Logging](https://cloud.google.com/logging/docs/) for easy debugging and troubleshooting.
    1. Many more managed services offered by Google Cloud.

<img src="/docs/images/gke/full-kf-home.png" 
    alt="Full Kubeflow Central Dashboard"
    class="mt-3 mb-3 border border-info rounded">


## Management cluster

Kubeflow on GCP employs management cluster, which allows you to manage Google Cloud resources via [Config Connector](https://cloud.google.com/config-connector/docs/overview). The management cluster is independent from Kubeflow cluster. Its purpose is to manage Kubeflow clusters (see figure below). The management cluster can live in a different Google Cloud project by assigning owner permission to the associated service account.

<img src="/docs/images/gke/full-deployment-structure.png" 
    alt="Full Kubeflow deployment structure"
    class="mt-3 mb-3 border border-info rounded">

## Deployment process

Follow the steps below to set up Kubeflow environment on Google Cloud. Some of these steps are one-time only, for example: OAuth Client can be shared by multiple Kubeflow clusters in the same Google Cloud project.

1.  [Set up Google Cloud project](/docs/deploy/project-setup/).
2.  [Set up OAuth Client](/docs/deploy/oauth-setup/).
3.  [Deploy Management Cluster](/docs/deploy/management-setup/).
4.  [Deploy Kubeflow Cluster](/docs/deploy/deploy-cli/).

If you encounter any issue during the deployment steps, refer to [Troubleshooting deployments](/docs/troubleshooting/) to find common issues
and debugging approaches. If this issue is new, file a bug to [GoogleCloudPlatform/kubeflow-distribution](https://github.com/GoogleCloudPlatform/kubeflow-distribution) for GKE related issue, 
or file a bug to the corresponding component in [Kubeflow on GitHub](https://github.com/kubeflow/) if the issue is component specific.

## Next steps

- Repeat [Deploy Kubeflow Cluster](/docs/deploy/deploy-cli/) if you want to deploy another Kubeflow cluster.
- Run a full ML workflow on Kubeflow, using the [end-to-end MNIST notebook](https://github.com/kubeflow/pipelines/blob/e42d9d2609369b96973c821dca11fe5b2565e705/samples/contrib/kubeflow-e2e-mnist/kubeflow-e2e-mnist.ipynb).
