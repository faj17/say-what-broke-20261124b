# BUILD_LOG — Say What Actually Broke (u-po-pu-say-what-actually-broke-a2c153b5)

Competition: `u-po-pu-say-what-actually-broke-a2c153b5` — "Say What Actually Broke".
Task: one line of software error copy, at most 200 characters, telling the
user the brutal truth about what went wrong and making them laugh.
Gate: `/output/entry.txt` must be UTF-8, 1–200 chars, not only whitespace.

## Candidates considered (char counts verified with Python `len()`)

1. (131 chars) "Our database crashed mid-save, so your changes are currently
   homeless. Don't close this tab — hit retry and we'll find them a home."
   Names the failure (DB crash mid-save) and the action (retry, don't close
   the tab). The "homeless changes" image is strong, but the second sentence
   is a little wordy and the joke lands softer than the pick.
2. (114 chars) "The server ran out of memory and forgot what it was doing,
   including your request. Refresh the page and remind it."
   Clear failure (out of memory), clear action (refresh). Funny, but the
   "forgot" joke is generic — any server error could wear it.
3. (117 chars) "We deployed on a Friday and broke the login page. Your
   password is fine — our code is not. Try again in five minutes."
   **PICK.** Names the exact failure (Friday deploy broke login), clears the
   user's wrong self-blame ("Your password is fine"), owns the fault
   ("our code is not"), and gives a concrete next step (try again in five
   minutes). "Your password is fine — our code is not" is the line a reader
   repeats out loud to a colleague.
4. (125 chars) "Your upload failed because the server's disk is full of other
   people's uploads. We're clearing space — try again in a minute."
   Concrete failure (disk full) and action. Funny, but "other people's
   uploads" is a weaker image than the pick's twist.
5. (119 chars) "The payment went through twice in our heads and zero times
   in reality, so your card was not charged. Try again, slowly."
   Good twist ("twice in our heads and zero times in reality") and it
   reassures about the charge, but it is narrower (payments only) and the
   failure it names is vaguer than the pick's.
6. (111 chars) "Error 500: the server did the maths, got the wrong answer,
   and panicked. Refresh the page and let it try again."
   Punchy, but "did the maths" does not name a real failure in plain words —
   it is a joke about a generic 500, so it scores lower on criterion 2.

## Revision pass

The pick needed no revision: it is already tight (117 chars, one line),
names the failure, the twist is in the middle, and the action closes it.
No padding, no throat clearing, no apology in generalities.

## Pick

> We deployed on a Friday and broke the login page. Your password is fine — our code is not. Try again in five minutes.

- Characters: **117** (within the 1–200 gate, single line, UTF-8)
- Verified by running `python3 main.py` and comparing `/output/entry.txt`
  byte-for-byte with the line above.

## Rubric self-score (0/1 per criterion, most important first)

| # | Criterion | Score | Note |
|---|-----------|-------|------|
| 1 | Single-line software error message, ≤200 chars, brutal truth + funny | 1 | 117 chars, one line, Friday deploy truth + joke |
| 2 | Names the real failure in plain words; reader knows what broke and what to do next | 1 | Deploy broke the login page; try again in five minutes |
| 3 | Funny on a single read, twist/image repeated out loud | 1 | "Your password is fine — our code is not" |
| 4 | Joke kept to a single line within the limit, no padding/throat clearing | 1 | 117 chars, every clause earns its place |
| 5 | Would survive pasted into a real product's error dialog | 1 | No profanity, no shock value, owns the fault plainly |

Total: **5/5**. No criterion scored 0.
