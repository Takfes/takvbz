#!/usr/bin/env python
from __future__ import annotations

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(filepath: str) -> None:
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))


def move_file(filepath: str, target: str) -> None:
    os.rename(
        os.path.join(PROJECT_DIRECTORY, filepath),
        os.path.join(PROJECT_DIRECTORY, target),
    )


def move_dir(src: str, target: str) -> None:
    shutil.move(
        os.path.join(PROJECT_DIRECTORY, src), os.path.join(PROJECT_DIRECTORY, target)
    )


def check_nodejs_availability() -> bool:
    """Check if Node.js is available for MCP servers"""
    return shutil.which("node") is not None


if __name__ == "__main__":
    # Handle .github directory based on what features are enabled
    github_actions_enabled = "{{cookiecutter.include_github_actions}}" == "y"
    vibecoding_enabled = "{{cookiecutter.include_vibecoding}}" == "y"

    if not github_actions_enabled and not vibecoding_enabled:
        # Remove entire .github directory if neither feature is enabled
        remove_dir(".github")
    elif not github_actions_enabled and vibecoding_enabled:
        # Keep .github for vibecoding, but remove workflows
        remove_dir(".github/workflows")
        remove_dir(".github/actions")
    elif github_actions_enabled:
        # GitHub Actions enabled - handle selective workflow removal
        if (
            "{{cookiecutter.mkdocs}}" != "y"
            and "{{cookiecutter.publish_to_pypi}}" == "n"
        ):
            remove_file(".github/workflows/on-release-main.yml")

    # Clean up vibecoding files if vibecoding is disabled (but .github directory exists)
    if "{{cookiecutter.include_vibecoding}}" != "y" and os.path.exists(".github"):
        if os.path.exists(".github/copilot-instructions.md"):
            remove_file(".github/copilot-instructions.md")
        if os.path.exists(".github/instructions"):
            remove_dir(".github/instructions")
        if os.path.exists(".github/prompts"):
            remove_dir(".github/prompts")

    if "{{cookiecutter.mkdocs}}" != "y":
        remove_dir("docs")
        remove_file("mkdocs.yml")

    if "{{cookiecutter.dockerfile}}" != "y":
        remove_file("Dockerfile")

    if "{{cookiecutter.codecov}}" != "y":
        remove_file("codecov.yaml")
        if "{{cookiecutter.include_github_actions}}" == "y":
            remove_file(".github/workflows/validate-codecov-config.yml")

    if "{{cookiecutter.devcontainer}}" != "y":
        remove_dir(".devcontainer")

    # ========================================
    # Handle MCP configuration FIRST (before VSCode settings)
    # ========================================
    if "{{cookiecutter.include_mcp_config}}" != "y":
        # Remove MCP-related files if MCP is disabled
        if os.path.exists(".vscode/mcp.json"):
            remove_file(".vscode/mcp.json")
        if os.path.exists(".env.template"):
            remove_file(".env.template")
        if os.path.exists("docs/mcp_setup.md"):
            remove_file("docs/mcp_setup.md")
    else:
        # MCP is enabled - check Node.js availability
        if not check_nodejs_availability():
            print("⚠️  Node.js not detected. Some MCP servers require Node.js.")
            print("📖 See docs/mcp_setup.md for installation instructions.")

    # ========================================
    # Handle VSCode settings with granular approach
    # ========================================
    if "{{cookiecutter.include_vscode_settings}}" != "y":
        # Remove only VSCode settings files, preserve .vscode directory for potential MCP files
        if os.path.exists(".vscode/settings.json"):
            remove_file(".vscode/settings.json")

    # ========================================
    # Clean up empty .vscode directory
    # ========================================
    if os.path.exists(".vscode") and not os.listdir(".vscode"):
        remove_dir(".vscode")

    if "{{cookiecutter.open_source_license}}" == "MIT license":
        move_file("LICENSE_MIT", "LICENSE")
        remove_file("LICENSE_BSD")
        remove_file("LICENSE_ISC")
        remove_file("LICENSE_APACHE")
        remove_file("LICENSE_GPL")

    if "{{cookiecutter.open_source_license}}" == "BSD license":
        move_file("LICENSE_BSD", "LICENSE")
        remove_file("LICENSE_MIT")
        remove_file("LICENSE_ISC")
        remove_file("LICENSE_APACHE")
        remove_file("LICENSE_GPL")

    if "{{cookiecutter.open_source_license}}" == "ISC license":
        move_file("LICENSE_ISC", "LICENSE")
        remove_file("LICENSE_MIT")
        remove_file("LICENSE_BSD")
        remove_file("LICENSE_APACHE")
        remove_file("LICENSE_GPL")

    if "{{cookiecutter.open_source_license}}" == "Apache Software License 2.0":
        move_file("LICENSE_APACHE", "LICENSE")
        remove_file("LICENSE_MIT")
        remove_file("LICENSE_BSD")
        remove_file("LICENSE_ISC")
        remove_file("LICENSE_GPL")

    if "{{cookiecutter.open_source_license}}" == "GNU General Public License v3":
        move_file("LICENSE_GPL", "LICENSE")
        remove_file("LICENSE_MIT")
        remove_file("LICENSE_BSD")
        remove_file("LICENSE_ISC")
        remove_file("LICENSE_APACHE")

    if "{{cookiecutter.open_source_license}}" == "Not open source":
        remove_file("LICENSE_GPL")
        remove_file("LICENSE_MIT")
        remove_file("LICENSE_BSD")
        remove_file("LICENSE_ISC")
        remove_file("LICENSE_APACHE")

    if "{{cookiecutter.layout}}" == "src":
        project_slug = "{{cookiecutter.project_slug}}"

        # Handle edge case where project_slug is "src" - avoid moving src into src/src
        if project_slug == "src":
            # Rename the existing src directory temporarily
            if os.path.exists("src"):
                temp_name = "temp_src_package"
                os.rename("src", temp_name)
                os.makedirs("src")
                move_dir(temp_name, os.path.join("src", project_slug))
        else:
            # Normal case: create src directory if needed and move package into it
            if not os.path.exists("src"):
                os.makedirs("src")
            if os.path.exists(project_slug):
                move_dir(project_slug, os.path.join("src", project_slug))
