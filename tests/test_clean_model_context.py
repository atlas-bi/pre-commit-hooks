from pathlib import Path

from pre_commit_hooks.clean_model_context import main
from testing.util import get_resource_path


def test_failing_file(tmpdir):
    f = tmpdir.join("Atlas_WebContext.cs")
    f.write_text(
        Path(get_resource_path("Atlas_WebContext.cs")).read_text("utf8"),
        encoding="utf-8",
    )

    assert main([str(f)]) == 1

    assert main([str(f)]) == 0


def test_no_file():
    assert main([]) == 0


def test_other_file(tmpdir):
    f = tmpdir.join("other.cs")
    f.write_text(
        Path(get_resource_path("Atlas_WebContext.cs")).read_text("utf8"),
        encoding="utf-8",
    )

    assert main([str(f)]) == 0
