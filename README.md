# TestFlow 🧪

**TestFlow** is a Python-based **QA Test Analytics & Validation System** designed to validate software test execution data and, in later phases, analyze test results, failures, performance, and quality risks.

The project is being developed incrementally to simulate how a real-world QA/data-quality system would be designed and built.

---

## 🚀 Current Status

**Development Phase:** Phase 3 — Data Validation
**Current Version:** v0.1 (Validation Engine in Progress)

### Completed

* ✅ Project setup
* ✅ Project folder structure
* ✅ JSON input handling
* ✅ JSON parsing
* ✅ Root-level structural validation
* ✅ Root-level type validation
* ✅ Test-case structure validation
* ✅ Test-case type validation
* ✅ Detection of non-dictionary test cases
* ✅ Structured validation error reporting

### Not Implemented Yet

* ⏳ Semantic / business-rule validation
* ⏳ Data cleaning
* ⏳ Test result analysis
* ⏳ Failure analysis
* ⏳ Performance analysis
* ⏳ Risk detection
* ⏳ Reporting
* ⏳ Database / historical analysis
* ⏳ Dashboard / API

> **Note:** Semantic validation is intentionally excluded from the current version and will be implemented in the next development session.

---

# 📌 Project Objective

TestFlow will eventually accept test execution data and process it through multiple stages:

```text
Input Data
    ↓
Parser
    ↓
Validation
    ↓
Cleaning
    ↓
Test Analyzer
    ↓
Failure Analyzer
    ↓
Performance Analyzer
    ↓
Risk Engine
    ↓
Report Generator
    ↓
Historical Storage
    ↓
Dashboard / API
```

The current implementation covers the **Parser → Validation** portion of this pipeline.

---

# 🏗️ Current Architecture

```text
                 ┌───────────────┐
                 │    JSON File  │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │    Parser     │
                 │  parser.py    │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │ Python Dict   │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │   Validator   │
                 │ validator.py  │
                 └───────┬───────┘
                         │
                  ┌──────┴──────┐
                  ▼             ▼
              VALID          INVALID
                               │
                               ▼
                        Structured Errors
```

### Design Principle

The project follows a separation-of-responsibility approach:

* **Parser** → Reads and parses input.
* **Validator** → Checks whether the parsed data follows the defined contract.
* **Parser does not perform business validation.**
* **Validator does not modify the original data.**

---

# 📂 Project Structure

```text
TestFlow/
│
├── main.py
├── README.md
├── .gitignore
│
├── data/
│   ├── sample_tests.json
│   ├── invalid_tests.json
│   ├── invalid_structure.json
│   └── ...
│
├── output/
│   └── dict_error.py
│
└── src/
    ├── parser.py
    └── validator.py
```

---

# 📄 Data Contract

TestFlow currently expects JSON data following this structure:

```json
{
    "project": "E-Commerce Application",
    "run_id": "RUN_001",
    "test_cases": [
        {
            "test_id": "TC_001",
            "test_name": "Login Test",
            "status": "PASS",
            "response_time": 245,
            "error": null
        }
    ]
}
```

---

# 🔹 Root-Level Fields

| Field        | Required | Expected Type |
| ------------ | -------- | ------------- |
| `project`    | Yes      | String        |
| `run_id`     | Yes      | String        |
| `test_cases` | Yes      | List          |

---

# 🔹 Test Case Fields

Each item inside `test_cases` must currently be a dictionary containing:

| Field           | Required | Expected Type   |
| --------------- | -------- | --------------- |
| `test_id`       | Yes      | String          |
| `test_name`     | Yes      | String          |
| `status`        | Yes      | String          |
| `response_time` | Yes      | Integer / Float |
| `error`         | Yes      | String / `null` |

---

# 🔍 Current Validation

The validator currently performs **structural and type validation**.

### Root Validation

It checks whether:

* Root data is a dictionary.
* `project` exists.
* `project` is a string.
* `run_id` exists.
* `run_id` is a string.
* `test_cases` exists.
* `test_cases` is a list.

### Test Case Validation

For every test case, it checks:

* The item is a dictionary.
* `test_id` exists and is a string.
* `test_name` exists and is a string.
* `status` exists and is a string.
* `response_time` exists and is numeric.
* `error` exists and is either a string or `null`.

---

# ⚠️ Validation Error Format

TestFlow uses a structured validation result:

```python
{
    "valid": False,
    "errors": [
        "Required field 'project' is missing.",
        "'run_id' must be a string."
    ]
}
```

For valid data:

```python
{
    "valid": True,
    "errors": []
}
```

This format will later make it easier to integrate validation results with:

* CLI output
* Reports
* APIs
* Dashboards
* Automated QA pipelines

---

# 🧩 Parser

The current JSON parser is intentionally simple.

```python
import json

def load_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)

    return data
```

The parser's responsibility is only to:

1. Open the file.
2. Parse JSON.
3. Return the resulting Python object.

Business and structural validation are handled separately by the validator.

---

# 🧪 Testing the Validator

TestFlow uses different JSON datasets to verify validation behavior.

Example:

```text
data/
├── sample_tests.json
├── invalid_tests.json
└── invalid_structure.json
```

These datasets are used to test different scenarios such as:

* Valid JSON
* Invalid test-case structure
* Missing required fields
* Incorrect data types
* Non-dictionary test cases

---

# 🛠️ Technologies

Currently:

* **Python 3**
* **JSON**
* **Git / GitHub**

Planned technologies for later phases may include:

* SQLite
* pytest
* pandas
* HTML/CSS
* FastAPI
* Data visualization
* Statistical analysis

These will be introduced only when required by the relevant project phase.

---

# 🗺️ Development Roadmap

## Phase 0 — Project Setup

* [x] Project structure
* [x] Virtual environment
* [x] `.gitignore`
* [x] Initial Git repository

## Phase 1 — Requirements & Data Model

* [x] Define data contract
* [x] Define root fields
* [x] Define test-case fields
* [x] Define initial validation requirements

## Phase 2 — Input / Parser

* [x] JSON file loading
* [x] JSON parsing
* [x] Parser testing
* [x] Error scenario testing

## Phase 3 — Data Validation

* [x] Root structure validation
* [x] Root type validation
* [x] Test-case structure validation
* [x] Test-case type validation
* [ ] Semantic/business-rule validation

## Phase 4 — Data Cleaning

* [ ] Data normalization
* [ ] Cleaning strategy
* [ ] Handling inconsistent values

## Phase 5 — Test Result Analyzer

* [ ] Pass/fail statistics
* [ ] Test execution summary
* [ ] Test distribution analysis

## Phase 6 — Failure Analyzer

* [ ] Failure categorization
* [ ] Error analysis
* [ ] Failure frequency

## Phase 7 — Performance Analyzer

* [ ] Response-time analysis
* [ ] Slow-test detection
* [ ] Performance statistics

## Phase 8 — Risk Detection Engine

* [ ] Risk rules
* [ ] Risk scoring
* [ ] High-risk test detection

## Phase 9 — Report Generator

* [ ] CLI reports
* [ ] Summary reports
* [ ] Export functionality

## Phase 10 — Main Integration

* [ ] Complete pipeline
* [ ] End-to-end execution

## Phase 11 — Error Handling

* [ ] Robust exception handling
* [ ] User-friendly errors

## Phase 12 — Testing

* [ ] pytest
* [ ] Unit tests
* [ ] Integration tests

## Phase 13 — Refactoring / OOP

* [ ] Refactor modules
* [ ] Introduce classes where appropriate
* [ ] Improve maintainability

## Phase 14 — Historical Analysis

* [ ] SQLite
* [ ] Store test runs
* [ ] Historical comparisons
* [ ] Trend analysis

## Phase 15 — Dashboard

* [ ] Web dashboard
* [ ] Charts
* [ ] Test analytics visualization

## Phase 16 — Documentation

* [ ] Complete README
* [ ] Architecture documentation
* [ ] GitHub documentation
* [ ] Usage guide

## Phase 17 — College Project

* [ ] Project report
* [ ] System diagrams
* [ ] Presentation
* [ ] Viva preparation

---

# 📈 Planned Version Milestones

| Version  | Target                          |
| -------- | ------------------------------- |
| **v0.1** | Basic input + validation engine |
| **v0.2** | Test & failure analysis         |
| **v0.3** | Risk detection                  |
| **v1.0** | Complete CLI system             |
| **v1.5** | Testing + OOP + refactoring     |
| **v2.0** | SQLite + historical analytics   |
| **v3.0** | Dashboard / product layer       |

---

# 🎯 Long-Term Goal

TestFlow is intended to evolve from a simple Python validation project into a complete **QA analytics platform** capable of answering questions such as:

```text
How many tests passed?

Which tests are failing repeatedly?

Which failures are caused by the same error category?

Which tests are unusually slow?

Which areas of the application have the highest quality risk?

How is test quality changing across different test runs?
```

The final system will combine **QA concepts, Python programming, data analysis, software architecture, testing, and quality-risk analysis** into one project.

---

## 👨‍💻 Development Approach

TestFlow is being developed incrementally rather than building the entire system at once.

Each phase focuses on:

```text
Understand → Design → Implement → Test → Refactor → Move Forward
```

This approach keeps the system understandable while allowing more advanced concepts to be introduced as the project grows.

---

## 📌 Current Development Note

**Current focus:** Phase 3 — Data Validation

The next planned addition is **semantic/business-rule validation**, including validation of allowed status values and relationships between `status`, `response_time`, and `error`.

This section will be updated once semantic validation is implemented.
