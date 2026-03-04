# GitHub Repository Evaluator Agent

A Python-based agent that analyzes GitHub repositories and generates a quality score based on repository metadata and structure.

This project was built while experimenting with the Hive agent framework.

## Features

- Uses the GitHub REST API
- Detects repository license
- Detects README documentation
- Detects CI/CD workflows
- Detects tests directory
- Evaluates repository popularity (stars and forks)
- Generates a repository quality score
- Supports comparison of multiple repositories
- Automatically identifies the best repository

## Installation

Clone the repository and install dependencies.
```
git clone <repo-url>
cd github-repo-evaluator-agent
pip install requests
```

## Usage

Evaluate a single repository:

```
python3 agent.py https://github.com/aden-hive/hive
```

Compare multiple repositories:

```
python3 agent.py https://github.com/aden-hive/hive https://github.com/tensorflow/tensorflow
```

## Example Output

```
{
  "results": [
    {
      "repo": "https://github.com/aden-hive/hive",
      "score": 80
    },
    {
      "repo": "https://github.com/tensorflow/tensorflow",
      "score": 90
    }
  ],
  "best_repository": "https://github.com/tensorflow/tensorflow",
  "best_score": 90
}
```

## Purpose

This project demonstrates building an agent that interacts with the GitHub API and evaluates repository quality based on documentation, tests, CI/CD, and community signals.
