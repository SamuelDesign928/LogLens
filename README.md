# LogLens — Log File Analyser

LogLens is a Python command-line tool designed to read, parse and analyse log files. It aims to make it easier to identify errors, understand log activity and summarise important information without manually searching through large files.

The project is being developed as a learning exercise, with an emphasis on Python fundamentals, readable code, error handling and practical software development.

## Planned Features

- Read log files from a specified path.
- Parse log entries into structured records containing a timestamp, severity level and message.
- Summarise log activity, including total entries and counts by severity.
- Filter entries by severity level.
- Identify frequent log messages and calculate basic statistics.
- Display results in the terminal.
- Optionally save a report to a file.
- Handle invalid input and malformed log entries where practical.

*Features will be added and documented as development progresses.*

## Technologies

- **Python 3.12+** — main programming language.
- **Standard library** — including `pathlib`, `argparse`, `collections` and `unittest`, where appropriate.
- **Git and GitHub** — version control and project documentation.

The initial version is intended to work locally without external APIs or paid services.

## Getting Started

### Requirements

- Python 3.12 or later.
- Git is optional if you only want to download and run the project.

### Running the Project

The command-line interface and its final commands will be documented here once the main application is implemented.

During development, the experimental scripts in `prototypes/` can be run independently. Each prototype has its own purpose and may have different input requirements.

## Example Use Case

A developer investigating an application issue could use LogLens to analyse a log file and quickly see:

- How many entries were recorded.
- How many errors and warnings occurred.
- Which error messages appeared most frequently.
- Which entries match a selected severity level.

The goal is to make initial investigation easier, not to replace a full monitoring or observability platform.

## Repository Structure

- `src/loglens/` — main application code.
- `tests/` — automated tests.
- `sample_logs/` — example log files for testing.
- `prototypes/` — smaller experiments created while learning the concepts used in the application.
- `docs/DESIGN.md` — design decisions and planned architecture.
- `reports/` — location for generated reports or report examples.

## Development Approach

LogLens is being developed in stages. Small prototypes are used to explore individual concepts before they are incorporated into the main application. The finished application will bring these ideas together into a more organised, tested command-line tool.

## Limitations

The initial version will focus on supported, consistently formatted log entries. Log formats vary between applications, so compatibility with different formats will depend on the parser's design. LogLens is intended as a local analysis tool rather than a real-time monitoring system.

## Future Improvements

Possible improvements include support for additional log formats, more detailed filtering, richer reports and improved handling of malformed entries. These will be considered once the core functionality is complete.

## Licence

See `LICENSE` for the project's licence.