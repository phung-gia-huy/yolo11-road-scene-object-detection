# Dataset Notes

## Dataset Source

This project uses the [Self-Driving Cars dataset](https://www.kaggle.com/datasets/alincijov/self-driving-cars) from Kaggle, as referenced in the academic project report.

The report describes 18,000 training images and 4,241 images in a separate split referred to as "Test".

## Dataset Configuration

The YOLO11m model was trained to detect three object classes:

- `car`
- `pedestrian`
- `trafficLight`

The original dataset preparation and class conversion scripts are no longer available. The processed dataset and training data configuration are not included in this repository.

## Evaluation Notes

The reported detection metrics are based on the saved validation results from the original training experiment. No independent test-set evaluation is documented in the preserved records.

The dataset and its associated media remain subject to their respective usage and redistribution terms.