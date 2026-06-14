import pandas as pd


def test_dataframe_creation():
    data = {
        "service": ["API", "Database"],
        "status": ["Success", "Failed"]
    }

    df = pd.DataFrame(data)

    assert len(df) == 2
    assert "service" in df.columns
    assert "status" in df.columns


def test_success_failure_count():
    data = {
        "service": ["API", "API", "DB"],
        "status": ["Success", "Failed", "Success"]
    }

    df = pd.DataFrame(data)

    success = len(df[df["status"] == "Success"])
    failed = len(df[df["status"] == "Failed"])

    assert success == 2
    assert failed == 1