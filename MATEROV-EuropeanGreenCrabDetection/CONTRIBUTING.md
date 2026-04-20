# Contributing to MATEROV European Green Crab Detection

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the code and ideas, not individuals
- Help each other succeed

## Ways to Contribute

### 1. Report Bugs
- **Check existing issues** before creating new ones
- Provide clear, detailed description with steps to reproduce
- Include system information (OS, Python version, etc.)
- Attach relevant logs or screenshots

**Example issue:**
```
Title: Detection fails on Windows with non-ASCII filenames

Description:
When input images have special characters (é, ñ, etc.) in filenames, 
the detection script throws UnicodeDecodeError on Windows.

Steps to reproduce:
1. Place image "café_crabs.jpg" in input_images/
2. Run python green_crab_detector/detect.py
3. Observe error: UnicodeDecodeError...

Environment:
- OS: Windows 10
- Python: 3.11.0
- Conda environment: green_crab
```

### 2. Suggest Enhancements
- Share ideas for new features
- Describe use cases and benefits
- Provide examples if possible
- Suggest implementation approach (optional)

### 3. Submit Code Changes
See below for details.

### 4. Improve Documentation
- Fix typos or unclear explanations
- Add examples or clarifications
- Improve README or docstrings
- Create tutorials or guides

## Development Setup

### Fork and Clone
```bash
# Fork the repository on GitHub (click "Fork" button)

# Clone your fork
git clone https://github.com/YOUR-USERNAME/MATEROV-EuropeanGreenCrabDetection.git
cd MATEROV-EuropeanGreenCrabDetection

# Add upstream remote
git remote add upstream https://github.com/MATEROV/MATEROV-EuropeanGreenCrabDetection.git
```

### Create Development Environment
```bash
# Create conda environment
conda create -n green_crab_dev python=3.11
conda activate green_crab_dev

# Install requirements
pip install -r green_crab_ws/requirements.txt

# Run tests to verify setup
python green_crab_detector/test_portability.py
```

### Create Feature Branch
```bash
# Update from upstream
git fetch upstream
git rebase upstream/main

# Create feature branch
git checkout -b feature/your-feature-name
# or for bugfixes:
git checkout -b fix/issue-description
```

## Making Changes

### Code Style
- Follow PEP 8 style guidelines
- Use descriptive variable names
- Add comments for complex logic
- Keep functions focused and modular

### Example code style:
```python
def detect_crabs_in_image(image_path: str, confidence_threshold: float = 0.7) -> dict:
    """
    Detect crabs in a single image.
    
    Args:
        image_path: Path to input image (.jpg, .png)
        confidence_threshold: Minimum confidence score (0.0-1.0)
    
    Returns:
        Dictionary with keys: 'boxes', 'logits', 'phrases', 'count'
    
    Raises:
        FileNotFoundError: If image_path doesn't exist
        ValueError: If confidence_threshold not in [0.0, 1.0]
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    if not 0.0 <= confidence_threshold <= 1.0:
        raise ValueError("confidence_threshold must be in [0.0, 1.0]")
    
    # Load and process image
    image = cv2.imread(image_path)
    # ... detection logic ...
    
    return results
```

### Testing
- Test your changes thoroughly
- Run the test suite: `python green_crab_detector/test_portability.py`
- Add new tests for new features
- Ensure backward compatibility

### Documentation
- Update docstrings for modified functions
- Update README if behavior changes
- Add comments for complex logic
- Document new features or parameters

### Commit Messages
Write clear, descriptive commit messages:

```
# Good commit messages
git commit -m "Add GPU support for inference"
git commit -m "Fix Windows encoding issue in test suite"
git commit -m "Improve detection confidence threshold filtering"

# Less helpful
git commit -m "Fix stuff"
git commit -m "Update"
git commit -m "WIP"
```

### Format: `<type>: <description>`

Types:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation
- `refactor:` - Code restructuring
- `test:` - Test additions/changes
- `perf:` - Performance improvements
- `style:` - Code style changes

## Submitting Changes

### Push to Your Fork
```bash
git push origin feature/your-feature-name
```

### Create Pull Request
1. Go to https://github.com/YOUR-USERNAME/MATEROV-EuropeanGreenCrabDetection
2. Click "New pull request"
3. Select your branch
4. Fill out PR template with:
   - Clear title
   - Description of changes
   - Motivation and context
   - Testing performed
   - Related issues

**PR Title Examples:**
- "Add real-time video stream detection"
- "Fix memory leak in batch processing"
- "Improve confidence score filtering"
- "Add GPU acceleration support"

### PR Description Template
```markdown
## Description
Brief description of changes made.

## Type of Change
- [ ] Bug fix (non-breaking change)
- [ ] New feature (non-breaking change)
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Breaking change

## Related Issue
Closes #123

## Testing
- [x] Tested on Windows
- [x] Tested on macOS
- [ ] Tested on Linux
- [x] Ran test_portability.py with all tests passing

## Changes Made
- Change 1
- Change 2
- Change 3

## Screenshots (if applicable)
Show before/after if relevant.

## Checklist
- [x] Code follows style guidelines
- [x] Docstrings updated
- [x] Tests added/updated
- [x] README updated if needed
- [x] No breaking changes
```

## Review Process

### What to Expect
- Maintainer will review your PR
- May ask for clarifications or changes
- May suggest improvements
- Will test thoroughly

### Addressing Feedback
```bash
# Make requested changes locally
# Commit with descriptive message
git add .
git commit -m "Address review feedback: improve error handling"

# Push to your branch (don't force push unless requested)
git push origin feature/your-feature-name
```

The PR will automatically update with your new commits.

## Feature Proposals

### For Major Features
Before submitting code for major features:
1. Open an issue describing the feature
2. Discuss approach with maintainers
3. Get approval on design
4. Then submit PR

This saves time for everyone!

## Need Help?

- **Questions?** Open a Discussion
- **Setup issues?** Check README troubleshooting
- **Problems?** Create an Issue with details
- **Ideas?** Start a Discussion

## Project Areas for Contribution

### High Priority
- [ ] GPU/CUDA support
- [ ] Docker containerization
- [ ] REST API endpoint
- [ ] Web UI dashboard
- [ ] Performance optimization

### Medium Priority
- [ ] Video stream support
- [ ] Batch processing optimization
- [ ] Additional model variants
- [ ] Advanced filtering
- [ ] Data augmentation

### Nice to Have
- [ ] Additional documentation
- [ ] Example notebooks
- [ ] Integration with other tools
- [ ] Community examples

## Development Resources

### Project Structure
```
src/
├── detect.py              # Main detection logic
├── test_portability.py    # Test suite
└── model/
    ├── config.py
    └── weights.pth

tests/
├── test_detection.py
├── test_integration.py
└── test_edge_cases.py
```

### Key Dependencies
- **torch**: Deep learning framework
- **transformers**: BERT tokenizer
- **groundingdino**: Object detection model
- **opencv**: Image processing
- **supervision**: Annotation utilities

### Testing
```bash
# Run all tests
python green_crab_detector/test_portability.py

# Run specific test
python -m pytest tests/test_detection.py::test_crab_detection

# Run with coverage
pytest --cov=green_crab_detector tests/
```

## Documentation Standards

### Docstring Format (Google Style)
```python
def function_name(arg1: str, arg2: int) -> dict:
    """
    One-line summary of what the function does.
    
    Longer description if needed. Explain the algorithm,
    important details, or special cases.
    
    Args:
        arg1: Description of arg1
        arg2: Description of arg2
    
    Returns:
        Description of return value
    
    Raises:
        ValueError: When this condition occurs
        FileNotFoundError: When that condition occurs
    
    Example:
        >>> result = function_name("input", 42)
        >>> result['key']
        'expected_value'
    """
```

## Licensing

By contributing, you agree that your contributions will be licensed under the Apache License 2.0.

## Questions?

- Check existing issues and discussions
- Read the main README
- Look at example code
- Ask in GitHub Discussions

Thank you for contributing! 🎉
