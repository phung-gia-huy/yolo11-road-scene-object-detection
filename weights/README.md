# Local Model Weights (not distributed)

The original trained YOLO11m checkpoint, `best.pt`, is **not committed** in this public browser-upload package (about 39 MB). It exceeds the 25 MiB browser file-upload limit, and any redistribution must also comply with applicable licenses and permissions.

To run local inference, place a legitimately obtained original checkpoint here as `weights/best.pt`, then run:

```bash
python scripts/predict.py --weights weights/best.pt --source path/to/image_or_video.mp4
```

Without the checkpoint, the model cannot perform inference. `results/` still contains the archived training and validation figures.
