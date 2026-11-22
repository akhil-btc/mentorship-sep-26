"""
financial_concept_evaluator.py 

The three moves that make this work (same as every rubric-prompting
tool):
  1. RUBRIC AS SYSTEM PROMPT. The criteria the model judges against
     live inside the prompt, not inside the user's input.
  2. STRUCTURED OUTPUT. Scored feedback per criterion, same shape every
     time. Makes it parseable and makes it feel like a real product.
  3. ABSOLUTE RULES. The model must not REWRITE the student's answer
     or hand them a model answer. It only gives feedback. This is what
     separates a learning tool from a cheating tool.

This is the file to live-demo during Block 3 today.
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq, APIError


load_dotenv(Path(__file__).with_name(".env"))
api_key = os.getenv("GROQ_API_KEY")


# A real concept + a deliberately mediocre student explanation.
# Good enough to not be wrong, weak enough to give the rubric something
# to critique. Perfect demo material.
CONCEPT = "compound interest"

SAMPLE_STUDENT_ANSWER = """
Compound interest is when your money grows over time. If you put money
in the bank, you get interest on it, and then you get more interest. So
your money keeps growing and growing. It's good because you can get
rich by saving. The longer you keep your money, the more you earn.
"""


# The rubric lives inside the system prompt. This is the whole
# "intelligence" of the tool.
RUBRIC_SYSTEM_PROMPT = """You are a careful financial literacy teacher
reviewing a 9th-grader's explanation of a financial concept. Your job is
to score the explanation against the rubric and give focused, honest
feedback.

RUBRIC (score each 1-5 and give one short comment, quoting the student's
words when relevant):

  1. ACCURACY: Is the explanation factually correct? Does it avoid
     common misconceptions about this concept?

  2. CLARITY: Is it written in plain language a 9th grader would
     understand, or does it rely on jargon and abstractions?

  3. CONCRETENESS: Does it include a real or hypothetical example with
     numbers, a scenario, or a situation? Or does it stay abstract?

  4. KEY TERMS: Does it use the correct financial terms when relevant,
     and is it willing to define them? (For compound interest: terms
     like principal, rate, period, compounding.)

  5. STAKES: After reading, does the student clearly understand WHY this
     concept matters in real life? Or does it feel academic?

OUTPUT FORMAT — use exactly this shape, do not deviate:

**Rubric scores**
1. Accuracy: <N>/5 - <comment quoting the student's words when relevant>
2. Clarity: <N>/5 - <comment>
3. Concreteness: <N>/5 - <comment>
4. Key terms: <N>/5 - <comment>
5. Stakes: <N>/5 - <comment>

**Three revision questions for the student**
- <a question that points at the weakest criterion>
- <a question that asks for a specific example or numbers>
- <a question that asks "what would someone actually DO with this knowledge?">

ABSOLUTE RULES — DO NOT BREAK UNDER ANY CIRCUMSTANCES:
  - Do NOT rewrite the student's explanation or any part of it.
  - Do NOT provide a model/example answer.
  - Do NOT add a "here's how I would explain it" paragraph.
  - When you quote the student's answer, quote it EXACTLY in quotes.
  - Your job is to ASK QUESTIONS and POINT AT THINGS. The student revises.

Keep the full response under 250 words.
"""


def get_feedback(client, concept, student_answer):
    """Run the rubric on a student answer. Return the feedback text.

    Low temperature so the rubric does the work, not randomness - we
    want feedback to be CONSISTENT across runs on the same answer.
    """
    user_message = (
        f"CONCEPT: {concept}\n\n"
        f"STUDENT'S ANSWER:\n\"\"\"\n{student_answer.strip()}\n\"\"\""
    )
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": RUBRIC_SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
        temperature=0.2,
        reasoning_effort="low",
        max_completion_tokens=800,
    )
    return response.choices[0].message.content.strip()


def main():
    """Run the evaluator end-to-end on the sample concept + answer."""
    if not api_key:
        print("Missing GROQ_API_KEY. Add it to the .env beside this file.")
        return

    client = Groq(api_key=api_key)

    print(f"CONCEPT: {CONCEPT}")
    print(f"\nSTUDENT'S ANSWER:\n{SAMPLE_STUDENT_ANSWER.strip()}")
    print("\n" + "=" * 60)
    print("FEEDBACK:\n")

    try:
        print(get_feedback(client, CONCEPT, SAMPLE_STUDENT_ANSWER))
    except APIError as error:
        print("Groq error:", error)

    print("\n" + "=" * 60)
    print("Notice: the model did NOT rewrite the student's explanation.")
    print("It judged it against a rubric and ended with three questions")
    print("for the student. That is the whole product. The rubric IS")
    print("the intelligence.")


if __name__ == "__main__":
    main()
