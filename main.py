from decimal import Decimal
import logging

from app.calculator import Calculator
from app.exceptions import OperationError, ValidationError
from app.history import AutoSaveObserver
from app.logger import LoggingObserver
from app.operations import OperationFactory
from app.output_formatter import OutputFormatter
from app.linearizer import Linearizer


def calculator_repl():
    """
    Command-line interface for the calculator.

    Implements a Read-Eval-Print Loop (REPL) that continuously prompts the user
    for commands, processes arithmetic operations, and manages calculation history.
    """
    try:
        # Initialize the Calculator instance
        calc = Calculator()

        # Register observers for logging and auto-saving history
        calc.add_observer(LoggingObserver())
        calc.add_observer(AutoSaveObserver(calc))

        OutputFormatter.print_info(
            "Calculator started. Type 'help' for commands.")

        while True:
            try:
                # Prompt the user for a command
                command = input(OutputFormatter.print_prompt(
                    "\nEnter command (or expression): ")).lower().strip()

                if command.strip()[0].isnumeric():
                    experssion = Linearizer(command)
                    try:
                        experssion.parse()
                        operation = OperationFactory.create_operation(
                            experssion.operation_name)
                        calc.set_operation(operation)
                        result = calc.perform_operation(
                            experssion.a, experssion.b)

                        # Normalize the result if it's a Decimal
                        if isinstance(result, Decimal):
                            result = result.normalize()

                        OutputFormatter.print_success(
                            f"\n({experssion.operation_name})\t{experssion.a} {experssion.operator} {experssion.b} = {result}")

                    except (ValidationError, OperationError) as e:
                        # Handle known exceptions related to validation or operation errors
                        OutputFormatter.print_error(f"Error: {e}")
                    except Exception as e:
                        # Handle any unexpected exceptions
                        OutputFormatter.print_error(f"Unexpected error: {e}")
                    continue

                if command == 'help':
                    # Display available commands
                    print("\nAvailable commands:")
                    print("\t"+", ".join(OperationFactory._operations.keys()
                                         )+"\t"+"Perform calculations")
                    print("\thistory \t Show calculation history")
                    print("\tclear \t Clear calculation history")
                    print("\tundo \t Undo the last calculation")
                    print("\tredo \t Redo the last undone calculation")
                    print("\tsave \t Save calculation history to file")
                    print("\tload \t Load calculation history from file")
                    print("\texit \t Exit the calculator")
                    continue

                if command == 'exit':
                    # Attempt to save history before exiting
                    try:
                        calc.save_history()
                        OutputFormatter.print_success(
                            "History saved successfully.")
                    except Exception as e:
                        OutputFormatter.print_warning(
                            f"Warning: Could not save history: {e}")
                    OutputFormatter.print_success("Goodbye!")
                    break

                if command == 'history':
                    # Display calculation history
                    history = calc.show_history()
                    if not history:
                        print("No calculations in history")
                    else:
                        print("\nCalculation History:")
                        for i, entry in enumerate(history, 1):
                            print(f"{i}. {entry}")
                    continue

                if command == 'clear':
                    # Clear calculation history
                    calc.clear_history()
                    OutputFormatter.print_success("History cleared")
                    continue

                if command == 'undo':
                    # Undo the last calculation
                    if calc.undo():
                        OutputFormatter.print_success("Operation undone")
                    else:
                        print("Nothing to undo")
                    continue

                if command == 'redo':
                    # Redo the last undone calculation
                    if calc.redo():
                        OutputFormatter.print_success("Operation redone")
                    else:
                        print("Nothing to redo")
                    continue

                if command == 'save':
                    # Save calculation history to file
                    try:
                        calc.save_history()
                        OutputFormatter.print_success(
                            "History saved successfully")
                    except Exception as e:
                        OutputFormatter.print_error(
                            f"Error saving history: {e}")
                    continue

                if command == 'load':
                    # Load calculation history from file
                    try:
                        calc.load_history()
                        OutputFormatter.print_success(
                            "History loaded successfully")
                    except Exception as e:
                        OutputFormatter.print_error(
                            f"Error loading history: {e}")
                    continue

                if command in OperationFactory._operations.keys():
                    # Perform the specified arithmetic operation
                    try:
                        print("\nEnter numbers (or \'" + OutputFormatter.format(
                            "cancel", OutputFormatter.ERROR_STYLE) + "\' to abort):")
                        a = input(OutputFormatter.print_prompt(
                            "First number: "))
                        if a.lower() == 'cancel':
                            print("Operation cancelled")
                            continue
                        b = input(OutputFormatter.print_prompt(
                            "Second number: "))
                        if b.lower() == 'cancel':
                            print("Operation cancelled")
                            continue

                        # Create the appropriate operation instance using the Factory pattern
                        operation = OperationFactory.create_operation(command)
                        calc.set_operation(operation)

                        # Perform the calculation
                        result = calc.perform_operation(a, b)

                        # Normalize the result if it's a Decimal
                        if isinstance(result, Decimal):
                            result = result.normalize()

                        OutputFormatter.print_success(f"\nResult: {result}")
                    except (ValidationError, OperationError) as e:
                        # Handle known exceptions related to validation or operation errors
                        OutputFormatter.print_error(f"Error: {e}")
                    except Exception as e:
                        # Handle any unexpected exceptions
                        OutputFormatter.print_error(f"Unexpected error: {e}")
                    continue

                # Handle unknown commands
                OutputFormatter.print_error(
                    f"Unknown command: '{command}'. Type 'help' for available commands.")

            except KeyboardInterrupt:
                # Handle Ctrl+C interruption gracefully
                print("\nOperation cancelled")
                continue
            except EOFError:
                # Handle end-of-file (e.g., Ctrl+D) gracefully
                print("\nInput terminated. Exiting...")
                break
            except Exception as e:
                # Handle any other unexpected exceptions
                OutputFormatter.print_error(f"Error: {e}")
                continue

    except Exception as e:
        # Handle fatal errors during initialization
        OutputFormatter.print_error(f"Fatal error: {e}")
        logging.error(f"Fatal error in calculator REPL: {e}")
        raise


if __name__ == "__main__":
    calculator_repl()
