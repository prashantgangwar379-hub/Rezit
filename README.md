# Rezit

Rezit is a CLI-based image optimization tool that resizes and compresses images to fit under a target file size.

## Features

* Constraint-based optimization (size-aware)
* Adaptive resizing + quality tuning
* Supports JPG/PNG input
* Outputs optimized JPG
* CLI interface
* Packaged as standalone `.exe`

## Usage

```bash
rezit.exe --input "image.png" --target 500
```

## Example

```bash
rezit.exe --input "photo.png" --target 300
```

## Output

Optimized image will be saved in:

```
output/
```

## Tech Stack

* Python
* Pillow
* PyInstaller

## Version

v1.0

