import colorama
from colorama import Fore, Back, Style
from enum import Enum

colorama.init()


class OutputFormatter:
    # Utility class for formatting console output with colors and styles using colorama.
    # All methods are static, allowing for easy formatting of text without needing to instantiate the class.

    # create static style variables for common styles
    ERROR_STYLE = (Fore.RED, Style.BRIGHT)
    SUCCESS_STYLE = (Fore.GREEN, Style.BRIGHT)
    WARNING_STYLE = (Fore.YELLOW, Style.BRIGHT)
    INFO_STYLE = (Fore.CYAN, Style.BRIGHT)
    PROMPT_STYLE = (Fore.BLUE, Style.BRIGHT)

    @staticmethod
    def format(text, style: tuple) -> str:
        color, style_type = style
        return f"{color}{style_type}{text}{Style.RESET_ALL}"

    @staticmethod
    def format_output(text, color=Fore.WHITE, style=Style.NORMAL) -> str:
        return f"{color}{style}{text}{Style.RESET_ALL}"

    @staticmethod
    def print_formatted(text, color=Fore.WHITE, style=Style.NORMAL) -> None:
        formatted_text = OutputFormatter.format_output(
            text, color, style)
        print(formatted_text)

    @staticmethod
    def print_error(text) -> None:
        OutputFormatter.print_formatted(
            text, color=Fore.RED, style=Style.BRIGHT)

    @staticmethod
    def print_success(text) -> None:
        OutputFormatter.print_formatted(
            text, color=Fore.GREEN, style=Style.BRIGHT)

    @staticmethod
    def print_warning(text) -> None:
        OutputFormatter.print_formatted(
            text, color=Fore.YELLOW, style=Style.BRIGHT)

    @staticmethod
    def print_info(text):
        OutputFormatter.print_formatted(
            text, color=Fore.CYAN, style=Style.BRIGHT)

    @staticmethod
    def print_prompt(text):
        return OutputFormatter.format_output(
            text, color=Fore.BLUE, style=Style.BRIGHT)
