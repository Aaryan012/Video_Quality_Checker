# Video Quality Analyzer

A Python-based video quality analysis tool for evaluating recorded videos before they are used for annotation or downstream AI/robotics tasks.

The project analyzes objective video properties such as resolution, FPS, duration, sharpness, motion blur, brightness, and contrast, and stores the results in an Excel report.

## Project Structure

```text
python/
├── analyzer/
│   ├── brightness.py
│   ├── contrast.py
│   ├── motion_blur.py
│   ├── sharpness_motionblur.py
│   └── video_info.py
│
├── utils/
│   └── file_path.py
│
├── videos/
│   ├── GX018448.MP4
│   ├── GX018456.MP4
│   └── GX018461.MP4
│
├── Analysis1.xlsx
├── main.py
├── video_quality.py
├── requirements.txt
└── README.md
```

## Features

### 1. Video Metadata Analysis

Extracts:
- File name
- Width and height
- Resolution
- Total frame count
- FPS
- Duration
- Aspect ratio
- Other available video metadata

### 2. Sharpness Analysis

Sharpness is estimated using **Laplacian variance** on sampled grayscale frames.

```text
Video → Sample frames → Grayscale → Laplacian → Variance → Sharpness score
```

The analyzer records:
- Average sharpness
- Minimum sharpness

A higher Laplacian variance generally indicates stronger edges and greater image detail, while a lower value can indicate blur or a low-detail scene.

> **Important:** Sharpness thresholds are dataset-dependent. A value such as `30` should not be treated as a universal definition of a bad video. Thresholds should be calibrated using videos already judged acceptable or poor.

### 3. Motion Blur Analysis

The project includes motion-blur analysis using directional image gradients.

Implementation:
```text
analyzer/motion_blur.py
analyzer/sharpness_motionblur.py
```

### 4. Brightness / Exposure Analysis

Brightness is calculated from sampled grayscale frames to help identify videos that are too dark, too bright, or within an acceptable lighting range.

Implementation:
```text
analyzer/brightness.py
```

### 5. Contrast Analysis

Contrast is estimated using the standard deviation of grayscale pixel intensities.

Implementation:
```text
analyzer/contrast.py
```

## Output

The analyzer produces an Excel report such as:

```text
Analysis1.xlsx
```

Example:

| File Name | Height | Width | Total Frames | FPS | Duration | Quality | Average Sharpness | Minimum Sharpness |
|---|---:|---:|---:|---:|---:|---|---:|---:|
| GX018448 | 1080 | 1920 | 1392 | 59.94 | 23.22 | Good | 34.15 | 18.95 |
| GX018456 | 1080 | 1920 | 1388 | 59.94 | 23.16 | Good | 35.26 | 22.08 |
| GX018461 | 1080 | 1920 | 1506 | 59.94 | 25.13 | Good | 34.59 | 22.34 |

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

Create a virtual environment.

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Requirements

- Python 3.10+
- OpenCV
- NumPy
- Pandas
- OpenPyXL

See `requirements.txt` for the Python dependencies.

## Usage

Place the videos to be analyzed inside:

```text
videos/
```

Then run:

```bash
python main.py
```

The analyzer processes the videos and generates the quality analysis report.

## Current Development Status

| Feature | Status |
|---|---|
| Video metadata | ✅ Implemented |
| Resolution check | ✅ Implemented |
| FPS check | ✅ Implemented |
| Duration calculation | ✅ Implemented |
| Sharpness analysis | ✅ Implemented |
| Motion blur analysis | ✅ Implemented |
| Brightness analysis | ✅ Implemented |
| Contrast analysis | ✅ Implemented |
| Excel reporting | ✅ Implemented |
