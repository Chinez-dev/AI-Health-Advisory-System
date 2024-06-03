# AI-Powered Health Advisory System

## Introduction

The AI-powered health advisory system is designed to provide medical guidance through conversational interfaces. By leveraging advanced AI models and natural language processing technologies, the system facilitates interactive and informative communication between users and virtual health advisors.

## Features

- Natural language understanding and response generation.
- Real-time health advisory based on user input.
- Integration of synthetic and real-world medical conversation datasets.
- Scalable and adaptable to various medical scenarios.

## Technologies Used

- **Langchain**: Framework for building scalable AI applications.
- **Chainlit**: Framework for creating chatbots.
- **SentenceTransformers**: Pre-trained models for sentence embeddings.
- **CTransformers**: Efficient model loading and inference.
- **Faiss**: Library for efficient similarity search and clustering.
- **Llama 2 (TheBloke/Llama-2-7B-Chat-GGML)**: AI model used for generating responses.

## Development Environment

- **Python 3.11.7**
- **Anaconda**: Virtual environment management.
- **VS Code**: Integrated development environment.

## Datasets

- **ChatGPT GenMedGPT-5k**: Synthetic dataset containing 5,000 generated conversations between patients and physicians.
- **HealthCareMagic.com**: Real-world dataset with 100,000 authentic conversations between patients and doctors. Download from from HealthCareMagic.com [HealthCareMagic-100k](https://drive.google.com/file/d/1lyfqIwlLSClhgrCutWuEe_IACNq6XNUt/view?usp=sharing) and add it to the data folder
- **Format**: JSON.

## System Architecture

![System Architecture](link_to_system_architecture_diagram)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ai-health-advisory-system.git
   cd ai-health-advisory-system
   ```

2. **Create and activate the Anaconda environment:**
   ```bash
   conda create -n ai-health-advisory python=3.11.7
   conda activate ai-health-advisory
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the chatbot interface:**
   ```bash
   run python ingest.py
   then run chainlit run model.py -w
   ```

2. **Interact with the chatbot:**
   - Start a conversation by typing your symptoms or health-related questions.
   - The chatbot will process your input and provide relevant medical advice.

## Testing


## Contributions

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.


## Additional Information

For more detailed information about this project, visit my [LinkedIn post](https://www.linkedin.com/posts/chinez-dev_healthtech-ai-healthcare-activity-7191732822397620226-wPkn?utm_source=share&utm_medium=member_desktop).

