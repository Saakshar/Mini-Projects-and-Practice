# MATEROV European Green Crab Detection

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-green.svg)](LICENSE)
[![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)]()

A deep learning-powered object detection system for automatically detecting and localizing European green crabs (*Carcinus maenas*) in images. Built with **GroundingDINO** (SwinT OGC) for high-accuracy detections on CPU hardware.

## 🎯 Overview

This repository provides an end-to-end solution for:
- **Automated crab detection** in images using state-of-the-art vision models
- **Portable inference** (CPU-based, no GPU required)
- **Batch processing** with automatic bounding box annotation
- **Cross-platform support** (Windows, macOS, Linux)

Perfect for ecological monitoring, invasive species tracking, and research applications.

## 📦 Key Features

✅ **Pre-trained Model** - GroundingDINO SwinT OGC weights included (662MB)  
✅ **CPU Inference** - Works on standard laptops without GPU  
✅ **Portable** - No complex pip installs, runs on any device with Python  
✅ **Production Ready** - Comprehensive testing and error handling  
✅ **Easy to Use** - Simple folder-based workflow (input → detect → output)  
✅ **Fully Tested** - 5-part validation test suite included  
✅ **Well Documented** - Complete setup and usage guides  

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/Saakshar/MATEROV-EuropeanGreenCrabDetection.git
cd MATEROV-EuropeanGreenCrabDetection
```

### 2. Install Dependencies
```bash
# Create conda environment
conda create -n green_crab python=3.11
conda activate green_crab

# Install requirements
pip install -r green_crab_ws/requirements.txt
```

### 3. Run Detection
```bash
# On Windows
set KMP_DUPLICATE_LIB_OK=TRUE
python green_crab_detector/detect.py

# On macOS/Linux
export KMP_DUPLICATE_LIB_OK=TRUE
python green_crab_detector/detect.py
```

### 4. View Results
- **Input images**: Place in `green_crab_detector/input_images/`
- **Output images**: Check `green_crab_detector/outputs/`

📖 **Full documentation**: See [green_crab_detector/README.md](green_crab_detector/README.md)

## 📋 System Requirements

| Requirement | Specification |
|-------------|---------------|
| **Python** | 3.10 or higher |
| **RAM** | 4GB minimum (8GB recommended) |
| **Storage** | 2GB for dependencies + weights |
| **OS** | Windows, macOS, Linux |
| **GPU** | Not required (CPU inference) |

## 🏗️ Project Structure

```
MATEROV-EuropeanGreenCrabDetection/
├── green_crab_detector/           # Main detection application
│   ├── detect.py                  # Entry point for detection
│   ├── test_portability.py        # Validation test suite (5 tests)
│   ├── README.md                  # Detailed usage guide
│   ├── input_images/              # Place your images here
│   └── outputs/                   # Results saved here
│
├── green_crab_ws/                 # ROS workspace (optional)
│   ├── src/
│   │   ├── GroundingDINO/         # Local model clone
│   │   └── green_crab_detector/
│   │       └── model/
│   │           ├── groundingdino_config.py
│   │           └── groundingdino_weights.pth (662MB)
│   ├── requirements.txt           # Python dependencies
│   └── README.md                  # ROS-specific docs
│
├── .gitignore
├── LICENSE
└── README.md                      # This file
```

## 🔧 Installation & Setup

### Detailed Setup Instructions

#### Option 1: Conda (Recommended)
```bash
# Create environment
conda create -n green_crab python=3.11
conda activate green_crab

# Install dependencies
cd MATEROV-EuropeanGreenCrabDetection
pip install -r green_crab_ws/requirements.txt

# Verify installation
python green_crab_detector/test_portability.py
```

#### Option 2: Virtual Environment (venv)
```bash
# Create environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r green_crab_ws/requirements.txt
```

## 💻 Usage Guide

### Basic Workflow

1. **Prepare images**
   ```bash
   mkdir green_crab_detector/input_images
   # Copy your .jpg, .png files here
   ```

2. **Run detection**
   ```bash
   set KMP_DUPLICATE_LIB_OK=TRUE  # Windows
   python green_crab_detector/detect.py
   ```

3. **Check results**
   - Annotated images in `green_crab_detector/outputs/`
   - Red bounding boxes show detected crabs
   - Text overlay: "Crabs: N" (total count)

### Example

```bash
$ python green_crab_detector/detect.py

Processing image: harbor_crabs.jpg
Detected 5 crabs with confidence scores: 0.89, 0.92, 0.85, 0.88, 0.91
✓ Saved annotated image to outputs/harbor_crabs.jpg

Processing image: beach_scan.png
Detected 2 crabs with confidence scores: 0.94, 0.87
✓ Saved annotated image to outputs/beach_scan.png

Total: 2 images processed, 7 crabs detected
```

## 🧪 Testing

Run the comprehensive test suite to verify everything works:

```bash
set KMP_DUPLICATE_LIB_OK=TRUE
python green_crab_detector/test_portability.py
```

**Tests include:**
1. ✅ Path Resolution - Config/weights file discovery
2. ✅ GroundingDINO Import - Local model clone injection
3. ✅ Model Loading - Weights & architecture compatibility
4. ✅ Detection Pipeline - End-to-end inference
5. ✅ Output Handling - Folder creation and writability

Expected output:
```
===== TEST SUMMARY =====
[PASS] Path Resolution
[PASS] GroundingDINO Import
[PASS] Model Loading
[PASS] Detection Pipeline
[PASS] Output Handling

Total: 5/5 passed
[SUCCESS] All tests passed! Project is ready for deployment.
```

## 📊 Model Information

**GroundingDINO SwinT OGC (v0.1.0-alpha)**

| Property | Details |
|----------|---------|
| **Architecture** | Swin Transformer backbone with grounding head |
| **Backbone** | SwinT (Small) |
| **Training Data** | Large-scale vision-language datasets |
| **Inference** | CPU-based, ~2-5 sec per image |
| **Weights** | 662MB (pre-trained, ready to use) |
| **Prompt** | "European green crab" |

### Performance

- **Latency**: 2-5 seconds per image (varies by CPU)
- **Memory**: 2-3GB during inference
- **Best Practice**: High-res images (1080p+) with visible crabs
- **Confidence**: Returns 0.0-1.0 scores (higher = more confident)

## 🔍 Troubleshooting

### Common Issues

**"ModuleNotFoundError: No module named 'torch'"**
```bash
conda activate green_crab  # Ensure environment is active
pip install -r green_crab_ws/requirements.txt
```

**KMP_DUPLICATE_LIB_OK warning**
```bash
# Set environment variable before running:
set KMP_DUPLICATE_LIB_OK=TRUE        # Windows
export KMP_DUPLICATE_LIB_OK=TRUE    # macOS/Linux
```

**No detections in output**
- Verify image quality (high-res preferred)
- Check lighting (avoid very dark images)
- Ensure crabs are visible in image
- Try test images first

📖 **Full troubleshooting guide**: [green_crab_detector/README.md](green_crab_detector/README.md#troubleshooting)

## 📁 File Descriptions

### Core Files

| File | Purpose |
|------|---------|
| `green_crab_detector/detect.py` | Main detection script - entry point for users |
| `green_crab_detector/test_portability.py` | 5-part validation test suite |
| `green_crab_ws/requirements.txt` | Python package dependencies |
| `green_crab_ws/src/GroundingDINO/` | Local clone of GroundingDINO model |

### Model Files

| File | Size | Purpose |
|------|------|---------|
| `groundingdino_config.py` | ~2KB | Model architecture config |
| `groundingdino_weights.pth` | 662MB | Pre-trained model weights |

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- [ ] GPU support (CUDA acceleration)
- [ ] Multi-GPU batch inference
- [ ] Real-time video stream detection
- [ ] Web UI for detection
- [ ] Advanced filtering/post-processing
- [ ] Additional model variants

## 📝 License

This project is licensed under the **Apache License 2.0** - see [LICENSE](LICENSE) file for details.

GroundingDINO is licensed under Apache 2.0 by IDEA Research.

## 📚 References

**Academic Papers:**
- [GroundingDINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection](https://arxiv.org/abs/2303.05499)
- Bertasius et al. (2023) - IDEA Research Lab

**Related Projects:**
- [GroundingDINO GitHub](https://github.com/IDEA-Research/GroundingDINO)
- [DINO: DETR with Improved DeNoising Anchor Boxes](https://arxiv.org/abs/2203.03605)

## 🎓 Biological Context

**European Green Crab** (*Carcinus maenas*) is an invasive species in many regions. Automated detection assists with:
- Population monitoring
- Early warning systems
- Research data collection
- Ecological impact assessment

## 💬 Support & Questions

- **Issues**: Open a GitHub Issue for bugs and feature requests
- **Discussions**: Use GitHub Discussions for questions
- **Documentation**: Check [green_crab_detector/README.md](green_crab_detector/README.md) for detailed usage
- **Tests**: Run `python green_crab_detector/test_portability.py` to diagnose issues

## 🚀 Deployment

### Deploy on New Device

1. Clone repository
2. Install Python 3.10+
3. Create conda environment and install requirements
4. Run test suite to verify: `python green_crab_detector/test_portability.py`
5. Place images in `input_images/`, run `detect.py`

### Production Use

For production systems:
- Batch process via scripts or job schedulers
- Monitor logs for errors
- Set up automated backups
- Use version control for tracking outputs

## 🎯 Roadmap

- [x] Core detection pipeline
- [x] Comprehensive documentation
- [x] Test suite
- [x] GitHub repository
- [ ] Docker container support
- [ ] REST API endpoint
- [ ] Web dashboard
- [ ] Model optimization (quantization, pruning)
- [ ] Video stream support

## 📞 Contact

**Project**: MATEROV European Green Crab Detection  
**Repository**: https://github.com/Saakshar/MATEROV-EuropeanGreenCrabDetection  
**Issues**: [GitHub Issues](../../issues)

---

**Built with ❤️ for ecological research and invasive species monitoring.**

Last updated: February 2026 | Status: Production Ready ✅
