

import re


# -------- Stage 1: Explicit Yes/No extraction --------

def extract_yes_no(prediction: str):
    """
    Try to extract an explicit Yes/No decision from the end of the model output.
    Returns "yes", "no", or None.
    """
    if not prediction:
        return None

    text = prediction.lower().strip()

    # focus on the last part (final decision usually appears there)
    tail = "\n".join(text.splitlines()[-2:])

    yes = bool(re.search(r"\byes\b", tail))
    no = bool(re.search(r"\bno\b", tail))

    if yes and not no:
        return "yes"
    if no and not yes:
        return "no"

    return None


# -------- Stage 2: LLM-as-judge for implicit answers --------

def judge_with_llm(prediction: str, client):
    """
    Use a lightweight LLM call to classify the semantic meaning
    of an answer as Yes or No.
    """
    prompt = f"""
Classify the following answer strictly as Yes or No.
If the answer is ambiguous, choose the most likely one.

Answer:
{prediction}

Final answer (Yes or No):
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
        max_output_tokens=16,
        temperature=0
    )

    out = response.output_text.lower()

    if "yes" in out:
        return "yes"
    if "no" in out:
        return "no"

    return None


# -------- Final scoring function --------

def exact_match(prediction: str, gold: str, client=None):
    """
    Hybrid evaluation:
    1) Extract explicit Yes/No if present
    2) Otherwise infer semantic Yes/No via LLM judge
    """
    gold = gold.lower()

    # Stage 1: explicit extraction
    extracted = extract_yes_no(prediction)

    # Stage 2: semantic judgment if needed
    if extracted is None and client is not None:
        extracted = judge_with_llm(prediction, client)

    if extracted is None:
        return 0

    return int(extracted == gold)


