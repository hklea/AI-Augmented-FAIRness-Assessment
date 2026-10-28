"""FastAPI app for the FAIRness assessment demo.

Serves two things:
- A JSON API (/api/*) wrapping the existing scoring code in code/src.
- The static frontend (code/web/frontend).

Run from the project root with:
    python code/web/backend/main.py
"""

from __future__ import annotations

import sys
from pathlib import Path

BACKEND_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BACKEND_DIR.parents[2]
SRC_DIR = PROJECT_ROOT / "code" / "src"
FRONTEND_DIR = BACKEND_DIR.parent / "frontend"

# code/src has no top-level package init (its modules are used as scripts
# elsewhere in the project), so it's added to sys.path directly rather than
# imported as a package.
sys.path.insert(0, str(SRC_DIR))
sys.path.insert(0, str(BACKEND_DIR))

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Literal
from models import LLAMA

import dataset_overview
import live_assessment

app = FastAPI(title="FAIRness Assessment Demo")


class AssessRequest(BaseModel):
    repo: str
    run_llm: bool = True
    model: Literal["llama3.1:8b", "Qwen3.6-35B-A3B-MLX-8bit"] = LLAMA


@app.get("/api/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/api/overview")
def overview(model: str = LLAMA) -> dict:
    try:
        return dataset_overview.get_overview(model)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@app.get("/api/models")
def models():
    return live_assessment.model_availability()


@app.get("/api/languages")
def languages(cohort: Literal["full", "hybrid"] = "full") -> dict:
    return dataset_overview.language_groups(cohort)


@app.get("/api/comparison")
def comparison(annotator: int = 1, subset: str = "all"):
    try:
        return dataset_overview.model_comparison_metrics(annotator, subset)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@app.get("/api/comparison/{repo_id}")
def compare_repository(repo_id: str):
    report = dataset_overview.compare_report(repo_id)
    if report is None:
        raise HTTPException(status_code=404, detail="Saved comparison not found.")
    return report


@app.post("/api/assess")
def assess(request: AssessRequest) -> dict:
    try:
        return live_assessment.assess_repo_live(
            request.repo, run_llm_scoring=request.run_llm, model=request.model
        )
    except live_assessment.InvalidRepoInputError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except live_assessment.RepoNotFoundError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except RuntimeError as error:
        raise HTTPException(status_code=502, detail=str(error))


@app.get("/api/repositories/{repo_id}")
def repository(repo_id: str, cohort: str = "hybrid", model: str = LLAMA) -> dict:
    try:
        result = dataset_overview.saved_report(repo_id, cohort, model)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    if result is None:
        raise HTTPException(status_code=404, detail="Saved repository report not found.")
    return result


app.mount("/", StaticFiles(directory=str(FRONTEND_DIR), html=True), name="frontend")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, app_dir=str(BACKEND_DIR))
