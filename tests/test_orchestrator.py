from types import SimpleNamespace

from src.orchestrator import HorizonOrchestrator


def _make_orchestrator(timezone="UTC") -> HorizonOrchestrator:
    config = SimpleNamespace(email=None, webhook=None, timezone=timezone)
    storage = SimpleNamespace()
    return HorizonOrchestrator(config, storage)


def test_run_label_is_normalized_for_same_day_archive_keys():
    orchestrator = _make_orchestrator()

    today, summary_key, display_date, normalized = orchestrator._build_run_context(
        "Afternoon Push"
    )

    assert normalized == "afternoon-push"
    assert summary_key == f"{today}-afternoon-push"
    assert display_date == f"{today} afternoon-push"


def test_empty_run_label_preserves_daily_archive_key():
    orchestrator = _make_orchestrator()

    today, summary_key, display_date, normalized = orchestrator._build_run_context()

    assert normalized == ""
    assert summary_key == today
    assert display_date == today
