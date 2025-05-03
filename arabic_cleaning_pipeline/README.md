# nlp-preprocessing-pipeline
A modular data cleaning pipeline for Arabic-language text datasets. This project is designed to preprocess, clean, and deduplicate raw input files. It is especially useful as a preprocessing step before Arabic NLP tasks like Named Entity Recognition (NER), topic modeling, or sentiment analysis.

📁 Project Structure

arabic_cleaning_pipeline/
├── data/
│   ├── raw/
│   │   └── your_input_file.csv           # Raw input files go here
│   └── processed/
│       └── civil_pii_cleaned.csv         # Cleaned and deduplicated output
│
├── src/
│   ├── __init__.py
│   ├── clean_pipeline.py                 # All preprocessing functions here
│   └── run_cleaning.py                   # Main script that runs the full pipeline
│
├── notebooks/
│   └── exploratory_analysis.ipynb        # for data exploration/testing
│
├── requirements.txt                      # required Python packages
├── README.md                             # Project overview and usage
└── .gitignore                            # Ignore .csv, .ipynb_checkpoints.

🧠 Features

Unicode normalization for Arabic text (e.g., replacing 'أ', 'إ', and 'آ' with 'ا')

Removal of emojis and diacritics

Whitespace and special character normalization

Deduplication of entries

Modular and extensible code

🚀 Getting Started

1. Install dependencies

pip install -r requirements.txt

2. Add your data

Place your raw .csv input file in:

data/raw/your_input_file.csv

3. Run the pipeline

python src/run_cleaning.py

The cleaned output will be saved to:

data/processed/civil_pii_cleaned.csv

🧪 Notebook

To interactively explore and test the pipeline, open the notebook:

notebooks/exploratory_analysis.ipynb

You can visualize samples and debug issues here.

🛠️ Customization

All preprocessing logic is in src/clean_pipeline.py. You can:

Add new cleaning functions

Adjust normalization rules

Plug in additional filtering (e.g., regex, stopwords)

