# Repository Status

This is a **public, browser-upload-ready portfolio edition** of an archived academic YOLO11m object detection project, not a complete training reproduction.

## Included

- Archived validation log (`results/results.csv`) and evaluation figures (`results/*.png`)
- Preserved experiment configuration (`results/args_original.yaml`)
- Script to summarize archived metrics (`scripts/summarize_metrics.py`)
- Inference utility (`scripts/predict.py`) that requires a locally available trained checkpoint
- Dataset description (`docs/DATASET.md`)

## Not included

- Original training notebook or exact preprocessing/conversion code (no longer available)
- Source dataset or the processed training split
- Trained `weights/best.pt` (about 39 MB; exceeds the 25 MiB GitHub browser-upload limit)
- Original demonstration videos or academic report (redistribution/identifying details not cleared)
- Independent test-set scores or a freshly reproduced evaluation

For local inference, supply an authorized checkpoint at `weights/best.pt`. The source utility does not substitute for the missing training code.
