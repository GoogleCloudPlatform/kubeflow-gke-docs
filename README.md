# Contributing to this repository

Welcome, Kubeflow users! This website contains the latest documentation for Kubeflow on GCP. It is hosted at https://gkcalat.github.io/kubeflow-docs. 
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

Contributions are very welcome! Please, follow these simple steps:

1. Review [CONTRIBUTING.md](https://github.com/googlestaging/kubeflow-gke-docs/blob/main/CONTRIBUTING.md).

1. Fork the [repo](https://github.com/gkcalat/kubeflow-docs) on GitHub.

1. Make your changes and send a pull request (PR) with a few sentences describing your changes. Merge into:
   * `main` branch, if the changes are related to the latest released Kubeflow on GCP.
   * `dev` branch if the changes are related to the unreleased ([master branch](https://github.com/GoogleCloudPlatform/kubeflow-distribution)) version of Kubeflow on GCP.
   * `v*-release` if the changes are related to `v*` release of Kubeflow on GCP.


1. Assign one of the [reviewers](https://github.com/kubeflow/website/edit/main/OWNERS.md) to the PR.

## Releasing

Kubeflow gets minor releases twice a year. [Kubeflow on GCP](https://github.com/GoogleCloudPlatform/kubeflow-distribution) follows the same cadence, but may also have patch releases in-between. Patch releases typically contain bug fixes, while minor releases include new features. Documentation (this repository) should stay in sync with the latest version of Kubeflow on GCP.

For each minor release, we create a new branch for the relevant documentation (e.g. `v1.6-release`). When a new version is released, we create a new branch of the previous version and the `main` branch is updated with the content for the new version.

The versioned sites follow this convention:

* `gkcalat.github.io/kubeflow-docs` is deployed from `gh-pages` branch, which is automatically updated once new changes are pushed to `main` or `v*-release` branches.
* Changes to `main` branch are pushed to the `./dev` directory of `gh-pages` branch, which is then reflected on `gkcalat.github.io/kubeflow-docs/dev`.
* Changes to `v*-release` branches are pushed to `./v*` subdirectories of `gh-pages` branch, which are then reflected on `gkcalat.github.io/kubeflow-docs/v*`.
* Changes to the latest `v*-release` branch are pushed to `./` subdirectory of `gh-pages` branch, which is then reflected on `gkcalat.github.io/kubeflow-docs/`. One need to keep this logic when releasing a minor version of Kubeflow on GCP.

Whenever any documents reference any source code, you should use the version shortcode in the links, like so:

```
https://github.com/GoogleCloudPlatform/kubeflow-distribution/blob/{{< params "githubbranch" >}}/...
```

This ensures that all the links in a versioned webpage point to the correct branch.

### Releasing a new patch of the latest minor version:

1. Create a PR with the changes to the documentation and merge them to `main` branch.
2. Cherry-pick your changes to the latest `v*-release` branch.
3. Make sure that everything deploys successfully. If needed trigger the corresponding GitHub actions and investigate the logs.
4. Test the deployment.

### Releasing a new minor version:

1. Create a PR with the changes to the documentation and merge them to `main` branch.
2. Create a new branch from `main` following the convention `vX.Y-release`, where `X` is a major version, and `Y` is a minor version.
3. Add the new branch to [this GitHub action](.github/workflows/hugo-build-deploy-on-push.yml#L6) and replace the latest version tag in [this line](.github/workflows/hugo-build-deploy-on-push.yml#L56). The later makes sure that the latest version deploys to the root folder of `gh-pages` branch.
4. Update the `./config.toml` in every branch you want to release to make sure every branch includes all versions in the drop-down menu `[[params.versions]]` and set `archived_version = true` for the previous version (now, you should have the latest version pointing to the new `vX.Y-release` branch).
5. Optionally, deprecate the older version by adjusting `[[params.versions]]` and removing the corresponding subdirectories in `gh-pages` branch.
6. Ensure that all the branches have been built and published to `gh-pages` branch. If not, trigger the corresponding GitHub actions manually.
7. Test the deployment.

## Styling your content

The theme holds its styles in the [`assets/scss` directory](https://github.com/gkcalat/kubeflow-docs/tree/main/themes/docsy/assets/scss).

**Do not change these files**, they are not actually inside this repo, but are part of the [google/docsy](https://github.com/google/docsy) repo. To update referenced docsy commit, run the following command at the root of the repo:

```bash
git submodule update --remote
```

The site's [front page](https://gkcalat.github.io/kubeflow-docs):

* See the [page source](https://github.com/gkcalat/kubeflow-docs/blob/main/content/en/_index.html).

* The CSS styles are in the [project variables file](https://github.com/gkcalat/kubeflow-docs/blob/main/assets/scss/_variables_project.scss).

* The page uses the [cover block](https://www.docsy.dev/docs/adding-content/shortcodes/#blocks-cover) defined by the theme.

* The page also uses the [linkdown block](https://www.docsy.dev/docs/adding-content/shortcodes/#blocks-link-down).

## Using Hugo shortcodes

Sometimes it's useful to define a snippet of information in one place and reuse it wherever we need it. 
For example, we want to be able to refer to the minimum version of various frameworks/libraries throughout the docs, 
without causing a maintenance nightmare.

For this purpose, we use Hugo's "shortcodes". 
Shortcodes are similar to Django variables. You define a shortcode in a file, then use a specific markup 
to invoke the shortcode in the docs. That markup is replaced by the content of the shortcode file when the page is built.

To create a shortcode:

1. Add an HTML file in the `layouts/shortcodes/` directory. 
   The file name must be short and meaningful, as it determines the shortcode you and others use in the docs.

1. For the file content, add the text and HTML markup that should replace the shortcode markup when the web page is built.

To use a shortcode in a document, wrap the name of the shortcode in braces and percent signs like this:

  ```
  {{% shortcode-name %}}
  ```

The shortcode name is the file name minus the `.html` file extension.

**Example:** The following shortcode defines the minimum required version of Kubernetes:

* File name of the shortcode:

  ```
  kubernetes-min-version.html
  ```

* Content of the shortcode:

  ```
  1.8
  ```

* Usage in a document:

  ```
  You need Kubernetes version {{% kubernetes-min-version %}} or later.
  ```
