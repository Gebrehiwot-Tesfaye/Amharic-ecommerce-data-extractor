# Amharic E-commerce Data Extractor

## Project Overview

This project implements a comprehensive Named Entity Recognition (NER) system for Amharic e-commerce data extraction from Telegram channels. The system is designed to support EthioMart's vision of becoming the primary hub for all Telegram-based e-commerce activities in Ethiopia.

### Business Context

EthioMart aims to consolidate real-time data from multiple e-commerce Telegram channels into one unified platform, providing seamless customer experience for exploring and interacting with multiple vendors. This NER system extracts key business entities such as:

- **Product Names/Types**: Specific product identifiers and categories
- **Material/Ingredients**: Materials used in products
- **Location Mentions**: Geographic locations and delivery areas
- **Monetary Values/Prices**: Product pricing information
- **Delivery Fees**: Transaction costs beyond product price
- **Contact Information**: Phone numbers and Telegram usernames

### Key Objectives

1. **Data Collection & Preprocessing**: Automated ingestion from Telegram channels
2. **Data Labeling**: High-quality NER annotations for Amharic text
3. **Model Fine-tuning**: Transformer-based models for Amharic NER
4. **Model Comparison**: Systematic evaluation of different approaches
5. **Model Interpretability**: SHAP/LIME analysis for explainable AI

## Project Structure

```
Amharic-ecommerce-data-extractor/
├── data/                          # Data storage
│   ├── raw/                      # Raw scraped data
│   ├── processed/                # Preprocessed data
│   ├── labeled/                  # Manually labeled data
│   └── models/                   # Trained models
├── src/                          # Source code
│   ├── data_collection/          # Telegram scraping modules
│   ├── preprocessing/            # Data cleaning and preparation
│   ├── labeling/                 # Data annotation tools
│   ├── models/                   # NER model implementations
│   ├── evaluation/               # Model evaluation scripts
│   └── utils/                    # Utility functions
├── notebooks/                    # Jupyter notebooks for analysis
├── config/                       # Configuration files
├── tests/                        # Unit tests
├── logs/                         # Application logs
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## Features

- **Multi-channel Data Collection**: Automated scraping from 5+ Ethiopian Telegram e-commerce channels
- **Amharic Text Processing**: Specialized handling for Amharic linguistic features
- **Entity Recognition**: Extraction of products, prices, locations, and contact info
- **Model Fine-tuning**: Adaptation of transformer models for Amharic NER
- **Performance Analysis**: Comprehensive evaluation with F1-score, precision, recall
- **Explainable AI**: SHAP and LIME integration for model interpretability

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd Amharic-ecommerce-data-extractor
```

2. Create and activate virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up configuration:

```bash
cp config/config.example.yaml config/config.yaml
# Edit config.yaml with your Telegram API credentials
```

## Usage

### Data Collection

```bash
python src/data_collection/telegram_scraper.py
```

### Data Preprocessing

```bash
python src/preprocessing/preprocess_data.py
```

### Model Training

```bash
python src/models/train_ner_model.py
```

### Model Evaluation

```bash
python src/evaluation/evaluate_models.py
```

## Configuration

The system uses YAML configuration files for:

- Telegram API credentials
- Target channel IDs
- Model hyperparameters
- Data processing settings

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or support, please contact the development team.
