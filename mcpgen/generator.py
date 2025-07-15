import json
import os
import re
from pathlib import Path
from typing import Iterable, Tuple


def sanitize(name: str) -> str:
    """Sanitize a string to be a valid Python identifier."""
    name = re.sub(r"[^0-9a-zA-Z_]+", "_", name)
    if not name:
        name = "operation"
    if name[0].isdigit():
        name = f"_{name}"
    return name


def iter_operations(spec: dict) -> Iterable[Tuple[str, str, dict]]:
    """Yield (path, method, operation) tuples from spec."""
    paths = spec.get("paths", {})
    for path, methods in paths.items():
        for method, op in methods.items():
            yield path, method.lower(), op


def generate_server(spec_path: str, output_dir: str) -> None:
    """Generate a basic MCP proxy server, docs and tests from an OpenAPI spec."""
    with open(spec_path, "r") as f:
        spec = json.load(f)

    base_url = ""
    servers = spec.get("servers")
    if servers and isinstance(servers, list):
        base_url = servers[0].get("url", "").rstrip("/")

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    _generate_code(spec, base_url, output_path)
    _generate_requirements(output_path)
    _generate_docs(spec, output_path)
    _generate_tests(spec, base_url, output_path)


def _generate_code(spec: dict, base_url: str, out: Path) -> None:
    server_file = out / "server.py"
    with server_file.open("w") as f:
        f.write("import os\nimport requests\nfrom fastapi import FastAPI\n\n")
        f.write(f"BASE_URL = '{base_url}'\n")
        f.write("app = FastAPI()\n\n")
        f.write(
            "def get_headers():\n"
            "    token = os.environ.get('KM_ACCESS_KEY', '')\n"
            "    return {'X-KM-AccessKey': f'Bearer {token}'}\n\n"
        )

        for path, method, info in iter_operations(spec):
            op_id = sanitize(info.get("operationId", f"{method}_{path}"))
            path_params = [p["name"] for p in info.get("parameters", []) if p.get("in") == "path"]

            params_sig = ", ".join(f"{p}: str" for p in path_params)
            if params_sig:
                params_sig += ", "
            func_sig = f"{params_sig}data: dict | None = None, **query"

            format_params = ", ".join(f"{p}={p}" for p in path_params)
            if format_params:
                format_params = f", {format_params}"

            f.write(f"@app.{method}(\"{path}\")\n")
            f.write(f"def {op_id}({func_sig}):\n")
            f.write(f"    url = BASE_URL + \"{path}\".format({format_params.strip(', ')})\n")
            f.write(f"    resp = requests.{method}(url, headers=get_headers(), params=query, json=data)\n")
            f.write("    return resp.json()\n\n")


def _generate_requirements(out: Path) -> None:
    req_file = out / "requirements.txt"
    with req_file.open("w") as f:
        f.write("fastapi\nuvicorn\nrequests\n")


def _generate_docs(spec: dict, out: Path) -> None:
    readme_file = out / "README.md"
    with readme_file.open("w") as f:
        f.write("# Generated MCP Server\n\n")
        f.write("## Setup\n\n")
        f.write("```bash\n")
        f.write("pip install -r requirements.txt\n")
        f.write("export KM_ACCESS_KEY=<your-token>\n")
        f.write("uvicorn server:app --reload\n")
        f.write("```\n\n")
        f.write("## Endpoints\n\n")
        for path, method, info in iter_operations(spec):
            summary = info.get("summary", "")
            f.write(f"- **{method.upper()} {path}** - {summary}\n")


def _generate_tests(spec: dict, base_url: str, out: Path) -> None:
    test_file = out / "test_endpoints.py"
    with test_file.open("w") as f:
        f.write("import os\nimport requests\nimport json\n\n")
        f.write(f"BASE_URL = '{base_url}'\n")
        f.write("HEADERS = {'X-KM-AccessKey': f'Bearer {os.environ.get(\"KM_ACCESS_KEY\", \"\")}' }\n\n")
        f.write("def run_tests(spec_path):\n")
        f.write("    with open(spec_path, 'r') as fp:\n")
        f.write("        spec = json.load(fp)\n")
        f.write("    for path, methods in spec.get('paths', {}).items():\n")
        f.write("        op = methods.get('get')\n")
        f.write("        if not op:\n")
        f.write("            continue\n")
        f.write("        params = op.get('parameters', [])\n")
        f.write("        required = [p for p in params if p.get('required')]\n")
        f.write("        if required:\n")
        f.write("            continue\n")
        f.write("        url = BASE_URL + path\n")
        f.write("        resp = requests.get(url, headers=HEADERS)\n")
        f.write("        print(f'{path} -> {resp.status_code}')\n")
        f.write("\n")
        f.write("if __name__ == '__main__':\n")
        f.write("    import sys\n")
        f.write("    run_tests(sys.argv[1])\n")

