# CHANGELOG


## v1.0.9 (2024-11-11)

### Bug Fixes

* fix: simplify build configuration and update citation format (#42) ([`0839e21`](https://github.com/Bjarten/early-stopping-pytorch/commit/0839e2139ab4fe23160619b59cbf87db369c8044))


## v1.0.8 (2024-11-11)

### Bug Fixes

* fix: trigger version bump (#41) ([`2c72682`](https://github.com/Bjarten/early-stopping-pytorch/commit/2c726827b507410e08ea1c08c3342915d92f7899))

### Chores

* chore: update project metadata and README for citation and versioning (#40) ([`6834653`](https://github.com/Bjarten/early-stopping-pytorch/commit/68346536b22171c6820b95886a8b6d527a426805))


## v1.0.7 (2024-11-11)

### Bug Fixes

* fix: correct versioning for __version__ in __init__.py (#39) ([`bdb4545`](https://github.com/Bjarten/early-stopping-pytorch/commit/bdb4545c13e46c601d185510d52d0c724fc77b24))

### Unknown

* Revert "1.0.6"

This reverts commit 9244ca36814ae4a331b6477cb08edc0a91fc2609. ([`c96c7df`](https://github.com/Bjarten/early-stopping-pytorch/commit/c96c7df3fa834103ebd71726533d657700fb14f0))


## v1.0.6 (2024-11-11)

### Bug Fixes

* fix: manual version bump ([`0ea0305`](https://github.com/Bjarten/early-stopping-pytorch/commit/0ea0305703a6b949438d78fa47b27cf63eb27009))


## v1.0.5 (2024-11-11)

### Bug Fixes

* fix: Update semantic-release configuration for consistency and correct versioning (#38) ([`0faabd0`](https://github.com/Bjarten/early-stopping-pytorch/commit/0faabd091ba9661c2fd8419e8332d9cb8dcdef60))


## v1.0.4 (2024-11-11)

### Bug Fixes

* fix: correct version regex in semantic release config for version updates (#37) ([`a3a82b2`](https://github.com/Bjarten/early-stopping-pytorch/commit/a3a82b2f11a82caa13c50c5e07086cd2e74699b1))


## v1.0.3 (2024-11-11)

### Bug Fixes

* fix: semantic release version updating pattern (#36) ([`ccda0f5`](https://github.com/Bjarten/early-stopping-pytorch/commit/ccda0f52ce6fa2298be7d46f49e0315933ff4800))


## v1.0.2 (2024-11-11)

### Bug Fixes

* fix: manual release and publish workflows with version updates (#35)

## Description
This PR updates both the release and publish workflows to:
1. Ensure proper version updating across all package files
2. Use manual triggers for better control and reliability

## Changes

### Release Workflow Updates
- Added `version: true` parameter to semantic-release action
- This ensures updates to both `__init__.py` and `pyproject.toml`
versions
- Kept explicit tag and push parameters for clarity
- Maintained all necessary permissions

### Publish Workflow Updates
- Changed from tag-based trigger to manual `workflow_dispatch`
- Simplified workflow control and verification process
- Maintained all PyPI trusted publisher configurations

## Process After Changes
1. Manual trigger of "Create New Release" workflow:
   - Updates versions in package files
   - Creates new tag and GitHub release
2. Manual trigger of "Publish Python Package" workflow:
   - Builds package with updated versions
   - Publishes to PyPI ([`45de9bb`](https://github.com/Bjarten/early-stopping-pytorch/commit/45de9bb72e15295ff47c1896c01fd53218990d77))


## v1.0.1 (2024-11-10)

### Bug Fixes

* fix: improve release process and documentation (#34)

## Description
This PR improves the release process and documentation by:
1. Makes tag pushing explicit in the release workflow
2. Fixes version management in semantic release
3. Updates README with PyPI installation instructions

## Changes
- Added explicit tag pushing parameters to semantic-release workflow
- Updated version management in pyproject.toml:
  - Added version_toml configuration
  - Changed from dynamic to static versioning
  - Set version to match current release (1.0.1)
- Updated README.md:
  - Added PyPI installation instructions
  - Fixed image URL for PyPI compatibility
  - Reorganized installation and usage sections ([`f42d5d1`](https://github.com/Bjarten/early-stopping-pytorch/commit/f42d5d1dfa092dac5d33835e7b6d3092783baf53))

* fix: use PyPI trusted publisher authentication (#33)

Updates the GitHub Actions publish workflow to use PyPI's Trusted
Publisher authentication instead of token-based authentication. This
change improves security by:
- Removing the need to store PyPI tokens in GitHub secrets
- Using OpenID Connect (OIDC) for secure authentication
- Leveraging PyPI's recommended authentication method for GitHub Actions

## Changes
- Removed token-based authentication (TWINE_USERNAME and TWINE_PASSWORD)
- Added required `id-token: write` permission for OIDC
- Switched from manual twine upload to `pypa/gh-action-pypi-publish`
action ([`3a0d9b8`](https://github.com/Bjarten/early-stopping-pytorch/commit/3a0d9b8ed0ac95f8ee4010368319be2f8c38da61))


## v1.0.0 (2024-10-18)

### Breaking

* chore!: rename package, restructure files, and add pip integration (#29)

This update introduces significant changes to the project, including
renaming the package, restructuring the directory, and setting up
automated publishing to PyPI using API tokens.

### **Key Changes:**

1. **Package Renaming:**
- The package has been renamed from `pytorchtools` to
`early_stopping_pytorch` for clearer naming and better alignment with
its functionality.

2. **Directory Restructuring:**
- Project files have been reorganized for clarity, with the source code
placed under the `early_stopping_pytorch/` directory in the root of the
project.

3. **PyPI Integration:**
- Added support for automated publishing to PyPI using GitHub Actions.
- **API tokens** are used for secure publishing, stored as GitHub
Secrets (`PYPI_TOKEN`).

### **Impact:**

- **Breaking Changes**: Users will need to update their import paths
from:
  ```python
  from pytorchtools import EarlyStopping
  ```
  to:
  ```python
  from early_stopping_pytorch import EarlyStopping
  ```

- New versions will be automatically published to PyPI when a new tag is
pushed, using the API token for authentication. ([`f9522dd`](https://github.com/Bjarten/early-stopping-pytorch/commit/f9522dd2da7d14e3dce18eebcbb867260ffdcde4))

### Bug Fixes

* fix: release workflow 2 (#32)

This PR modifies our Semantic Release workflow to ensure it's only
triggered manually:

1. Removed automatic trigger on push to main branch
2. Retained only the `workflow_dispatch` trigger
3. Simplified job structure while maintaining all necessary steps and
permissions

These changes provide more control over when releases are created,
allowing us to:
- Prevent unintended automatic releases
- Manually initiate the release process when desired
- Maintain full functionality of the Semantic Release process ([`ddc6493`](https://github.com/Bjarten/early-stopping-pytorch/commit/ddc6493075be8b2184956eb73ba621666df715b4))

* fix: release workflow (#31)

This PR updates our Semantic Release workflow to align with best
practices and official documentation. Key changes include:

1. Simplified the workflow to use the official Python Semantic Release
GitHub Action.
2. Adjusted permissions to ensure proper access for creating releases
and tags.
3. Updated pyproject.toml to prevent double publishing to PyPI.

These changes aim to:
- Streamline our release process
- Improve reliability and consistency of our versioning ([`b291782`](https://github.com/Bjarten/early-stopping-pytorch/commit/b291782635bbb605fcd784778fa7bb8b16b02488))

* fix: add check for NaN validation loss in EarlyStopping (#28)

This PR addresses an issue where `EarlyStopping` incorrectly treats
`nan` validation losses as an improvement, often caused by exploding
gradients.

Key changes:
- Added `np.isnan(val_loss)` check to ensure that `nan` validation
losses are ignored.
- Updated the logic to ensure that the patience counter and model
checkpointing are unaffected by `nan` values.
- Introduced a new unit test, `test_validation_loss_nan`, to verify that
`EarlyStopping` behaves correctly when `nan` values are encountered
during training.

Closes #16 ([`676686b`](https://github.com/Bjarten/early-stopping-pytorch/commit/676686b2b489d99fa5fd8b87ec9594a4e751e323))

### Chores

* chore: consolidate version definitions and update release workflow (#30)

This pull request consolidates version definitions and improves the
release workflow to streamline the versioning and publishing processes.
The changes are part of an effort to improve maintainability and ensure
the workflows are efficient and modular.

**Changes Made:**
- **Consolidated Version Management**: 
- Removed duplicate version definitions to maintain a single source of
truth. The version is now only defined in
`early_stopping_pytorch/__init__.py` to avoid conflicts.
- Removed the `version` field from `pyproject.toml`, as
`python-semantic-release` handles versioning automatically.
  
- **Updated Release Workflow**:
- Improved the `Create New Release` workflow by separating the release
process from the publishing process.
- The release process now handles version bumping, tagging, and creating
GitHub releases via `python-semantic-release`.
  
- **New Publish Workflow**:
- A dedicated workflow now handles publishing the package to PyPI when a
new version tag is pushed.
- This ensures a clear separation of responsibilities between creating
releases and publishing to PyPI, reducing complexity. ([`e79817a`](https://github.com/Bjarten/early-stopping-pytorch/commit/e79817ad40a6c5c688e91e5c60de0aaf307ea0b2))

### Features

* feat(ci): add GitHub Action for Python tests, fix EarlyStopping logic, and add unit tests (#27)

This PR introduces several key changes:
1. A GitHub Actions workflow for continuous integration, running tests
across multiple Python versions.
2. Fixes to the `EarlyStopping` class logic, changing `best_score` to
`best_val_loss` to improve clarity and correctness.
3. A new test suite for the `EarlyStopping` class to ensure its correct
behavior after the logic fix.

### Changes:
- **Added Python application tests**:
- A new workflow named "Python Application Tests" runs on GitHub
Actions.
- Tests are executed across multiple Python versions (`3.9`, `3.10`,
`3.11`, `3.12`).
- The workflow is triggered on pushes and pull requests to the `main`
branch.
  - Pip dependencies are cached to optimize performance.

- **Fixed EarlyStopping logic**:
- The variable `best_score` was renamed to `best_val_loss` for clarity,
improving the code's readability and matching the purpose of the
variable.
- Logic for early stopping was updated to properly handle edge cases for
delta and stopping conditions based on validation loss behavior.

- **Added Unit Tests for `EarlyStopping`**:
- The file `test_early_stopping.py` contains a thorough set of tests
covering:
    - Initialization and attribute checks.
    - Behavior when validation loss improves.
    - Handling when validation loss does not improve.
    - Proper functionality of patience and delta parameters.
    - Edge cases for early stopping triggers and verbose output.

### Why this change is important:
- Automates testing across different Python versions to ensure
compatibility and reliability.
- Fixes logic issues in the `EarlyStopping` class, making it more robust
and clear.
- Ensures the `EarlyStopping` class functions as expected through the
added unit tests.
- Improves development velocity by automatically running tests on every
push and pull request. ([`ffe12ee`](https://github.com/Bjarten/early-stopping-pytorch/commit/ffe12ee1edc3700ea3f06a2dcd36793667db2b7e))


## v0.1.0 (2024-10-14)

### Bug Fixes

* fix: wrong sign on delta argument

elif score < self.best_score - self.delta: -> elif score < self.best_score + self.delta: ([`7d8a086`](https://github.com/Bjarten/early-stopping-pytorch/commit/7d8a086c4e43e4db05fd850361224fab275fdc6b))

* fix: remove pytorch 

Seems like only torchvision is required ([`8644d65`](https://github.com/Bjarten/early-stopping-pytorch/commit/8644d657b31857335502e94d0d756f1704f476e7))

* fix: remove version numbers

Could not find a version error on https://mybinder.org/
Try to fix the error by removing version numbers ([`8029865`](https://github.com/Bjarten/early-stopping-pytorch/commit/802986590a40b4cba7e4228cffef8eb914acbea2))

* fix: format file for use with mybinder.org ([`a144aff`](https://github.com/Bjarten/early-stopping-pytorch/commit/a144aff271a743864aa43304b9a847e94a4e7f3d))

### Chores

* chore: add requirement.txt ([`2cdd950`](https://github.com/Bjarten/early-stopping-pytorch/commit/2cdd95012d075ebc02464d65fba87b061309cbd9))

* chore: add loss_plot.png ([`f675463`](https://github.com/Bjarten/early-stopping-pytorch/commit/f6754634e1a07f792a7be6da745deb86c51ab284))

* chore: add checkpoint.pt ([`07a0221`](https://github.com/Bjarten/early-stopping-pytorch/commit/07a02218d9f55497b3badc2ca2a73b40be2cd01d))

* chore: add data/* to gitignore ([`5aee053`](https://github.com/Bjarten/early-stopping-pytorch/commit/5aee053181b2bc8e7f5efe6c9fe8f30d3e205353))

### Continuous Integration

* ci: add semantic versioning workflow (#26)

This PR introduces a manual semantic versioning process using
python-semantic-release. It sets up a GitHub Actions workflow that can
be manually triggered to determine the next version number, update the
version in our code, create a new release, and generate release notes
based on our commit history.

## Changes
- Add `pyproject.toml` with semantic-release configuration
- Update `pytorchtools.py` to include a `__version__` variable,
initially set to "0.1.0"
- Add a new GitHub Actions workflow file:
`.github/workflows/release.yml` for manual release triggering

## Why
- Provides a controlled, manual process for versioning and releasing
- Ensures consistent version numbering based on commit messages when
releases are created
- Generates comprehensive release notes automatically
- Improves tracking of changes and features across versions
- Allows for dry-run releases to verify the process without making
changes

## Configuration Details
- Starting version: 0.1.0
- Semantic Versioning: Using `major_on_zero = false` to treat 0.x
versions similarly to 1.x versions
- Release Process: Manual trigger through GitHub Actions, with option
for dry-run

## Additional Notes
- This change does not affect the existing functionality of the
EarlyStopping class

## Usage Instructions
To create a new release:
1. Ensure all desired changes are merged to the main branch
2. Go to the "Actions" tab in the GitHub repository
3. Select the "Create New Release" workflow
4. Click "Run workflow"
5. Choose whether to perform a dry run or create an actual release
6. Review the results in the Actions tab and in the Releases section of
the repository

## Future Considerations
- Evaluate the need for automatic releases based on project growth and
development pace
- Consider implementing additional checks or approvals before releases
are created ([`686db54`](https://github.com/Bjarten/early-stopping-pytorch/commit/686db54c9da625f7a8fdc78755afc8a046b621e8))

* ci: add PR title linting workflow (#25)

This PR introduces a GitHub Actions workflow to lint Pull Request
titles. The workflow ensures that all PR titles follow the Conventional
Commits specification, which will improve our changelog generation and
semantic versioning process.

## Changes
- Add a new GitHub Actions workflow file:
`.github/workflows/pr-title-lint.yml`
- Configure the workflow to run on PR creation, edit, and
synchronization
- Use the `amannn/action-semantic-pull-request` action to validate PR
titles

## Why
- Enforces consistent and meaningful PR titles
- Facilitates automated versioning and changelog generation
- Improves clarity and communication in our development process

## Additional Notes
- This change does not affect the existing codebase or functionality ([`0003e63`](https://github.com/Bjarten/early-stopping-pytorch/commit/0003e63420134c4bbb6a05d52283f17c6f7c6742))

### Documentation

* docs: create CODE_OF_CONDUCT.md ([`0e22ef3`](https://github.com/Bjarten/early-stopping-pytorch/commit/0e22ef3175f7e8db3c9161a892779f7766087ea8))

* docs: add usage section

Add a link to mybinder.org to run the project in the browser. ([`abcd4ed`](https://github.com/Bjarten/early-stopping-pytorch/commit/abcd4ed78f90c966310163c79496966b0703ae29))

* docs: fix minor errors in the text ([`f15c2a8`](https://github.com/Bjarten/early-stopping-pytorch/commit/f15c2a85f5a0bd8c6dd80b09d8d1cfb01a4716b6))

* docs: fix punctuation ([`745fdba`](https://github.com/Bjarten/early-stopping-pytorch/commit/745fdba1b726ab303ea2d19df0a5f8e00b0a53c9))

* docs: add the loss_plot and write a better explenation ([`68529d6`](https://github.com/Bjarten/early-stopping-pytorch/commit/68529d64047605cffd6bfcd015b4367bad9a1e94))

* docs: write introduction ([`bae0775`](https://github.com/Bjarten/early-stopping-pytorch/commit/bae07755e397740fde9acba95974071237921549))

### Features

* feat: create MNIST_Early_Stopping_example notebook

Notebook with an example of how to use the EarlyStopping class ([`5102fa5`](https://github.com/Bjarten/early-stopping-pytorch/commit/5102fa5a5b61d972d465546906f09cf34ed10cf6))

* feat: add verbose argument to EarlyStopping class ([`d64801f`](https://github.com/Bjarten/early-stopping-pytorch/commit/d64801f678b1615163ebdb1bc07c447e6a6235da))

* feat: change checkpoint save path

'saved_models/checkpoint.pt' --> 'checkpoint.pt' ([`11da3df`](https://github.com/Bjarten/early-stopping-pytorch/commit/11da3dfeb4c97d3e85ba801e28245e873525ded7))

* feat: import torch and numpy ([`b345d0b`](https://github.com/Bjarten/early-stopping-pytorch/commit/b345d0b781db52da40b6f65b141deb2ad4772c17))

* feat: add EarlyStopping class ([`9c7d9e6`](https://github.com/Bjarten/early-stopping-pytorch/commit/9c7d9e6139975d827aee1b0e4f99b758d4076e27))

* feat: create pytorchtools.py ([`7396b39`](https://github.com/Bjarten/early-stopping-pytorch/commit/7396b39d6a5505ecc93c9a78cedf454bd2bc2546))

### Unknown

* Merge pull request #9 from eddinho/custum_trace_function

add a custom trace print function to earlEarlyStopping class ([`f1a4cad`](https://github.com/Bjarten/early-stopping-pytorch/commit/f1a4cad7ebe762c1e3ca9e74c0845a555616952b))

* add a custom trace print function to earlEarlyStopping class ([`3a28f68`](https://github.com/Bjarten/early-stopping-pytorch/commit/3a28f68adeb44eab97716694367cc8c19ab331fd))

* Merge pull request #7 from SimonMossmyr/patch-1

Add path argument to EarlyStopping init ([`7ec86aa`](https://github.com/Bjarten/early-stopping-pytorch/commit/7ec86aa946468877bd74427f183d7d68a3eb2dc9))

* Add path argument to EarlyStopping init

Add an argument to the class initialization that specifies where the checkpoint model is saved to. Defaults to 'checkpoint.pt'. ([`321aa0d`](https://github.com/Bjarten/early-stopping-pytorch/commit/321aa0d084ac3f616ee53202e0d39f45ff8db158))

* Merge pull request #4 from wolframalpha/master

Update pytorchtools.py ([`effbcce`](https://github.com/Bjarten/early-stopping-pytorch/commit/effbcce06fe5e6459ad9df894616eb3a6bff87a4))

* Update pytorchtools.py ([`780b1dc`](https://github.com/Bjarten/early-stopping-pytorch/commit/780b1dc820d3dd9ed80281453c2a0639abfb600f))

* Merge pull request #2 from AdilZouitine/master

Add delta argument ([`36cff88`](https://github.com/Bjarten/early-stopping-pytorch/commit/36cff885cd4d255463b31ccc4823661522a50c9e))

* add delta ([`dfe8e45`](https://github.com/Bjarten/early-stopping-pytorch/commit/dfe8e45f77768959444d6a05c4bbd1e797206924))

* Merge pull request #1 from anshulrai/patch-1

Checkpoint model after first score improvement ([`fbcd638`](https://github.com/Bjarten/early-stopping-pytorch/commit/fbcd6388bd69cb067681a7b21aceec170b9077c6))

* Update pytorchtools.py ([`ffb781e`](https://github.com/Bjarten/early-stopping-pytorch/commit/ffb781e55f7bfee252e509fbfcadd856ff0e9271))

* Checkpoint model after first score improvement

To get expected output in cases where validation loss doesn't improve after fist epoch.

Example of bug:
Epoch 1/5 	 loss=140.3084 	 val_loss=118.2384 	 time=105.34s
Epoch 2/5 	 loss=120.4707 	 val_loss=120.7402 	 time=109.57s
Validation loss decreased (inf --> 120.7402).  Saving model ... ([`826f803`](https://github.com/Bjarten/early-stopping-pytorch/commit/826f8033969094ffbbc7e819421dae8667ed700f))

* rename: requirement.txt --> requirements.txt ([`0632940`](https://github.com/Bjarten/early-stopping-pytorch/commit/0632940c3695865a340403fd8e17d87b31102ce1))

* typo: Checkoint --> Checkpoint ([`5b15a68`](https://github.com/Bjarten/early-stopping-pytorch/commit/5b15a68f944de87ac78d639d74f79301f941b3cc))

* Initial commit ([`eac0fb1`](https://github.com/Bjarten/early-stopping-pytorch/commit/eac0fb13b4ff30f79049360ac43c9eaef85aaa57))
