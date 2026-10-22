import re

import version


def test_version_is_semver():
    assert re.fullmatch(r"\d+\.\d+\.\d+", version.__version__)
