"""Portfolio inference utility, added AFTER the original lab.

This is not the missing training notebook. It uses a saved Ultralytics checkpoint
for inference on locally supplied images or videos.
"""

from pathlib import Path
import argparse


def main():
    parser = argparse.ArgumentParser(description="Run YOLO11 inference with a local checkpoint")
    parser.add_argument("--source", type=str, required=True, help="Local image, directory, or video")
    parser.add_argument("--weights", type=Path, default=Path("weights/best.pt"))
    parser.add_argument("--imgsz", type=int, default=800)
    parser.add_argument("--conf", type=float, default=0.25)
    parser.add_argument("--project", type=str, default="outputs")
    args = parser.parse_args()

    if not args.weights.is_file():
        parser.error(f"Missing checkpoint: {args.weights}. See weights/README.md")
    if not Path(args.source).exists():
        parser.error(f"Missing input: {args.source}")

    from ultralytics import YOLO

    model = YOLO(str(args.weights))
    print("Checkpoint classes:", model.names)
    predictions = model.predict(
        source=args.source,
        imgsz=args.imgsz,
        conf=args.conf,
        save=True,
        project=args.project,
        name="predictions",
        exist_ok=True,
    )
    print(f"Saved predictions in {args.project}/predictions")
    print(f"Processed batches/frames returned: {len(predictions)}")


if __name__ == "__main__":
    main()
