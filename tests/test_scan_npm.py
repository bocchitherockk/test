import json

from src.scan_npm import read_npm_dependencies


def test_reads_dependencies_and_dev_dependencies(tmp_path):
    manifest = tmp_path / "package.json"
    manifest.write_text(json.dumps({
        "name": "example-app",
        "dependencies": {
            "express": "^4.18.2"
        },
        "devDependencies": {
            "jest": "^29.7.0"
        }
    }))

    result = read_npm_dependencies(str(manifest))

    assert result == {
        "express": "^4.18.2",
        "jest": "^29.7.0"
    }


def test_returns_empty_dict_when_no_dependencies(tmp_path):
    manifest = tmp_path / "package.json"
    manifest.write_text(json.dumps({"name": "empty-app"}))

    result = read_npm_dependencies(str(manifest))

    assert result == {}