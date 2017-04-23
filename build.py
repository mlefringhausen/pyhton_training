
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
#use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin('copy_resources')


default_task = ['clean', 'analyze', 'package']


@init
def set_properties(project):
    project.build_depends_on("unittest2")
    project.build_depends_on("moto")
    project.build_depends_on("mock")
    project.build_depends_on("requests_mock")

    project.depends_on("boto3")
    project.depends_on("requests")
    project.depends_on("isodate")
    project.depends_on("BeautifulSoup")