---
title: AI Red teamer
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - ai
  - red team
---

# AI Red teamer

## Setup

### Miniconda 
Miniconda is a minimal installer for the Anaconda distribution of the Python programming language. It provides the conda package manager and a core Python environment without automatically installing the full suite of data science libraries available in Anaconda.

```powershell
# Windows
# Allow scripts to run
Set-ExecutionPolicy RemoteSigned -scope CurrentUser

# First, install Scoop. Open PowerShell and run:
irm get.scoop.sh | iex

# Next, add the extras bucket, which contains Miniconda:
scoop bucket add extras

# Finally, install Miniconda. This command installs the latest Python 3 version of Miniconda:
scoop install miniconda3

conda --version
```

```bash
# MacOS
# If you don't have Homebrew, install it first by pasting the following command in your terminal:
/bin/bash -c "$(curl -fsSL  https://raw.githubusercontent.com/Homebrew/install/HEAD/install"

# Once Homebrew is set up, you can install Miniconda with this simple command:
brew install --cask miniconda

conda --version
```

```bash
# Linux
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

chmod +x Miniconda3-latest-Linux-x86_64.sh

./Miniconda3-latest-Linux-x86_64.sh -b -u

eval "$(/home/$USER/miniconda3/bin/conda shell.$(ps -p $$ -o comm=) hook)"

conda --version
```


Init the project:

```bash
# To initialize conda for your shell, run the following command after installing Miniconda:
conda init zsh
# This command will modify your shell configuration files (e.g., .bashrc or .zshrc) to include the necessary conda settings. You might need to close and reopen your terminal for the changes to take effect.
```

Finally, run these two commands to complete the init process:

```bash
conda config --add channels defaults

conda config --add channels conda-forge

conda config --add channels conda-forge

conda config --add channels pytorch

conda config --set channel_priority strict
```

After installing Miniconda, you'll notice that the base environment is activated by default every time you open a new terminal. This is indicated by the (base) prefix on your path.

To prevent the base environment from activating automatically, you can use the following command:

```bash
conda config --set auto_activate_base false
```


conda provides a simple way to create virtual environments. For example, to create a new environment named ai with Python 3.11, use the following command:

```bash
conda create -n ai python=3.11
```

This will create a virtual environment, ai, which can then be used to contain all ai-related packages.

Activating the Environment:

```bash
conda activate ai
```

To deactivate the environment, use:

```bash
conda deactivate
```

### Dependencies

Use the `conda install` command to install the following core packages:

```bash
conda install -y numpy scipy pandas scikit-learn matplotlib seaborn transformers datasets tokenizers accelerate evaluate optimum huggingface_hub nltk category_encoders

conda install -y pytorch torchvision torchaudio pytorch-cuda=12.4 -c pytorch -c nvidia

pip install requests requests_toolbelt
```

Updates:

```bash
conda update --all
```

### Install # JupyterLab

[Documentation](https://jupyterlab.readthedocs.io/en/latest/getting_started/overview.html).

Make sure you are running the command from within your ai environment.

```bash
conda install -y jupyter jupyterlab notebook ipykernel
```

To start Jupyter:

```bash
jupyter lab
```

`JupyterLab`'s primary component is the notebook, which allows combining code, text, and visualizations in a single document. Notebooks are organized into cells, where each cell can contain either code or markdown text.

- `Code cells`: Execute code in various languages (Python, R, Julia).
- `Markdown cells`: Create formatted text, equations, and images using markdown syntax.
- `Raw cells`: Untyped raw text.

Click the "Python 3" icon under the "Notebook" section in the Launcher interface to create a new notebook. This will open a notebook with a single empty code cell.

![[jupyter_001.png]]

![[jupyter_002.png]]

Type your Python code into the code cell and press Shift + Enter to execute it. For example:

```python
print("Hello, JupyterLab!")
```

The output of the code will appear below the cell.

`JupyterLab` integrates with libraries like `pandas`, `matplotlib`, and `seaborn` for data exploration and visualization. Here's an example of loading a dataset with `pandas` and creating a simple plot:

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a sample DataFrame
data = pd.DataFrame({
    "column1": np.random.rand(50),  # 50 random values for column1
    "column2": np.random.rand(50) * 10  # 50 random values (multiplied by 10) for column2
})

# Display the first few rows
print(data.head())

# Create a scatter plot
plt.scatter(data["column1"], data["column2"])
plt.xlabel("Column 1")
plt.ylabel("Column 2")
plt.title("Scatter Plot")
plt.show()
```

`JupyterLab` uses a `kernel` to run your code. The `kernel` is a separate process responsible for executing code and maintaining the state of your computations. Sometimes, you may need to reset your environment if it becomes cluttered with variables or you encounter unexpected behavior.

To restart the `kernel`:

1. Open the `Kernel` menu in the top toolbar.
2. Select `Restart Kernel` to reset the environment while preserving cell outputs, or `Restart Kernel and Clear All Outputs` to also remove all previously generated outputs from the notebook.

### Python Libraries for AI

 This section focuses on two prominent Python libraries for AI development: `Scikit-learn` and `PyTorch`.

#### Scikit-learn

`Scikit-learn` is a comprehensive library built on `NumPy`, `SciPy`, and `Matplotlib`. It offers a wide range of algorithms and tools for machine learning tasks and provides a consistent and intuitive API, making implementing various machine learning models easy.

- `Supervised Learning:` `Scikit-learn` provides a vast collection of supervised learning algorithms, including:
    - `Linear Regression`
    - `Logistic Regression`
    - `Support Vector Machines (SVMs)`
    - `Decision Trees`
    - `Naive Bayes`
    - `Ensemble Methods` (e.g., Random Forests, Gradient Boosting)
- `Unsupervised Learning:` It also offers various unsupervised learning algorithms, such as:
    - `Clustering` (K-Means, DBSCAN)
    - `Dimensionality Reduction` (PCA, t-SNE)
- `Model Selection and Evaluation:` `Scikit-learn` includes tools for model selection, hyperparameter tuning, and performance evaluation, enabling developers to optimize their models effectively.
- `Data Preprocessing:` It provides functionalities for data preprocessing, including:
    - Feature scaling and normalization
    - Handling missing values
    - Encoding categorical variables


`Scikit-learn` provides various scaling techniques:

- `StandardScaler` : Standardizes features by removing the mean and scaling to unit variance.
- `MinMaxScaler` : Scales features to a given range, typically between 0 and 1.
- `RobustScaler` : Scales features using statistics that are robust to outliers.

```python
from sklearn.preprocessing import StandardScaler 

scaler = StandardScaler() 
X_scaled = scaler.fit_transform(X)
```


`Scikit-learn` offers encoding techniques:

- `OneHotEncoder` : Creates binary (0 or 1) columns for each category.
- `LabelEncoder` : Assigns a unique integer to each category.

```python
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder()
X_encoded = encoder.fit_transform(X)
```

Real-world datasets often contain missing values. `Scikit-learn` provides methods to handle these missing values:

- `SimpleImputer` : Replaces missing values with a specified strategy (e.g., mean, median, most frequent).
- `KNNImputer` : Imputes missing values using the k-Nearest Neighbors algorithm.

```python
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)
```


`Scikit-learn` offers tools for selecting the best model and evaluating its performance. Splitting data into training and testing sets is crucial to evaluating the model's generalization ability to unseen data.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

Cross-validation provides a more robust evaluation by splitting the data into multiple folds and training/testing on different combinations.

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5)
```

`Scikit-learn` provides various **metrics** to evaluate model performance:

- `accuracy_score` : For classification tasks.
- `mean_squared_error` : For regression tasks.
- `precision_score`, `recall_score`, `f1_score` : For classification tasks with imbalanced classes.

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
```

**Model Training and Prediction**: Scikit-learn follows a consistent API for training and predicting with different models. Create an instance of the desired model with appropriate hyperparameters.

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(C=1.0)
```

Train the model using the fit() method with the training data.

```python
model.fit(X_train, y_train)
```

Make predictions on new data using the predict() method.

```python
y_pred = model.predict(X_test)
```


#### PyTorch

PyTorch is an open-source machine learning library developed by Facebook's AI Research lab. It provides a flexible and powerful framework for building and deploying various types of machine learning models, including deep learning models.

- `Deep Learning:` `PyTorch` excels in deep learning, enabling the development of complex neural networks with multiple layers and architectures.
- `Dynamic Computational Graphs:` Unlike static computational graphs used in libraries like TensorFlow, `PyTorch` uses dynamic computational graphs, which allow for more flexible and intuitive model building and debugging.
- `GPU Support:` `PyTorch` supports GPU acceleration, significantly speeding up the training process for computationally intensive models.
- `TorchVision Integration:` `TorchVision` is a library integrated with `PyTorch` that provides a user-friendly interface for image datasets, pre-trained models, and common image transformations.
- `Automatic Differentiation:` `PyTorch` uses `autograd` to automatically compute gradients, simplifying the process of backpropagation.
- `Community and Ecosystem:` `PyTorch` has a large and active community, leading to a rich ecosystem of tools, libraries, and resources.


`Tensors` are multi-dimensional arrays that hold the data being processed. They can be constants, variables, or placeholders. `PyTorch` tensors are similar to NumPy arrays but can run on GPUs for faster computation.

```python
import torch

# Creating a tensor
x = torch.tensor([1.0, 2.0, 3.0])

# Tensors can be moved to GPU if available
if torch.cuda.is_available():
    x = x.to('cuda')
```

`PyTorch` provides a flexible and intuitive interface for building and training deep learning models. The `torch.nn` module contains various layers and modules for constructing neural networks.

The Sequential API allows building models layer by layer, adding each layer sequentially.

```python
import torch.nn as nn

model = nn.Sequential(
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10),
    nn.Softmax(dim=1)
)
```

The `Module` class provides more flexibility for building complex models with non-linear topologies, shared layers, and multiple inputs/outputs.

```python
import torch.nn as nn

class CustomModel(nn.Module):
    def __init__(self):
        super(CustomModel, self).__init__()
        self.layer1 = nn.Linear(784, 128)
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(128, 10)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        x = self.layer1(x)
        x = self.relu(x)
        x = self.layer2(x)
        x = self.softmax(x)
        return x

model = CustomModel()
```


`PyTorch` provides tools for training and evaluating models.

`Optimizers` are algorithms that adjust the model's parameters during training to minimize the loss function. `PyTorch` offers various optimizers:

- `Adam`
- `SGD` (Stochastic Gradient Descent)
- `RMSprop`

```python
import torch.optim as optim

optimizer = optim.Adam(model.parameters(), lr=0.001)
```

`Loss Functions` measure the difference between the model's predictions and the actual target values. `PyTorch` provides a variety of loss functions:

- `CrossEntropyLoss` : For multi-class classification.
- `BCEWithLogitsLoss` : For binary classification.
- `MSELoss` : For regression.

```python
        python
import torch.nn as nn

loss_fn = nn.CrossEntropyLoss()
```

The training loop updates the model's parameters based on the training data.

```python
import torch

epochs = 10
num_batches = 100

for epoch in range(epochs):
    for batch in range(num_batches):
        # Get batch of data
        x_batch, y_batch = get_batch(batch)
        
        # Forward pass
        y_pred = model(x_batch)
        
        # Calculate loss
        loss = loss_fn(y_pred, y_batch)
        
        # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        # Optional: print loss or other metrics
        if batch % 10 == 0:
            print(f'Epoch [{epoch+1}/{epochs}], Batch [{batch+1}/{num_batches}], Loss: {loss.item():.4f}')
```

`PyTorch` provides the `torch.utils.data.Dataset` and `DataLoader` classes for handling data loading and preprocessing.

```python
from torch.utils.data import Dataset, DataLoader

class CustomDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]

# Example usage
dataset = CustomDataset(data, labels)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
```

PyTorch allows models to be saved and loaded for inference or further training.

```python
# Save model
torch.save(model.state_dict(), 'model.pth')

# Load model
model = CustomModel()
model.load_state_dict(torch.load('model.pth'))
model.eval()  # Set the model to evaluation mode
```

## Datasets

`Datasets` are structured collections of data used for analysis and model training. They come in various forms, including:

- `Tabular Data`: Data organized into tables with rows and columns, common in spreadsheets or databases.
- `Image Data`: Sets of images represented numerically as pixel arrays.
- `Text Data`: Unstructured data composed of sentences, paragraphs, or full documents.
- `Time Series Data`: Sequential data points collected over time, emphasizing temporal patterns.

The quality of a dataset is fundamental to the success of any data analysis or machine learning project. Here’s why:

- `Model Accuracy`: High-quality datasets produce more accurate models. Poor-quality data—such as noisy, incomplete, or biased datasets—leads to reduced model performance.
- `Generalization`: Carefully curated datasets enable models to generalize effectively to unseen data. This minimizes overfitting and ensures consistent performance in real-world applications.
- `Efficiency`: Clean, well-prepared data reduces both training time and computational demands, streamlining the entire process.
- `Reliability`: Reliable datasets lead to trustworthy insights and decisions. In critical domains like healthcare or finance, data quality directly affects the dependability of results.

### Preparing the dataset 

We have a dataset named demo_dataset.csv

```csv
log_id	source_ip	destination_port	protocol	bytes_transferred	threat_level
1	10	10.0.0.100	STRING_PORT	FTP	4096	?
2	12	172.16.254.100	110	POP3	NEGATIVE	1
3	27	172.16.254.200	110	POP3	NON_NUMERIC	1
4	1	192.168.1.100	80	HTTP	1024	0
5	2	192.168.1.81	53	TLS	9765	0
6	3	192.168.1.147	80	SSH	1296	1
7	4	192.168.1.94	22	POP3	7185	0
8	5	192.168.1.55	110	DNS	5088	2
9	6	192.168.1.171	443	HTTPS	5989	2
10	7	192.168.1.196	22	SMTP	3166	2
11	8	192.168.1.67	443	HTTP	8279	1
12	9	192.168.1.66	22	SSH	6124	0
13	11	192.168.1.55	80	TLS	1003	1
14	13	192.168.1.84	80	DNS	4138	2
15	14	192.168.1.160	80	HTTP	7480	0
16	15	192.168.1.232	22	SMTP	6571	1
....
```

We first load it into a `pandas DataFrame` to begin working with the dataset. A `pandas DataFrame` is a flexible, two-dimensional labeled data structure that supports a variety of operations for data exploration and preprocessing.

```python
import pandas as pd

# Load the dataset
data = pd.read_csv("./demo_dataset.csv")
```

In this code, `pd.read_csv("./demo_dataset.csv")` loads the downloaded CSV file into a DataFrame named `data`. From here, inspecting, manipulating, and preparing the dataset for further steps in the analysis pipeline becomes straightforward.

Viewing Sample Entries:

```python
# Display the first few rows of the dataset
print(data.head())
```

Inspecting Data Structure and Types

```python
# Get a summary of column data types and non-null counts
print(data.info())
```

The `info()` method reveals the dataset's shape, column names, data types, and how many entries are present for each column, enabling early detection of columns with missing or unexpected data.

Checking for Missing Values:

```python
# Identify columns with missing values
print(data.isnull().sum())
```

This command returns the count of null values for each column, helping to prioritize which features need attention. Addressing these missing values may involve imputation, removal, or other cleaning strategies to ensure the dataset remains reliable and valid for further analysis.

![[jupyter_003.png]]


`Data preprocessing` transforms raw data into a suitable format for machine learning algorithms. Key techniques include:

- `Data Cleaning`: Handling missing values, removing duplicates, and smoothing noisy data.
- `Data Transformation`: Normalizing, encoding, scaling, and reducing data.
- `Data Integration`: Merging and aggregating data from multiple sources.
- `Data Formatting`: Converting data types and reshaping data structures.


Checking for Invalid IP Addresses:

```python
import re

def is_valid_ip(ip):
    pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    return bool(pattern.match(ip))

# Check for invalid IP addresses
invalid_ips = data[~data['source_ip'].astype(str).apply(is_valid_ip)]
print(invalid_ips)
```


Checking for Invalid Port Numbers:

```python
def is_valid_port(port):
    try:
        port = int(port)
        return 0 <= port <= 65535
    except ValueError:
        return False

# Check for invalid port numbers
invalid_ports = data[~data['destination_port'].apply(is_valid_port)]
print(invalid_ports)
```


Checking for Invalid Protocol Values:

```python
valid_protocols = ['TCP', 'TLS', 'SSH', 'POP3', 'DNS', 'HTTPS', 'SMTP', 'FTP', 'UDP', 'HTTP']

# Check for invalid protocol values
invalid_protocols = data[~data['protocol'].isin(valid_protocols)]
print(invalid_protocols)
```

Checking for Invalid Bytes Transferred:

```python
def is_valid_bytes(bytes):
    try:
        bytes = int(bytes)
        return bytes >= 0
    except ValueError:
        return False

# Check for invalid bytes transferred
invalid_bytes = data[~data['bytes_transferred'].apply(is_valid_bytes)]
print(invalid_bytes)
```

Checking for Invalid Threat Levels:

```python
def is_valid_threat_level(threat_level):
    try:
        threat_level = int(threat_level)
        return 0 <= threat_level <= 2
    except ValueError:
        return False

# Check for invalid threat levels
invalid_threat_levels = data[~data['threat_level'].apply(is_valid_threat_level)]
print(invalid_threat_levels)
```


#### Strategy 1: Dropping Invalid Entries

The most straightforward approach is to discard the invalid entries entirely. This ensures that the remaining dataset is clean and free of potentially misleading information.

```python
# the ignore errors covers the fact that there might be some overlap between indexes that match other invalid criteria
data = data.drop(invalid_ips.index, errors='ignore') 
data = data.drop(invalid_ports.index, errors='ignore')
data = data.drop(invalid_protocols.index, errors='ignore')
data = data.drop(invalid_bytes.index, errors='ignore')
data = data.drop(invalid_threat_levels.index, errors='ignore')

print(data.describe(include='all'))
```


This method is generally preferred when data accuracy is paramount, and the loss of some data points does not significantly compromise the overall analysis. However, it may not always be feasible, especially if the dataset is small or the invalid entries constitute a substantial portion of the data.

After dropping the bad data from our dataset, we are only left with 77 clean entries.

#### Strategy 2: Imputing Missing Values

`Imputing` is the process of replacing missing or invalid values in a dataset with estimated values. This is crucial for maintaining the integrity and usability of the data, especially in machine learning and data analysis tasks where missing values can lead to biased or inaccurate results.

First, convert all invalid or corrupted entries, such as `MISSING_IP`, `INVALID_IP`, `STRING_PORT`, `UNUSED_PORT`, `NON_NUMERIC`, or `?`, into `NaN`. This approach standardizes the representation of missing values, enabling uniform downstream imputation steps.

```python
import pandas as pd
import numpy as np
import re
from ipaddress import ip_address

df = pd.read_csv('demo_dataset.csv')

invalid_ips = ['INVALID_IP', 'MISSING_IP']
invalid_ports = ['STRING_PORT', 'UNUSED_PORT']
invalid_bytes = ['NON_NUMERIC', 'NEGATIVE']
invalid_threat = ['?']

df.replace(invalid_ips + invalid_ports + invalid_bytes + invalid_threat, np.nan, inplace=True)

df['destination_port'] = pd.to_numeric(df['destination_port'], errors='coerce')
df['bytes_transferred'] = pd.to_numeric(df['bytes_transferred'], errors='coerce')
df['threat_level'] = pd.to_numeric(df['threat_level'], errors='coerce')

def is_valid_ip(ip):
    pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?\d?\d)\.){3}(25[0-5]|2[0-4]\d|[01]?\d?\d)$')
    if pd.isna(ip) or not pattern.match(str(ip)):
        return np.nan
    return ip

df['source_ip'] = df['source_ip'].apply(is_valid_ip)
```

After this step, `NaN` represents all missing or invalid data points.

![[jupyter_004.png]]

For basic numeric columns like `bytes_transferred`, use simple methods such as the median or mean. For categorical columns like `protocol`, use the most frequent value.

#### Strategy 3: meaningful imputations

For more sophisticated scenarios, employ advanced techniques like `KNNImputer` or `IterativeImputer`. These methods consider relationships among features to produce contextually meaningful imputations.

```python
from sklearn.impute import KNNImputer

knn_imputer = KNNImputer(n_neighbors=5)
df[numeric_cols] = knn_imputer.fit_transform(df[numeric_cols])
```

After cleaning and imputations, apply domain knowledge. For `source_ip` values that remain missing, assign a default such as `0.0.0.0`. Validate `protocol` values against known valid protocols. For ports, ensure values fall within the valid range `0-65535`, and for protocols that imply certain ports, consider mode-based assignments or domain-specific mappings.

```python
valid_protocols = ['TCP', 'TLS', 'SSH', 'POP3', 'DNS', 'HTTPS', 'SMTP', 'FTP', 'UDP', 'HTTP']
df.loc[~df['protocol'].isin(valid_protocols), 'protocol'] = df['protocol'].mode()[0]

df['source_ip'] = df['source_ip'].fillna('0.0.0.0')
df['destination_port'] = df['destination_port'].clip(lower=0, upper=65535)
```

Perform final verification steps to confirm that distributions are reasonable and categorical sets remain valid. Adjust imputation strategies and transformations or remove problematic records if anomalies persist.

```python
print(df.describe(include='all'))
```


### Data transformation

#### Encoding

Encoding converts categorical values into numeric form so machine learning algorithms can utilize these features. Depending on the situation, you can choose:

- `OneHotEncoder` for binary indicator features that represent each category separately.
- `LabelEncoder` for integer codes, though this may imply unintended order.
- `HashingEncoder` or frequency-based methods to handle high-cardinality features and control feature space size.

**One-Hot Encoding**

This process creates a set of indicator columns that hold `1` or `0`, indicating the presence or absence of a particular category in each row.

>For example, consider the categorical feature `color`, which can take on the values `red`, `green`, or `blue`. In a dataset, you might have rows where `color` is `red` in one instance, `green` in another, and so on. By applying `one-hot encoding`, instead of keeping a single column with values like `red`, `green`, or `blue`, the encoding creates three new binary columns:
>
>- `color_red`
>- `color_green`
>- `color_blue`
>
>Each of these new columns corresponds to one of the original categories. If a row had `color` set to `red`, the `color_red` column for that row would be `1`.


In this case, we are going to encode the `protocol` feature.

```python
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
encoded = encoder.fit_transform(df[['protocol']])

encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(['protocol']))
df = pd.concat([df.drop('protocol', axis=1), encoded_df], axis=1)
```

The original `protocol` feature is replaced with distinct binary columns, ensuring the model interprets each category independently.

## Phising site

### Downloading and extracting the Dataset

```python
import requests
import zipfile
import io
import os

# URL of the dataset
url = "https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip"
# Download the dataset
response = requests.get(url)
if response.status_code == 200:
    print("Download successful")
else:
    print("Failed to download the dataset")

# After downloading the dataset, we need to extract its contents. The dataset is provided in a .zip file format, which we will handle using Python's zipfile and io libraries. Extract the dataset:
with zipfile.ZipFile(io.BytesIO(response.content)) as z:
    z.extractall("sms_spam_collection")
    print("Extraction successful")
    
# List the extracted files
extracted_files = os.listdir("sms_spam_collection")
print("Extracted files:", extracted_files)
```


### Loading the Dataset

```python
import pandas as pd

# Load the dataset
# Here, we specify that the file is tab-separated (sep="\t"), and since the file does not contain a header row, we set header=None and provide column names manually using the names parameter.
df = pd.read_csv(
    "sms_spam_collection/SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "message"],
)
```

After loading the dataset, it is important to inspect it for basic information, missing values, and duplicates. This helps ensure that the data is clean and ready for analysis.

```python
# Display basic information about the dataset. To get an overview of the dataset, we can use the `head`, `describe`, and info `methods` provided by pandas.
print("-------------------- HEAD --------------------")
print(df.head())
print("-------------------- DESCRIBE --------------------")
print(df.describe())
print("-------------------- INFO --------------------")
print(df.info())

# Checking for missing values is crucial to ensure that our dataset does not contain any incomplete entries.
print("Missing values:\n", df.isnull().sum())

# Check for duplicates
print("Duplicate entries:", df.duplicated().sum())

# Remove duplicates if any
df = df.drop_duplicates()
```


### Preprocessing the dataset

The steps outlined here rely on the `nltk` library for tasks such as tokenization, stop word removal, and stemming. Before processing any text, you must download the required NLTK data files. These include `punkt` for tokenization and `stopwords` for removing common words that do not contribute to meaning.

```python
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download the necessary NLTK data files
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

print("=== BEFORE ANY PREPROCESSING ===") 
print(df.head(5))

# Convert all message text to lowercase. `Lowercasing the text` ensures that the classifier treats words equally, regardless of their original casing.
df["message"] = df["message"].str.lower()
print("\n=== AFTER LOWERCASING ===")
print(df["message"].head(5))

# Removing Punctuation and Numbers. Remove non-essential punctuation and numbers, keep useful symbols like $ and !
df["message"] = df["message"].apply(lambda x: re.sub(r"[^a-z\s$!]", "", x))
print("\n=== AFTER REMOVING PUNCTUATION & NUMBERS (except $ and !) ===")
print(df["message"].head(5))

# Tokenizing the Text. Tokenization divides the message text into individual words or tokens, a crucial step before further analysis. Each token corresponds to a meaningful unit
# Split each message into individual tokens
df["message"] = df["message"].apply(word_tokenize)
print("\n=== AFTER TOKENIZATION ===")
print(df["message"].head(5))

# Removing Stop Words. `Stop words` are common words like `and`, `the`, or `is` that often do not add meaningful context.
# Define a set of English stop words and remove them from the tokens
stop_words = set(stopwords.words("english"))
df["message"] = df["message"].apply(lambda x: [word for word in x if word not in stop_words])
print("\n=== AFTER REMOVING STOP WORDS ===")
print(df["message"].head(5))


# Stem each token to reduce words to their base form. Stemming normalizes words by reducing them to their base form (e.g., running becomes run).
stemmer = PorterStemmer()
df["message"] = df["message"].apply(lambda x: [stemmer.stem(word) for word in x])
print("\n=== AFTER STEMMING ===")
print(df["message"].head(5))


# Joining Tokens Back into a Single String. While tokens are useful for manipulation, many machine-learning algorithms and vectorization techniques (e.g., TF-IDF) work best with raw text strings. Rejoining the tokens into a space-separated string restores a format compatible with these methods, allowing the dataset to move seamlessly into the feature extraction phase.
# Rejoin tokens into a single string for feature extraction
df["message"] = df["message"].apply(lambda x: " ".join(x))
print("\n=== AFTER JOINING TOKENS BACK INTO STRINGS ===")
print(df["message"].head(5))
```

At this point, the messages are fully preprocessed. Each message is a cleaned, normalized string ready for vectorization and subsequent model training, ultimately improving the classifier’s performance.


### Feature Extraction

`Feature extraction` transforms preprocessed SMS messages into numerical vectors suitable for machine learning algorithms. A common way to represent text numerically is through a `bag-of-words` model. `CountVectorizer` from the `scikit-learn` library efficiently implements the bag-of-words approach. It converts a collection of documents into a matrix of term counts, where each row represents a message and each column corresponds to a term (unigram or bigram). Before transformation, `CountVectorizer` applies tokenization, builds a vocabulary, and then maps each document to a numeric vector.

Key parameters for refining the feature set:

- `min_df=1`: A term must appear in at least one document to be included. While this threshold is set to `1` here, higher values can be used in practice to exclude rare terms.
- `max_df=0.9`: Terms that appear in more than 90% of the documents are excluded, removing overly common words that provide limited differentiation.
- `ngram_range=(1, 2)`: The feature matrix captures individual words and common word pairs by including unigrams and bigrams, potentially improving the model’s ability to detect spam patterns.

```python
from sklearn.feature_extraction.text import CountVectorizer

# Initialize CountVectorizer with bigrams, min_df, and max_df to focus on relevant terms
vectorizer = CountVectorizer(min_df=1, max_df=0.9, ngram_range=(1, 2))

# Fit and transform the message column
X = vectorizer.fit_transform(df["message"])

# Labels (target variable)
y = df["label"].apply(lambda x: 1 if x == "spam" else 0)  # Converting labels to 1 and 0
```

After this step, `X` becomes a numerical feature matrix ready to be fed into a classifier, such as Naive Bayes.

### Training

After preprocessing the text data and extracting meaningful features, we train a machine-learning model for spam detection. We use the `Multinomial Naive Bayes` classifier. To streamline the entire process, we employ a `Pipeline`. A pipeline chains together the vectorization and modeling steps, ensuring that the same data transformation (in this case, `CountVectorizer`) is consistently applied before feeding the transformed data into the classifier.

```python
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Build the pipeline by combining vectorization and classification
pipeline = Pipeline([
    ("vectorizer", vectorizer),
    ("classifier", MultinomialNB())
])
```

With the pipeline in place, we can easily integrate hyperparameter tuning to improve model performance. The objective is to find optimal parameter values for the classifier, ensuring that the model generalizes well and avoids overfitting.

To achieve this, we use `GridSearchCV`. This method systematically searches through specified hyperparameter values to identify the configuration that produces the best performance. In the case of `MultinomialNB`, we focus on the `alpha` parameter, a smoothing factor that adjusts how the model handles unseen words and prevents probabilities from being zero. We can balance bias and variance by tuning `alpha`, ultimately improving the model’s robustness.

```python
# Define the parameter grid for hyperparameter tuning
param_grid = {
    "classifier__alpha": [0.01, 0.1, 0.15, 0.2, 0.25, 0.5, 0.75, 1.0]
}

# Perform the grid search with 5-fold cross-validation and the F1-score as metric
grid_search = GridSearchCV(
    pipeline,
    param_grid,
    cv=5,
    scoring="f1"
)

# Fit the grid search on the full dataset
grid_search.fit(df["message"], y)

# Extract the best model identified by the grid search
best_model = grid_search.best_estimator_
print("Best model parameters:", grid_search.best_params_)
```


The combination of `Pipeline` and `GridSearchCV` ensures a clean, consistent workflow. First, `CountVectorizer` converts raw text into numeric features suitable for the classifier. Next, `MultinomialNB` applies its probabilistic principles to distinguish between spam and ham messages.

Finally, by evaluating `alpha` values and leveraging cross-validation, we reliably select the best configuration based on the F1-score, a balanced metric for precision and recall.



## Other example

```python
# Example SMS messages for evaluation
new_messages = [
    "Congratulations! You've won a $1000 Walmart gift card. Go to http://bit.ly/1234 to claim now.",
    "Hey, are we still meeting up for lunch today?",
    "Urgent! Your account has been compromised. Verify your details here: www.fakebank.com/verify",
    "Reminder: Your appointment is scheduled for tomorrow at 10am.",
    "FREE entry in a weekly competition to win an iPad. Just text WIN to 80085 now!",
]     
```


Preprocessing New Messages

```python
# Preprocessing New Messages
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk
import re

# Download NLTK resources (only needed once)
nltk.download("punkt")
nltk.download("stopwords")

# Initialize
stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()

# Preprocess function that mirrors the training-time preprocessing
def preprocess_message(message):
    message = message.lower()
    message = re.sub(r"[^a-z\s$!]", "", message)
    tokens = word_tokenize(message)
    tokens = [word for word in tokens if word not in stop_words]
    tokens = [stemmer.stem(word) for word in tokens]
    return " ".join(tokens)
    
    
# Next, we apply this function to each of the new messages:
# Preprocess and vectorize messages
processed_messages = [preprocess_message(msg) for msg in new_messages]
```

Vectorizing the Processed Messages:

```python
# The model expects numerical input features. To achieve this, we apply the same vectorization method used during training. The CountVectorizer saved within the pipeline (best_model.named_steps["vectorizer"]) transforms the preprocessed text into a numerical feature matrix.
# Transform preprocessed messages into feature vectors
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

X_new = best_model.named_steps["vectorizer"].transform(processed_messages)
```

Making Predictions:

```python
# With the data properly preprocessed and vectorized, we feed the new messages into the trained MultinomialNB classifier (best_model.named_steps["classifier"]). This classifier outputs both a predicted label (spam or not spam) and class probabilities, indicating the model’s confidence in its decision.
# Predict with the trained classifier
predictions = best_model.named_steps["classifier"].predict(X_new)
prediction_probabilities = best_model.named_steps["classifier"].predict_proba(X_new)
```

Displaying Predictions and Probabilities:

```python
# Display predictions and probabilities for each evaluated message
for i, msg in enumerate(new_messages):
    prediction = "Spam" if predictions[i] == 1 else "Not-Spam"
    spam_probability = prediction_probabilities[i][1]  # Probability of being spam
    ham_probability = prediction_probabilities[i][0]   # Probability of being not spam
    
    print(f"Message: {msg}")
    print(f"Prediction: {prediction}")
    print(f"Spam Probability: {spam_probability:.2f}")
    print(f"Not-Spam Probability: {ham_probability:.2f}")
    print("-" * 50)
```

## Using joblib for Saving Models

After confirming satisfactory performance, preserving the trained model to be reused later is often necessary. By saving the model to a file, users can avoid the computational expense of retraining it from scratch each time. This is especially helpful in production environments where quick predictions are required.

`joblib` is a Python library designed to efficiently serialize and deserialize Python objects, particularly those containing large arrays such as NumPy arrays or scikit-learn models. `Serialization` converts an in-memory object into a format that can be stored on disk or transmitted across networks. `Deserialization` involves converting the stored representation back into an in-memory object with the exact same state it had when saved.

`joblib` works by leveraging optimized binary file formats that compress and split objects, if necessary, to handle large datasets or complex models. When a model, such as a scikit-learn pipeline, is saved with `joblib`, it stores the entire model state including learned parameters and configurations. Later, when the model is reloaded, it will immediately be ready to make predictions as if it had just been trained.

By doing so, `joblib` helps streamline the deployment process. Instead of retraining the model every time the application restarts, developers and operations teams can load the saved model into memory and start making predictions. This reduces both computational overhead and startup latency.

```python
import joblib

# Save the trained model to a file for future use
model_filename = 'spam_detection_model.joblib'
joblib.dump(best_model, model_filename)

print(f"Model saved to {model_filename}")
```

In this example, `best_model` likely refers to a finalized and tested pipeline or classifier. The file `spam_detection_model.joblib` will contain all the necessary information to predict new data. To reuse the model later, load it back into the environment. Remember that new data must be preprocessed the same way as the training data before making predictions:

```python
# Load the saved model
loaded_model = joblib.load(model_filename)

# Preprocess new messages before prediction
new_data_processed = [preprocess_message(msg) for msg in new_messages]

# Make predictions on the preprocessed data
predictions = loaded_model.predict(new_data_processed)
```


Model Evaluation (Spam Detection)

```python
import requests
import json

# Define the URL of the API endpoint
url = "http://localhost:8000/api/upload"

# Path to the model file you want to upload
model_file_path = "spam_detection_model.joblib"

# Open the file in binary mode and send the POST request
with open(model_file_path, "rb") as model_file:
    files = {"model": model_file}
    response = requests.post(url, files=files)

# Pretty print the response from the server
print(json.dumps(response.json(), indent=4))

```

