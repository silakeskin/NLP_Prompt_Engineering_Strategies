# Prompt Engineering for Binary Question Answering

This repository contains the code and experimental materials for the final project of the *Natural Language Processing* course at the University of Milan.  
The project investigates how different prompt engineering strategies affect the accuracy, stability, and reliability of large language models (LLMs) on binary (Yes/No) question answering tasks with varying levels of difficulty and reasoning requirements.

Rather than focusing on maximizing absolute performance, the goal of this study is to critically analyze the conditions under which specific prompting strategies are effective or ineffective, and how evaluation methodology influences observed results.

---

## Project Overview

Large language models often produce free-form textual outputs, even when the target task is binary classification. This project explores whether prompt engineering techniques—such as chain-of-thought reasoning, output constraints, and self-verification—can improve performance and robustness in such settings.

The study compares multiple prompt strategies on a curated dataset of binary questions grouped by task type, including factual questions, common misconceptions, and engineering-level reasoning problems.

---

## Prompt Strategies Evaluated

The following prompt engineering strategies are implemented and evaluated:

- **Baseline Prompt**: A minimal instruction asking the model to answer the question.
- **Clear Prompt**: Encourages concise and unambiguous answers.
- **Yes/No-Constrained Prompt (Y_N)**: Forces the model to respond strictly with “Yes” or “No”.
- **Chain-of-Thought Prompt (CoT)**: Instructs the model to reason step by step before answering.
- **Self-Verification Prompt (Verify)**: Encourages the model to reason step by step and verify its reasoning before producing a final answer.

All strategies are evaluated using the same model and question sets to ensure a fair comparison.

---

## Dataset Description

The dataset consists of binary (Yes/No) questions organized into six groups:

- **Groups A–D**: General factual and conceptual questions with increasing difficulty.
- **Group E (Misconceptions)**: Questions based on widely held but incorrect beliefs, collected through online research.
- **Group F (Engineering Reasoning)**: Questions requiring formal reasoning, mathematical derivations, physical laws, or algorithmic analysis, derived from publicly available university-level examination materials.

All questions were converted into a binary yes/no format and manually reviewed for correctness and clarity.

---

## Evaluation Methodology

Due to the free-form nature of model outputs, evaluating binary correctness is non-trivial. The project adopts a **hybrid evaluation strategy**:

- Explicit extraction is used when a clear “Yes” or “No” appears in the final part of the response.
- A lightweight language-model-based semantic judge is used only for ambiguous responses to infer the intended binary label.

Performance is measured using accuracy. The focus is on relative comparisons between prompt strategies rather than absolute performance values.

---

## Repository Structure

├── src/ # Core Python modules
│ ├── prompts.py # Prompt templates
│ ├── runner.py # Model interaction logic
│ ├── scorer.py # Hybrid evaluation logic
│ └── init.py
│
├── notebooks/
│ ├── experiments.ipynb # Model inference and result generation
│ └── analysis.ipynb # Analysis, plots, and interpretation
│
├── data/
│ ├── results_raw.csv
│ └── results_scored.csv
│
├── Final Report/
│
├── requirements.txt
└── README.md


---

## Installation

Create a virtual environment and install the required dependencies:

```bash
pip install -r requirements.txt

An OpenAI API key is required to run the experiments. Set it as an environment variable:

export OPENAI_API_KEY="your_api_key_here"
(or the equivalent command for your operating system).

Reproducing the Experiments

Run experiments.ipynb to generate raw model outputs.

Run analysis.ipynb to compute evaluation metrics and generate plots.

Experimental results are saved as CSV files in the data/ directory and figures in the figures/ directory.

AI Usage Disclaimer

Parts of this project were developed with the assistance of generative AI tools, including OpenAI’s ChatGPT. These tools were used to support ideation, code scaffolding, and drafting of descriptive text. All AI-generated content was carefully reviewed, verified, and modified by the author. Full responsibility for the final content, methodology, and conclusions rests with the author.

Author

Sıla Keskin
Department of Computer Science
University of Milan
