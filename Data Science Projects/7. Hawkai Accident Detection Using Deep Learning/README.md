# HawkAI: Monitoring Road Accidents Real-time Using Deep Learning

## Topics Covered

- Computer Vision
- Deep Learning
- Cloud Computing
- Supervised and self-supervised learning
- Data Transformation

## 0. Links

[Project Presentation](https://github.com/shahbakhthamdani/Projects/blob/master/Data%20Science%20Projects/7.%20Hawkai%20Accident%20Detection%20Using%20Deep%20Learning/HawkAI_%20Accident%20Detection%20using%20Deep%20Learning.pdf)

[Project Website](https://www.ischool.berkeley.edu/projects/2019/hawkai-monitoring-road-accidents-real-time-using-deep-learning)

## 1. Abstract

*HawkAI* detects motor-vehicle collisions using CCTV footage in real-time, using a combination of supervised and self-supervised machine learning techniques. HawkAI alerts traffic management centers when a collision has occurred so that they can immediately dispatch emergency services to the accident scene, thereby reducing emergency response times through real-time reporting and accurate incident location. Trained on Caltrans live traffic footage, HawkAI is an ML initiative paving the way for United Nations Sustainable Development Goal of reducing road-accident deaths by 50% till 2020. HawkAI also reduces information clutter at CCTV control rooms, prioritizing anomalous CCTV footage thereby improving agent throughput.with anomalies.

## 2. Key Highlights

### Data

- Almost 25K hours of live Caltran traffic CCTV footage recorded across 370+ cameras.
- 10% of recorded video content preprocessed into optical flow.
- More than 10K labelled video frames manually annotated for car collisions.
- Parsed 100K images through Google Vision API for semi-supervised tagging of events, crashes and glass to detect incidents. Cross-validation disappointed with 47% accuracy of detecting car accidents.

### Architecture

- The analytics layer comprised of two learners:
  - Supervised classifier
  - Self-supervised anomaly detector
- The serving layer comprised of a heatmap to monitor incidents real-time.
- For advanced use, a Big Query table records signals for custom application.

### Supervised Learning

- Two binary classifiers are retrained on top of an Inception V3, using raw and preprocessed video frame inputs respectively
- Preprocessing involved background subtraction and calculating optical flow
- While precision was impressive (+80%) for classifiers trained on raw images, recall rates (65%) were disappointing
- In contrast, we found better recall rates with optical flow based classifiers, which also showcased the highest F1 score
- Background subtraction performed poorly on both, precision and recall

### Self-supervised Learning

- A convolutional autoencoder was trained as an anomaly detector
- By training to reconstruct a sequence of video frames, it was used to detect incidents based on reconstruction error
- Frames with accidents had 4% higher reconstruction error than normal traffic activity
- Currently, the anomaly detector tends to captures gaps in streaming
- Identifying the right threshold to distinguish between normality and an anomaly is a challenge

### Challenges

- Initially, we used the YT8M feature extractor to quantize videos and cluster the derived latent vectors
- Raw videos clustered based on time of day while optical flow versions clustered on intesity of traffic
- Due to the scale of the data, the models were trained on a sample of the data collected. We believe there is opportunity to leverage the entire dataset more efficiently by managing data preprocessing more efficiently
  