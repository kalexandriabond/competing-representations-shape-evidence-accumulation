library(pROC)
library(ggplot2)
library(tidyverse)

df <- read.csv('~/Downloads/LR_preds_df.csv')
thresholds = seq(0,1,0.001)
# all
roc_obj <- plot.roc(x = df$y_true, predictor = df$y_pred)

ci.thresholds.obj <- ci.thresholds(roc_obj,thresholds=thresholds)

plot(ci.thresholds.obj, type='shape', col='blue')

gl <- ggroc(roc_obj, legacy.axes = TRUE,)
gl + xlab("FPR") + ylab("TPR") +
  geom_segment(aes(x = 0, xend = 1, y = 0, yend = 1), color="darkgrey", linetype="dashed")



# sub by sub ROC curves with bs CIs
rocs <- df %>% group_by(subj) %>% group_modify(~ data.frame(ci.thresholds(plot.roc(x=.x$y_true, predictor=.x$y_pred), 
                                                                          n.boot=1000,thresholds=thresholds)))
write.table(rocs, file='~/Downloads/human_ROCs_CIs.csv', sep=',')

# get aucs with bs CIs
aucs <- df %>% group_by(subj) %>% group_map(~ ci.auc(plot.roc(x=.x$y_true, predictor=.x$y_pred),
                                                                method='bootstrap', n.boot=1000))

rounded_aucs <- lapply(aucs, round, 2)

for (s in seq_along(unique(rocs$subj))) {
  rounded_aucs[[s]]['subj'] = s
} 


auc_df = do.call(rbind.data.frame, rounded_aucs)
names(auc_df) = c('lower_25', 'median_50', 'upper_975', 'subj')
write.table(auc_df,file = '~/Downloads/human_AUCs_CIs.csv', sep=',')