from datetime import datetime
import re
from html import unescape


def format_posted_date(iso_date):
    if not iso_date:
        return "-"
    try:
        dt = datetime.fromisoformat(iso_date.replace("Z", "+00:00"))
        return dt.strftime("%d/%m/%Y")
    except Exception:
        return "-"


def format_epoch_date(epoch):
    if not epoch:
        return "-"
    try:
        dt = datetime.fromtimestamp(epoch)
        return dt.strftime("%d/%m/%Y")
    except Exception:
        return "-"


def clean_description(html_text):
    if not html_text:
        return "-"

    text = unescape(html_text)
    text = re.sub(r"<br\s*/?>", "\n", text)
    text = re.sub(r"</p>", "\n\n", text)
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"\n\s*\n\s*\n+", "\n\n", text)
    return text.strip()