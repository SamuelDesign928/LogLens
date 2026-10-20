# Development Prototypes

This directory contains small experimental projects developed while researching and building LogLens.

Each prototype explored a specific Python concept before its relevant functionality was incorporated into the main application. They are retained to demonstrate the development process and are not intended to be separate production applications.

## Prototypes
- **01 — Log Parser:** Splitting log lines into structured records.
- **02 — Log Statistics:** Practising severity counts, filtering, message frequencies and percentages.
- **03 — Command-Line Arguments:** Experimenting with `argparse`, including input filenames, severity filters and output filenames.

The main application is located in `src/loglens/` and combines these foundations into a single command-line tool.