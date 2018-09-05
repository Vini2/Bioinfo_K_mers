# Gnuplot script file for plotting the k-mer frequency distribution of Human X and Y Chr
set   autoscale                        # scale axes automatically
unset log                              # remove any log-scaling
unset label                            # remove any previous labels
set xtic auto                          # set xtics automatically
set ytic auto                          # set ytics automatically
set xlabel "k-mer frequency"
set ylabel "Number of k-mers"
plot "k_X_mer_dist.txt" with line, "k_Y_mer_dist.txt" with line

# How to run script?
# load 'k-mer-dist.p'