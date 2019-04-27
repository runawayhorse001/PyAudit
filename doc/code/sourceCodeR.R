
'''
This is a source R code demo for Sphinx.
@date:  Apr 25, 2016
@author: Wenqiang Feng 
'''

library(reshape2)
library(ggplot2)

# import data 
d <- melt(diamonds[,-c(2:4)])
# plot histogram
ggplot(d,aes(x = value)) + 
  facet_wrap(~variable,scales = "free_x") + 
  geom_histogram()

print("This is a source R code demo for Sphinx.")

