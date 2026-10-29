import os
import json
import hashlib
from datetime import datetime

BASELINE_FILE = "baseline.json"
MONITOR_DIR = "monitored_files"


def calculate_hash(filepath):
    sha256 = hashlib.sha256()

    with open(filepath, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def scan_files():
    results = {}

    for root, _, files in os.walk(MONITOR_DIR):
        for filename in files:
            filepath = os.path.join(root, filename)

            if os.path.isfile(filepath):
                relative_path = os.path.relpath(filepath, MONITOR_DIR)

                try:
                    results[relative_path] = calculate_hash(filepath)
                except OSError as error:
                    print(f"Could not read {filepath}: {error}")

    return results


def save_baseline():
    current_files = scan_files()

    with open(BASELINE_FILE, "w") as file:
        json.dump(current_files, file, indent=4)

    print(f"Baseline created: {len(current_files)} file(s).")


def check_integrity():
    if not os.path.exists(BASELINE_FILE):
        print("No baseline found. Create one first.")
        return

    with open(BASELINE_FILE, "r") as file:
        baseline = json.load(file)

    current = scan_files()

    added = current.keys() - baseline.keys()
    deleted = baseline.keys() - current.keys()
    modified = {
        path for path in current.keys() & baseline.keys()
        if current[path] != baseline[path]
    }

    print("\n--- FILE INTEGRITY REPORT ---")
    print("Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    for path in sorted(added):
        print("[NEW FILE]", path)

    for path in sorted(modified):
        print("[MODIFIED]", path)

    for path in sorted(deleted):
        print("[DELETED]", path)

    if not added and not modified and not deleted:
        print("No changes detected.")

    print("\nSummary:")
    print("New:", len(added))
    print("Modified:", len(modified))
    print("Deleted:", len(deleted))


def main():
    os.makedirs(MONITOR_DIR, exist_ok=True)

    while True:
        print("\n=== FILE INTEGRITY MONITOR ===")
        print("1. Create baseline")
        print("2. Check file integrity")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            save_baseline()
        elif choice == "2":
            check_integrity()
        elif choice == "3":
            print("Exiting.")
            break
        else:
            print("Invalid option. Choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
