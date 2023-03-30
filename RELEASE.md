# Releasing

Kubeflow gets minor releases twice a year. [Kubeflow on Google Cloud](https://github.com/googlecloudplatform/kubeflow-distribution) follows the same cadence, but may also have patch releases in-between. Patch releases typically contain bug fixes, while minor releases include new features. Documentation (this repository) should stay in sync with the latest version of Kubeflow on Google Cloud.

For each minor release, we create a new branch for the relevant documentation (e.g. `v1.6-release`). When a new version is released, we create a new branch of the previous version and the `main` branch is updated with the content for the new version.

The versioned sites follow this convention:

* `googlecloudplatform.github.io/kubeflow-gke-docs` is deployed from `gh-pages` branch, which is automatically updated once new changes are pushed to `main` or `v*-release` branches.
* Changes to `main` branch are pushed to the `./dev` directory of `gh-pages` branch, which is then reflected on `googlecloudplatform.github.io/kubeflow-gke-docs/dev`.
* Changes to `v*-release` branches are pushed to `./v*` subdirectories of `gh-pages` branch, which are then reflected on `googlecloudplatform.github.io/kubeflow-gke-docs/v*`.
* Changes to the latest `v*-release` branch are pushed to `./` subdirectory of `gh-pages` branch, which is then reflected on `googlecloudplatform.github.io/kubeflow-gke-docs/`. One need to keep this logic when releasing a minor version of Kubeflow on Google Cloud.

Whenever any documents reference any source code, you should use the version shortcode in the links, like so:

```
https://github.com/googlecloudplatform/kubeflow-distribution/blob/{{< params "githubbranch" >}}/...
```

This ensures that all the links in a versioned webpage point to the correct branch.

## Releasing a new patch of the latest minor version:

1. Create a PR with the changes to the documentation and merge them to `main` branch.
2. Cherry-pick your changes to the latest `v*-release` branch.
3. Make sure that everything deploys successfully. If needed trigger the corresponding GitHub actions and investigate the logs.
4. Test the deployment.

## Releasing a new minor version:

1. Create a PR with the changes to the documentation and merge them to `main` branch.
2. TODO(gkcalat): fix this. As we deploy the `dev` version from the `main` branch, it contains hard-coded references to the manifests from the `master` branch. Therefore, we need to add references to the `latest-version` short-code in `content/en/docs/deploy/deploy-cli.md` and `content/en/docs/deploy/management-setup.md`. See what you need to revert from PR #7.
3. Create a new branch from `main` following the convention `vX.Y-release`, where `X` is a major version, and `Y` is a minor version.
4. Add the new branch to [this GitHub action](.github/workflows/hugo-build-deploy-on-push.yml#L6) and replace the latest version tag in [this line](.github/workflows/hugo-build-deploy-on-push.yml#L56). The later makes sure that the latest version deploys to the root folder of `gh-pages` branch.
5. Update the `./config.toml` in every branch you want to release to make sure every branch includes all versions in the drop-down menu `[[params.versions]]` and set `archived_version = true` for the previous version (now, you should have the latest version pointing to the new `vX.Y-release` branch).
6. Optionally, deprecate the older version by adjusting `[[params.versions]]` and removing the corresponding subdirectories in `gh-pages` branch.
7. Ensure that all the branches have been built and published to `gh-pages` branch. If not, trigger the corresponding GitHub actions manually.
8. Test the deployment.
