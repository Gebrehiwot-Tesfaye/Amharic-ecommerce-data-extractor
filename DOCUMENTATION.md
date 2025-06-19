# Amharic E-commerce Data Extractor - Complete Documentation

## Table of Contents

1. [Project Overview](#project-overview)
2. [Architecture](#architecture)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Usage](#usage)
6. [Data Collection](#data-collection)
7. [Data Preprocessing](#data-preprocessing)
8. [Model Training](#model-training)
9. [API Reference](#api-reference)
10. [Troubleshooting](#troubleshooting)
11. [Contributing](#contributing)

## Project Overview

The Amharic E-commerce Data Extractor is a comprehensive Named Entity Recognition (NER) system designed specifically for Ethiopian e-commerce data from Telegram channels. The project addresses the business need of EthioMart to consolidate and analyze data from multiple decentralized e-commerce channels.

### Key Features

- **Multi-channel Data Collection**: Automated scraping from 5+ Ethiopian Telegram e-commerce channels
- **Amharic Text Processing**: Specialized handling for Amharic linguistic features
- **Entity Recognition**: Extraction of products, prices, locations, and contact information
- **Model Fine-tuning**: Adaptation of transformer models for Amharic NER
- **Performance Analysis**: Comprehensive evaluation with F1-score, precision, recall
- **Explainable AI**: SHAP and LIME integration for model interpretability

### Business Impact

This system enables EthioMart to:

- Centralize e-commerce data from multiple Telegram channels
- Extract structured business information from unstructured Amharic text
- Identify vendor loan candidates based on extracted data
- Provide insights for business decision-making

## Architecture

### Project Structure

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

### Component Overview

#### 1. Data Collection (`src/data_collection/`)

**TelegramScraper Class**

- Handles authentication with Telegram API
- Collects messages from specified channels
- Downloads media attachments (images, documents)
- Implements rate limiting and error handling
- Stores data in structured format

**Key Methods:**

- `authenticate()`: Establish Telegram connection
- `collect_channel_data()`: Collect from specific channel
- `collect_all_channels()`: Collect from all configured channels
- `_process_message()`: Process individual messages
- `_process_media()`: Handle media attachments

#### 2. Data Preprocessing (`src/preprocessing/`)

**DataPreprocessor Class**

- Loads and validates raw data
- Applies text cleaning and normalization
- Implements quality control measures
- Prepares data for NER training
- Creates train/validation/test splits

**Key Methods:**

- `load_raw_data()`: Load collected data
- `clean_data()`: Apply cleaning operations
- `quality_control()`: Filter low-quality content
- `prepare_for_ner()`: Format for model training
- `split_data()`: Create data splits

#### 3. Utilities (`src/utils/`)

**ConfigLoader Class**

- Loads YAML configuration files
- Validates configuration structure
- Handles environment variable substitution
- Provides default values

**AmharicTextProcessor Class**

- Handles Amharic character detection
- Implements text normalization
- Extracts entities using regex patterns
- Calculates text statistics

## Installation

### Prerequisites

- Python 3.8 or higher
- Git
- Telegram API credentials (see Configuration section)

### Quick Installation

#### Linux/macOS

```bash
git clone <repository-url>
cd Amharic-ecommerce-data-extractor
chmod +x install.sh
./install.sh
```

#### Windows

```cmd
git clone <repository-url>
cd Amharic-ecommerce-data-extractor
install.bat
```

### Manual Installation

1. **Clone the repository**

```bash
git clone <repository-url>
cd Amharic-ecommerce-data-extractor
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Create directories**

```bash
mkdir -p data/{raw,processed,labeled,models}
mkdir -p logs notebooks reports plots tests
```

5. **Setup configuration**

```bash
cp config/config.example.yaml config/config.yaml
# Edit config.yaml with your credentials
```

## Configuration

### Telegram API Setup

1. **Get API Credentials**

   - Visit https://my.telegram.org
   - Log in with your phone number
   - Create a new application
   - Note your `api_id` and `api_hash`

2. **Configure the Application**
   - Edit `config/config.yaml`
   - Add your API credentials:
   ```yaml
   telegram:
     api_id: "YOUR_API_ID"
     api_hash: "YOUR_API_HASH"
     phone_number: "YOUR_PHONE_NUMBER"
   ```

### Channel Configuration

Add target Telegram channels to `config/config.yaml`:

```yaml
channels:
  - name: "Shageronlinestore"
    channel_id: "@shageronlinestore"
    description: "Ethiopian online store for electronics"
    category: "electronics"

  - name: "EthioMart"
    channel_id: "@ethiomart"
    description: "General Ethiopian marketplace"
    category: "general"
```

### Data Collection Settings

```yaml
data_collection:
  max_messages_per_channel: 1000
  message_limit: 100
  delay_between_requests: 1.0
  include_images: true
  include_documents: true
```

### Preprocessing Settings

```yaml
preprocessing:
  remove_emojis: true
  remove_urls: true
  remove_phone_numbers: false
  normalize_amharic: true
  max_length: 512
  min_amharic_ratio: 0.3
```

## Usage

### Quick Start

1. **Setup Configuration**

```bash
# Copy example configuration
cp config/config.example.yaml config/config.yaml

# Edit with your credentials
nano config/config.yaml
```

2. **Run Data Collection**

```bash
python run_data_collection.py
```

3. **Run Preprocessing Only**

```bash
python run_data_collection.py --skip-collection
```

4. **Create Example Configuration**

```bash
python run_data_collection.py --create-config
```

### Command Line Options

```bash
python run_data_collection.py [OPTIONS]

Options:
  --config PATH              Configuration file path
  --skip-collection          Skip data collection phase
  --skip-preprocessing       Skip preprocessing phase
  --create-config            Create example configuration
```

### Programmatic Usage

```python
from src.data_collection.telegram_scraper import TelegramScraper
from src.preprocessing.preprocess_data import DataPreprocessor

# Data Collection
scraper = TelegramScraper("config/config.yaml")
await scraper.authenticate()
all_data = await scraper.collect_all_channels()

# Data Preprocessing
preprocessor = DataPreprocessor("config/config.yaml")
processed_df, splits = preprocessor.run_preprocessing_pipeline()
```

## Data Collection

### Channel Selection

The system is configured to collect data from at least 5 Ethiopian e-commerce channels:

1. **Shageronlinestore** - Electronics and gadgets
2. **EthioMart** - General marketplace
3. **AddisFashion** - Fashion and clothing
4. **EthioElectronics** - Electronics and appliances
5. **AddisFood** - Food and beverage delivery
6. **EthioBooks** - Books and educational materials

### Data Types Collected

- **Text Messages**: Product descriptions, prices, contact information
- **Images**: Product photos, marketing materials
- **Documents**: Price lists, catalogs
- **Metadata**: Timestamps, channel information, message statistics

### Rate Limiting

The system implements intelligent rate limiting to avoid API restrictions:

- 1-second delay between requests
- Automatic handling of FloodWaitError
- Graceful error recovery

### Data Storage

Collected data is stored in multiple formats:

- **JSON**: Structured data with metadata
- **CSV**: Tabular format for analysis
- **Database**: SQLite for structured queries

## Data Preprocessing

### Text Cleaning Pipeline

1. **Normalization**

   - Unicode normalization (NFC)
   - Whitespace standardization
   - Common typo corrections

2. **Content Filtering**

   - Emoji removal
   - URL removal
   - Phone number handling (configurable)

3. **Language Detection**

   - Amharic character ratio calculation
   - Content filtering based on language

4. **Quality Control**
   - Length filtering
   - Entity density analysis
   - Duplicate detection

### Entity Extraction

The system extracts the following entity types:

- **PRODUCT**: Product names and categories
- **PRICE**: Monetary values in various currencies
- **LOCATION**: Geographic locations and delivery areas
- **MATERIAL**: Product materials and ingredients
- **DELIVERY_FEE**: Transaction costs
- **CONTACT_INFO**: Phone numbers and usernames

### Data Splitting

Data is split into three sets:

- **Training**: 70% of data
- **Validation**: 15% of data
- **Test**: 15% of data

Splits are stratified to ensure balanced representation across channels and entity types.

## Model Training

### Model Architectures

The system supports multiple transformer architectures:

1. **XLM-RoBERTa Base**

   - Multilingual model with good Amharic support
   - 512 token maximum length
   - Recommended for production use

2. **BERT Base Multilingual**

   - Original multilingual BERT
   - Good baseline performance
   - Smaller model size

3. **AfriBERTa**
   - African language specialized model
   - Optimized for African languages
   - Experimental support

### Training Configuration

```yaml
training:
  learning_rate: 2e-5
  batch_size: 16
  epochs: 10
  warmup_steps: 500
  weight_decay: 0.01
  patience: 3
  min_delta: 0.001
```

### Evaluation Metrics

- **F1-Score**: Primary metric for NER performance
- **Precision**: Accuracy of positive predictions
- **Recall**: Coverage of actual entities
- **Accuracy**: Overall prediction accuracy

## API Reference

### TelegramScraper

#### `__init__(config_path: str)`

Initialize the scraper with configuration.

#### `authenticate() -> bool`

Authenticate with Telegram API.

#### `collect_channel_data(channel_id: str, max_messages: int = None) -> List[Dict]`

Collect data from a specific channel.

#### `collect_all_channels() -> Dict[str, List[Dict]]`

Collect data from all configured channels.

### DataPreprocessor

#### `__init__(config_path: str)`

Initialize the preprocessor with configuration.

#### `load_raw_data() -> pd.DataFrame`

Load all raw data from collection phase.

#### `clean_data(df: pd.DataFrame) -> pd.DataFrame`

Clean and preprocess raw data.

#### `quality_control(df: pd.DataFrame) -> pd.DataFrame`

Apply quality control measures.

#### `prepare_for_ner(df: pd.DataFrame) -> Tuple[List[str], List[Dict]]`

Prepare data for NER model training.

### AmharicTextProcessor

#### `get_amharic_ratio(text: str) -> float`

Calculate ratio of Amharic characters in text.

#### `normalize_amharic_text(text: str) -> str`

Normalize Amharic text for consistency.

#### `clean_text(text: str, **kwargs) -> str`

Clean text with various options.

#### `extract_prices(text: str) -> List[Dict]`

Extract price information from text.

#### `extract_locations(text: str) -> List[Dict]`

Extract location information from text.

#### `extract_products(text: str) -> List[Dict]`

Extract product information from text.

## Troubleshooting

### Common Issues

#### 1. Authentication Errors

**Problem**: "Authentication failed"
**Solution**:

- Verify API credentials in config.yaml
- Ensure phone number includes country code
- Check internet connection

#### 2. Rate Limiting

**Problem**: "FloodWaitError"
**Solution**:

- Increase delay_between_requests in config
- Reduce max_messages_per_channel
- Wait for rate limit to reset

#### 3. Channel Access

**Problem**: "ChannelPrivateError"
**Solution**:

- Verify channel IDs are correct
- Ensure channels are public
- Check if you're a member of private channels

#### 4. Memory Issues

**Problem**: "Out of memory"
**Solution**:

- Reduce batch_size in preprocessing
- Process data in smaller chunks
- Increase system memory

#### 5. Unicode Issues

**Problem**: "UnicodeDecodeError"
**Solution**:

- Ensure files are saved with UTF-8 encoding
- Check Amharic text normalization
- Verify character encoding in data

### Debug Mode

Enable debug logging by modifying the logging level in config:

```yaml
logging:
  level: "DEBUG"
```

### Performance Optimization

1. **Data Collection**

   - Use multiple API sessions
   - Implement parallel processing
   - Optimize rate limiting

2. **Preprocessing**

   - Use multiprocessing for large datasets
   - Implement caching for repeated operations
   - Optimize regex patterns

3. **Model Training**
   - Use GPU acceleration
   - Implement gradient accumulation
   - Use mixed precision training

## Contributing

### Development Setup

1. **Fork the repository**
2. **Create feature branch**

```bash
git checkout -b feature/amazing-feature
```

3. **Install development dependencies**

```bash
pip install -e ".[dev]"
```

4. **Run tests**

```bash
pytest tests/
```

5. **Format code**

```bash
black src/
flake8 src/
```

6. **Submit pull request**

### Code Style

- Follow PEP 8 guidelines
- Use type hints
- Write comprehensive docstrings
- Add unit tests for new features

### Testing

Run the test suite:

```bash
pytest tests/ -v --cov=src
```

### Documentation

- Update README.md for user-facing changes
- Update DOCUMENTATION.md for technical changes
- Add docstrings for new functions
- Update API reference

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions, issues, or contributions:

- Create an issue on GitHub
- Contact the development team
- Join our community discussions
