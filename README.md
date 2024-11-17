# Deep Cave

An artistic Python project that simulates an infinite scrolling cave animation.  
Originally inspired by Al Sweigart's work, this project serves as a fun and educational exercise in Python programming.

## Features

- Procedural generation of a scrolling cave animation.
- Adjustable parameters for width, gap size, and speed.
- Built with simplicity and clarity, perfect for beginners or small experiments.

## Getting Started

Follow these steps to get the project up and running on your local machine.

### Prerequisites

- **Python 3.6+**  
  Ensure Python is installed on your system. You can check your version with:
  ```bash
  python --version
  ```

### Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/deep-cave.git
   cd deep-cave
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

### Usage

To run the animation, simply execute the `main.py` script:
```bash
python main.py
```

Press `Ctrl+C` to exit the program at any time.

## Configuration

You can adjust various parameters of the cave animation by editing the `config.py` file:

- `WIDTH`: The total width of the cave.
- `PAUSE_AMOUNT`: Time (in seconds) between animation frames.
- `LEFT_WIDTH`: Initial width of the left wall.
- `GAP_WIDTH`: Initial size of the cave gap.

Example `config.py`:
```python
WIDTH = 70
PAUSE_AMOUNT = 0.05
LEFT_WIDTH = 20
GAP_WIDTH = 10
```

## Project Structure

```
deep-cave/
│
├── deepcave/             # Core package
│   ├── __init__.py       # Package initialization
│   ├── deepcave.py       # Main animation logic
│
├── config.py             # Configuration constants
├── main.py               # Entry point
└── requirements.txt      # Dependencies
```

## Contributing

Contributions are welcome!  
If you'd like to contribute, please fork the repository and submit a pull request. Be sure to adhere to the coding standards (PEP 8) and provide proper documentation for any changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by [Al Sweigart](https://nostarch.com/big-book-small-python-programming) and his wonderful book on Python.
- Big thanks to everyone who works to make programming fun and accessible!
