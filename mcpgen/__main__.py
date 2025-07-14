import argparse
from .generator import generate_server


def main():
    parser = argparse.ArgumentParser(
        description="Generate an MCP proxy server, docs and basic tests from an OpenAPI spec"
    )
    parser.add_argument("--input", required=True, help="Path to OpenAPI JSON file")
    parser.add_argument("--output", required=True, help="Directory to write generated server")
    args = parser.parse_args()

    generate_server(args.input, args.output)
    print(f"Server generated in {args.output}")


if __name__ == "__main__":
    main()
