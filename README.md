![Build dev](https://github.com/GoogleCloudPlatform/kubeflow-gke-docs/actions/workflows/hugo-build-deploy-on-push.yml/badge.svg?branch=main)

# Contributing to this repository

Welcome, Kubeflow users! This website contains the latest documentation for Kubeflow on Google Cloud. It is hosted at https://googlecloudplatform.github.io/kubeflow-gke-docs. 
Before contributing, please read [these guidelines](./CONTRIBUTING.md).

## Running locally

1. This website is being generated with [Hugo](https://gohugo.io/), a popular open-source static site generator. You will need to install the `extended` version of Hugo to be able to generate a website locally.

    You can install Hugo using `brew`:
    ```bash
    brew install hugo
    ```

    Alternatively, you can also use `snap`:
    ```bash
    snap install hugo --channel=extended
    ```

    Check the [official documentation](https://gohugo.io/getting-started/installing/) on other installation options. See more details on how to deploy [GitHub pages static website using Hugo](https://gohugo.io/hosting-and-deployment/hosting-on-github/).

1. We use [Docsy](https://github.com/google/docsy) theme, which has its prerequisites.

    ```bash
    npm install --save-dev autoprefixer
    npm install --save-dev postcss-cli
    npm install -D postcss
    ```
    If you don't have `npm`, install it using:
    ```bash
    sudo apt-get install npm
    ```

1. To run the website locally:

    ```bash
    hugo server
    ```

## Contributing

See [CONTRIBUTING.md](https://github.com/googlecloudplatform/kubeflow-gke-docs/blob/main/CONTRIBUTING.md).

## Releasing a new version

See [RELEASE.md](https://github.com/googlecloudplatform/kubeflow-gke-docs/blob/main/RELEASE.md).
