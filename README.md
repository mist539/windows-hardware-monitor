![Windows Hardware Monitor](assets/banner.png)

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="MIT License">
  <img src="https://img.shields.io/badge/Platform-Windows-blue" alt="Windows Platform">
  <img src="https://img.shields.io/badge/Price-Free-brightgreen" alt="Free Software">
  <img src="https://img.shields.io/badge/Source-Open--Source-orange" alt="Open Source">
  <img src="https://img.shields.io/badge/Interface-Desktop-purple" alt="Desktop Application">
</p>

**Windows Hardware Monitor is a free, open-source PC monitoring application for Windows that provides real-time insights into your computer's hardware.** Track CPU and GPU temperatures, fan speeds, voltages, clock frequencies, memory usage and system performance through an intuitive graphical interface — no command line required.

## ⬇️ Installation

**Download the Windows application**

1. Open the repository's [Releases](https://github.com/mist539/windows-hardware-monitor/releases) page.
2. Download the latest release archive **`Windows Hardware Monitor 4.2.3.zip`**.
3. Extract the archive into a folder of your choice.
4. Keep **`Windows Hardware Monitor 4.2.3.exe`** and `libvlc.dll` together in that folder.
5. Double-click **`Windows Hardware Monitor 4.2.3.exe`** to launch the application.


## ✨ Features

- 🌡️ **Real-Time CPU Temperature Monitoring** — View processor temperatures and thermal sensor readings to understand system heat levels during everyday use, gaming and demanding workloads.
- 🎮 **GPU Temperature and Performance Monitoring** — Monitor supported NVIDIA, AMD and Intel graphics hardware, including temperatures, utilization and operating frequencies.
- ⚡ **CPU Load and Clock Speeds** — Inspect processor utilization, clock frequencies and operating behavior to understand system performance.
- 🌀 **Fan Speed Monitoring** — Read available cooling fan RPM measurements and monitor supported hardware controller sensors.
- 🔋 **Voltage and Power Sensors** — Access motherboard voltage readings and other available electrical sensor information.
- 🧠 **RAM and Memory Monitoring** — Keep track of memory-related readings and available system information.
- 💾 **Storage Health and Temperature** — Inspect supported HDD, SSD and NVMe storage device sensors.
- 🖥️ **Motherboard Sensor Detection** — Discover supported motherboard monitoring chips and hardware controller information.
- 📊 **Live Hardware Overview** — Bring important PC sensor readings together in one convenient desktop interface.
- 🔓 **Free and Open Source** — Use an auditable monitoring application without subscription fees or proprietary monitoring services.

## 🖼️ Overview

![Features](assets/features.png)

## 🚀 Usage

Getting started with Windows Hardware Monitor is straightforward:

1. **Launch the application** on your Windows desktop.
2. **Allow hardware access** if Windows requests the necessary permissions for sensor detection.
3. **Explore your hardware** using the component tree to inspect your processor, graphics card, motherboard, memory and storage devices.
4. **Expand individual components** to view available temperature, utilization, voltage, fan speed and clock frequency readings.
5. **Run your usual workloads** to observe how hardware measurements change during gaming, rendering, multitasking or other activities.

### Hardware Compatibility

Hardware sensor availability depends on the device, motherboard controller, firmware and driver support.

| Hardware | Available Monitoring |
|---|---|
| Intel CPUs | Temperature, load, clock speeds |
| AMD CPUs | Temperature, load, clock speeds |
| NVIDIA GPUs | Temperature, utilization, clock speeds |
| AMD GPUs | Temperature, utilization, clock speeds |
| Intel GPUs | Supported GPU sensor readings |
| Motherboards | Voltages, temperatures, fan speeds |
| HDD and SSD | Supported drive temperatures |
| NVMe drives | Supported NVMe sensor readings |
| Network adapters | Available hardware information |

**Note:** Not every device exposes every sensor. Some readings require elevated permissions or compatible hardware monitoring interfaces.

## 🎯 Who Is This Application For?

Windows Hardware Monitor is useful for:

- **PC enthusiasts** who want detailed information about their computer hardware.
- **Gamers** who want to check CPU and GPU temperatures while playing.
- **Overclocking enthusiasts** who need visibility into clock speeds, temperatures and voltages.
- **System administrators** who want convenient access to hardware sensor information.
- **PC builders** who want to inspect cooling behavior and component readings.
- **Developers** who need hardware monitoring capabilities for Windows applications.
- **Troubleshooting users** investigating overheating, unstable performance or cooling issues.

## 🔍 Why Monitor Your PC Hardware?

Monitoring hardware measurements helps you understand how your computer behaves under different workloads.

| Metric | Why It Matters |
|---|---|
| CPU temperature | Identify potentially excessive processor heat |
| GPU temperature | Understand graphics card thermal behavior |
| CPU utilization | Identify demanding processes and workloads |
| GPU utilization | Observe graphics processing activity |
| Clock frequency | Inspect processor and graphics operating speeds |
| Fan RPM | Check available cooling fan activity |
| Voltage readings | Inspect supported motherboard sensor values |
| Storage temperature | Monitor supported drive thermal conditions |

Regular hardware monitoring can help identify thermal problems, evaluate cooling configurations and understand performance changes.

## 🪟 Windows Desktop Experience

The application provides a graphical way to explore PC hardware without requiring terminal commands or manually querying individual sensors.

Its component-oriented layout makes it easier to navigate between:

- Processor and graphics hardware.
- Motherboard and embedded controllers.
- Memory and storage devices.
- Available temperature and voltage sensors.
- Fan controllers and rotational speed readings.

Whether you are checking CPU temperature before a gaming session or investigating GPU behavior during a demanding workload, the application keeps supported hardware measurements accessible.

## 🔒 Security

Your computer's hardware information should remain under your control.

- **Open-source software:** The source code can be inspected and independently reviewed.
- **No telemetry or tracking:** The application is designed for local hardware monitoring without built-in user tracking.
- **No subscription:** Core monitoring functionality is available without a paid account.
- **Local operation:** Hardware sensor readings are collected from supported local devices.
- **Permission transparency:** Some hardware readings may require additional Windows permissions.

### Reporting Issues

Found an incorrect sensor reading, missing motherboard support or an unexpected application crash?

Please report issues through the repository's issue tracker.

When submitting a report, include:

- Windows version and architecture.
- CPU and GPU models.
- Motherboard manufacturer and model.
- A description of the affected sensor.
- Relevant error messages or diagnostic information.

Please avoid publishing personal information or sensitive system details in public reports.

## 🤝 Contributing

Contributions from the open-source hardware monitoring community are welcome.

Ways to help improve the project include:

- Reporting hardware compatibility problems.
- Testing sensor readings across different motherboard models.
- Improving CPU and GPU monitoring support.
- Fixing bugs and improving application stability.
- Enhancing the desktop interface.
- Improving documentation and developer examples.

When submitting code changes, keep compatibility, reliability and maintainability in mind.

## 💻 Developer Integration

Hardware monitoring functionality can also be useful beyond the desktop application.

Developers can integrate supported monitoring capabilities into their own .NET applications using the associated hardware monitoring library.

Potential integration scenarios include:

- Custom PC monitoring dashboards.
- Hardware diagnostics utilities.
- System information applications.
- Performance monitoring tools.
- Hardware testing applications.

Refer to the available project documentation and library package information for supported APIs and integration details.

## ❓ Frequently Asked Questions

### Is Windows Hardware Monitor free?

Yes. It is intended to be free and open-source software distributed under the MIT License.

### Can I monitor CPU temperature?

Yes. The application can display available processor temperature sensors on supported Intel and AMD hardware.

### Does it support NVIDIA and AMD graphics cards?

It supports available monitoring information from supported NVIDIA and AMD graphics hardware. Exact sensor availability depends on the device and driver environment.

### Can I check GPU temperature while gaming?

Yes. You can inspect supported GPU temperature and utilization readings while running games or other graphics-intensive applications.

### Can it display fan speeds?

Yes. Supported motherboard and hardware controller sensors can expose fan speed measurements in RPM.

### Does it support SSD and NVMe temperature monitoring?

Supported HDD, SSD and NVMe devices can expose temperature information through their available hardware monitoring interfaces.

### Why are some sensor readings missing?

Sensor availability varies between hardware manufacturers, motherboard controllers, firmware versions and device drivers. Not every device exposes every measurement.

### Is an internet connection required?

Normal local hardware monitoring does not require a continuous internet connection.

### Is it suitable for gaming PCs?

Yes. It can help gamers inspect available CPU and GPU temperatures, clock speeds, utilization and cooling measurements.

## 📄 License

Released under the **MIT License**. You are free to use, modify and distribute the software in accordance with its license terms.

---

**Windows Hardware Monitor — Understand your PC hardware, monitor system temperatures and keep track of performance with free open-source Windows software.**