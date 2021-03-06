from os import path
from selenium.webdriver.chrome.options import Options

from django.utils import timezone
from django.core.exceptions import ValidationError

CODE = """
{0}
"""

IMAGE_FILE_TYPES = ["jpeg", "jpg", "png", "bmp"]

DEFAULT_HEADER = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
    "AppleWebKit/537.11 (KHTML, like Gecko) "
    "Chrome/23.0.1271.64 Safari/537.11",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "Accept-Encoding": "none",
    "Accept-Language": "en-US,en;q=0.8",
    "Connection": "keep-alive",
}


def is_image(ext):
    if ext.lower() not in IMAGE_FILE_TYPES:
        raise ValidationError("unknown file format")
    return True


def report_image_path(instance, filename):
    ext = filename.split(".")[-1].lower()
    if is_image(ext):
        return path.join(
            ".",
            "report",
            "images",
            "{}.{}".format(int(timezone.now().timestamp()), ext),
        )


def get_browser_options():
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--enable-automation")
    options.add_argument("--no-sandbox")
    return options
