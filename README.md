# Room Area Calculator for ArchiCAD

## Overview

This Python script is designed to integrate with ArchiCAD, helping automate the process of calculating the area of each apartment (zone) within an ArchiCAD project. The script identifies zones, performs area calculations for room stamps, and updates the ArchiCAD project properties accordingly.

It is particularly useful in projects where multiple zones need to have their areas calculated and displayed in a customized manner.

## Prerequisites

Before using this script, ensure you have set up the necessary custom properties in your ArchiCAD project:

1. **Create a new subcategory** under the Properties section in the ArchiCAD project named `zone_calculator`.

2. **Add the following custom properties** under the `sum_of_units` subcategory:
   - `zone_number`: Represents the unit number of each zone.
   - `total_area_show`: A Boolean flag to determine whether the total area should be displayed.
   - `sum_of_zone_area`: Represents the total area of the units.

3. **Video Tutorial**: Follow this [YouTube video guide](https://www.youtube.com/watch?v=arC290t5Ejg) for detailed instructions on setting up the required properties in ArchiCAD.

## ArchiCAD File Compatibility

This script has been tested and is compatible with **ArchiCAD version 28**. If you are using a different version, you may need to modify the script for compatibility with that version. This may include adjusting API functions or the names of custom properties.

   ```bash
   python "Room Area Calculator for ArchiCAD.py"
