#!/usr/bin/env bash
cd /workspace
uvicorn main:app --host 0.0.0.0 --port 8000
