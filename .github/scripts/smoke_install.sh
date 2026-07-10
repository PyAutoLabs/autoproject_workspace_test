#!/usr/bin/env bash
# Workspace-owned install epilogue for the reusable Smoke Tests workflow.
# The template library's dependencies (autoconf, autofit) come from PyPI.
set -e

pip install ./PyAutoProject
