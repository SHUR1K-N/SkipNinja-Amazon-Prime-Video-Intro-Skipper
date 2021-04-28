# SkipNinja: Amazon Prime Video Intro Skipper

## Description
A simple tool that will run in the background and look for the "Skip Intro" button in your Amazon Prime Video window. Once the button appears on-screen, depending on which method you choose—automatic or hotkey—the tool will send a click to the button, and then click within the video frame again to restore typical keyboard controls (such as play, pause, skip backward/forward, etc.).

This project was created in Python, for personal use, since Amazon Prime Video does not feature a "Skip Intro" keyboard shortcut yet (can you believe that?!). It is headless (will run in the background) and will not generate a window upon execution.

## Usage
### Autoskip.pyw
1. Clone this repository or download it as a ZIP file (and extract its contents)

2. PIP-install all the packages mentioned under the [last subheading](https://github.com/SHUR1K-N/SkipNinja-Amazon-Prime-Video-Intro-Skipper#dependencies-to-pip-install "last subheading") on this page, either automatically via running the `pip install -r requirments.txt` command, or manually via separate `pip install` commands for each package

3. Double-click "Autoskip.pyw" and it will start running in the background. Every time the "Skip Intro" button is present on the screen, it will automatically send a click onto it without any user interference required.

### Hotkey Skip.pyw
1. Clone this repository or download it as a ZIP file (and extract its contents)

2. PIP-install all the packages mentioned under the [last subheading](https://github.com/SHUR1K-N/SkipNinja-Amazon-Prime-Video-Intro-Skipper#dependencies-to-pip-install "last subheading") on this page, either automatically via running the `pip install -r requirments.txt` command, or manually via separate `pip install` commands for each package

3. Double-click "Hotkey Skip.pyw" and it will start running in the background. When the hotkey is pressed on the keyboard, if the "Skip Intro" button is present on the screen, it will be clicked without any further user interference required.
- Hotkey to click the "Skip Intro" button: **CTRL**
- Hotkey to exit the tool: **\ (Backslash)**

## Optimization
Since the program is designed to indefinitely look for the "Skip Intro" button *and* listen for key strokes (in the case of "Hotkey Skip.pyw") until terminated in order to serve its purpose, the consumption of resources (CPU) has also been minimized and optimized; so the program can be left running in the background for as long as required, or even be scheduled to run automatically at every system start (by placing the shortcut of either .pyw file in the **\Users\USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup** directory) without any prominent CPU usage.

## Dependencies to PIP-Install
- **keyboard** (for keyboard control/listening)
- **pyautogui** (for detecting the "Skip Intro" button on-screen)

------------

My website: https://TheComputerNoob.com
