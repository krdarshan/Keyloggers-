import os
import logging
from keylogger.main import on_press

def test_on_press_writes_log(tmp_path):
    testlog = tmp_path / "testlog.txt"
    
    logger = logging.getLogger()
    logger.handlers.clear()  # Clear any previous handlers
    handler = logging.FileHandler(testlog, mode='w')
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    on_press(type("K", (), {"char": "a"}))
    on_press(type("Special", (), {"name": "space"}))

    handler.flush()  # Force flush to disk
    logger.removeHandler(handler)

    content = testlog.read_text()
    assert content.startswith("a[space]") or content.replace("\n", "").startswith("a[space]")
