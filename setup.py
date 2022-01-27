import os
import sys
from pkg_resources import parse_version
from configparser import ConfigParser
import setuptools

assert parse_version(setuptools.__version__) >= parse_version('36.2')

# For the cases you want a different package to be installed on local and prod environments
LOCAL_ARG = '--test'
if LOCAL_ARG in sys.argv:
    index = sys.argv.index(LOCAL_ARG)  # Index of the local argument
    sys.argv.pop(index)  # Removes the local argument in order to prevent the setup() error
    testing = True
else:
    testing = False


class CleanCommand(setuptools.Command):
    """Custom clean command to tidy up the project root."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')


# note: all settings are in settings.ini; edit there, not here
config = ConfigParser(delimiters=['='])
config.read('settings.ini')
cfg = config['DEFAULT']
if testing:
    lib_version = cfg['testing_version']
else:
    lib_version = cfg['version']

cfg_keys = 'description keywords author author_email'.split()
expected = cfg_keys + "lib_name user branch license status min_python audience language".split()
for o in expected:
    assert o in cfg, "missing expected setting: {}".format(o)
setup_cfg = {o: cfg[o] for o in cfg_keys}
licenses = {'apache2': ('Apache Software License 2.0', 'OSI Approved :: Apache Software License')}
statuses = ['1 - Planning', '2 - Pre-Alpha', '3 - Alpha', '4 - Beta',
            '5 - Production/Stable', '6 - Mature', '7 - Inactive']
py_versions = '2.0 2.1 2.2 2.3 2.4 2.5 2.6 2.7 3.0 3.1 3.2 3.3 3.4 3.5 3.6 3.7 3.8'.split()
with open(cfg.get('requirements', '')) as f:
    requirements = f.readlines()
print(requirements)
data_files = cfg['data_files'].split()
lic = licenses[cfg['license']]
min_python = cfg['min_python']

setuptools.setup(
    name=cfg['lib_name'],
    license=lic[0],
    classifiers=['Development Status :: ' + statuses[int(cfg['status'])],
                 'Intended Audience :: ' + cfg['audience'].title(),
                 'License :: ' + lic[1],
                 'Natural Language :: ' + cfg['language'].title()] +
                ['Programming Language :: Python :: ' + o for o in
                 py_versions[py_versions.index(min_python):]],
    url=cfg['git_url'],
    packages=setuptools.find_packages(),
    include_package_data=True,
    data_files=[('', data_files)],
    test_suite='tests',
    install_requires=requirements,
    setup_requires=requirements,
    tests_require=requirements,
    cmdclass={
        'clean': CleanCommand,
    },
    dependency_links=cfg.get('dep_links', '').split(),
    python_requires='>=' + cfg['min_python'],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    zip_safe=False,
    entry_points={'console_scripts': cfg.get('console_scripts', '').split()},
    version=lib_version,
    **setup_cfg)
