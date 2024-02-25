
# Furniture Classifier

## Project Overview

This repository contains the implementation of a machine learning project aimed at classifying furniture images. The project uses a deep learning model for classifying images into various furniture categories. It is designed to be easily deployable using Docker, making it accessible for a wide range of users.

### Structure

- `static/`: Contains static files for the web interface.
- `test/`: Directory for test images or scripts.
- `uploads/`: Temporary storage for uploaded images for classification.
- `Dockerfile`: Instructions for building a Docker container for the project.
- `app.py`: The Flask application server for hosting the web interface.
- `base.html` & `index.html`: HTML templates for the web interface.
- `furniture_test.ipynb`: Jupyter notebook containing the code for training and testing the model.
- `requirements.txt`: Specifies the Python dependencies required by the project.

## Getting Started

### Prerequisites

Ensure you have Docker installed on your system to run this project. If you prefer running it locally, ensure you have Python 3.x and the necessary libraries installed.

### Running with Docker

1. Build the Docker image:
    ```sh
    docker build -t furniture-classifier .
    ```
2. Run the container:
    ```sh
    docker run -p 5000:5000 furniture-classifier
    ```

### Running Locally

1. Install Python dependencies:
    ```sh
    pip install -r requirements.txt
    ```
2. Start the Flask application:
    ```sh
    python app.py
    ```

## Usage

Navigate to `http://localhost:5000` to access the web interface. Upload an image of furniture to classify it into categories such as chairs, tables, sofas, or beds.

## Training the Model

The `furniture_test.ipynb` notebook contains the steps for training and evaluating the furniture classification model. Follow the instructions within the notebook to retrain the model or evaluate its performance on a new dataset.

## Contributing

Contributions to the Furniture Classifier project are welcome. Please read through the contributing guidelines before submitting pull requests or issues.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

