# Evaluation tasks

Each task is self-contained: fork, make the failing tests pass, keep the rest green. Ground truth is the test suite, so no network is needed.

| ID | Task | Skill probed | Difficulty |
|----|------|--------------|-----------|
| T1 | `dedupe` keeps the newest item when URLs collide (add `seen` ordering) | data cleaning | Easy |
| T2 | `source_mix` should accept a `weights` argument | API design | Easy |
| T3 | Add a `un_sdg.goal_targets(code)` client with retries and tests | API integration | Medium |
| T4 | Add on-disk caching to `http.get_json` with a TTL, without breaking mocks | systems | Medium |
| T5 | Add a `--format md` option to the CLI that renders a cited brief | product/UX | Medium |
| T6 | Replace keyword `tag_theme` with a scored classifier and justify thresholds | ML eval | Hard |

Reviewers: grade on correctness, tests added, readability, and whether claims in generated briefs cite a source URL.
