import os
from reviewer.static_checker import run_static_checks
from reviewer.llm_reviewer import review_code_with_llm
from reviewer.refactorer import generate_refactor_patch
from utils.file_loader import load_code_files

PROJECT_PATH = "./target_project"

def main():
    files = load_code_files(PROJECT_PATH)

    for file_path, code in files.items():
        print(f"\n🔍 Reviewing: {file_path}")

        static_issues = run_static_checks(code)
        llm_feedback = review_code_with_llm(code)
        patch = generate_refactor_patch(code, llm_feedback)

        print("\n=== Static Issues ===")
        print(static_issues)

        print("\n=== LLM Review ===")
        print(llm_feedback)

        print("\n=== Suggested Patch ===")
        print(patch)

if __name__ == "__main__":
    main()
