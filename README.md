# Getting Started
This repository contains the common utility functions shared across the eCAPTION backend, such as the shared wrapper over Kafka, centralized store of Kafka topic names, and corresponding event types.

## Installation from GitHub repository via pip
To install this package, run the following command to pull it directly from GitHub.
```
pip install "git+https://github.com/eCAPTION/ecaption_utils.git"
```

## Adding a new package
To add a new package (such as `ecaption_utils.XXX`):
1. Create a new directory under `root > ecaption_utils > XXX`.
1. `cd` to this directory.
1. Write the utility functions under this directory.
1. Configure an `__init__.py` file in this directory to make sure your utility functions are visible in your newly created package.
1. Under `root > setup.py`, modify the `packages` array to include this new directory you have created.
1. Test out the installation of this package locally using `pip`. E.g.
    - Activate a virtual environment, e.g.
      ```
      virtualenv venv
      source venv/bin/activate
      ```
    - In the root directory of this repository, run
      ```
      pip install .
      ```
    - A `build` folder should be created. Check that `build/lib` contains the new package.
1. Once ready, bump the version number in `setup.py`.
1. Make a new commit with the relevant changes and push it to the GitHub repository.
