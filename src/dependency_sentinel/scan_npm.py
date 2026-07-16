
import json
from pathlib import Path


def read_npm_dependencies(manifest_path: str) -> dict:

    path = Path(manifest_path)
    data = json.loads(path.read_text())

    dependencies = {}
    dependencies.update(data.get("dependencies", {}))
    dependencies.update(data.get("devDependencies", {}))
    return dependencies


if __name__ == "__main__":
    npm_dependencies = read_npm_dependencies('./src/package.json')
    print(f"Found {len(npm_dependencies)} dependencies:")
    for dependency, version in npm_dependencies.items():
        print(f"  {dependency}: {version}")
