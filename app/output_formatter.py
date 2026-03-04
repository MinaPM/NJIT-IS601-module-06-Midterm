import colorama
from colorama import Fore, Back, Style
from enum import Enum

colorama.init()


colorama.init()


class OutputFormatter:
    """Utility class for formatting console output with colors and styles using colorama."""

    ERROR_STYLE = (Fore.RED,    Style.BRIGHT)
    SUCCESS_STYLE = (Fore.GREEN,  Style.BRIGHT)
    WARNING_STYLE = (Fore.YELLOW, Style.BRIGHT)
    INFO_STYLE = (Fore.CYAN,   Style.BRIGHT)
    PROMPT_STYLE = (Fore.BLUE,   Style.BRIGHT)
    DEFAULT_STYLE = (Fore.WHITE,  Style.NORMAL)

    @staticmethod
    def format(text, style: tuple) -> str:
        color, style_type = style
        return f"{color}{style_type}{text}{Style.RESET_ALL}"

    @staticmethod
    def print_formatted(text, style: tuple = None) -> None:  # type: ignore
        print(OutputFormatter.format(text, style or OutputFormatter.DEFAULT_STYLE))

    @staticmethod
    def print_error(text) -> None:
        OutputFormatter.print_formatted(text, OutputFormatter.ERROR_STYLE)

    @staticmethod
    def print_success(text) -> None:
        OutputFormatter.print_formatted(text, OutputFormatter.SUCCESS_STYLE)

    @staticmethod
    def print_warning(text) -> None:
        OutputFormatter.print_formatted(text, OutputFormatter.WARNING_STYLE)

    @staticmethod
    def print_info(text) -> None:
        OutputFormatter.print_formatted(text, OutputFormatter.INFO_STYLE)

    @staticmethod
    def print_prompt(text) -> str:
        return OutputFormatter.format(text, OutputFormatter.PROMPT_STYLE)
