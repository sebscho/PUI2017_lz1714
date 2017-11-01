 ## HYPOTHESIS FORMULATION

You should state why your idea is interesting in your report, and what motivates it. 

The Null/Alternatively is formnulate appropriately in accordance with the original question, and the significance level is clearly stated.

## DATA

The data supports the analysis and seems appropriately pre-processed. The plots are very useful to give a hint of the answer.

## STATISTICAL TEST

You are testing proportions between two samples split along a categorical variables. 
While the z test may be used, and it often is in the literature in this case, 
it assumes simple random sampling from a normally distributed population (typical when testing pharmaceuticals with a placebo and a true medication)

There is no reason to believe your population distributions are inherently Gaussian so a better choice is the chi sq test for proportion, 
which is non parametric, or the Fisher exact test, also non-parametric. However, since your sample size is large, of the two tests mention the appropriate one to use is the chi sq test for proportion (contingency table)


NOTE: For whichever test you chose, you want the one-tailed version

