# 🧾 AI Bill Reading System

An intelligent web application that automatically extracts key information from bill and receipt images using Google's Gemini AI.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📋 Overview

This project automates the extraction of billing information from images, eliminating the need for manual data entry. Simply upload a bill image, and the AI will identify and extract:

- 📄 **Bill Number**
- 📅 **Date**
- 🔢 **Quantity**
- 💰 **Amount**
- 🏪 **Shop Name**

## ✨ Features

- **Automatic Field Detection** - AI identifies billing fields without manual input
- **Multi-format Support** - Handles various bill layouts and formats
- **Visual Verification** - View original image alongside extracted data
- **Simple Interface** - Clean, intuitive web interface built with Streamlit
- **Fast Processing** - Quick extraction powered by Google Gemini AI

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key
- pip package manager

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/ai-bill-reading-system.git
cd ai-bill-reading-system
```

2. Install required packages
```bash
pip install -r requirements.txt
```

3. Set up your Gemini API key
```bash
export GEMINI_API_KEY='your-api-key-here'
```

4. Run the application
```bash
streamlit run app.py
```

5. Open your browser and navigate to `http://localhost:8501`

## 📦 Requirements

```
streamlit>=1.28.0
google-generativeai
Pillow
python-dotenv
```

## 💻 Usage

1. Launch the application
2. Upload a bill or receipt image (max 200MB)
3. Wait for AI processing
4. View extracted information displayed next to the image
5. Verify and use the extracted data

### Supported Image Formats

- JPEG/JPG
- PNG
- WebP
- BMP

## 🏗️ Architecture

```
┌─────────────────┐
│  User Interface │  (Streamlit)
└────────┬────────┘
         │
┌────────▼────────┐
│ Image Processing│
└────────┬────────┘
         │
┌────────▼────────┐
│   Gemini AI     │  (Google Gemini API)
└────────┬────────┘
         │
┌────────▼────────┐
│ Result Display  │
└─────────────────┘
```

## 🎯 Use Cases

- **Personal Finance** - Track expenses and manage personal budgets
- **Small Business** - Streamline invoice processing and record-keeping
- **Expense Reporting** - Quick digitization for reimbursement submissions
- **Inventory Management** - Extract quantity and item information

## ⚠️ Limitations

- Maximum file size: 200MB
- Requires clear, readable images for best results
- Internet connection required for AI processing
- Processing time varies based on image complexity

## 🔮 Future Enhancements

- [ ] Batch processing for multiple bills
- [ ] Export to CSV/Excel
- [ ] Database integration for historical tracking
- [ ] Multi-language support
- [ ] Mobile application
- [ ] Expense categorization and analytics

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Your Name - [JoyD58528](https://youtube.com/@Kleo-ul5ri)

Project Link: [https://github.com/joyd58528/Learning-python](https://github.com/joyd58528/Learning-python)

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) - Web framework
- [Google Gemini](https://deepmind.google/technologies/gemini/) - AI model
## 📞 Support

If you have any questions or run into issues, please open an issue on GitHub.

---

⭐ Star this repository if you find it helpful!