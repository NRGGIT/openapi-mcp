Great. I’ll design a development plan for a CLI tool (built in Python or Rust) that takes an OpenAPI spec and builds a Model Context Protocol (MCP) server around it. The tool will use AI agents to test API endpoints in sandboxed environments (preferably Docker-based), infer behavior, and generate documentation. The objective is to emulate how a developer would analyze and document an unfamiliar API, enabling a fully documented MCP interface.

I'll look into the best agentic frameworks and sandbox testing tools suitable for automating endpoint exploration and inference. I'll also include recommendations for integrating AI components and generating high-quality documentation.

I'll get back to you shortly with a detailed development plan.


# Development Plan: AI-Powered MCP Server Generation Tool

## Overview

We aim to build a **CLI tool** that takes an OpenAPI JSON specification and automatically generates an **MCP (Model Context Protocol) server** for that API. The MCP server will act as a bridge, exposing the API’s endpoints as **tools/resources** that Large Language Models (LLMs) can invoke securely. By leveraging AI, the tool will not only scaffold the server but also **test the API endpoints in a sandbox** environment and **generate documentation**, much like a diligent developer exploring and documenting a new API. This will result in a “ready-to-use” MCP server with verified behavior and rich documentation, accelerating integration with AI agents (Claude, ChatGPT, etc.) that use the MCP standard.

**Why MCP and OpenAPI?** The MCP standard (introduced in late 2024) provides a uniform way for LLMs to interface with tools and data sources – essentially *“a USB-C port for AI”*. An MCP server for an API translates REST endpoints into standardized functions (tools) that an LLM agent can call. Since our starting point is a well-defined OpenAPI spec, we can treat it as the single source of truth to generate these tool definitions and the proxy logic, ensuring consistency with the API’s official contract. OpenAPI gives us structured, machine-readable details of endpoints, parameters, and responses, which is critical for LLM integration (LLMs can’t reliably infer API usage from prose alone). By automating generation from OpenAPI, we save development time and keep the MCP server in sync with the underlying API, avoiding duplicate manual work.

However, a **naïve one-to-one mapping** of every endpoint to an MCP tool is not always ideal – too many low-level tools can confuse the LLM, causing it to pick the wrong action or misuse the API. Our plan accounts for this by allowing curation or filtering of the generated tools. We’ll initially expose all operations (for completeness), but the design will enable developers to **exclude or group certain endpoints** to present a cleaner, higher-level interface to the AI if needed (aligning with best practices noted by others). The end result will be a **“LLM-ready” API interface** that is robust, well-documented, and safe for autonomous agents to use.

## Technology Stack Selection (Python vs. Rust)

**Preferred Language:** **Python** is the primary choice for this tool, with Rust as an alternative for future consideration. The reasons for preferring Python are:

* **Rich AI Ecosystem:** Python has a mature ecosystem for AI and LLM integration. Many libraries (e.g. OpenAI/Anthropic SDKs, LangChain, etc.) exist to help with prompt orchestration, agent frameworks, and calling LLMs. This aligns with our need for an “agentic flow engine” to generate tests and documentation, without reinventing the wheel for tool usage or sandboxing. For example, frameworks like LangChain provide OpenAPI agents that can interpret a spec and formulate API calls, and we can leverage those capabilities directly in Python. Rust’s AI tooling is catching up but is not as extensive as Python’s yet.

* **MCP Support:** Python has first-class support in the MCP community. The official MCP **Python SDK** (and high-level frameworks like **FastMCP**) make it easy to create servers and tools with minimal boilerplate. FastMCP in particular is a “pythonic” way to build MCP servers, handling protocol details so we can focus on our logic. It even supports features like generating servers from REST API specs and built-in testing utilities, which perfectly aligns with our project goals. Rust does have an MCP SDK as well, but using it would involve more low-level work to integrate with an AI agent. Python’s dynamic nature and async support (via `httpx` or `asyncio`) also simplify making API calls during testing.

* **Developer Productivity:** Given this tool will involve a lot of dynamic behavior (parsing JSON, making HTTP calls, orchestrating an AI agent), Python’s concise syntax and wealth of libraries (for OpenAPI parsing, HTTP requests, etc.) will speed up development. Rapid prototyping is important here since we’ll likely fine-tune prompt templates and parsing logic. Rust, while performant and type-safe, would result in a longer development cycle for experimenting with LLM prompts and could complicate calling external AI services (which often have Python examples/SDKs).

**Rust as Second Choice:** We acknowledge that Rust could be a viable choice for performance and strong typing of the generated server. If we were prioritizing a high-performance MCP server or needing fine-grained control (and if an embedded LLM was to be used), Rust might be considered. It could use the MCP Rust SDK and perhaps call out to an AI service for documentation generation. However, the added complexity in integrating AI agent logic in Rust (likely via web API calls to an AI service) outweighs its benefits for the initial version. We will design the architecture in a language-agnostic way so that porting to Rust later is possible if needed (for example, by clearly separating the spec processing logic and using an intermediate representation of the API that could feed into a Rust codegen pipeline). For now, **Python** offers the fastest path to a working solution with AI capabilities.

## Architecture and Key Components

The tool will be structured into clear components/modules to handle: **OpenAPI parsing & code generation, AI-driven testing, documentation generation,** and the **sandbox environment management.** Below is the proposed architecture:

* **CLI Interface:** A command-line entry point (e.g. using Python’s `argparse` or `click`) will allow users to specify input (path or URL to the OpenAPI JSON) and output directory, plus optional flags (like selecting a sandbox mode, providing API keys, filtering endpoints, etc.). For example:

  ```bash
  mcp-generator --input ./api_spec.json --output ./generated-server --run-tests --doc-gen  
  ```

  This CLI will orchestrate the end-to-end process: loading the spec, generating code, running tests, and producing docs. It keeps the tool headless/CLI-only as requested, with no GUI, but provides verbose console output so the user can follow what’s happening (e.g. which endpoint is being tested).

* **OpenAPI Parsing Module:** This component reads the OpenAPI spec (JSON or YAML) and constructs an internal representation of the API. We can use existing libraries (like `openapi-schema-pydantic` or `apispec`) to parse and validate the spec structure. The output will be data structures for: **endpoints (paths + methods)**, their **parameters and schemas**, expected responses, auth requirements, etc., as described in the spec. If the spec is large, we’ll ensure to handle it efficiently (potentially dereferencing `$ref` references for schemas using something like `jsonref` or `pydantic` models).

* **MCP Server Code Generator:** Using the parsed spec, this module generates the source code for an MCP server that proxies calls to the real API. In Python, we have two strategic options:

  1. **Leverage a Framework:** Utilize **FastMCP (the Python MCP SDK)** to quickly define tools. For each operation in the spec, we can programmatically create a function decorated as an MCP tool or resource. FastMCP allows defining a tool with a Python function signature (using type hints) and docstring. We could auto-generate these functions: the function name and description coming from the OpenAPI operation (e.g. use the `operationId` or path to name it, and use the OpenAPI summary/description for the docstring). The function’s logic will call the real API – likely using an HTTP client like `httpx`. We’ll include any necessary transformation: e.g., assembling the URL (base URL + path, substituting path parameters), adding query params, headers, body, etc., according to the spec. Authentication can be handled by injecting an API key or token from environment variables into the headers (the user can supply these via env or config; our code will read them). This essentially creates a **proxy** for each endpoint, validated against the spec. Using a framework saves us from writing low-level MCP protocol handling – FastMCP will take care of the JSON-RPC or HTTP interface that the MCP client (LLM side) uses to call these tools.

  2. **Custom Lightweight Server:** Alternatively, implement a minimal MCP server manually (for learning or flexibility). For example, the MCP spec defines a standardized JSON-over-STDIO or HTTP interface. We could generate a FastAPI app or even a simple asyncio server that listens for JSON-RPC requests (Claude Desktop supports launching an MCP server as a subprocess via stdio). A reference implementation by Earthly (N. Khan) simply used FastAPI with an `/invoke` endpoint to dispatch to tool functions stored in a registry. Our codegen could follow a similar pattern if not using FastMCP: build an internal `tool_registry` dict of operation name -> function, and an `/invoke` handler that finds the right function and executes it. While this is more control, it duplicates some protocol work. Given time constraints, **using FastMCP or the official SDK is preferable** to ensure we adhere to MCP spec details correctly (content types, streaming, etc.).

  Regardless of approach, the output will be a scaffolded project (in the output directory) containing the generated code: tool definitions, any helper code (like schema validation if needed), a `main` to run the server, and configuration files (requirements.txt or setup.py for Python). We’ll mirror features found in similar tools: e.g., **input validation** (we can generate Pydantic models or use a library like `pydantic`/`schemathesis` to validate that inputs match the OpenAPI schemas). This is akin to how another generator uses Zod schemas for runtime validation. We will also support **authentication schemes** declared in the spec (API keys, OAuth flows) by prompting the user for credentials or reading env vars, then injecting them appropriately. The goal is to produce a **runnable MCP server** out-of-the-box. At this stage, the MCP server code is in place but untested and with documentation directly from the OpenAPI spec.

* **AI-driven Testing Module:** Here lies the core “smart” part of the tool. Once the server code is generated, we will use AI to **automatically test each endpoint** (or a representative subset) to validate assumptions and gather real response data. Testing serves two purposes: (1) ensure the proxy logic actually works against the real API (or at least the API responds as expected), and (2) capture examples and nuances for documentation.

  **Sandbox Environment:** Tests will be executed in a controlled environment to avoid unwanted side effects. If the API is external but we have a test/development instance or credentials, we will use those. The tool will support running the tests inside a **Docker container** if needed (for example, if the API itself is something the user can spin up locally in Docker, or if isolation is required). Using Docker ensures any state changes can be rolled back, and provides a consistent environment with required dependencies. Alternatively, for purely external APIs (SaaS), “sandbox” means using test API keys or dummy data provided by the user. We’ll incorporate configuration for the user to specify a **base URL** for testing (which might be a staging server or localhost if they have the API running locally). This corresponds to the `--base-url` option seen in similar tools.

  **Test Case Generation:** We will utilize an LLM (via an API call to OpenAI, Anthropic, etc.) to generate test input data for each operation. The prompt to the LLM will include the endpoint description, the parameter schema (types, constraints), and any examples from the OpenAPI spec if available. For each endpoint, the AI can propose a plausible set of parameters. For example, if an endpoint is `/users/{id}` (GET user by ID), the LLM might propose an ID like “123” or some valid format. For a POST that creates an entity, the LLM can fill in a dummy object respecting the schema (e.g. create a new “user” with name "Test User"). Recent research has shown LLMs are capable of interpreting API specs to produce valid calls and even whole sequences of calls. We will constrain the AI to **non-destructive actions** by default: e.g., run GETs and safe POSTs. For dangerous operations (DELETE, etc.), we either skip them or perform them last and possibly only on test data. The user might opt-in to run destructive tests if they have a disposable testing environment.

  **Agentic Flow Engine:** Instead of manually coding the logic for iterating endpoints and calling the LLM repeatedly, we will explore using an **agent framework** to manage this flow. For instance, **LangChain** provides an agent that can ingest an OpenAPI spec and autonomously decide how to call the API (it can parse the spec and formulate requests). By giving the agent the goal “test all endpoints and record responses,” it could plan and execute calls. However, since our use-case is fairly structured (we *do* want to test essentially every endpoint in a systematic way), a simpler loop with LLM assistance might suffice. We might utilize LangChain’s OpenAPI tools under the hood or Semantic Kernel’s plugin mechanism to generate HTTP calls. The key is we **don’t want to implement the low-level HTTP calling agent from scratch** – we will use existing tooling to parse the spec and perform calls, letting us focus on prompts and verification logic. This addresses the requirement to *“find some agentic flow engine… to not spend time on tools, agents, sandbox implementation”* – effectively, we plug into an existing agent or workflow library to drive the testing.

  **Executing Tests & Verification:** For each generated test input, the tool will call the real API (likely not through the MCP server code, but directly using an HTTP client, to isolate testing of the underlying API first). It will capture the HTTP response status, headers, and body. We’ll then verify if the response conforms to the OpenAPI spec (e.g., if a 200 OK is expected with a certain schema, we can check if the JSON fields match the schema). Any deviations or errors will be logged. This provides quick feedback: if an endpoint is mis-specified or our generation logic was wrong (e.g., missing a required header), we catch it now. In essence, this is like an **automated contract test** for each endpoint. Using LLM for test generation is a novel approach, but it’s supported by emerging practices – *“LLMs can automate testing by creating test cases based on endpoint specifications”*. Additionally, by exercising the API, we ensure it’s **“agent-ready”**; as one paper notes, many APIs have complex inputs or ambiguous docs that hinder LLM usage, so runtime verification and refining of the tool definitions is crucial.

  If any test fails or returns an unexpected result, our tool could take a couple of actions:

  * **Adjust and Retry:** Possibly ask the AI to analyze the error and suggest a fix (e.g., “the API returned 400 for this payload, maybe the parameter X needs a different format”). This is an advanced step that truly treats the AI as an autonomous tester. While not in the initial scope, this could be a future enhancement (see *Future Enhancements* below). For now, we’ll log the issue and move on.
  * **Mark as Not for MCP:** If certain endpoints consistently fail or require complex setups (auth flows, etc.), we might tag them to be excluded from the final MCP server (with a note in docs that they weren’t auto-integrated). This ties back to the curation aspect – it’s better to omit a dysfunctional tool than to expose it to an LLM agent and have it misfire.

  After testing, we will have actual example inputs and outputs for many endpoints. These will be invaluable for documentation.

* **Documentation Generation Module:** The final step is to produce **comprehensive documentation** for the generated MCP server and its tools. While the OpenAPI spec provides a baseline (descriptions of endpoints, parameter info, etc.), we can greatly enrich the documentation using the data gathered and the language abilities of an LLM. Documentation will include:

  * **Tool Reference:** For each MCP tool (essentially each exposed endpoint or action), we’ll create a clear description of what it does, the inputs (parameters) it expects, and the output format. We’ll incorporate the OpenAPI description and **enhance it** with any insights gained from testing. For example, if the OpenAPI description was sparse, the LLM can expand on it, or if we discovered via testing that “parameter X must be a valid email format” we can note that. We will also list example calls. Ideally, we include a **concrete example** of usage with the actual response. E.g., for a GET endpoint, we might show a sample JSON response (truncated if large) that we obtained in testing. This makes the docs much more practical. Using an LLM for this is perfect because LLMs excel at summarizing and explaining technical information in a human-readable way. We’ll prompt the LLM with something like: *“Here is the OpenAPI spec info for the endpoint `GET /users/{id}` and a sample response we received. Please write a documentation entry that explains what this tool does, the meaning of its parameters, and shows the example response with an explanation.”* The LLM can output a nicely formatted Markdown section. A similar approach can generate code examples (maybe showing how an MCP client would call the tool, though that might be more for advanced documentation since typical users will be LLMs themselves rather than humans calling the MCP server directly).

  * **Overall README:** We’ll generate a README for the whole MCP server project. This will explain how to run the server (e.g. “`pip install -r requirements.txt` then `python main.py`”), any setup needed (like setting environment variables for API keys or base URLs), and an overview of available tools. This is akin to what Stainless or Speakeasy provide when they generate an MCP server – often a README that includes how to install or run it, and maybe how to connect it to an MCP client (Claude Desktop etc.). We can have the LLM draft this as well, ensuring it’s clear and comprehensive. For instance, *“This MCP server allows an AI agent to interact with the **ExampleAPI**. It includes X tools (listed below) covering functionality such as ... To use this server with an MCP-compatible client, run ... etc.”*.

  Automating documentation in this way addresses a common pain point: developers often lack time to write good docs, but here AI can do it quickly. As Stoplight’s API blog noted, *“AI can generate consistent, easy-to-read documentation much faster than humans... documentation is as simple as a prompt like ‘create an API reference for this endpoint’”*. We will still review the AI-generated docs for accuracy, but this saves a lot of time and yields professional-looking documentation for our tool out of the box.

* **Sandbox & Environment Configuration:** Throughout the above components, we will emphasize configurability and safety. This includes:

  * Docker integration (perhaps the CLI has a flag `--use-docker` to run tests inside a container or `--docker-api <image>` to spin up a given API image).
  * Environment variable management for secrets (API keys, etc.) – the generated code will expect certain env vars for auth (not hard-code them). We’ll document which ones are needed, possibly even generating a `.env.example` file.
  * Logging and error handling: The tool should log what it’s doing, especially when calling external APIs or the LLM. If the AI outputs something unexpected or an API call fails, it should be caught and logged rather than crashing. This way a user running the tool can troubleshoot (e.g., maybe the provided API key was invalid, etc.).
  * Extensibility: Design the modules so that each can be run in isolation if needed. For example, a user might want to skip testing or skip documentation generation (maybe if they trust the spec or are in a hurry). The CLI can allow `--no-test` or `--no-doc` flags to omit those phases. Similarly, if they want to later re-run just the docs generation (perhaps after editing something), they could. This modularity also makes the development easier (we can implement and debug each part one by one).

## Development Steps and Timeline

Following is a step-by-step plan to implement the tool, ensuring all required capabilities are addressed:

1. **Spec Parsing & Baseline Code Generation (Week 1-2):**

   * Set up the project structure (Python package, CLI entrypoint).
   * Implement OpenAPI loading (support local file or URL). Validate the spec.
   * Generate MCP server skeleton: for each endpoint, create a function or class (depending on framework) with appropriate name, parameters, and placeholder logic (e.g., a call to `pass` or a simple print). Initially, focus on GET endpoints as tools returning dummy data, just to test the flow.
   * Integrate with FastMCP or MCP SDK: get a minimal server running with one or two dummy tools, to verify that we can start the server and it’s discoverable (e.g., hitting a `/tools` or seeing the server respond on stdio).
   * **Output:** A minimal CLI that reads a spec and produces a project with an MCP server that compiles/runs. At this stage, the tools might not actually call the real API yet.

2. **Proxy Logic Implementation (Week 2-3):**

   * Flesh out the tool functions to perform real HTTP calls to the API. Use the spec info to construct requests (this includes path parameter substitution, query params, headers, body). We can use an HTTP client like `requests` or `httpx` (with async support).
   * Support authentication: e.g., if spec uses API Key in header, ensure our client adds it from env var. If OAuth2, document that user must get a token – possibly out of scope to fully automate OAuth, so just allow them to supply a token.
   * Add basic validation using the spec schemas: e.g., if a required parameter is missing, our tool can immediately return an error to the LLM (so the LLM knows it called the tool wrong). This can be done by checking the `input_data` against parameter definitions, or by using Pydantic models auto-generated from the schemas.
   * Test this component manually with a small spec (like the Petstore example or a simple internal API): run the generated server and manually call a couple tools (via HTTP or an MCP client) to see if it hits the real API and returns data.
   * **Output:** Fully functional proxy implementation. At this point, an LLM agent *could* use the server, though it’s not documented or verified yet.

3. **AI Test Generation Integration (Week 3-4):**

   * Choose and integrate an LLM API (e.g., OpenAI GPT-4 or Claude) for generating test cases. Ensure API keys and usage are configured.
   * Develop prompt templates for generating test inputs per endpoint. Possibly use few-shot examples: provide the model one or two example endpoint specs and a valid input, so it learns the pattern.
   * Implement the loop/agent that goes through endpoints: For each endpoint, call LLM to suggest inputs. Then execute the call using the requests library. Capture responses. If the response indicates an error (status 4xx/5xx), possibly log and attempt a second try with a modified input (we can have the LLM analyze the error message if available – e.g., 400 with some message – and adjust the input).
   * Manage the sandbox: if using Docker, ensure the API is up in Docker. Possibly integrate `docker-py` to programmatically run a container for the API (if user provided an image). If it’s an external API, ensure that test calls are hitting a safe environment (this may rely on user’s test credentials).
   * As tests run, store the results in memory or on disk. We’ll create a structure to hold example requests and responses for each operation. Also note any discrepancies with the spec (if response schema didn’t match exactly, etc.). These will be fed into docs.
   * **Output:** A completed testing phase in the CLI tool. If the user runs with `--run-tests`, it will output logs like “Testing GET /users -> Success (200 OK)” or “Testing POST /orders -> Got 201 Created” etc. We should also handle the case of rate limiting or API quotas (maybe slow down or stop if too many calls). At the end of this phase, we have confidence in the correctness of the generated tools, or at least identified problematic endpoints.

4. **Documentation Generation (Week 4):**

   * Integrate LLM prompts for documentation. This can be done after all tests complete. We feed the LLM with structured info for each endpoint: the OpenAPI description + any additional notes we have (from testing or common sense) + a sample request/response. Ask it to produce a Markdown section documenting the endpoint in a friendly way.
   * Also prompt it to produce the general README. We’ll supply the list of tools, their one-line summaries, and any setup instructions (we can template some parts like how to run). The LLM can then produce nicely formatted text.
   * Review the outputs for correctness. Ideally, keep the model outputs editable (perhaps the tool writes them to `.md` files in the output directory). The developer can review and tweak if needed before publishing.
   * Preserve any **citations or references** if we want, though since this is internal documentation for the API, citations are not as relevant as just clarity and accuracy. (In our response here we cite external sources, but the tool’s docs will cite the API itself).
   * **Output:** Markdown/HTML documentation files. For example, an `API_TOOLS.md` file listing each tool and usage, and the main `README.md`. Optionally, embed the docs as docstrings in the code too (so that if someone opens the code, they see the AI-written explanation in the function docstring).

5. **Final Packaging & Quality Assurance (Week 5):**

   * Put it all together and test the CLI on a few different API specs (small and large). For instance, try with the Petstore OpenAPI, a more complex one like GitHub’s API (if available), etc., to see how it handles various schemas. This will flush out issues like unusual parameter formats, or very large specs (we may need to paginate the LLM calls if the spec is huge).
   * Optimize prompt usage to stay within context limits (for very large specs, perhaps generate tests for one endpoint at a time rather than giving the LLM the whole spec at once – which we already plan to do endpoint by endpoint).
   * Ensure the tool’s output (code + docs) is clean and professional. E.g., run a formatter on the code (black for Python) and a linter to ensure no obvious issues.
   * Write our own usage documentation for the tool itself (how to install our tool, etc.) and prepare for release (could be open-sourced on GitHub, for example). Possibly create examples to showcase its usage (like a before-and-after of turning an OpenAPI spec into an MCP server).
   * **Output:** A polished CLI tool (perhaps published as a Python package) ready for users.

Throughout these steps, we will incorporate feedback from tests and, if possible, early users. The plan is quite comprehensive, but given the iterative nature, we might cycle back: for instance, after implementing docs generation, we might realize we need more data from testing, etc., so adjust accordingly.

## Future Enhancements and Considerations

Once the initial version is complete, there are several areas to further improve the tool:

* **Smarter Endpoint Filtering and Grouping:** As noted, not all API endpoints are equally useful to expose to an LLM. In future, we could use AI to analyze the OpenAPI and suggest a more abstracted interface. For example, if an API has separate endpoints for list/read/create on a resource, an LLM might handle it better if they are grouped or the less-used ones are hidden. We could implement heuristics or prompts to **recommend which endpoints to include** as MCP tools by default. (This is similar to Stainless’s approach of allowing developers to mark `mcp: false` on less relevant endpoints.) The tool could ask the LLM: *“Which API operations are most essential for high-level use?”* and use that to filter. This would reduce the cognitive load on the AI agent using the MCP server.

* **Behavior Inference & Multi-step Workflows:** Beyond just input/output types, an AI could infer higher-level behaviors or workflows. For instance, if certain endpoints must be called in sequence (like login then fetch data), we might document that or even combine them into a single MCP tool. This gets into **agent workflow design** – eventually the tool might output not just atomic tools but also some **MCP prompt templates or chains** that encapsulate common sequences. That would truly make the API “agent-friendly.” This wasn’t in the initial scope (we start CLI-only, no complex workflows), but it’s a logical extension as we aim to make integration seamless.

* **Enhanced Testing (Property-based or Fuzz):** While LLM-generated tests are a great start (and cover realistic scenarios), we could integrate traditional testing tools for thoroughness. For example, using Schemathesis or RESTler to fuzz test each endpoint for edge cases. This would ensure our MCP server handles unexpected inputs gracefully (e.g., returns errors properly to the LLM). This could be an optional mode for power users who want to harden their API for AI use.

* **Support for Other Protocols/Transports:** MCP supports multiple transports (stdio, HTTP server with Server-Sent Events, etc.). We will initially likely use stdio (for Claude Desktop) or a simple HTTP interface. In the future, the tool could allow choosing the transport (like the openapi-mcp-generator does with a flag). For example, generating a web server variant that could be deployed and used by remote agents. We’d also consider packaging the MCP server as a Docker image for easy deployment.

* **User Interface (if ever needed):** The current plan is CLI only, which is fine for developers. But if a broader audience (less technical) wanted to use it, a minimal UI or web interface could be built on top to select a spec and get an MCP server. For now, CLI suffices as requested.

* **Continuous Updates:** If the underlying API changes (spec updates), we could allow re-running the tool to update the MCP server. Maybe integrate with a git repo to intelligently patch changes. This is more of a product improvement to keep the MCP server in sync with API versions.

By executing this development plan, we will create a powerful tool that automates the transformation of any API into an **MCP-compliant, AI-friendly service**. It will embody the latest best practices in LLM integration with APIs: using OpenAPI as the source of truth, AI for intelligent test generation and documentation, and robust frameworks for MCP implementation. Ultimately, this tool will **empower developers to expose their services to AI agents with minimal manual effort**, speeding up the creation of the “API intermediaries” that let LLMs safely and effectively perform complex tasks.

## References and Supporting Sources

* Alexis Rico, *“From OpenAPI spec to MCP: How we built Xata’s MCP server,”* Xata Blog – describing an OpenAPI-driven approach to generating MCP servers (codegen with curation).
* Harsha HR, *“openapi-mcp-generator”* – an open-source CLI tool that converts OpenAPI 3.0 specs into MCP servers (Node/TypeScript) with features like request proxying, auth support, and validation.
* Nafiul Khan, *“Turn your OpenAPI into MCP Server in 5 minutes!”* – Medium article demonstrating a Python FastAPI approach to dynamically create MCP tools from an OpenAPI JSON.
* **Model Context Protocol (MCP) Documentation:** Official MCP Introduction and Quickstart – outlines the MCP architecture (client-server model for LLMs and tools) and the concept of resources vs tools.
* Israel T., Ambassador Labs, *“Automate AI Workflows with OpenAPI: Building LLM-Ready APIs,”* – highlights the importance of clear OpenAPI specs for LLM integrations and how automation (codegen, testing) can make APIs “LLM-ready”.
* Valeriu, StackOnCloud, *“LLM Agents and OpenAPI: Building Autonomous API Intermediaries,”* – discusses how LLMs + OpenAPI enable code generation, documentation, test creation, and agent-based API usage.
* IBM Research (Bandlamudi et al.), *“A Framework for Testing and Adapting REST APIs as LLM Tools,”* (2025) – research paper proposing automated test generation and tool definition enrichment to ensure APIs are ready for LLM agents.
* Stoplight API Blog, *“Supercharge Your API Program with LLMs,”* – describes using LLMs to automate API code and documentation tasks, with examples of generating docs from code and tests from specs.

These sources reinforce our plan by showing industry trends: using OpenAPI as a foundation for AI integration, leveraging LLMs for documentation and testing, and the need for careful design so that AI agents can reliably use the generated tools. The development plan builds directly on these insights to create a robust, cutting-edge tool.

## Quickstart Example

After implementing the generator you can create a minimal MCP server from any OpenAPI JSON file. The tool also writes simple documentation and a small test script alongside the server code.

```bash
# install package dependencies
pip install -e .
# generate server
python -m mcpgen --input openapi-example.json --output generated_server
# run the server (requires FastAPI and uvicorn)
cd generated_server
export KM_ACCESS_KEY=<your-access-key>
uvicorn server:app --reload
```

The `KM_ACCESS_KEY` environment variable should hold the token used for requests. When running tests against the knowledge model API you must include the `X-KM-AccessKey` header.
