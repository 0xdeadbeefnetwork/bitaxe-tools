# BitAxe Tools

These tools were developed to address specific issues encountered with a BitAxe device that arrived without a factory reset and was already connected to an existing swarm. Due to this pre-configured state, the device had restricted settings that prevented configuration changes. The following tools provide solutions to regain control of the device and update it as needed. 
These tools requre you to have Tkinter installed to use.

## Tools

### Tool 1: BitAxe Configuration from Default IP

This tool allows you to configure the BitAxe from its default SSID IP. It connects to the BitAxe's default `SSID IP` address to allow modifications to the device settings. This is particularly useful for BitAxe devices that are not properly factory reset and may not have been correctly disconnected from previous configurations.

- **Usage**: Connect to the BitAxe’s default IP address (SSID IP), and use this tool to access configuration settings.
- **Requirements**: Ensure that the BitAxe is accessible via its default SSID IP address.

### Tool 2: Partial Brick and ESP-Miner Update

This tool provides a way to perform a ‘partial brick’ on the BitAxe device, allowing you to reset its settings when the "Save" button is grayed out and unresponsive. This tool also facilitates an update to the `esp-miner.bin` firmware in cases where the device's OTAWWW endpoint returns HTTP 500, preventing Over-The-Air (OTA) updates.

- **Functionality**: 
  - Partially bricks the device via the API, which enables the “Save” button to function.
  - Updates `esp-miner.bin` firmware to restore OTA functionality if the OTAWWW endpoint fails (HTTP 500 error).
- **Usage**: Run this tool when unable to save configuration settings or when OTA updates fail. After partial bricking, the save button should become active, allowing proper configuration changes.

## Background

Upon receiving the BitAxe, it was found to be pre-configured with another swarm, and the save functionality was locked, making it impossible to modify settings before restarting. Additionally, the OTAWWW endpoint was responding with a 500 HTTP status code, preventing firmware updates. These tools were created to overcome these limitations by resetting the configuration access and updating the firmware.

---

For additional support, please refer to the documentation provided with your BitAxe or reach out to BitAxe discord for support after doing your own due process.
Please donate hashing power or BTC to: 1CNg32ut3ABbtGVqfcsTeWvXHHFJtGy1mE
