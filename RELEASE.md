# Releasing a new version

## Prerequisites

1. This website is being generated with [Hugo](https://gohugo.io/), a popular open-source static site generator. You will need to install the `extended` version of Hugo.

    You can install Hugo using `brew`:
    ```bash
    brew install hugo
    ```

    Alternatively, you can also use `snap`:
    ```bash
    snap install hugo --channel=extended
    ```

    Check the [official documentation](https://gohugo.io/getting-started/installing/) on other installation options.

1. We use [Docsy](https://github.com/google/docsy) template, which has its prerequisites.

    ```bash
    npm install --save-dev autoprefixer
    npm install --save-dev postcss-cli
    npm install -D postcss
    ```
    If you don't have `npm`, install it using:
    ```bash
    sudo apt-get install npm
    ```

1. Before publishing a new release, it is recommended to run the website locally:
```bash
hugo server
```
## Schedule

Kubeflow has roughly minor releases twice a year. [GCP distribution of Kubeflow](https://github.com/GoogleCloudPlatform/kubeflow-distribution) follows the same cadence, but may also have patch releases in between. Patch releases typically contain bug fixes, while minor releases include new features
additionally.

## General instructions



### Build

See more details on how to deploy [GitHub pages static website using Hugo](https://gohugo.io/hosting-and-deployment/hosting-on-github/).

