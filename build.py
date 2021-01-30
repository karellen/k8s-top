# -*- coding: utf-8 -*-
#
# (C) Copyright 2020 Karellen, Inc. (https://www.karellen.co/)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from pybuilder.core import (use_plugin, init, Author)

use_plugin("pypi:karellen_pyb_plugin", ">=0.0.1")
use_plugin("python.coveralls")

name = "k8s-top"
version = "0.0.1.dev"

summary = "K8S Top is a console dashboard and monitoring utility for Kubernetes"
authors = [Author("Karellen, Inc.", "supervisor@karellen.co")]
maintainers = [Author("Arcadiy Ivanov", "arcadiy@karellen.co")]
url = "https://github.com/karellen/k8s-top"
urls = {
    "Bug Tracker": "https://github.com/karellen/k8s-top/issues",
    "Source Code": "https://github.com/karellen/k8s-top/",
    "Documentation": "https://github.com/karellen/k8s-top/"
}
license = "Apache License, Version 2.0"

requires_python = ">=3.6"

default_task = ["analyze", "publish"]


@init
def set_properties(project):
    project.depends_on("gevent", ">=21.1.2")
    project.depends_on("kubernetes", "~=12.0")
    project.depends_on("picotui", "~=1.1.2")

    project.set_property("coverage_break_build", False)
    project.set_property("cram_fail_if_no_tests", False)

    project.set_property("integrationtest_inherit_environment", True)

    project.set_property("copy_resources_target", "$dir_dist/k8stop")
    project.get_property("copy_resources_glob").append("LICENSE")
    project.include_file("k8stop", "LICENSE")

    project.set_property("distutils_setup_keywords", ["kubernetes", "k8s", "kube", "top", "monitoring", "dashboard"])

    project.set_property("distutils_classifiers", [
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Environment :: Console",
        "Topic :: Utilities",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Distributed Computing",
        "Topic :: System :: Clustering",
        "Topic :: System :: Networking",
        "Topic :: System :: Networking :: Monitoring",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta"
    ])
