# Crypto Miner Pro

A Python-based cryptocurrency mining simulator with a graphical desktop interface built using Tkinter.

Crypto Miner Pro demonstrates the basic concepts behind proof-of-work mining, including SHA-256 hashing, mining difficulty, shares, blocks, hashrate measurement, and mining logs.

> **Important:** This project is currently a **mining simulator**. It does not connect to a real cryptocurrency network, mining pool, blockchain, or wallet, and the displayed shares/blocks are not real cryptocurrency rewards.

## Features

- 🖥️ Graphical desktop interface using Tkinter
- 🔐 Simple username/password login
- ⛏️ Start and stop mining
- #️⃣ SHA-256 hashing simulation
- 📊 Real-time hashrate display
- 📈 Share counter
- 🧱 Simulated block counter
- ⚙️ Adjustable mining difficulty
- 📝 Live mining log
- 🧵 Background mining thread so the GUI remains responsive
- 💻 Designed to run locally on your computer

## How It Works

The application creates simulated mining jobs and calculates SHA-256 hashes.

A hash is considered a simulated share when it begins with the required number of zeros.

For example, with a difficulty of `4`, the program looks for hashes beginning with:

```text
0000
```

When a qualifying hash is found, the application increases the share counter and displays the result in the mining log.

The application can also simulate a block when a hash meets a higher difficulty threshold.

## Requirements

### Python

Python 3.10 or newer is recommended.

Check your Python installation:

```bash
python3 --version
```

Example:

```text
Python 3.14.6
```

### Tkinter

This project uses Python's built-in Tkinter GUI library.

Test Tkinter with:

```bash
python3 -m tkinter
```

If a small Tkinter window opens, Tkinter is installed correctly.

## Installation — macOS

### 1. Install Python

Install Python from the official Python website if it is not already installed.

After installation, open Terminal and check:

```bash
python3 --version
```

### 2. Clone the repository

Clone the GitHub repository:

```bash
git clone https://github.com/YOUR-USERNAME/crypto-miner-app.git
```

Enter the project directory:

```bash
cd crypto-miner-app
```

### 3. Check the project files

Run:

```bash
ls
```

You should see:

```text
my_miner_app.py
```

### 4. Test Tkinter

Run:

```bash
python3 -m tkinter
```

If Tkinter opens successfully, close the test window.

### 5. Start the application

Run:

```bash
python3 my_miner_app.py
```

The **Crypto Miner Pro** window should open.

## Installation — Windows

### 1. Install Python

Install Python 3.10 or newer.

During installation, make sure Python is added to your PATH.

Check the installation:

```powershell
python --version
```

### 2. Clone the repository

```powershell
git clone https://github.com/YOUR-USERNAME/crypto-miner-app.git
```

Enter the project directory:

```powershell
cd crypto-miner-app
```

### 3. Run the application

```powershell
python my_miner_app.py
```

Tkinter is normally included with standard Python installations on Windows.

## Installation — Linux

Install Python and Tkinter using your distribution's package manager.

For Debian/Ubuntu-based systems:

```bash
sudo apt update
sudo apt install python3 python3-tk
```

Check Python:

```bash
python3 --version
```

Test Tkinter:

```bash
python3 -m tkinter
```

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/crypto-miner-app.git
```

Enter the project:

```bash
cd crypto-miner-app
```

Run:

```bash
python3 my_miner_app.py
```

## Login

The application currently uses username/password authentication defined in the Python source.

Open:

```text
my_miner_app.py
```

and locate:

```python
USERNAME = "admin"
PASSWORD = "miner4life"
```

Change these values before distributing the application.

### Security Warning

Do not commit real passwords, API keys, wallet private keys, seed phrases, or other secrets to a public GitHub repository.

For a production application, authentication should be moved to a secure configuration or authentication system rather than being hard-coded in the source code.

## Project Structure

```text
crypto-miner-app/
│
├── my_miner_app.py
└── README.md
```

## Running the Application

From the project directory:

```bash
python3 my_miner_app.py
```

After launching:

1. Enter your username.
2. Enter your password.
3. Click **Login**.
4. Click **Start Mining**.
5. Monitor hashrate, shares, blocks, and mining logs.
6. Click **Stop Mining** to stop the simulation.

## Mining Statistics

The application displays:

### Hashrate

The approximate number of simulated hashes calculated per second.

### Shares

The number of simulated hashes that satisfy the current share difficulty.

### Blocks

The number of simulated blocks found by the application.

These statistics are generated locally by the program and are not blockchain records.

## Difficulty

The initial difficulty is set in the mining engine.

Higher difficulty means the program requires more leading zeros in the SHA-256 hash.

The difficulty can increase after a simulated block is found.

## Technology

This project uses Python standard-library modules including:

- `hashlib`
- `time`
- `threading`
- `tkinter`
- `random`

No external Python packages are currently required.

## Important Disclaimer

This project is educational software demonstrating simplified cryptocurrency mining concepts.

It does **not** currently:

- Connect to a real mining pool
- Connect to a blockchain network
- Submit real mining shares
- Mine real Bitcoin or other cryptocurrency
- Generate real cryptocurrency rewards
- Connect to a cryptocurrency wallet
- Provide withdrawable balances

The hashrate, shares, and blocks displayed by the application are simulated locally.

## Future Development

Possible future improvements include:

- Real mining-pool integration
- Wallet address configuration
- Mining-pool connection status
- Persistent statistics
- Configuration file support
- Secure authentication
- User profiles
- Mining history
- Performance monitoring
- CPU/GPU mining support
- Real payout tracking
- Improved error handling
- Cross-platform packaging
- `.env` configuration for secrets

## License

Choose an appropriate open-source license before publishing the project publicly.

If you are unsure which license to use, review the available GitHub license options before selecting one.

## Author

Developed as a Python desktop application project for learning and experimentation.