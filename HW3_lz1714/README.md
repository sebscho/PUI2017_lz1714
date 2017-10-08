
# HW3

I mainly followed Dr. Federica's instructions on Assignment 1 and 2.
Based on those instructions, I understood the goals of the assignments and how to achieve them in general.

Zhiao Zhou taught me how to fit a gaussian to the distribution of means.
Yukun Wan helped me understand where to store the data when my script reads data on compute.

With Zhiao Zhou, Cheng Ma, Chenrui Zhang, Ci He, Yukun Wan, we have also discussed the meaning of "Fit a gaussian to the distribution of means."

I did everything else of this homework alone.


## Outline of what I did
### Assignment 1: Write an ipython notebook that demonstrates visually in a data-driven way the Central Limit Theorem. 

1. Plot Chi-square distribution, Normal distribution, Poisson distribution, Binomial distribution, and Laplace distribution.
2. Plot the distribution of means with different sample size of each distribution.
3. Fit a gaussian to the distribution of means (together for all distributions).

### Assignment 2: Set up the work for data-driven inference based on CitiBike data. 

1. Form a hypothesis and assign a significance level.
2. Store the data in PUIDATA and read the data.
3. Plot the number of trips, separate Subscriber from Customer.
4. Add the std in the figure.
5. Normalize the distribution of trips.

### Assignment 3: Finish z-test lab and turn it in as a notebook.

1. Form a hypothesis and assign a significance level.
2. Store the data in PUIDATA and read the data.
3. Calculating the Z-statistic.
4. Draw a conclusion based on the result.

### Feedback on the research plan
#### Problem Statement: Does Subscribers take more rides on weekdays than Customers?
#### Null Hypothesis: Customers take the same or more number of rides than Subscribers during Weekdays.

1. The Null and alternative hypotheses are established correctly.

2. All the data needed in this research can be processed from the CitiBike raw data.
Based on the Null hypotheses, I think the 'Weekdays' excluded the data of 'weekends',
so I would suggest drop the data of Saturday and Sunday.

### Suggested test
As the two samples (Subscribers and Customers) here are the daily counts of trips during weekdays in January(31 days) 2017, meaning the size of the sample is 22 (<30).
In this case, I would suggest using the one-tailed t-test.
Good luck!
