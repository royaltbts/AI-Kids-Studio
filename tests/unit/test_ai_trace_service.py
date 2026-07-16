"""
Tests for AITraceService.
"""

import json

from backend.app.services.ai_trace_service import AITraceService


def test_ai_trace_service(tmp_path):
    """
    Verify prompts, responses and validated JSON are written.
    """

    trace = AITraceService(tmp_path)

    trace.save_prompt(
        "lesson",
        "Lesson prompt",
    )

    trace.save_response(
        "lesson",
        '{"title":"ABC"}',
    )

    trace.save_validated(
        "lesson",
        json.dumps(
            {
                "title": "ABC",
            },
            indent=2,
        ),
    )

    assert (tmp_path / "prompts" / "lesson.txt").exists()

    assert (tmp_path / "responses" / "lesson.json").exists()

    assert (tmp_path / "validated" / "lesson.json").exists()
