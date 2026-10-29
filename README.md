# File Integrity Monitoring System (FIM)

## Overview
A Python-based cybersecurity project that monitors file integrity using SHA-256 cryptographic hashes. It identifies modified, newly added, and deleted files by comparing current file hashes against a saved baseline.

## Features
- SHA-256 file hashing
- Baseline creation and storage in JSON format
- Detection of modified files
- Detection of newly added files
- Detection of deleted files
- Timestamped integrity reports
- Simple command-line interface

## Technologies
- Python 3
- hashlib
- os
- json
- datetime

## How to Run

```bash
python3 fim.py
```

## Usage
1. Select option 1 to create a baseline.
2. Add, modify, or delete files in `monitored_files/`.
3. Select option 2 to check file integrity.
4. Review the report for detected changes.

## Security Note
The baseline should be protected from unauthorized modification. This educational project demonstrates basic file integrity monitoring; it is not a replacement for a production security monitoring solution.

## Learning Outcomes
- Understanding SHA-256 hashing
- File integrity verification
- Detecting unauthorized file changes
- Basic Python automation for cybersecurity
