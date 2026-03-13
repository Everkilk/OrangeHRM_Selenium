from pathlib import Path
from datetime import datetime


def save_screenshot(driver, test_name: str) -> str:
    reports_dir = Path("reports/screenshots")
    reports_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{test_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    file_path = reports_dir / filename
    driver.save_screenshot(str(file_path))
    return str(file_path)
