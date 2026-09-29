# TestFlow 🧪

> **Python QA Test Analytics & Validation System**

TestFlow is a Python-based project for validating software test
execution data. It currently focuses on reliable JSON input handling,
structural validation, semantic/business-rule validation, duplicate
detection, and structured validation results.

The project is being developed incrementally so that each version adds a
clear layer of functionality.

------------------------------------------------------------------------

## 📊 Project Progress

**Current Version: v0.1 --- Basic Input + Validation Engine**\
**Current Phase: Phase 3 --- Data Validation**\
**Status: ✅ v0.1 functionality complete and regression-tested**

  --------------------------------------------------------------------------------------
  Area                    Status                  Documentation
  ----------------------- ----------------------- --------------------------------------
  Project setup           ✅ Complete             [Project
                                                  Structure](#-project-structure)

  Requirements & data     ✅ Complete             [Data Contract](#-data-contract)
  contract                                        

  JSON parser             ✅ Complete             [Parser](#-parser)

  Structural validation   ✅ Complete             [Structural
                                                  Validation](#-structural-validation)

  Semantic validation     ✅ Complete             [Semantic
                                                  Validation](#-semantic-validation)

  Duplicate detection     ✅ Complete             [Duplicate
                                                  Detection](#-duplicate-detection)

  Main pipeline           ✅ Complete             [Application Flow](#-application-flow)
  integration                                     

  A--H regression testing ✅ Complete             [Testing](#-testing)

  Error handling          ⏳ Planned              [Future Work](#-future-work)

  pytest test suite       ⏳ Planned              [Future Work](#-future-work)

  Data analysis           ⏳ Planned              [Roadmap](#-roadmap)

  Risk detection          ⏳ Planned              [Roadmap](#-roadmap)

  SQLite / history        ⏳ Planned              [Roadmap](#-roadmap)

  Dashboard / API         ⏳ Planned              [Roadmap](#-roadmap)
  --------------------------------------------------------------------------------------

------------------------------------------------------------------------

## 🎯 Project Objective

TestFlow is intended to evolve from a simple validation utility into a
QA analytics system that can answer questions such as:

-   How many tests passed or failed?
-   Which tests are failing?
-   Which failures occur repeatedly?
-   Which tests are unusually slow?
-   Which areas have higher quality risk?
-   How does test quality change across different test runs?

The current version establishes the **input, validation, and result
foundations** required for these later features.

------------------------------------------------------------------------

## 🔄 Application Flow

The current v0.1 pipeline is:

``` text
User
  │
  ▼
JSON File Path
  │
  ▼
Parser
  │
  ▼
Structural Validation
  │
  ├── Invalid ──► Stop
  │
  └── Valid
        │
        ▼
  Semantic Validation
        │
        ├── Rule Validation
        ├── Duplicate Detection
        ├── Summary Calculation
        └── Structured Result
```

### Separation of Responsibilities

  -----------------------------------------------------------------------
  Component                           Responsibility
  ----------------------------------- -----------------------------------
  `main.py`                           Application orchestration and user
                                      input

  `parser.py`                         Reads and parses JSON

  `validator.py`                      Structural/type validation

  `semantic_validation.py`            Semantic validation orchestration
                                      and result aggregation

  `semantic_rules/`                   Individual semantic rule validators

  `output/`                           Supporting validation output
                                      utilities

  `data/`                             Test and sample datasets
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 📁 Project Structure

``` text
TestFlow/
│
├── main.py
├── README.md
├── .gitignore
│
├── data/
│   ├── sample_tests.json
│   ├── invalid_parser.json
│   ├── invalid_root.json
│   ├── invalid_structure.json
│   ├── invalid_tests.json
│   ├── invalid_tests_a.json
│   │
│   └── test_group/
│       ├── group_a.json
│       ├── group_b.json
│       ├── group_c.json
│       ├── group_d.json
│       ├── group_e.json
│       ├── group_f.json
│       ├── group_g.json
│       └── group_h.json
│
├── output/
│   └── dict_error.py
│
└── src/
    ├── parser.py
    ├── validator.py
    ├── semantic_validation.py
    │
    └── semantic_rules/
        ├── __init__.py
        ├── validate_status.py
        ├── validate_response_time.py
        ├── validate_pass.py
        ├── validate_fail.py
        └── validate_skip.py
```

------------------------------------------------------------------------

## 📄 Data Contract

TestFlow currently expects JSON data with the following structure:

``` json
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

### Root-Level Fields

  Field          Required   Type
  -------------- ---------- --------
  `project`      Yes        String
  `run_id`       Yes        String
  `test_cases`   Yes        List

### Test-Case Fields

  Field             Required   Type
  ----------------- ---------- -----------------
  `test_id`         Yes        String
  `test_name`       Yes        String
  `status`          Yes        String
  `response_time`   Yes        Integer / Float
  `error`           Yes        String / `null`

------------------------------------------------------------------------

## 🔍 Structural Validation

Structural validation is implemented in:

``` text
src/validator.py
```

It verifies:

-   Root data is a dictionary.
-   `project` exists and is a string.
-   `run_id` exists and is a string.
-   `test_cases` exists and is a list.
-   Each test case is a dictionary.
-   `test_id` exists and is a string.
-   `test_name` exists and is a string.
-   `status` exists and is a string.
-   `response_time` exists and is numeric.
-   `error` exists and is a string or `null`.

Structural validation does **not** perform business-rule validation.

------------------------------------------------------------------------

## 🧠 Semantic Validation

Semantic validation is implemented in:

``` text
src/semantic_validation.py
```

Individual rules are separated into:

``` text
src/semantic_rules/
```

### Rule Validators

  -------------------------------------------------------------------------------
  Validator                    Rule                       Requirement
  ---------------------------- -------------------------- -----------------------
  `validate_status()`          `INVALID_STATUS`           Status must be `PASS`,
                                                          `FAIL`, or `SKIP`

  `validate_response_time()`   `NEGATIVE_RESPONSE_TIME`   Response time must be ≥
                                                          0

  `validate_pass()`            `PASS_ERROR`               PASS must have
                                                          `error = None`

  `validate_fail()`            `FAIL_ERROR`               FAIL must contain an
                                                          error message

  `validate_skip()`            `SKIP_RESPONSE_TIME`       SKIP must have
                                                          `response_time = 0`

  `validate_skip()`            `SKIP_ERROR`               SKIP must have
                                                          `error = None`
  -------------------------------------------------------------------------------

Each helper evaluates its own rule family and returns structured error
dictionaries. `semantic_validation()` aggregates those results and
calculates the overall summary.

------------------------------------------------------------------------

## 🔁 Duplicate Detection

Test IDs must be unique within a test run.

Duplicate detection is handled by `semantic_validation.py`.

The system maintains:

-   a set of IDs already seen
-   a list of duplicate occurrences
-   a duplicate count

For example:

``` text
TC001
TC002
TC001
```

produces:

``` text
duplicate_ids   = ["TC001"]
duplicate_count = 1
```

A duplicate ID is tracked separately from semantic rule violations.

------------------------------------------------------------------------

## 📦 Validation Result

Semantic validation returns a machine-readable result:

``` python
{
    "valid": False,
    "summary": {
        "total": 9,
        "passed": 3,
        "failed": 6,
        "error_count": 6,
        "duplicate_count": 1
    },
    "errors": [
        {
            "test_id": "TC002",
            "rule": "INVALID_STATUS",
            "message": "Status must be one of PASS, FAIL, or SKIP"
        }
    ],
    "duplicate_ids": ["TC005"]
}
```

### Summary Definitions

-   `total` --- number of test-case records processed.
-   `passed` --- test-case records with no semantic errors.
-   `failed` --- test-case records with one or more semantic errors.
-   `error_count` --- number of individual semantic error objects.
-   `duplicate_count` --- number of duplicate occurrences.
-   `valid` --- `True` only when there are no semantic errors and no
    duplicate IDs.

Important distinction:

``` text
failed      = failed test-case records
error_count = individual rule violations
```

One test case can therefore contribute one failed record and multiple
errors.

------------------------------------------------------------------------

## 🧪 Testing

TestFlow currently uses dedicated JSON fixtures under:

``` text
data/test_group/
```

### Test Groups

  Group   Purpose
  ------- -----------------------------------------
  A       Valid test cases
  B       Invalid status
  C       Negative response time
  D       Invalid PASS/error combination
  E       Invalid FAIL/error combination
  F       Invalid SKIP combinations
  G       Duplicate test IDs
  H       Multiple semantic errors + duplicate ID

### v0.1 Regression Result

All Groups **A--H** have been executed successfully after the
semantic-validation refactor.

Group H verifies combined behavior:

``` text
total           = 9
passed          = 3
failed          = 6
error_count     = 6
duplicate_count = 1
duplicate_ids   = ["TC005"]
valid           = False
```

Additional pipeline tests verified:

-   Valid input reaches semantic validation.
-   Structurally invalid input stops before semantic validation.
-   Missing files currently raise `FileNotFoundError`.
-   Malformed JSON currently raises `JSONDecodeError`.

------------------------------------------------------------------------

## ▶️ How to Run

### 1. Activate the virtual environment

On Windows PowerShell:

``` powershell
.venv\Scripts\Activate.ps1
```

### 2. Run the application

``` powershell
python main.py
```

### 3. Enter the JSON file path

Example:

``` text
Enter JSON File Path: data/test_group/group_a.json
```

The application then performs:

``` text
Input
  ↓
JSON Parsing
  ↓
Structural Validation
  ↓
Semantic Validation
  ↓
Result Output
```

------------------------------------------------------------------------

## 🛠️ Technologies

### Currently Used

-   Python 3
-   JSON
-   Git / GitHub

### Planned

-   pytest
-   SQLite
-   pandas
-   HTML/CSS
-   FastAPI
-   Data visualization
-   Statistical analysis

------------------------------------------------------------------------

## 🚧 Current Limitations

The current v0.1 release intentionally has a limited scope.

-   JSON is currently the primary input format.
-   Parser exceptions are not yet converted into user-friendly
    application errors.
-   There is no automated pytest suite yet.
-   There is no database or historical storage.
-   There is no performance analytics engine yet.
-   There is no risk-scoring engine yet.
-   There is no web dashboard.
-   There is no API.
-   The application currently uses a simple interactive file-path input.

These are planned future stages rather than missing requirements for
v0.1.

------------------------------------------------------------------------

## 🗺️ Roadmap

### v0.1 --- Basic Input + Validation Engine

**Status: ✅ Complete**

-   JSON input
-   Parser
-   Structural validation
-   Semantic validation
-   Duplicate detection
-   Structured results
-   Main pipeline
-   Regression testing

### v0.2 --- Test & Failure Analysis

**Planned**

-   Test result statistics
-   Failure categorization
-   Error analysis
-   Failure frequency
-   Execution summaries

### v0.3 --- Risk Detection

**Planned**

-   Risk rules
-   Risk scoring
-   High-risk test detection
-   Quality-risk analysis

### v1.0 --- Complete CLI

**Planned**

-   Improved command-line interface
-   User-friendly error handling
-   Report generation
-   Export functionality
-   Complete end-to-end workflow

### v1.5 --- Testing + OOP + Refactoring

**Planned**

-   pytest
-   Unit tests
-   Integration tests
-   Object-oriented design where appropriate
-   Maintainability improvements

### v2.0 --- Historical Analytics

**Planned**

-   SQLite
-   Test-run storage
-   Historical comparisons
-   Trend analysis
-   Regression-oriented analytics

### v3.0 --- Dashboard / Product Layer

**Planned**

-   Web dashboard
-   Charts
-   QA analytics visualization
-   API layer
-   Product-style interface

------------------------------------------------------------------------

## 📌 Development Method

TestFlow is developed incrementally:

``` text
Understand
    ↓
Design
    ↓
Implement
    ↓
Test
    ↓
Refactor
    ↓
Document
    ↓
Move to next version
```

This approach keeps each stage understandable and makes it possible to
verify one layer before adding the next.

------------------------------------------------------------------------

## 🎓 Project Scope

TestFlow combines concepts from:

-   Python programming
-   Software testing
-   QA engineering
-   Data validation
-   Data analysis
-   Software architecture
-   Error detection
-   Quality-risk analysis
-   Database systems
-   Reporting and visualization

The long-term objective is to evolve the current validation engine into
a complete QA analytics platform.

------------------------------------------------------------------------

## 📜 Version Milestones

  Version    Target
  ---------- ---------------------------------
  **v0.1**   Basic Input + Validation Engine
  **v0.2**   Test + Failure Analysis
  **v0.3**   Risk Detection Engine
  **v1.0**   Complete CLI
  **v1.5**   Testing + OOP + Refactoring
  **v2.0**   SQLite + Historical Analytics
  **v3.0**   Dashboard / Product Layer

------------------------------------------------------------------------

## 👨‍💻 Current Milestone

**TestFlow v0.1 --- Basic Input + Validation Engine**

The current version establishes the foundation for the future analytics
platform by providing:

``` text
Reliable Input
     ↓
Structural Validation
     ↓
Semantic Validation
     ↓
Duplicate Detection
     ↓
Structured QA Result
```

**Next major development target:** Test and Failure Analysis (`v0.2`).
