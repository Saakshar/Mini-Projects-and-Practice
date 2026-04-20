# European Green Crab Detector

A deep learning-based object detection system using GroundingDINO (SwinT OGC) to automatically detect and localize European green crabs in images. The system is portable and works across different devices.

## Overview

This program uses a pre-trained GroundingDINO model to:
- Automatically detect European green crabs in images
- Draw bounding boxes around detected crabs
- Count the number of crabs per image
- Save annotated images with detection results

## System Requirements

- **Python**: 3.10 or higher
- **OS**: Windows, macOS, or Linux
- **RAM**: 4GB minimum (8GB recommended)
- **Storage**: 2GB free space for dependencies and model weights

## Installation

### Step 1: Clone or Extract the Repository

Download or clone the MATEROV-AI_Imaging workspace to your computer.

### Step 2: Set Up Python Environment

We recommend using Conda for easy dependency management. If you don't have Conda installed, download it from [anaconda.com](https://anaconda.com).

#### Option A: Using Conda (Recommended)

```bash
# Create a new conda environment
conda create -n green_crab_detector python=3.11

# Activate the environment
conda activate green_crab_detector

# Navigate to the workspace directory
cd path/to/MATEROV-AI_Imaging

# Install dependencies
pip install -r green_crab_ws/requirements.txt
```

#### Option B: Using venv (Python built-in)

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r green_crab_ws/requirements.txt
```

### Step 3: Verify Installation

Run the portability test to confirm everything is set up correctly:

```bash
# Windows
set KMP_DUPLICATE_LIB_OK=TRUE
python green_crab_detector/test_portability.py

# macOS/Linux
export KMP_DUPLICATE_LIB_OK=TRUE
python green_crab_detector/test_portability.py
```

You should see output showing all 5 tests passed. If not, check the error messages and ensure all dependencies installed correctly.

## How to Use

### Quick Start

1. **Prepare your images**: Place all images you want to analyze in the `green_crab_detector/input_images/` folder
   - Supported formats: `.jpg`, `.jpeg`, `.png`
   - Images can be any size (resizing happens automatically)

2. **Run detection**: Execute the detection script

```bash
# Windows
set KMP_DUPLICATE_LIB_OK=TRUE
python green_crab_detector/detect.py

# macOS/Linux
export KMP_DUPLICATE_LIB_OK=TRUE
python green_crab_detector/detect.py
```

3. **View results**: Check the `green_crab_detector/outputs/` folder for annotated images
   - Each output image has the same name as the input image
   - Red bounding boxes show detected crabs
   - Text overlay shows total crab count: "Crabs: N"

### Detailed Workflow

#### Create Input Folder (if it doesn't exist)

```bash
mkdir green_crab_detector/input_images
```

#### Add Your Images

Copy or move your crab images to the input folder:
```
green_crab_detector/
├── input_images/
│   ├── image1.jpg
│   ├── image2.png
│   └── image3.jpg
├── outputs/
├── detect.py
└── README.md
```

#### Run the Detection Script

```bash
python green_crab_detector/detect.py
```

**What happens:**
- The script scans `input_images/` for all `.jpg`, `.jpeg`, and `.png` files
- For each image, it runs inference using the GroundingDINO model
- Detections are drawn as red bounding boxes with confidence scores
- Crab count is displayed in the top-left corner
- Results are saved to `outputs/` with the same filename

#### Check Output Images

Open the annotated images in `green_crab_detector/outputs/`:
- Red boxes indicate detected crabs
- Each box has a confidence score (0.0-1.0, where 1.0 is highest confidence)
- Text shows "Crabs: N" where N is the total count

### Example Output

```
Processing image: harbor_crabs.jpg
Detected 5 crabs with confidence scores: 0.89, 0.92, 0.85, 0.88, 0.91
✓ Saved annotated image to outputs/harbor_crabs.jpg

Processing image: beach_scan.png
Detected 2 crabs with confidence scores: 0.94, 0.87
✓ Saved annotated image to outputs/beach_scan.png
```

## File Structure

```
green_crab_detector/
├── README.md                          # This file
├── detect.py                          # Main detection script
├── test_portability.py                # Validation test suite
├── input_images/                      # Place your images here
│   └── (add your .jpg, .png files)
├── outputs/                           # Results folder (auto-created)
│   └── (annotated images will appear here)
└── captured_images/                   # (Optional) sample images

green_crab_ws/
├── requirements.txt                   # Python dependencies
├── src/
│   ├── GroundingDINO/                # Local GroundingDINO clone
│   └── green_crab_detector/
│       └── model/
│           ├── groundingdino_config.py    # Model configuration
│           └── groundingdino_weights.pth  # Pre-trained weights (662MB)
```

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'torch'"

**Solution**: Make sure you've activated the conda environment and installed requirements.txt
```bash
conda activate green_crab_detector
pip install -r green_crab_ws/requirements.txt
```

### Issue: "KMP_DUPLICATE_LIB_OK" warning appears

**Solution**: This is a warning about OpenMP libraries. Set the environment variable before running:
```bash
# Windows (Command Prompt)
set KMP_DUPLICATE_LIB_OK=TRUE
python green_crab_detector/detect.py

# Windows (PowerShell)
$env:KMP_DUPLICATE_LIB_OK="TRUE"
python green_crab_detector/detect.py

# macOS/Linux
export KMP_DUPLICATE_LIB_OK=TRUE
python green_crab_detector/detect.py
```

### Issue: No detections or very few detections

**Possible causes**:
- Image quality too low (try high-resolution images)
- Lighting issues (very dark or overexposed images)
- Crabs partially obscured (detection works best with visible crabs)
- Model confidence threshold filtering detections

**Solution**: Try with different images or adjust detection parameters in `detect.py`

### Issue: Script runs but produces no output files

**Solution**: Check that:
1. Input images are in `green_crab_detector/input_images/`
2. File extensions are `.jpg`, `.jpeg`, or `.png` (case-sensitive on some systems)
3. Output folder `green_crab_detector/outputs/` exists and is writable
4. Run the test suite to verify: `python green_crab_detector/test_portability.py`

### Issue: "CUDA out of memory" or GPU errors

**Solution**: The system is configured for CPU inference. If you're trying to use GPU, ensure you have CUDA installed and the right PyTorch version.

## Advanced Usage

### Adjusting Detection Confidence

Edit `detect.py` to change the text prompt or detection parameters:

```python
# Current setting (very specific)
text_prompt = "European green crab"

# More general
text_prompt = "crab"
```

### Batch Processing on New Device

1. Copy the entire `MATEROV-AI_Imaging` folder to the new computer
2. Follow the Installation steps on the new device
3. Place new images in `input_images/`
4. Run `python green_crab_detector/detect.py`

### Viewing Detection Logs

The script prints progress to console. To save logs to a file:

```bash
# Windows
python green_crab_detector/detect.py > detection_log.txt 2>&1

# macOS/Linux
python green_crab_detector/detect.py | tee detection_log.txt
```

## Model Information

**Model**: GroundingDINO SwinT OGC (v0.1.0-alpha)
- **Architecture**: Swin Transformer backbone with grounding head
- **Weights**: Pre-trained on large-scale vision-language datasets
- **Inference**: CPU-based (no GPU required)
- **Latency**: ~2-5 seconds per image (depending on resolution and CPU)

## Performance Notes

- **Inference speed**: Faster on modern multi-core CPUs
- **Memory usage**: Typically 2-3GB for detection
- **Best results**: High-resolution images (1080p+) with good lighting and visible crabs
- **Batch processing**: Process multiple images sequentially (one at a time)

## Common Confidence Score Ranges

- **0.90-1.0**: Very high confidence detections (highly reliable)
- **0.80-0.90**: High confidence (reliable)
- **0.70-0.80**: Medium confidence (probable crab)
- **Below 0.70**: Low confidence (may be false positive)

## Uninstalling / Cleanup

To remove the conda environment and free up disk space:

```bash
# Remove conda environment
conda env remove -n green_crab_detector

# Remove temporary files (optional)
rm -rf green_crab_detector/input_images/*
rm -rf green_crab_detector/outputs/*
```

## Support

For issues or questions:
1. Check the **Troubleshooting** section above
2. Run `python green_crab_detector/test_portability.py` to diagnose system issues
3. Verify all dependencies with: `pip list | grep -E "torch|transformers|opencv"`

## License

This project uses GroundingDINO (IDEA Research), which is released under the Apache 2.0 License.

## Quick Reference

| Task | Command |
|------|---------|
| Activate environment | `conda activate green_crab_detector` |
| Run detection | `set KMP_DUPLICATE_LIB_OK=TRUE && python green_crab_detector/detect.py` |
| Run tests | `set KMP_DUPLICATE_LIB_OK=TRUE && python green_crab_detector/test_portability.py` |
| Create input folder | `mkdir green_crab_detector/input_images` |
| Check dependencies | `pip list` |
| Update dependencies | `pip install --upgrade -r green_crab_ws/requirements.txt` |
