# Hierarchical Clustering

set.seed(1234)
x <- rnorm(12, rep(1:3, each = 4), 0.2)
y <- rnorm(12, rep(c(1, 2, 1), each = 4), 0.2)
plot(x, y, col = "blue", pch = 19, cex = 2)
text(x + 0.05, y + 0.05, labels = as.character(1:12))

dataFrame <- data.frame(x=x, y=y)
dist(dataFrame)

rdistxy <- as.matrix(dist(dataFrame))
diag(rdistxy) <- diag(rdistxy) + 100000
ind <- which(rdistxy == min(rdistxy), arr.ind = TRUE)
ind
