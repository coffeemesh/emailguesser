
# Email Guesser Tool - How to Use

This tool helps you generate possible email combinations based on a given first name, surname, and domain. You can choose to display the results in the console or save them to a file.

## Step-by-Step Guide

### 1. Download and Install Python

If you don't have Python installed on your computer, you need to download and install it first.

1. Go to the [Python website](https://www.python.org/downloads/).
2. Download the latest version of Python.
3. Run the installer and follow the instructions to install Python on your computer.

### 2. Download the Email Guesser Script

1. Download the emailGuesser.py script file to your computer.
2. Save it in a folder where you can easily find it.

### 3. Run the Script

1. Open a terminal or command prompt:
   - On Windows: Press `Win + R`, type `cmd`, and press Enter.
   - On macOS: Open `Terminal` from the Applications folder.
   - On Linux: Open your preferred terminal application.

2. Navigate to the folder where you saved the emailGuesser.py script. You can use the `cd` command to change directories. For example:
   ```sh
   cd path\to\your\folder
   ```

3. Run the script by typing the following command and pressing Enter:
   ```sh
   python emailGuesser.py
   ```

### 4. Enter the Required Information

The script will prompt you to enter the following information:

1. **First Name**: Enter the first name of the person.
2. **Surname**: Enter the surname of the person.
3. **Domain**: Enter the domain without the `@` symbol (e.g., `example.com`).

You can enter the information in two ways:
- **Comma-separated**: Enter the first name, surname, and domain separated by commas (e.g., `John, Doe, example.com`).
- **Space-separated**: Enter the first name, surname, and domain separated by spaces (e.g., `John Doe example.com`).

### 5. Choose the Output Option

The script will ask you how you want to see the results:

- **Console Output**: Type `C` and press Enter to display the results in the console.
- **File Output**: Type `F` and press Enter to save the results to a file.

### 6. View the Results

- If you chose **Console Output**, the email combinations will be displayed in the console.
- If you chose **File Output**, the email combinations will be saved to a file named `emails_HH-MM_DD_MM_YY.txt` (e.g., `emails_14-30_10_01_25.txt`). The file will be automatically opened in your default text editor.

### Example

Here's an example of how to use the script:

1. Run the script:
   ```sh
   python emailGuesser.py
   ```

2. Enter the information:
   ```
   Enter the first name, surname, and domain (comma-separated or space-separated) or press Enter to input separately: John, Doe, example.com
   ```

3. Choose the output option:
   ```
   Do you want to display the results in the console or save to a file? (C/F): C
   ```

4. View the results in the console.
---
