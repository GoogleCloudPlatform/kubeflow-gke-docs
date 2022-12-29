# How to Contribute

We'd love to accept your patches and contributions to this project. There are
just a few small guidelines you need to follow.

## Contributor License Agreement

Contributions to this project must be accompanied by a Contributor License
Agreement. You (or your employer) retain the copyright to your contribution;
this simply gives us permission to use and redistribute your contributions as
part of the project. Head over to <https://cla.developers.google.com/> to see
your current agreements on file or to sign a new one.

You generally only need to submit a CLA once, so if you've already submitted one
(even if it was for a different project), you probably don't need to do it
again.

## Code reviews

All submissions, including submissions by project members, require review. We
use GitHub pull requests for this purpose. Consult
[GitHub Help](https://help.github.com/articles/about-pull-requests/) for more
information on using pull requests.

## Community Guidelines

This project follows
[Google's Open Source Community Guidelines](https://opensource.google.com/conduct/).

## Reporting Bugs/Feature Requests

Use the GitHub issue tracker to search existing bugs and feature request. If you want to report a new bug or suggest new features, create a new issue and include the following information:

* High-level description of the issue.
* Version of the code and platform that are used.
* Steps to reproduce (if applicable).
* Detailed description of a bug or a feature with all necessary materials.

## Prior contributions

This repository is based on [kubeflow/website](https://github.com/kubeflow/website) repository. To see prior contributions, see the corresponding [commit history](https://github.com/kubeflow/website/commits/master).

## Contributing via Pull Requests

Contributions are very welcome! Please, follow these simple steps:

1. Fork this repository on GitHub.

1. Make your changes and send a pull request (PR) with a few sentences describing your changes. Merge into:
   * `main` branch, if the changes are related to the latest released Kubeflow on Google Cloud.
   * `dev` branch if the changes are related to the unreleased ([master branch](https://github.com/GoogleCloudPlatform/kubeflow-distribution)) version of Kubeflow on Google Cloud.
   * `v*-release` if the changes are related to `v*` release of Kubeflow on Google Cloud.

1. Assign one of the [reviewers](https://github.com/GoogleCloudPlatform/kubeflow-gke-docs/blob/main/OWNERS) to the PR.


### Styling your content

The theme holds its styles in the [`assets/scss` directory](https://github.com/GoogleCloudPlatform/kubeflow-gke-docs/tree/main/themes/docsy/assets/scss).

**Do not change these files**, they are not actually inside this repo, but are part of the [google/docsy](https://github.com/google/docsy) repo. To update referenced docsy commit, run the following command at the root of the repo:

```bash
git submodule update --remote
```

The site's [front page](https://GoogleCloudPlatform.github.io/kubeflow-gke-docs):

* See the [page source](https://github.com/GoogleCloudPlatform/kubeflow-gke-docs/blob/main/content/en/_index.html).

* The CSS styles are in the [project variables file](https://github.com/GoogleCloudPlatform/kubeflow-gke-docs/blob/main/assets/scss/_variables_project.scss).

* The page uses the [cover block](https://www.docsy.dev/docs/adding-content/shortcodes/#blocks-cover) defined by the theme.

* The page also uses the [linkdown block](https://www.docsy.dev/docs/adding-content/shortcodes/#blocks-link-down).

### Using Hugo shortcodes

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
