# The-Farmer-Was-Replaced Strategy Collection

A community driven project that collects all farming strategies for each crop along with common utility functions.

## Repository Structure

- Resource folders (e.g., cactus, bone, maze ...) hold many script files and a README.md with more details.
	- /resource
		- /subfolder (one strategy split into multiple files for readability)
		- strategy.py (one strategy small enough to fit in a single file)
		- README.md (contains a description of the folder and its contents)
- Special folders:
	- movement
		Contains common movement scripts in groups (e.g., loop_around, non_wrapping_shortest_path, wrapping_shortest_path) with its own README.md.
	- general
		Source files for libraries split into multiple files for specific functions (e.g., math operations).
	- libraries
		Bundled files generated automatically from the general folder (e.g., math.py, string.py, random.py, etc.)

## How to Use

1. Browse the repository online on GitHub or clone/download it.
2. Each script is a standalone code snippet meant to be manually inserted into the game—it is not a complete savegame file.
3. Open the script file you need, copy its code, and paste it into the game.
4. Always include any required utilities from the movement, general, and libraries folders as specified in each file.

## Contributing

All types of contributions are welcome – new strategies (regardless of efficiency), improvements to existing code, or bug fixes. Please submit a pull request or contact me on Discord if you want to help.

## License

This project is under the GNU General Public License v3.0 (GPL-3.0). If you use any of these scripts, your code must also be open source and under a compatible license.
The GPL3 means that any changes or new work based on this code must be shared publicly so everyone can use, change, and share the code.

## Contact

For questions, suggestions, or discussions, you can reach out on Discord: **flekay**
