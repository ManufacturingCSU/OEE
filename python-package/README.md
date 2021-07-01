# Build package

- `cd package`

- `pip install wheel setuptools`

- Update version number in the `pacakge\setup.py` file if needed

- `python setup.py bdist_wheel`

# Test the package

- `cd package-test`

- `create .env file using sample-env and update the configuration`

- `pip install manufacturingmetrics-0.1.0-py3-none-any.whl`

- `python .\testpackage.py`