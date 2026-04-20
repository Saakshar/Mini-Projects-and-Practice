# MATEROV European Green Crab Detection - Project Documentation

## Project Overview

**MATEROV-EuropeanGreenCrabDetection** is a production-ready deep learning system for automated detection of European green crabs (*Carcinus maenas*) in images using GroundingDINO.

### Mission
Provide researchers and environmental managers with an easy-to-use tool for rapid, accurate identification and monitoring of invasive green crabs.

## Quick Facts

| Aspect | Details |
|--------|---------|
| **Model** | GroundingDINO SwinT OGC (v0.1.0-alpha) |
| **Inference** | CPU-based (no GPU required) |
| **Accuracy** | High confidence detections with per-crab scores |
| **Speed** | 2-5 seconds per image |
| **Memory** | 2-3GB during inference |
| **License** | Apache 2.0 (Open Source) |
| **Language** | Python 3.10+ |
| **Platform** | Windows, macOS, Linux |

## Getting Started

### Minimum Requirements
- Python 3.10+
- 4GB RAM
- 2GB disk space

### Quick Install
```bash
git clone https://github.com/MATEROV/MATEROV-EuropeanGreenCrabDetection.git
cd MATEROV-EuropeanGreenCrabDetection
conda create -n green_crab python=3.11
conda activate green_crab
pip install -r green_crab_ws/requirements.txt
```

### First Run
```bash
set KMP_DUPLICATE_LIB_OK=TRUE
python green_crab_detector/detect.py
```

Place images in `green_crab_detector/input_images/` - results appear in `outputs/`

📖 **Full guide**: [See README.md](README.md)

## Project Structure

```
MATEROV-EuropeanGreenCrabDetection/
├── README.md                          # Main documentation
├── LICENSE                            # Apache 2.0 license
├── CONTRIBUTING.md                    # Contribution guidelines
├── GITHUB_SETUP.md                    # GitHub publishing guide
├── DOCUMENTATION.md                   # This file
│
├── green_crab_detector/               # Main application
│   ├── detect.py                      # Entry point
│   ├── test_portability.py            # Test suite (5 tests)
│   ├── README.md                      # Usage guide
│   ├── input_images/                  # Input folder
│   └── outputs/                       # Results folder
│
└── green_crab_ws/                     # ROS workspace
    ├── requirements.txt               # Dependencies
    ├── README.md                      # ROS docs
    └── src/
        ├── GroundingDINO/             # Model implementation
        └── green_crab_detector/       # Detection package
            └── model/
                ├── groundingdino_config.py    # Model config
                └── groundingdino_weights.pth  # Pre-trained weights
```

## Key Components

### 1. detect.py (Main Detection Script)
**Location**: `green_crab_detector/detect.py`

**Purpose**: 
- Loads GroundingDINO model
- Processes images from `input_images/` folder
- Runs inference on each image
- Draws bounding boxes and crab count
- Saves results to `outputs/`

**Usage**:
```bash
python green_crab_detector/detect.py
```

**Supported formats**: `.jpg`, `.jpeg`, `.png`

**Output**: 
- Annotated images with red bounding boxes
- Text overlay: "Crabs: N" (total count)
- Confidence scores per detection

### 2. test_portability.py (Validation Suite)
**Location**: `green_crab_detector/test_portability.py`

**Purpose**: Comprehensive validation with 5 tests:
1. **Path Resolution** - Verify config/weights file discovery
2. **GroundingDINO Import** - Check local model clone injection
3. **Model Loading** - Test weights compatibility
4. **Detection Pipeline** - End-to-end inference test
5. **Output Handling** - Verify folder creation

**Usage**:
```bash
set KMP_DUPLICATE_LIB_OK=TRUE
python green_crab_detector/test_portability.py
```

**Expected output**: All 5 tests passing

### 3. GroundingDINO Model
**Location**: `green_crab_ws/src/GroundingDINO/`

**Details**:
- Local git clone of GroundingDINO repository
- Automatically injected into `sys.path` by `detect.py`
- Eliminates dependency on `pip install` for portability
- Includes compatibility patches for transformers 5.2.0+

**Patches Applied**:
- `get_head_mask` fallback for BertModel compatibility
- `get_extended_attention_mask` exception handling

### 4. Model Weights & Config
**Location**: `green_crab_ws/src/green_crab_detector/model/`

| File | Size | Purpose |
|------|------|---------|
| `groundingdino_config.py` | ~2KB | Model architecture config |
| `groundingdino_weights.pth` | 662MB | Pre-trained weights |

**Configuration Specs**:
- Backbone: Swin Transformer (Small)
- Hidden dim: 256
- Layers: 6 encoder, 6 decoder
- Queries: 900
- Text encoder: BERT-base-uncased

## Technical Architecture

### Data Flow
```
Input Image File
    ↓
Load with OpenCV
    ↓
Convert to tensor
    ↓
Run GroundingDINO inference
    ↓
Post-process detections
    ↓
Filter by confidence
    ↓
Draw bounding boxes
    ↓
Add text overlay
    ↓
Save annotated image
```

### Dependencies
```
torch==2.1.0              # Deep learning framework
torchvision==0.25.0       # Vision models
transformers==5.2.0       # BERT tokenizer
groundingdino (local)     # Object detection model
opencv-python==4.8.1      # Image processing
supervision==0.27.0       # Annotation utilities
addict, yapf, timm, etc.  # Supporting libraries
```

## Performance Characteristics

### Inference Speed
- **Typical**: 2-5 seconds per image (CPU)
- **Variables**: Image resolution, CPU model, batch size
- **Optimization**: Larger images = slower, but better detection

### Memory Usage
- **Peak**: 2-3GB during inference
- **Base**: ~500MB for model weights
- **Per-image**: ~100-200MB overhead

### Detection Confidence
Confidence scores range from 0.0 to 1.0:
- **0.90-1.0**: Very reliable (use)
- **0.80-0.90**: Reliable (use)
- **0.70-0.80**: Probable (review)
- **<0.70**: Low confidence (consider filtering)

## Deployment & Usage

### Single Device
```bash
# Copy project to device
git clone <repo>

# Install
conda create -n green_crab python=3.11
conda activate green_crab
pip install -r green_crab_ws/requirements.txt

# Use
cp images/* green_crab_detector/input_images/
python green_crab_detector/detect.py
# Results in green_crab_detector/outputs/
```

### Batch Processing Script
```python
from pathlib import Path
import subprocess

image_dir = Path("green_crab_detector/input_images")

# Copy all images to input folder
for image in Path("data/field_survey").glob("*.jpg"):
    shutil.copy(image, image_dir)

# Run detection
subprocess.run([
    "python", "green_crab_detector/detect.py"
], env={**os.environ, "KMP_DUPLICATE_LIB_OK": "TRUE"})

# Process results
for result in Path("green_crab_detector/outputs").glob("*.jpg"):
    print(f"Processed: {result}")
```

### Docker (Future)
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r green_crab_ws/requirements.txt
ENTRYPOINT ["python", "green_crab_detector/detect.py"]
```

## Development & Contribution

### Setting Up Development Environment
```bash
git clone https://github.com/MATEROV/MATEROV-EuropeanGreenCrabDetection.git
cd MATEROV-EuropeanGreenCrabDetection

# Create dev environment
conda create -n green_crab_dev python=3.11
conda activate green_crab_dev
pip install -r green_crab_ws/requirements.txt

# Optional: install dev tools
pip install pytest black flake8

# Run tests
python green_crab_detector/test_portability.py
```

### Code Style
- **PEP 8** compliance
- **Type hints** for functions
- **Docstrings** (Google style)
- **Comments** for complex logic

### Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Bug reporting guidelines
- Feature request process
- Code submission workflow
- Testing requirements
- Documentation standards

## Testing

### Test Suite
```bash
cd green_crab_detector
python test_portability.py
```

### Manual Testing
```bash
# 1. Create test images
# 2. Place in input_images/
# 3. Run detection
python detect.py

# 4. Verify outputs in outputs/ folder
# 5. Check bounding boxes visually
# 6. Confirm crab counts are reasonable
```

### Expected Results
- All images processed without errors
- Output files created in `outputs/` folder
- Detections shown with bounding boxes
- Confidence scores displayed
- Crab count visible in text overlay

## Troubleshooting

### Issue: Import Error
**Problem**: `ModuleNotFoundError: No module named 'torch'`
```bash
# Solution:
conda activate green_crab
pip install -r green_crab_ws/requirements.txt
```

### Issue: Environment Variable
**Problem**: KMP_DUPLICATE_LIB_OK warning
```bash
# Windows:
set KMP_DUPLICATE_LIB_OK=TRUE
python green_crab_detector/detect.py

# Linux/Mac:
export KMP_DUPLICATE_LIB_OK=TRUE
python green_crab_detector/detect.py
```

### Issue: No Detections
**Causes**:
- Low image quality
- Poor lighting
- Crabs partially hidden
- Image too small

**Solutions**:
- Try high-res images (1080p+)
- Test with different images
- Check lighting conditions
- Ensure crabs are clearly visible

See [green_crab_detector/README.md](green_crab_detector/README.md#troubleshooting) for more.

## Roadmap & Future Work

### Planned Features
- [ ] GPU/CUDA support for faster inference
- [ ] Real-time video stream processing
- [ ] Docker containerization
- [ ] REST API endpoint
- [ ] Web UI dashboard
- [ ] Batch optimization
- [ ] Additional model variants

### Research Applications
- Ecological monitoring
- Population surveys
- Invasive species tracking
- Environmental tracking
- Climate research

## References & Citations

### Academic Papers
- [GroundingDINO: Marrying DINO with Grounded Pre-Training](https://arxiv.org/abs/2303.05499)
- [DINO: DETR with Improved DeNoising Anchor Boxes](https://arxiv.org/abs/2203.03605)

### Related Projects
- [GroundingDINO](https://github.com/IDEA-Research/GroundingDINO)
- [DETR](https://github.com/facebookresearch/detr)
- [Swin Transformer](https://github.com/microsoft/Swin-Transformer)

### Biological Context
- European Green Crab (*Carcinus maenas*)
- Invasive Species Research
- Marine Ecosystem Monitoring

## License & Attribution

**License**: Apache 2.0 (Permissive Open Source)

**Attribution**:
- GroundingDINO by IDEA Research Lab
- Swin Transformer by Microsoft
- DETR by Facebook Research

**Using This Project**:
- ✅ Commercial use allowed
- ✅ Modification allowed
- ✅ Distribution allowed
- ✅ Private use allowed
- ⚠️ Requires license notice
- ⚠️ No warranty provided

See [LICENSE](LICENSE) for full terms.

## Support & Contact

### Getting Help
1. **Check Documentation**: [README.md](README.md), [green_crab_detector/README.md](green_crab_detector/README.md)
2. **Run Tests**: `python green_crab_detector/test_portability.py`
3. **Search Issues**: GitHub Issues tab
4. **Open Issue**: If problem not documented
5. **Request Feature**: GitHub Discussions

### Reporting Bugs
Include:
- OS and Python version
- Exact error message
- Steps to reproduce
- Relevant logs
- Expected vs actual behavior

### Submitting Feedback
- Feature requests → GitHub Discussions
- Code contributions → Pull Requests
- Documentation → Issues or PRs
- General feedback → GitHub Discussions

## Project Statistics

### Codebase
- **Lines of Code**: ~500+ (main detection)
- **Test Coverage**: 5 comprehensive tests
- **Dependencies**: 10+ major packages
- **Documentation**: 4 guides + inline comments
- **License**: Apache 2.0

### Resources
- **Model**: 662MB pre-trained weights
- **Config**: Optimized for all systems
- **Memory**: 2-3GB inference
- **Speed**: 2-5 sec per image

### Community
- Open to contributions
- Apache 2.0 licensing
- Professional documentation
- Active maintenance

---

**Project Status**: Production Ready ✅  
**Last Updated**: February 2026  
**Version**: 1.0.0  
**Maintainer**: MATEROV Team

For more information, see the main [README.md](README.md) or visit the [GitHub repository](https://github.com/MATEROV/MATEROV-EuropeanGreenCrabDetection).
