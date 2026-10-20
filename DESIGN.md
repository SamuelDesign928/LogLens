# LogLens — Design Document

## 1. Overview

LogLens is a local Python command-line application for analysing log files. Its purpose is to help users extract useful information from log entries without manually reading every line.

The project will focus on a clear structure, reusable functions, predictable behaviour and meaningful error handling. It will initially support a defined log format rather than attempting to parse every possible format.

## 2. Problem Statement

Log files can contain many entries, making it time-consuming to identify errors, understand how frequently particular events occur and investigate recurring problems.

LogLens aims to simplify this initial analysis by converting raw log lines into structured records and using those records to produce summaries and filtered results.

## 3. Intended Users

Potential users include:

- **Developers** investigating errors produced by their applications.
- **IT support staff** reviewing logs while troubleshooting issues.
- **Students and learners** exploring log analysis, file handling and command-line application development.

The initial project is a small offline tool. It is not intended to replace professional logging, monitoring or security information and event management (SIEM) systems.

## 4. Scope

### Included in the Initial Version

- Reading a user-specified log file.
- Parsing supported log entries.
- Counting entries by severity level.
- Filtering entries by severity.
- Identifying frequent messages and calculating basic statistics.
- Displaying results in the terminal.
- Optionally exporting a report.
- Validating command-line arguments and handling common errors.
- Automated tests for important functionality.

### Outside the Initial Scope

- Real-time log monitoring.
- Automatically collecting logs from other machines.
- Cloud services or external APIs.
- Machine learning or AI-based anomaly detection.
- Support for every application-specific log format.
- A graphical user interface.

These boundaries keep the first version achievable while leaving room for future improvements.

## 5. Input Format

The initial parser will use log entries following this general structure:

`YYYY-MM-DD HH:MM:SS LEVEL Message text`

For example:

`2026-10-12 09:00:08 ERROR Database connection failed`

A successfully parsed entry should contain three fields:

- **Timestamp:** when the event occurred.
- **Level:** the severity of the entry, such as `INFO`, `WARNING` or `ERROR`.
- **Message:** the descriptive text associated with the event.

The parser should distinguish valid entries from malformed lines. The exact behaviour for malformed entries, including whether they are skipped or reported, will be decided during implementation and documented once tested.

## 6. Planned Architecture

The application will be organised into separate modules, each responsible for a particular part of the workflow.

| Module | Responsibility |
|---|---|
| `parser.py` | Convert raw log lines into structured records and handle malformed entries. |
| `analyzer.py` | Calculate counts, percentages, message frequencies and other statistics. |
| `reporter.py` | Format results for display or export them to a file. |
| `cli.py` | Define command-line arguments and coordinate the application. |
| `__main__.py` | Provide an entry point for running the application as a Python module. |
| `__init__.py` | Mark the package and hold package-level information if needed. |

The `tests/` directory will contain automated tests for the main parsing, analysis and reporting behaviour.

The `prototypes/` directory will retain the smaller experiments that informed the implementation.

## 7. Processing Workflow

The intended workflow is:

1. The user supplies an input filename and any optional command-line arguments.
2. The application validates the arguments and checks whether the input can be read.
3. The parser reads and interprets the log entries.
4. The analyser processes the structured entries and calculates the requested statistics.
5. The reporter presents the results in the terminal or writes them to an optional output file.
6. The application exits with an appropriate status, including a useful error message if the operation fails.

The implementation may refine these steps as practical requirements become clearer.

## 8. Error Handling

The application should handle common problems without producing confusing tracebacks for ordinary user mistakes.

Examples include:

- The input file does not exist.
- The input path points to a directory rather than a file.
- The file cannot be read because of permissions or an I/O error.
- A log entry does not match the supported format.
- The user supplies an unsupported severity level.
- The output file cannot be written.

Malformed log entries should not silently become incorrect records. The chosen approach should be consistent and covered by tests.

## 9. Design Principles

The implementation will follow these principles:

- **Separation of concerns:** parsing, analysis, reporting and command-line handling should have distinct responsibilities.
- **Reusability:** core functions should be usable independently of the command-line interface.
- **Standard library first:** avoid third-party dependencies unless they provide a clear benefit.
- **Readable code:** favour clear names, small functions and straightforward logic.
- **Testability:** make core behaviour easy to test using controlled input.
- **Useful error messages:** explain what went wrong and, where possible, how the user can correct it.
- **Scope control:** prioritise a reliable core application over unnecessary features.

## 10. Testing Strategy

Testing will focus on the behaviour most important to the application.

- Valid log lines produce the expected structured records.
- Malformed lines are handled according to the documented policy.
- Severity counts and other statistics are correct for known input.
- Empty input does not cause division errors or misleading results.
- Command-line arguments accept valid values and reject invalid ones.
- File and report-writing errors are handled appropriately.

Tests will use small, predictable sample files and data so that expected results can be checked easily.

## 11. Development and Version Control

Development will proceed in stages, using small prototypes to investigate individual Python concepts before integrating them into the main application.

Git will be used to track changes. Commits should represent meaningful steps, and the repository will retain the prototypes as a record of the development process.

## 12. Known Limitations and Future Work

The first version will support a defined log format and a limited set of analysis features. Different applications may use different timestamps, severity labels, multiline messages or entirely different structures.

Future improvements could include configurable formats, date-range filtering, more report formats, performance improvements for large files and additional analysis features.

Any expansion will depend on the reliability and usefulness of the initial implementation.