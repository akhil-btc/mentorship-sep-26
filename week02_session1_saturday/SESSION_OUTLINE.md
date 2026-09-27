# Saturday · Week 2 Session 1 — Mentor Outline

Everything for today. Have this open on a second screen.

## Time budget (60 min)

| Block | Time | Purpose |
|---|---|---|
| 1. Warm open + welcome Shaurya back | 0:00 – 0:05 | Set tone. Acknowledge his return without shame. |
| 2. Shloka's code review + the silent-failure lesson | 0:05 – 0:22 | THE headline moment. Silent corruption is worse than crashing. |
| 3. Teach classes with live refactor | 0:22 – 0:47 | Introduce OOP by rebuilding what they already have. |
| 4. Virtual environments + pip | 0:47 – 0:57 | Hygiene layer, ready for Week 3 APIs. |
| 5. Assign + preview Sunday | 0:57 – 1:00 | Short, specific. |

## Files in this folder

| File | Purpose |
|---|---|
| `analyze_marks_honest.py` | The "return None, skip Nones, report skipped" fix for Shloka's silent-failure bug. Show side-by-side with her code in Block 2. |
| `student_class.py` | Reference Student class. Live-code this together in Block 3. |
| `analyze_marks_with_class.py` | The refactored analyze_marks using Student. Show after building the class. |
| `venv_cheatsheet.md` | Reference for Block 4. Share with students after class. |
| `ASSIGNMENT_WEEK02_SATURDAY.md` | Their assignment for the week. |

## THE headline lesson: silent failure is worse than crashing

Shloka's `safe_int` returns `0` for bad values. Her code doesn't crash. Great — but the results are **silently wrong**:

- Subject averages divide by TOTAL rows, not by valid rows. Every blank cell drags the subject average down.
- Top student is computed by total, but now the total includes zeros. Whoever had bad data gets unfairly penalized.
- The user has no idea any data was skipped.

Say this out loud in Block 2:

> "There are three kinds of failure. One — your code crashes. Bad, but obvious. You know something is wrong. Two — your code runs, but the answers are quietly wrong. Nobody notices. That's the worst kind. Three — your code handles what it can, and tells the user what it couldn't. That's the honest version. Last week we moved you from one to two. Today we move you to three."

Then show `analyze_marks_honest.py` next to her code. The difference is small (return None instead of 0, filter Nones in aggregation, add a report_issues function). The impact is huge.

## Classes: the pedagogical arc

Do NOT start with theory. Start with pain.

1. Open Shloka's code. Point at the fact that all logic sits in loose functions.
2. Ask: "What if we want to add a method that checks which subjects a student scored below 80 in?" She'd have to write another loose function that takes a row. And another for the next question. And another.
3. Say: "A class lets you bundle the DATA (marks) and the BEHAVIOR (methods) together. Then adding a new question is one method inside the class, not a new function outside it."

Then live-code Student together. Reference: `student_class.py`.

## Class concepts to introduce, in order

1. `class Student:` — declaration
2. `def __init__(self, name):` — the constructor. Explain `self` as "the object I'm working on right now."
3. `self.name = name` — assigning to an attribute
4. Adding methods that use `self.marks`
5. `__str__` — the "what happens when you print(student)" method

Explain `self` explicitly. Every beginner is confused by it. Say:

> "Every method takes `self` as the first argument. Python fills it in for you when you call the method on an object. So `shloka.total()` becomes `Student.total(shloka)` behind the scenes. `self` is just the object you're calling the method on."

## Then refactor analyze_marks live

Open the dict-based version. Refactor step by step:

1. Import Student at top.
2. Replace the `read_file` logic: instead of returning a list of dicts, return a list of Student objects.
3. Replace subject_averages / top_student with methods on Student OR a small function that uses Students.

Reference: `analyze_marks_with_class.py`.

## Virtual environments (Block 4)

Keep this practical, not theoretical. Live-do it together.

```bash
python3 -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
```

Then say:

> "Notice the `(.venv)` in front of your prompt. That means every pip install now goes into this project only."

Show them:
- `pip install requests` (they don't need it yet, but this is the muscle memory)
- `pip freeze > requirements.txt`
- Add `.venv/` to `.gitignore`

Reference: `venv_cheatsheet.md`.

## One-liners to say

> "Silent failure is worse than crashing. Loud failure gives you a chance to fix it. Silent failure gives you wrong answers you trust."

> "A class is data plus behavior in one package. Loose functions plus loose dicts is what you write when you don't have a class."

> "The virtual environment is where you get to install anything without breaking anything."

## Between now and Sunday (their assignment)

Refactor analyze_marks to use a Student class. Set up a venv. Push to GitHub. Full brief: `ASSIGNMENT_WEEK02_SATURDAY.md`.

## Sunday preview (say this in Block 5)

- Review of both students' Student class refactors
- Deeper class concepts: class methods, inheritance basics if time
- Introduce next week: APIs and how programs talk to the internet
