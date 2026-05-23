# Agent Performance Optimization with DAG and LangGraph

## Introduction

This repository presents a case study on optimizing agent performance using a Directed Acyclic Graph (DAG) approach with LangGraph nodes. We compare the performance of a sequential `create_agent` approach with a DAG agent, highlighting the benefits of parallel tool calling and planning.

## Getting Started

1. Clone the repository: `git clone https://github.com/your-repo/agent-performance-optimization.git`
2. Install dependencies: `pip install -r requirements.txt`

## Agent Architectures

### Sequential `create_agent`

*   `agent.py`: A sequential agent created using `create_agent`, relying on a reasoning model with high reasoning effort.

### DAG Agent (LangGraph)

*   `dag_agent.py`: A DAG-based agent utilizing LangGraph nodes with a planner, enabling parallel tool calling.

## Performance Comparison

| Agent Architecture | Average Response Time |
| --- | --- |
| Sequential `create_agent` | 20 seconds |
| DAG Agent (LangGraph) | 5 seconds |

## Usage

1. Run the sequential agent: `python agent.py`
2. Run the DAG agent: `python dag_agent.py`

## Contributing

Contributions are welcome! Please submit a pull request with your changes and a brief description of the improvements.

## License

This repository is licensed under the [MIT License](https://opensource.org/licenses/MIT).