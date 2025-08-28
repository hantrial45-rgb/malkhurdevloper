import platform
import os
from config import (
    DEVICE_TOKEN,
    DEVICE_TOKEN_SECRET,
    DEVICE_SECRET,
    SIGNATURE,
    CERTIFICATE,
    SAFETYNET
)


def get_system_info():
    return {
        "sdk": f"{platform.system()} {platform.release()}",
        "app_version": platform.version(),
        "device": platform.node(),
        "system_lang_code": os.getenv("LANG", "en-US") or "en-US"
    }
