"""Split a cleaned narration recording into its spoken lines (pauses >= 0.55 s separate lines)."""
import numpy as np

def split_lines(y, SR, n_lines, min_gap=.55):
    win = int(.02 * SR); e = np.sqrt(np.convolve(y ** 2, np.ones(win) / win, "same"))
    thr = max(np.percentile(e, 20) * 4, 10 ** (-42 / 20)); voiced = e > thr
    segs, i = [], 0
    while i < len(voiced):
        if voiced[i]:
            j = i
            while j < len(voiced) and voiced[j]: j += 1
            segs.append([i, j]); i = j
        else: i += 1
    merged = []
    for a, b in segs:
        if merged and a - merged[-1][1] < min_gap * SR: merged[-1][1] = b
        else: merged.append([a, b])
    merged = [s for s in merged if s[1] - s[0] > .25 * SR]          # drop clicks and breaths
    while len(merged) > n_lines:                                   # too many pieces: join the closest pair
        gaps = [merged[k + 1][0] - merged[k][1] for k in range(len(merged) - 1)]
        k = int(np.argmin(gaps)); merged[k][1] = merged[k + 1][1]; del merged[k + 1]
    if len(merged) < n_lines:
        raise ValueError(f"found {len(merged)} lines, expected {n_lines}: leave a 1-second pause between lines")
    pad = int(.06 * SR)
    return [(max(0, a - pad), min(len(y), b + pad)) for a, b in merged]
