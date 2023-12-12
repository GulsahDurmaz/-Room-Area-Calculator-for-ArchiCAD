# Room Area Calculator for ArchiCAD

## Overview

This Python script is designed to be used in conjunction with ArchiCAD, specifically for calculating the area of each room in an ArchiCAD project. The script identifies zones and room stamps, performs area calculations, and updates the ArchiCAD project accordingly.

## Prerequisites

Before using this script, make sure you have completed the following preparations in your ArchiCAD project:

1. Create a new subcategory named `sum_of_units` under the "Eigenschaften" (Properties) section in the ArchiCAD project.

2. Add the following sub-properties under the `sum_of_units` subcategory:
   - **`unit_number`**: Represents the unit number of each zone.
   - **`unit_number_show`**: A flag to determine whether the unit number should be displayed.
   - **`sum_of_units_area`**: Represents the total area of the units.

## ArchiCAD File Compatibility

This script is compatible with ArchiCAD version 26. If you are using a different version, you may need to update the script accordingly.

## Usage

1. Open an ArchiCAD project.

2. Execute the Python script in an environment that supports ArchiCAD Python scripting.

3. The script will calculate the area for each room and update the ArchiCAD project.

## Detailed Explanation

The Python script utilizes the ArchiCAD Python API to interact with the project. It identifies zones and room stamps, calculates the area, and updates the total area for each unit.

Please note that this README provides a basic overview,
