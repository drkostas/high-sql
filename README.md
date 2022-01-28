# High SQL

[![CircleCI](https://circleci.com/gh/drkostas/high-sql/tree/master.svg?style=svg)](https://circleci.com/gh/drkostas/high-sql/tree/master)
[![GitHub license](https://img.shields.io/badge/license-Apache-blue.svg)](https://github.com/drkostas/high-sql/blob/master/LICENSE)

## About <a name = "about"></a>

A high-level sql command utility. Currently, only MySQL is
supported. [PYPI Package](https://pypi.org/project/high-sql/)

## Table of Contents

+ [Using the library](#using)
    + [Installing and using the library](#install_use)
    + [Examples of usage](#examples)
+ [Manually install the library](#manual_install)
    + [Prerequisites](#prerequisites)
    + [Install the requirements](#installing_req)
    + [Run the Unit Tests](#unit_tests)
+ [Continuous Integration](#ci)
+ [Update PyPI package](#pypi)
+ [License](#license)

## Using the library <a name = "using"></a>

For a detailed usage example see 
[example.py](https://github.com/drkostas/high-sql/tree/master/example.py).

### Installing and using the library <a name = "install_use"></a>

First, you need to install the library using pip:

```shell
$ pip install high_sql
```

Then, import it and initialize it like so:

```python
from high_sql import HighMySQL

db_conf = {'hostname': 'your hostname', 'username': 'your username', 'password': 'your password',
           'db_name': 'your db name', 'port': 3306}
mysql_obj = HighMySQL(config=db_conf)
```

If you want to use a yml file to load the configuration, you can use the `HighConfig` class:
```python
from high_sql import HighConfig
import os

config_path = str(os.path.join('confs', 'conf.yml'))
config = HighConfig(config_src=config_path)
db_conf = config.get_db_config()
```

Two example YAML files can be found in 
the [confs folder](https://github.com/drkostas/high-sql/blob/master/confs).
For more details on how to use this YAML configuration loader see 
this [Readme](https://github.com/drkostas/yaml-config-wrapper/blob/master/README.md).

### Examples of usage <a name = "examples"></a>

The currently supported operations are the following:
- Inserts, Updates, Deletes, Select
- Create, Truncate, Drop table
- Show all tables

**Insert**
```python
mysql_obj.insert_into_table('test_table', data={'firstname': 'Mr Name', 'lastname': 'surname'})
```
**Update**
```python
mysql_obj.update_table('test_table', set_data={'lastname': 'New Last Name'},
                       where='firstname="Mr Name"')
```
**Delete**
```python
mysql_obj.delete_from_table('test_table', where='firstname="Mr Name"')
```
**Select**
```python
res = mysql_obj.select_from_table('test_table', columns='*', where='firstname="Mr Name"', 
                                  order_by='firstname', asc_or_desc='ASC', limit=5)
```
**Truncate**
```python
mysql_obj.truncate_table('test_table')
```
**Create**
```python
mysql_obj.create_table(table='test_table', schema=table_schema)
```
**Drop**
```python
mysql_obj.drop_table('test_table')
```
**Show Tables**
```python
mysql_obj.show_tables()
```

All of these examples can be found 
in [example.py](https://github.com/drkostas/high-sql/tree/master/example.py).

## Manually install the library <a name = "manual_install"></a>

These instructions will get you a copy of the project up and running on your local machine for
development and testing purposes.

### Prerequisites <a name = "prerequisites"></a>

You need to have a machine with
[anaconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) installed and
any Bash based shell (e.g. zsh) installed.

```ShellSession

$ conda -V
conda 4.10.1

$ echo $SHELL
/usr/bin/zsh

```

### Install the requirements <a name = "installing_req"></a>

All the installation steps are being handled by
the [Makefile](https://github.com/drkostas/high-sql/tree/master/Makefile).

First, modify the python version (`min_python`) and everything else you need in
the [settings.ini](https://github.com/drkostas/high-sql/tree/master/settings.ini).

Then, execute the following commands:

```ShellSession
$ make create_env
$ conda activate yaml_config_wrapper
$ make dist
```

Now you are ready to use and modify the library.

### Run the Unit Tests <a name = "unit_tests"></a>

If you want to run the unit tests, execute the following command:

```ShellSession
$ make tests
```

## Continuous Integration <a name = "ci"></a>

For the continuous integration, the <b>CircleCI</b> service is being used. For more information you can
check the [setup guide](https://circleci.com/docs/2.0/language-python/).

For any modifications, edit
the [circleci config](https://github.com/drkostas/high-sql/tree/master/.circleci/config.yml).

## Update PyPI package <a name = "pypi"></a>

This is mainly for future reference for the developers of this project. First,
create a file called `~/.pypirc` with your pypi login details, as follows:

```
[pypi]
username = your_pypi_username
password = your_pypi_password
```

Then, modify the python version (`min_python`), project status (`status`), release version (`version`) 
and everything else you need in
the [settings.ini](https://github.com/drkostas/high-sql/tree/master/settings.ini).

Finally, execute the following commands:

```ShellSession
$ make create_env
$ conda activate yaml_config_wrapper
$ make release
```

For a dev release, change the `testing_version` and instead of `make release`, run `make release_test`.

## License <a name = "license"></a>

This project is licensed under the MIT License - see
the [LICENSE](https://github.com/drkostas/high-sql/tree/master/LICENSE) file for details.

<a href="https://www.buymeacoffee.com/drkostas" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
