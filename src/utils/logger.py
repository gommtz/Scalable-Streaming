from typing import Optional

colors = {
    "blue": "\033[34m",
    "green": "\033[32m",
    "red": "\033[91m",
    "yellow": "\033[33m",
    "cyan": "\033[36m",
    "magenta": "\033[35m",
    "white": "\033[37m",
    "bright_blue": "\033[94m",
    "bright_green": "\033[92m",
}  # Add other colors as needed


def colored_log(content, color: Optional[str] = "blue", flush: Optional[bool] = False):
    """Print logs in colors"""
    if color in colors:
        color_code = colors[color]
        print(color_code + "\033[1m" + content + "\033[0m", end="", flush=flush)
    else:
        print(content, end="", flush=flush)
