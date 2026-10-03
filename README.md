# TestFlow 🧪

> **Python QA Test Analytics & Validation System**

TestFlow is a Python-based project for validating and analyzing software test execution data. It currently focuses on reliable JSON input handling, structural validation, semantic/business-rule validation, duplicate detection, structured validation results, test-result analysis, failure categorization, failure statistics, performance analysis, and execution summaries.

The project is being developed incrementally so that each version adds a clear layer of functionality.

------------------------------------------------------------------------

## 📊 Project Progress

**Current Version: v0.2 --- Test & Failure Analysis**
**Current Phase: Phase C --- Test & Failure Analysis**
**Status: ✅ v0.2 functionality complete and tested**

| Area | Status | Documentation |
|---|---|---|
| Project setup | ✅ Complete | [Project Structure](#-project-structure) |
| Requirements & data contract | ✅ Complete | [Data Contract](#-data-contract) |
| JSON parser | ✅ Complete | [Parser](#-parser) |
| Structural validation | ✅ Complete | [Structural Validation](#-structural-validation) |
| Semantic validation | ✅ Complete | [Semantic Validation](#-semantic-validation) |
| Duplicate detection | ✅ Complete | [Duplicate Detection](#-duplicate-detection) |
| Main pipeline integration | ✅ Complete | [Application Flow](#-application-flow) |
| A–H regression testing | ✅ Complete | [Testing](#-testing) |
| Test result statistics | ✅ Complete | [Test Analysis](#-test-analysis) |
| Failure categorization | ✅ Complete | [Failure Analysis](#-failure-analysis) |
| Failure frequency | ✅ Complete | [Failure Analysis](#-failure-analysis) |
| Failure percentage analysis | ✅ Complete | [Failure Analysis](#-failure-analysis) |
| Dominant failure detection | ✅ Complete | [Failure Analysis](#-failure-analysis) |
| Performance analysis | ✅ Complete | [Performance Analysis](#-performance-analysis) |
| Execution summary | ✅ Complete | [Execution Summary](#-execution-summary) |
| Risk detection | ⏳ Planned | [Roadmap](#-roadmap) |
| Error handling improvements | ⏳ Planned | [Future Work](#-future-work) |
| pytest test suite | ⏳ Planned | [Roadmap](#-roadmap) |
| SQLite / historical analytics | ⏳ Planned | [Roadmap](#-roadmap) |
| Dashboard / API | ⏳ Planned | [Roadmap](#-roadmap) |

------------------------------------------------------------------------

## 🎯 Project Objective

TestFlow is intended to evolve from a simple validation utility into a QA analytics system that can answer questions such as:

- How many tests passed, failed, or were skipped?
- What percentage of tests passed or failed?
- Which tests are failing?
- What type of failures are occurring?
- Which failure categories occur repeatedly?
- What percentage of failures belong to each category?
- What is the dominant failure category?
- Which failure categories are tied for dominance?
- What are the average, minimum, and maximum response times?
- What was the overall execution status?
- Which areas have higher quality risk?
- How does test quality change across different test runs?

The current version establishes the **input, validation, analysis, and structured-result foundations** required for these later features.

------------------------------------------------------------------------

## 🔄 Application Flow

The current v0.2 pipeline is:

```text
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
  ├── Invalid ──► Stop + Return Validation Errors
  │
  └── Valid
        │
        ▼
Semantic Validation
        │
        ├── Invalid ──► Skip Analysis
        │
        └── Valid
              │
              ▼
        Test Analysis
              │
              ├── Test Statistics
              ├── Failure Categorization
              ├── Failure Frequency
              ├── Failure Percentage
              ├── Dominant Failure Detection
              ├── Performance Analysis
              └── Execution Summary
                    │
                    ▼
              Structured QA Result
```

### Separation of Responsibilities

| Component | Responsibility |
|---|---|
| `main.py` | Application orchestration and user input |
| `parser.py` | Reads and parses JSON |
| `validator.py` | Structural/type validation |
| `semantic_validation.py` | Semantic validation orchestration and result aggregation |
| `semantic_rules/` | Individual semantic rule validators |
| `analysis/` | Test-result analysis |
| `test_analysis.py` | Main analysis pipeline |
| `categorizing_failure.py` | Failure categorization logic |
| `output/` | Supporting output utilities |
| `data/` | Test and sample datasets |

------------------------------------------------------------------------

## 📁 Project Structure

```text
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
    ├── semantic_rules/
    │   ├── __init__.py
    │   ├── validate_status.py
    │   ├── validate_response_time.py
    │   ├── validate_pass.py
    │   ├── validate_fail.py
    │   └── validate_skip.py
    │
    └── analysis/
        ├── test_analysis.py
        └── categorizing_failure.py
```

------------------------------------------------------------------------

## 📄 Data Contract

TestFlow currently expects JSON data with the following structure:

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

### Root-Level Fields

| Field | Required | Type |
|---|---|---|
| `project` | Yes | String |
| `run_id` | Yes | String |
| `test_cases` | Yes | List |

### Test-Case Fields

| Field | Required | Type |
|---|---|---|
| `test_id` | Yes | String |
| `test_name` | Yes | String |
| `status` | Yes | String |
| `response_time` | Yes | Integer / Float |
| `error` | Yes | String / `null` |

------------------------------------------------------------------------

## 🔍 Structural Validation

Structural validation is implemented in:

```text
src/validator.py
```

It verifies:

- Root data is a dictionary.
- `project` exists and is a string.
- `run_id` exists and is a string.
- `test_cases` exists and is a list.
- Each test case is a dictionary.
- `test_id` exists and is a string.
- `test_name` exists and is a string.
- `status` exists and is a string.
- `response_time` exists and is numeric.
- `error` exists and is a string or `null`.

Structural validation does **not** perform business-rule validation.

If structural validation fails, the pipeline does not continue into semantic validation or test-result analysis.

------------------------------------------------------------------------

## 🧠 Semantic Validation

Semantic validation is implemented in:

```text
src/semantic_validation.py
```

Individual rules are separated into:

```text
src/semantic_rules/
```

### Rule Validators

| Validator | Rule | Requirement |
|---|---|---|
| `validate_status()` | `INVALID_STATUS` | Status must be `PASS`, `FAIL`, or `SKIP` |
| `validate_response_time()` | `NEGATIVE_RESPONSE_TIME` | Response time must be ≥ 0 |
| `validate_pass()` | `PASS_ERROR` | PASS must have `error = None` |
| `validate_fail()` | `FAIL_ERROR` | FAIL must contain an error message |
| `validate_skip()` | `SKIP_RESPONSE_TIME` | SKIP must have `response_time = 0` |
| `validate_skip()` | `SKIP_ERROR` | SKIP must have `error = None` |

Each helper evaluates its own rule family and returns structured error dictionaries. `semantic_validation()` aggregates those results and calculates the overall validation summary.

If semantic validation fails, the execution data is considered invalid for analytics and the test-analysis stage is skipped.

------------------------------------------------------------------------

## 🔁 Duplicate Detection

Test IDs must be unique within a test run.

Duplicate detection is handled by `semantic_validation.py`.

The system maintains:

- A set of IDs already seen.
- A list of duplicate occurrences.
- A duplicate count.

For example:

```text
TC001
TC002
TC001
```

produces:

```text
duplicate_ids   = ["TC001"]
duplicate_count = 1
```

A duplicate ID is tracked separately from semantic rule violations.

------------------------------------------------------------------------

## 📦 Validation Result

Semantic validation returns a machine-readable result:

```python
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

- `total` — number of test-case records processed.
- `passed` — test-case records with no semantic errors.
- `failed` — test-case records with one or more semantic errors.
- `error_count` — number of individual semantic error objects.
- `duplicate_count` — number of duplicate occurrences.
- `valid` — `True` only when there are no semantic errors and no duplicate IDs.

Important distinction:

```text
failed      = failed test-case records
error_count = individual rule violations
```

One test case can therefore contribute one failed record and multiple errors.

------------------------------------------------------------------------

## 📊 Test Analysis

Test-result analysis is implemented in:

```text
src/analysis/test_analysis.py
```

The main analysis function processes valid test execution data and produces a structured analysis result.

The analysis currently contains:

```text
summary
status_distribution
failure_analysis
performance_analysis
execution_summary
```

### Summary

The `summary` section contains:

- Total tests
- Passed tests
- Failed tests
- Skipped tests
- Pass percentage
- Fail percentage
- Skip percentage

Example:

```text
total           = 10
passed          = 5
failed          = 4
skipped         = 1

pass_percentage = 50.0
fail_percentage = 40.0
skip_percentage = 10.0
```

### Status Distribution

The `status_distribution` section provides a direct count of each execution status:

```text
PASS
FAIL
SKIP
```

Example:

```text
PASS = 5
FAIL = 4
SKIP = 1
```

------------------------------------------------------------------------

## 🔎 Failure Analysis

Failure categorization is implemented in:

```text
src/analysis/categorizing_failure.py
```

The categorization logic analyzes the error message of failed tests and assigns a failure category.

Current categories:

```text
TIMEOUT
AUTHENTICATION
PAYMENT
OTHER
```

### Failure Categorization

Examples:

```text
"Product service timeout"
        ↓
TIMEOUT
```

```text
"Authentication service unavailable"
        ↓
AUTHENTICATION
```

```text
"Payment gateway unavailable"
        ↓
PAYMENT
```

Errors that do not match the currently defined categories are assigned:

```text
OTHER
```

Each categorized failure preserves:

- `test_id`
- `test_name`
- `error`
- `category`

Example:

```json
{
  "test_id": "TC004",
  "test_name": "Add Product to Cart",
  "error": "Product service timeout",
  "category": "TIMEOUT"
}
```

### Failure Frequency

TestFlow counts how frequently each failure category occurs.

Example:

```text
TIMEOUT         = 3
AUTHENTICATION  = 1
PAYMENT         = 0
OTHER           = 0
```

The total frequency of all failure categories corresponds to the total number of failed tests.

### Failure Percentage

TestFlow calculates the percentage distribution of failure categories relative to all failed tests.

For example:

```text
Total failed tests = 4

TIMEOUT        = 3 → 75.0%
AUTHENTICATION = 1 → 25.0%
PAYMENT        = 0 → 0.0%
OTHER          = 0 → 0.0%
```

This allows the system to identify not only how many failures occurred, but also how failures are distributed across categories.

### Dominant Failure

TestFlow identifies the category or categories with the highest failure frequency.

The result is stored as a list so that ties are preserved.

Example:

```text
TIMEOUT = 3
PAYMENT = 3
AUTHENTICATION = 1
OTHER = 0
```

produces:

```text
failure_dominance = ["TIMEOUT", "PAYMENT"]
```

This tie-aware structure is intentionally used so future failure categories can be added without redesigning the result format.

------------------------------------------------------------------------

## ⚡ Performance Analysis

TestFlow also analyzes response-time information for non-skipped tests.

The current performance analysis contains:

```text
average_response_time
min_response_time
max_response_time
```

### Average Response Time

The average is calculated using all non-skipped test executions.

### Minimum Response Time

The lowest response time among non-skipped tests.

### Maximum Response Time

The highest response time among non-skipped tests.

Skipped tests are excluded from performance calculations because their response time is expected to be `0` and does not represent an actual execution.

Example:

```text
average_response_time = 376.67
min_response_time     = 90
max_response_time     = 850
```

------------------------------------------------------------------------

## 📋 Execution Summary

The execution summary provides a compact high-level representation of the complete analysis.

It contains:

```text
execution_status
total_tests
passed_tests
failed_tests
skipped_tests
pass_rate
fail_rate
skip_rate
dominant_failure
average_response_time
```

### Execution Status

The current execution-status rules are:

```text
NO_TESTS
    ↓
No test cases were executed.

FAILED
    ↓
At least one test failed.

PASSED_WITH_SKIPS
    ↓
No tests failed, but one or more tests were skipped.

PASSED
    ↓
All executed tests passed.
```

The execution summary is part of the same structured analysis result rather than being returned as a completely separate result.

This keeps the complete analytical output available through one result object while still separating the detailed analysis sections from the high-level execution summary.

------------------------------------------------------------------------

## 🧪 Testing

TestFlow currently uses dedicated JSON fixtures under:

```text
data/test_group/
```

### Test Groups

| Group | Purpose |
|---|---|
| A | Valid test cases |
| B | Invalid status |
| C | Negative response time |
| D | Invalid PASS/error combination |
| E | Invalid FAIL/error combination |
| F | Invalid SKIP combinations |
| G | Duplicate test IDs |
| H | Multiple semantic errors + duplicate ID |

### v0.1 Regression Result

All Groups **A–H** have been executed successfully after the semantic-validation refactor.

Group H verifies combined behavior:

```text
total           = 9
passed          = 3
failed          = 6
error_count     = 6
duplicate_count = 1
duplicate_ids   = ["TC005"]
valid           = False
```

Additional pipeline tests verified:

- Valid input reaches semantic validation.
- Structurally invalid input stops before semantic validation.
- Missing files currently raise `FileNotFoundError`.
- Malformed JSON currently raises `JSONDecodeError`.

### v0.2 Analysis Testing

The v0.2 analysis engine has been tested against multiple datasets covering:

- All-pass executions.
- Failed executions.
- Skipped executions.
- Multiple failure categories.
- Repeated failure categories.
- Failure-category frequency calculations.
- Failure percentage calculations.
- Dominant failure detection.
- Tied dominant failure categories.
- Performance calculations.
- Complete execution summaries.
- Zero-failure executions.
- Zero-test executions.
- Invalid structural input.
- Invalid semantic input.

The analysis output was verified against expected results before completing v0.2.

------------------------------------------------------------------------

## ▶️ How to Run

### 1. Activate the virtual environment

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 2. Run the application

```powershell
python main.py
```

### 3. Enter the JSON file path

Example:

```text
Enter JSON File Path: data/test_group/group_a.json
```

The application then performs:

```text
Input
  ↓
JSON Parsing
  ↓
Structural Validation
  ↓
Semantic Validation
  ↓
Test Analysis
  ↓
Failure Analysis
  ↓
Performance Analysis
  ↓
Execution Summary
  ↓
Result Output
```

Invalid structural input stops before the analysis layer.

Invalid semantic input is rejected before test-result analytics are performed.

------------------------------------------------------------------------

## 🛠️ Technologies

### Currently Used

- Python 3
- JSON
- Git / GitHub

### Planned

- pytest
- SQLite
- pandas
- HTML/CSS
- FastAPI
- Data visualization
- Statistical analysis

------------------------------------------------------------------------

## 🚧 Current Limitations

The current v0.2 release intentionally has a limited scope.

- JSON is currently the primary input format.
- Parser exceptions are not yet converted into fully user-friendly application errors.
- There is no automated pytest suite yet.
- Failure categorization currently uses rule-based keyword matching.
- Failure categories are currently predefined.
- Historical test-run storage is not implemented.
- There is no risk-scoring engine yet.
- There is no web dashboard.
- There is no API.
- The application currently uses a simple interactive file-path input.
- Analysis is currently performed on valid execution data after validation.
- Historical comparison between different test runs is not yet available.

These are planned future stages rather than missing requirements for v0.2.

------------------------------------------------------------------------

## 🗺️ Roadmap

### v0.1 --- Basic Input + Validation Engine

**Status: ✅ Complete**

- JSON input
- Parser
- Structural validation
- Semantic validation
- Duplicate detection
- Structured results
- Main pipeline
- Regression testing

### v0.2 --- Test & Failure Analysis

**Status: ✅ Complete**

- Test result statistics
- Failure categorization
- Error analysis
- Failure frequency
- Failure percentage analysis
- Dominant failure detection
- Tie-aware dominant failure handling
- Performance analysis
- Execution summaries
- Analysis result integration with the main pipeline
- Multiple-dataset validation

### v0.3 --- Risk Detection

**Planned**

- Risk rules
- Risk scoring
- High-risk test detection
- Quality-risk analysis

### v1.0 --- Complete CLI

**Planned**

- Improved command-line interface
- User-friendly error handling
- Report generation
- Export functionality
- Complete end-to-end workflow

### v1.5 --- Testing + OOP + Refactoring

**Planned**

- pytest
- Unit tests
- Integration tests
- Object-oriented design where appropriate
- Maintainability improvements

### v2.0 --- Historical Analytics

**Planned**

- SQLite
- Test-run storage
- Historical comparisons
- Trend analysis
- Regression-oriented analytics

### v3.0 --- Dashboard / Product Layer

**Planned**

- Web dashboard
- Charts
- QA analytics visualization
- API layer
- Product-style interface

------------------------------------------------------------------------

## 📌 Development Method

TestFlow is developed incrementally:

```text
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

This approach keeps each stage understandable and makes it possible to verify one layer before adding the next.

Each version is treated as a functional milestone rather than simply adding isolated features.

------------------------------------------------------------------------

## 🎓 Project Scope

TestFlow combines concepts from:

- Python programming
- Software testing
- QA engineering
- Data validation
- Data analysis
- Software architecture
- Error detection
- Quality-risk analysis
- Database systems
- Reporting and visualization

The long-term objective is to evolve the current validation and analysis engine into a complete QA analytics platform.

------------------------------------------------------------------------

## 📜 Version Milestones

| Version | Target |
|---|---|
| **v0.1** | Basic Input + Validation Engine |
| **v0.2** | Test + Failure Analysis |
| **v0.3** | Risk Detection Engine |
| **v1.0** | Complete CLI |
| **v1.5** | Testing + OOP + Refactoring |
| **v2.0** | SQLite + Historical Analytics |
| **v3.0** | Dashboard / Product Layer |

------------------------------------------------------------------------

## 👨‍💻 Current Milestone

**TestFlow v0.2 --- Test & Failure Analysis**

The current version builds on the v0.1 validation foundation and adds an analytical layer:

```text
Reliable Input
      ↓
Structural Validation
      ↓
Semantic Validation
      ↓
Duplicate Detection
      ↓
Validated Test Execution Data
      ↓
Test Statistics
      ↓
Failure Categorization
      ↓
Failure Frequency & Percentage
      ↓
Dominant Failure Detection
      ↓
Performance Analysis
      ↓
Execution Summary
      ↓
Structured QA Analysis Result
```

The v0.2 engine can now transform validated test execution data into structured analytical information that can later be consumed by the risk-detection, reporting, historical-analytics, and dashboard layers.

**Next major development target:** Risk Detection (`v0.3`).