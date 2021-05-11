# Happy Dogs - Investigating the Effect of Puppy Videos on Biological Stress Measures

## Topics Covered

- Field Experiment Design
- Statistical Inference
- Causality Analysis
- Exploratory Data Analysis
  
## 0. Links

[Project Report](https://github.com/shahbakhthamdani/Projects/blob/master/Data%20Science%20Projects/4.%20Causality%20Analysis%20of%20Stress-reducing%20videos/Stress%20versus%20Cute%20Dog%20Videos.pdf)

## 1. Overview

Dogs are considered man’s best friend: recent studies have even suggested that dogs can positively affect the emotional state of humans. Previous literature suggests that dogs can reduce work related stress (Barker,
2012). Barker’s work was limited to the effect of dogs in offices. Further, the sample size involved in the
study was extremely small (75 samples).

A second set of prior work showed that children with dogs had a lower score on an index for anxiety and
anxiety-related disorders than children without dogs (Gadomski, 2015). This study enrolled 643 children
ranging from 4 to 10 years of age. While this study alleviates the sample size concerns with the Barker study, there are concerns over the scope of the study (conclusions are restricted to the effect of growing up with dogs on children). Finally, a 2004 study at the University of Missouri-Columbia found that levels of serotonin rise dramatically after just a few minutes of physical interaction with dogs (Johnson and Meadows, 2004). This study was a major motivation for our own.

We are interested in understanding if exposure to even imagery of puppies can have a beneficial impact on
the average person. We have designed an experiment to quantify the effects of a video of puppies playing on
biological stress signs. We will take a difference-in-differences approach to evaluating this effect: we will take a baseline measurement, show the participant a video (puppies if treatment, white noise if control), and then take a follow-up measurement. Thus, we quantify the treatment effect as the average difference in treatment participants minus the average difference in control participants.

We anticipate several possible covariates ranging from age, height, and exercise characteristics to pet ownership details. We will survey for these covariates to include in post-treatment analysis.

## 2. Data Collection

We approached subjects in settings ranging from coffee shops to professional office settings to home or casual settings. Stress measurements were collected using smartphones: apps allowed use of the built-in infrared and red lights to serve as pulse-oximeters. Pulse oximetry allows for the measurement of heart rate (in beats per minute) and blood oxygenation levels (a quantification of what proportion of the participant’s hemoglobin is currently coupled to oxygen). Both measurements can be indicative of stress levels. We aimed to survey 40 participants each for a total of 120 participants in the experiment.

A total of 116 observations were collected by the three Collectors, hereby written as CollectorN (Nishant), CollectorB (Beau) and CollectorS (Shahbakht). Out of these, 60 were assigned to treatment and the rest were assigned to control group. There were no instances of attrition in the data since all the collection was done on spot. A total of 83 males and 33 females were part of the data, and the source of this bias was subsample from CollectorS. Age of the subjects ranged from 8 to 82 years, with an average of 34.6 years. The weight and height statistics have an expected distribution bordering on normal. Other parameters include current and former pet ownership.

The two outcomes of interest are: heart rate (bpm) and oxygenation level (percentage). These are collected
pre- and post-treatment or control and difference-in-difference methodology is employed to analyse our results. We selected these measures because they are measurable indicators of stress levels (AHA, 2018).

## 3. Results

We prespecified several regressions to avoid conducting a fishing expedition. For each outcome variable (BPM
and oxygenation), we conducted four regressions, listed below.

1. Baseline (treatment variable alone).
2. Baseline + demographic covariates.
3. Baseline + pet ownership covariates.
4. Omnibus regression with all covariates.

This gives us a final count of 8 regressions. Using the Bonferroni correction, we will thus look for a p-value of .05/8 as a cutoff.

[(Tabulated results are available in the project report).](https://github.com/shahbakhthamdani/Projects/blob/master/Data%20Science%20Projects/4.%20Causality%20Analysis%20of%20Stress-reducing%20videos/Stress%20versus%20Cute%20Dog%20Videos.pdf)

We fail to reject the null hypothesis that watching media involving puppies reduces stress
levels. We observe no significant treatment effect in either outcome measure when applying the Bonferroni
correction to our rejection threshold. It’s possible that a treatment effect exists for some specific demographic, but identifying this demographic would require a higher power study (perhaps an order of magnitude more observations). This proposed future work would center around identifying heterogeneous treatment effects (HTEs) involved in this treatment. We would suggest that further study center on one geographical region and look to understand how underlying attitudes or demographics in that region lead to a more localized treatment effect.
