from setuptools import setup
import setup_translate
import os
import re
import glob

src_dir = os.path.dirname(__file__)
plugin_dir = "__PLUGIN_NAME__"
package_path = os.path.join('src', plugin_dir)

version_file = os.path.join(package_path, '__init__.py')
with open(version_file, 'r', encoding='utf-8') as f:
    content = f.read()
match = re.search(r"^__version__\s*=\s*['\"]([^'\"]+)['\"]", content, re.M)
if not match:
    raise RuntimeError("Unable to find version string.")
version = match.group(1)

patterns = []


def add_pattern_if_exists(pattern):
    full_pattern = os.path.join(package_path, pattern)
    if glob(full_pattern):
        patterns.append(pattern)


add_pattern_if_exists('images/*.png')
add_pattern_if_exists('*.png')
add_pattern_if_exists('*.xml')
add_pattern_if_exists('locale/*/LC_MESSAGES/*.mo')

name = 'enigma2-plugin-extensions-__PLUGIN_NAME__'.lower()

pkg = 'Extensions.__PLUGIN_NAME__'
setup(name=name,
       version=version,
       description='__PLUGIN_NAME__ for E2',
       package_dir={pkg: '__PLUGIN_NAME__'},
       packages=[pkg],
       package_data={pkg: patterns},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
