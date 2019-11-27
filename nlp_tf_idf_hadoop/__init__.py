"""
nlp-tf-idf-hadoop
NLP analysis of Term Frequency - Inverse Document Frequency using Hadoop
"""

# Add imports here
from .nlp_tf_idf_hadoop import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
