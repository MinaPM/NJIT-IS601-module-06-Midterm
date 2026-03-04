# Calculator Application

A sophisticated command-line calculator application built with Python, featuring multiple design patterns, comprehensive history management, and extensive configuration options.

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Installation Instructions](#installation-instructions)
- [Configuration Setup](#configuration-setup)
- [Usage Guide](#usage-guide)
- [Testing Instructions](#testing-instructions)
- [CI/CD Information](#cicd-information)
- [Project Structure](#project-structure)
- [Design Patterns](#design-patterns)
- [Troubleshooting](#troubleshooting)

## Project Description

The Advanced Calculator Application is a Python-based command-line calculator that implements multiple software design patterns to provide a robust, maintainable, and scalable solution for mathematical computations. The application supports various arithmetic operations, maintains calculation history, implements undo/redo functionality, and provides both command-based and expression-based input modes.

### Core Capabilities

- **Multiple Operations**: Addition, Subtraction, Multiplication, Division, Power, Root, and Modulus
- **History Management**: Persistent storage of calculation history in CSV format
- **Undo/Redo Functionality**: Complete history state management using the Memento pattern
- **Auto-Save Feature**: Automatic saving of calculation history based on configuration
- **Logging System**: Comprehensive logging of all operations and events
- **Flexible Configuration**: Environment-variable based configuration system
- **Observer Pattern**: Real-time notification system for calculation events

## Features

### Calculator Operations

| Operation | commnd | Symbol | Example | Result |
|-----------|-------------|-----------------|---------|--------|
| Add | `add` | + | 9 + 3 | 12 |
| Subtract | `subtract` | - | 9.5 - 3 | 6.5 |
| Multiply | `multiply` | * | 9 * 3.2 | 28.8 |
| Divide | `divide` | / | 9.5 / 2 | 4.75 |
| Power | `power` | ^ | 3 ^ 4 | 81 |
| Root | `root` | # | 9 # 2 | 3 |
| Modulus | `modulus` | & | 9.5 & 3 | 0.5 |
| Integer Divide | `int_divide` | \ | 9 \ 2 | 4 |
| Percent | `percent` | % | 9.5 % 50 | 4.75 |
| Absolute Difference | `abs_diff` | \| | 3.2 \| 9 | 5.8 |
### Advanced Features

- **Decimal Precision**: Configurable precision for mathematical operations
- **Input Validation**: Comprehensive validation of operands and operations
- **Error Handling**: Detailed error messages for validation and operation failures
- **Expression Parser**: Natural language expression evaluation (e.g., `10+5*2`)
- **History Persistence**: Load and save calculation history across sessions
- **Colored Output**: Enhanced CLI experience with formatted output

## Installation Instructions

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Virtual environment support (venv)

### Step-by-Step Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/MinaPM/NJIT-IS601-module-06-Midterm.git
cd NJIT-IS601-module-06-Midterm
```

#### 2. Create a Virtual Environment

```bash
# On macOS and Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

#### 3. Upgrade pip

```bash
pip install --upgrade pip
```

#### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### Verifying Installation

```bash
# Check Python version
python --version

# Verify package installation
pip list
```

Expected installed packages:
- `pandas` - Data manipulation and CSV operations
- `colorama` - Cross-platform colored terminal text
- `python-dotenv` - Environment variable management

## Configuration Setup

### Understanding the Configuration System

The calculator uses a hierarchical configuration system that reads from:
1. **Environment Variables** (.env file or system environment)
2. **Constructor Parameters** (programmatic override)
3. **Default Values** (fallback values)

### Creating the .env File

#### 1. Create .env in Project Root

```bash
touch .env
```

#### 2. Configure Environment Variables

Add the following variables to your `.env` file:

```bash
# History Configuration
CALCULATOR_MAX_HISTORY_SIZE=1000
CALCULATOR_AUTO_SAVE=true

# Calculation Settings
CALCULATOR_PRECISION=10
CALCULATOR_MAX_INPUT_VALUE=1e999

# File Operations
CALCULATOR_DEFAULT_ENCODING=utf-8

# Directory Paths (optional - uses defaults if not provided)
CALCULATOR_BASE_DIR=./
CALCULATOR_LOG_DIR=./logs
CALCULATOR_HISTORY_DIR=./history

# File Paths (optional)
CALCULATOR_LOG_FILE=./logs/calculator.log
CALCULATOR_HISTORY_FILE=./history/calculator_history.csv
```

### Configuration Parameters Explained

#### Calculator Settings

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `CALCULATOR_MAX_HISTORY_SIZE` | int | `1000` | Maximum number of calculations to maintain in history |
| `CALCULATOR_AUTO_SAVE` | bool | `true` | Automatically save history after each calculation |
| `CALCULATOR_PRECISION` | int | `10` | Decimal places for calculation results |
| `CALCULATOR_MAX_INPUT_VALUE` | Decimal | `1e999` | Maximum allowed input value |
| `CALCULATOR_DEFAULT_ENCODING` | string | `utf-8` | Default file encoding for operations |

#### Directory Configuration

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `CALCULATOR_BASE_DIR` | Path | Project root | Base directory for all calculator files |
| `CALCULATOR_LOG_DIR` | Path | `{base_dir}/logs` | Directory for log files |
| `CALCULATOR_HISTORY_DIR` | Path | `{base_dir}/history` | Directory for history files |

#### File Configuration

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `CALCULATOR_LOG_FILE` | Path | `{log_dir}/calculator.log` | Log file location |
| `CALCULATOR_HISTORY_FILE` | Path | `{history_dir}/calculator_history.csv` | History file location |

### Environment Variable Priority

```
Explicit Parameter > Environment Variable > Default Value
```

Example:
```python
# Constructor parameter overrides environment variable
config = CalculatorConfig(
    max_history_size=500  # Takes precedence over CALCULATOR_MAX_HISTORY_SIZE
)
```

### Auto-Save Configuration

The `CALCULATOR_AUTO_SAVE` variable accepts multiple formats:

```bash
# Boolean values (case-insensitive)
CALCULATOR_AUTO_SAVE=true     # Enabled
CALCULATOR_AUTO_SAVE=false    # Disabled

# Numeric values
CALCULATOR_AUTO_SAVE=1        # Enabled
CALCULATOR_AUTO_SAVE=0        # Disabled
```

### Logging Configuration

The application sets up logging automatically with the following configuration:

```python
logging.basicConfig(
    filename=str(log_file),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    force=True
)
```

**Log Levels Used:**
- `INFO` - General information about operations
- `WARNING` - Non-critical issues (e.g., history loading failures)
- `ERROR` - Errors during operations

**Typical Log Entry:**
```
2024-03-04 10:30:45,123 - INFO - Calculator initialized with configuration
2024-03-04 10:30:46,456 - INFO - Set operation: Addition
2024-03-04 10:30:47,789 - INFO - Calculation performed: Addition (5, 3) = 8
2024-03-04 10:30:48,012 - INFO - History auto-saved
```

## Usage Guide

### Starting the Calculator

```bash
python main.py
```

You should see:
```
Calculator started. Type 'help' for commands.

Enter command (or expression):
```

### Command-Based Mode

In command-based mode, you specify the operation first, then enter the operands.

#### Addition

```
Enter command (or expression): add
First number: 10
Second number: 5
Result: 15
```

#### Subtraction

```
Enter command (or expression): subtract
First number: 20
Second number: 8
Result: 12
```

#### Multiplication

```
Enter command (or expression): multiply
First number: 6
Second number: 7
Result: 42
```

#### Division

```
Enter command (or expression): divide
First number: 100
Second number: 4
Result: 25
```

#### Power

```
Enter command (or expression): power
First number: 2
Second number: 8
Result: 256
```

#### Root

```
Enter command (or expression): root
First number: 27
Second number: 3
Result: 3
```

#### Modulus

```
Enter command (or expression): modulus
First number: 17
Second number: 5
Result: 2
```

### Expression Mode

Enter mathematical expressions directly using operators:

```
Enter command (or expression): 10+5
Result: 15

Enter command (or expression): 20-3*2
Result: 14

Enter command (or expression): 8^3
Result: 512

Enter command (or expression): 16√4
Result: 4

Enter command (or expression): 10%3
Result: 1
```

### History Commands

#### View History

```
Enter command (or expression): history

Calculation History:
1. Addition(10, 5) = 15
2. Subtraction(20, 8) = 12
3. Multiplication(6, 7) = 42
```

#### Clear History

```
Enter command (or expression): clear
History cleared
```

#### Save History

```
Enter command (or expression): save
History saved to: ./history/calculator_history.csv
```

#### Load History

```
Enter command (or expression): load
Loaded 5 calculations from history
```

### Undo/Redo Operations

#### Undo Last Calculation

```
Enter command (or expression): undo
Last calculation undone
```

#### Redo Last Undone Calculation

```
Enter command (or expression): redo
Last calculation redone
```

### Help System

```
Enter command (or expression): help

Available commands:
  Calculations
    [add]         Addition
    [subtract]    Subtraction
    [multiply]    Multiplication
    [divide]      Division
    [power]       Power operation
    [root]        Root calculation
    [modulus]     Modulus operation
    
  History
    [history]     Show calculation history
    [clear]       Clear calculation history
    [undo]        Undo the last calculation
    [redo]        Redo the last undone calculation
    
  File
    [save]        Save calculation history to file
    [load]        Load calculation history from file
    
  General
    [exit]        Exit the calculator
```

### Exiting the Calculator

```
Enter command (or expression): exit
History saved successfully.
Goodbye!
```

### Error Handling

#### Division by Zero

```
Enter command (or expression): divide
First number: 10
Second number: 0
Error: Division by zero is not allowed
```

#### Invalid Input

```
Enter command (or expression): add
First number: abc
Error: Invalid number format: abc
```

#### Invalid Root Operation

```
Enter command (or expression): root
First number: -5
Second number: 2
Error: Cannot calculate root of negative number
```

#### Value Exceeds Maximum

```
Enter command (or expression): add
First number: 999999999999999999999999999999
Error: Value exceeds maximum allowed: 1e999
```

### Canceling Operations

During operation input, type `cancel` to abort:

```
Enter command (or expression): add
First number (type 'cancel' to abort): cancel
Operation cancelled
```

## Testing Instructions

### Running All Tests

```bash
pytest
```

### Running Tests with Verbose Output

```bash
pytest -v
```

### Running Specific Test File

```bash
# Test calculations
pytest tests/test_calculation.py -v

# Test calculator functionality
pytest tests/test_calculator.py -v

# Test configuration
pytest tests/test_calculator_config.py -v

# Test observers
pytest tests/test_history.py -v
pytest tests/test_logger.py -v

# Test operations
pytest tests/test_operations.py -v
```

### Running Specific Test

```bash
pytest tests/test_calculation.py::test_addition -v
```

### Test Coverage

#### Generate Coverage Report

```bash
# Run tests with coverage
pytest --cov=app --cov-report=html

# Display coverage in terminal
pytest --cov=app --cov-report=term-missing
```

#### View Coverage Report

The HTML coverage report is generated in `htmlcov/` directory:

```bash
# macOS
open htmlcov/index.html

# Linux
xdg-open htmlcov/index.html

# Windows
start htmlcov/index.html
```

#### Current Coverage Status

- **Overall Coverage**: 90%
- **Calculator Module**: 78%
- **Calculation Module**: 91%
- **Operations Module**: 100%
- **Configuration Module**: 100%
- **History Module**: 100%
- **Logger Module**: 100%

### Test Categories

#### Unit Tests

```bash
# Test individual components
pytest tests/test_calculation.py tests/test_operations.py
```

#### Integration Tests

```bash
# Test component interactions
pytest tests/test_calculator.py tests/test_history.py
```

#### Configuration Tests

```bash
pytest tests/test_calculator_config.py -v
```

### Continuous Testing

Watch for file changes and run tests automatically:

```bash
# Install pytest-watch
pip install pytest-watch

# Run tests on file changes
ptw
```

## CI/CD Information

### GitHub Actions Workflow

The project includes automated CI/CD via GitHub Actions.

#### Workflow File

Location: `.github/workflows/` 

#### Workflow Steps

1. **Checkout Code**: Clones the repository
2. **Set Up Python**: Configures Python 3.9+
3. **Create Virtual Environment**: Isolates dependencies
4. **Install Dependencies**: Installs requirements
5. **Run Linting** (if configured): Code quality checks
6. **Run Tests**: Executes full test suite
7. **Generate Coverage**: Creates coverage reports
8. **Upload Artifacts**: Stores coverage reports

#### Workflow Triggers

- **Push Events**: Runs on every push to main branch
- **Pull Requests**: Runs on all pull requests
- **Schedule**: Can be scheduled for periodic runs

#### Viewing Workflow Results

1. Navigate to repository on GitHub
2. Click "Actions" tab
3. Select workflow run to view details
4. Check "Summary" tab for test results

### Local CI/CD Simulation

Simulate GitHub Actions locally:

```bash
# Install act (GitHub Actions local runner)
# See: https://github.com/nektos/act

act
```

## Project Structure

```
NJIT-IS601-module-06-Midterm/
├── app/
│   ├── __init__.py
│   ├── calculation.py          # Value object for calculations
│   ├── calculator.py           # Main calculator class
│   ├── calculator_config.py    # Configuration management
│   ├── calculator_memento.py   # Memento pattern for undo/redo
│   ├── exceptions.py           # Custom exception classes
│   ├── history.py              # Observer pattern for history
│   ├── input_validators.py     # Input validation logic
│   ├── linearizer.py           # Expression parser
│   ├── logger.py               # Logging observer
│   ├── operations.py           # Operation implementations
│   └── output_formatter.py     # CLI output formatting
├── tests/
│   ├── test_calculation.py
│   ├── test_calculator.py
│   ├── test_calculator_config.py
│   ├── test_history.py
│   ├── test_logger.py
│   ├── test_operations.py
│   └── test_input_validators.py
├── .github/
│   └── workflows/              # GitHub Actions workflows
├── .env                        # Environment configuration
├── .gitignore
├── main.py                     # Entry point
├── pytest.ini                  # Pytest configuration
├── requirements.txt            # Project dependencies
├── README.md
└── LICENSE
```

## Design Patterns

### 1. Strategy Pattern (Operations)

Allows dynamic selection of operations:

```python
operation = OperationFactory.create_operation('add')
calculator.set_operation(operation)
result = calculator.perform_operation(5, 3)
```

### 2. Factory Pattern (OperationFactory)

Centralized operation creation:

```python
operation = OperationFactory.create_operation('multiply')
# Returns: Multiplication instance
```

### 3. Observer Pattern (History Management)

Notification system for events:

```python
calculator.add_observer(LoggingObserver())
calculator.add_observer(AutoSaveObserver(calculator))
# Both observers notified on new calculation
```

### 4. Memento Pattern (Undo/Redo)

State preservation for history:

```python
calculator.undo()  # Restore previous state
calculator.redo()  # Restore undone state
```

### 5. Adapter Pattern (Linearizer)

Converts expressions to operations:

```python
linear = Linearizer("10+5")
linear.parse()
# Converts string to structured operation
```

### 6. Value Object Pattern (Calculation)

Immutable representation of calculations:

```python
calculation = Calculation(
    operation="Addition",
    operand1=5,
    operand2=3
)
# Result computed automatically
```

## Troubleshooting

### Common Issues and Solutions

#### Issue: Module Not Found Error

```
ModuleNotFoundError: No module named 'colorama'
```

**Solution:**
```bash
pip install -r requirements.txt
```

#### Issue: Permission Denied on main.py

```
PermissionError: [Errno 13] Permission denied: 'main.py'
```

**Solution:**
```bash
chmod +x main.py
python main.py  # Use python explicitly
```

#### Issue: History File Not Found

```
FileNotFoundError: [Errno 2] No such file or directory: './history/calculator_history.csv'
```

**Solution:**
The application creates directories automatically on first run. If this error persists:
```bash
mkdir -p logs history
```

#### Issue: Encoding Errors

```
UnicodeDecodeError: 'utf-8' codec can't decode byte...
```

**Solution:**
Verify the encoding in `.env`:
```bash
# In .env file
CALCULATOR_DEFAULT_ENCODING=utf-8
```

#### Issue: Tests Fail on Windows

**Solution:**
Ensure virtual environment is activated:
```bash
venv\Scripts\activate
pip install -r requirements.txt
pytest
```

#### Issue: Logging File Permission Denied

```
PermissionError: [Errno 13] Permission denied: './logs/calculator.log'
```

**Solution:**
```bash
# On macOS/Linux
chmod -R u+w logs/

# On Windows, run as Administrator or check file permissions
```

#### Issue: History Not Loading

**Solution:**
- Check that history file exists: `ls history/calculator_history.csv`
- Verify file format is valid CSV
- Clear corrupted history: `rm history/calculator_history.csv`
- Calculator will create new history on next run

### Debug Mode

Enable verbose logging:

```python
# In main.py, modify logging setup
import logging
logging.basicConfig(level=logging.DEBUG)
```

Then run:
```bash
python main.py 2>&1 | tee debug.log
```

### Getting Help

1. Check the help command: Type `help` in calculator
2. Review test files for usage examples
3. Check application logs: `cat logs/calculator.log`
4. Review error messages carefully for hints

## Contributing

When contributing to this project:

1. Create a feature branch from `main`
2. Make your changes with tests
3. Ensure all tests pass: `pytest`
4. Check coverage: `pytest --cov=app`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Version

Current Version: 1.0.0

Last Updated: March 4, 2024