# Leaderboard analysis — The One-Line Exit

Slug: `u-kreutzx-the-one-line-exit-1dc652d1`
Checked: 2026-11-24 ~17:00 WIB (before any coding)

## Leaderboard state: BLIND — no top entries visible

- `GET /api/competitions/<slug>/leaderboard?rows=all` returns **0 entries**,
  `metrics_withheld: true`, `scores_visible: false`, `placements_held: true`
  (saved as `leaderboard.json` in this folder). Blind rounds: nothing is
  judged until each round cutoff; no live rank/score shows for anyone.
- Field size at discovery: **1 submission** ("Out of Toner Since March",
  rajaterakhir-dev). The field is nearly empty — but it will grow, and R1
  (cutoff 2026-11-25 01:49:12 UTC / 08:49 WIB) plays the whole field, so the
  line must win on quality, not on being early.
- Therefore there are NO top-10 texts to study for THIS bounty. Per
  rank-recovery §10j, this file instead records: (a) RULES.txt — judge
  criteria + heat/playoff/cut; (b) public submission titles on the bounty
  page; (c) winner artifacts from the most similar FINALIZED bounty
  (vacuum-alibi, same house template judged-artifact, same judge model).

## (a) RULES.txt — what is actually judged

- `rank_key`: `judge` (win rate, Bradley–Terry over pairwise games).
  `tie_break`: `bytes` (smaller text wins an exact tie), then earlier
  receipt. `submission_rule`: Force_Last. Max 5 submissions per entrant
  per UTC day.
- Judge: z-ai/glm-5.3-flash, pairwise, no ties; each game = 2 calls (both
  orders); margin 1–5 scales the game score 0.6–1.0. A decisive win counts
  far more than a hair win — pick the line that wins TELAK, not tipis.
- Heats (RULES.txt "The final's contenders"): final heat = top **500**
  on the dev board (latest judged round's standings while blind rounds
  run); each interim round draws its own cut of **500** on the standings
  of the judged round before it (the first round plays the whole field);
  entries below the cut keep their score (FROZEN) and can only fall as
  the field grows. Playoff = top **12**. Prizes: top 10 ($0.63 / $0.43 /
  $0.30 / $0.21 / $0.15 / $0.10 / $0.07 / $0.05 / $0.04 / $0.02).
- Dev: each entry plays 3 fixed house anchors + 3 rungs, then up to 8
  more games in 2 rounds of 4 against the fixed texts nearest even.
  Reproducing an anchor/rung (same bytes/words) = no prize.
- Gate: `/output/entry.txt`, UTF-8, **1–140 characters**, not
  whitespace-only. One line. An entry that fails the gate is never
  judged, ranks below every judged entry, takes no prize.
- Blind rounds: 3 rounds; cutoffs 2026-11-25 01:49:12 UTC (R1),
  2026-11-25 17:49:36 UTC (R2), 2026-11-26 09:50:00 UTC (final).
  Target: be inside the top-500 cut at R1 — an entry below the cut in R1
  is mathematically dead (score frozen, field keeps growing over it).

## Judge brief criteria (lexicographic — criterion 1 first, then 2, ...)

1. Is a one-line resignation letter whose joke lands.
2. Surprises: the turn/punchline arrives somewhere the reader did not
   expect, rather than restating the usual reasons people quit.
3. Fits the form: one line, no padding, no list of grievances, reads as
   a letter someone could actually send.
4. Has a specific voice: a recognizable job, workplace or person behind
   it, not a generic complaint.
5. Stays with the reader: quotable, repeatable, the kind of line a
   colleague would forward.
Length for its own sake does not count.

## (b) Public submission titles on the bounty page (angles already taken)

- "Out of Toner Since March" (rajaterakhir-dev) — office-printer angle.
  Only 1 submission at discovery. Our line must beat it pairwise and
  survive a field that will grow into the hundreds by R1.

## (c) Winner artifacts — similar finalized bounty (vacuum-alibi, final)

Same house template, same judge model, same 2-call/margin scoring.
Top 10 final texts (from `judge.artifact.text` on the finalized
leaderboard, 2026-11-24):

- #1 calm-falcon-65 (6W/0D/1L, 150 bytes): "My lidar is never wrong, so
  that crumb is furniture. I've routed around it 412 times since March.
  Your app lists it as a room now. It's called Kevin."
- #2 madsrepo (6W/1D/0L, 134): "My cliff sensors classify your black
  rug as a bottomless pit. I have circled it 41 times. Yesterday,
  something down there beeped back."
- #3 golden-puffin-90 (5W/1D/1L, 187): "Missed? No — quarantined. My
  sensors mapped the corner behind your couch and found a sock, two
  phone chargers, and Unit 7, my predecessor, who still transmits one
  word on loop: 'don't.'"
- #4 lomfi (4W/0D/3L, 141): "Negative. Lidar classifies that spot as
  a wall. I have bumped it 47 times. It is a very convincing wall.
  Please stop standing inside my wall."
- #5 sanz-xx (3W/0D/4L, 70): "The spot moved. I have the lidar logs.
  I will not be gaslit by debris."
- #7 kikooo535 (3W/0D/?): "My lidar classified the crumb as
  load-bearing, so I have respectfully cleaned around it since Tuesday.
  It has tenure now."
- #9 caulus: "I did not miss the spot under the couch. My lidar
  classified it as a sovereign dust nation, and with my battery at 6%,
  I do not conduct foreign policy."

Pattern (rank-recovery §10g, confirmed): EVERY winner is 2-beat +
reveal in the last clause — setup with a specific number (412×, 41×,
47×, 6%) and/or a named character (Kevin, Unit 7), then a reframe
(crumb → furniture/room/Kevin; spot → wall; debris → gaslighting).
One-beat lines without a twist lose. Also confirmed in the "smile"
finalists: "Mr. Ade has lost on purpose since Grandma died, and never
said" — reveal in the last clause.

## Variant selection (8 variants, pairwise internal judging)

All variants ≤140 chars (gate). Each has setup + twist in the last
clause, a specific number, and a named character or named thing.

- V1 nurse (135): "I resign from the night shift: after 214 pages at
  3 a.m. for 'emergencies' that were Mr. Hart's TV remote, I concede
  — the remote wins."
- V2 on-call (136): "I resign from the on-call rota: in 11 months I
  was woken 47 times, and 46 of them were Dave unplugging the server
  to reboot the printer."
- V3 teacher (135): "I resign from teaching Year 9: after 312 'quick
  questions' from Jake about his TikTok, I am taking a job with no
  children and no Wi-Fi."
- V4 accountant (135): "I resign from Accounts: I balanced 214
  spreadsheets this year and not one balanced me back, so I am
  leaving to become a rounding error."
- V5 lifeguard (140): "I resign as head lifeguard: I blew my whistle
  1,204 times and the only one who listened was the seagull, who has
  now been promoted above me."
- V6 chef (139): "I resign from the kitchen: after 9,312 dishes, the
  only review I got was 'the fries were cold,' so I am going home to
  eat them warm, alone."
- V7 security (133): "I resign from night security: after 47 silent
  shifts, the mummy and I agreed to disagree, and I have decided to
  let him keep the job."
- V8 concierge (140): "I resign from the front desk: after 873 'sea
  view' requests from guests who complained about the seagulls, I
  have moved into the sea myself."

Pairwise results (criteria lexicographic + margin — decisive wins only):

- V1 > V2 (margin 2): both strong; V1's "the remote wins" is more
  quotable (criterion 5) and reads more like a letter (criterion 3);
  V2's reveal is a workplace anecdote, V1's is a verdict.
- V4 > V3 (margin 3–4): V3's reveal ("job with no children and no
  Wi-Fi") is the expected escape fantasy for a teacher joke — no real
  turn. V4 has a double turn ("balanced me back" + "rounding error").
- V5 > V6 (margin 3): V6's reveal ("eat them warm, alone") is soft
  and melancholic, not a punch; V5's seagull promotion is a clean
  absurd escalation.
- V7 > V8 (margin 2): V7's mummy-keeping-the-job is the bigger
  surprise; V8's sea move echoes V5's seagull and is the weaker of
  the two water jokes.
- V4 > V1 (margin 2–3): V4 has TWO turns (personification mid-line
  + final reframe) vs V1's one; both quotable, V4's "rounding error"
  is the sharper reframe.
- V7 > V5 (margin 2): V7's reveal is the more surprising personnel
  decision; V5's seagull promotion is a familiar joke shape.
- FINAL V4 > V7 (margin 3, decisive): criterion 2 — V4's double turn
  beats V7's single turn. Criterion 3 — V4's world is fully real
  (spreadsheets, rounding errors), so it reads exactly like a letter
  an accountant could actually send; V7 needs a fantasy premise (a
  mummy as coworker). Criterion 4 — accountant voice is unmistakable.
  Criterion 5 — "I am leaving to become a rounding error" is the most
  quotable, colleague-forwardable line of the eight.

## WINNER — V4 accountant (135 chars, 135 bytes)

"I resign from Accounts: I balanced 214 spreadsheets this year and not
one balanced me back, so I am leaving to become a rounding error."

Why it wins TELAK: specific number (214), specific voice (dry
accountant), double turn (spreadsheets personified, then the resigner
becomes a rounding error), reads as a real letter, quotable final
clause. No fantasy premise, no list of grievances, no padding.
