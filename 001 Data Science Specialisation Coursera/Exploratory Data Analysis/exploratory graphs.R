# Exploratory graphs

pm25<-read_csv("daily_88101_2015.csv",col_types = "ccccinncccccccinnnnnccccccccc")
names(pm25)<-make.names(names(pm25))

fivenum(pm25$Arithmetic.Mean)
summary(pm25$Arithmetic.Mean)

boxplot(pm25$Arithmetic.Mean,col="blue")
abline(h=12)
filter(pm25,Arithmetic.Mean > 25) %>% select(State.Name,County.Name,Arithmetic.Mean) %>%
    arrange(desc(Arithmetic.Mean))

install.packages("maps")
library(maps)

map("county","california")
with(filter(pm25,Arithmetic.Mean>99),points(Longitude,Latitude))

hist(pm25$Arithmetic.Mean, col="green",breaks=100)
abline(v=12,lwd=2)
abline(v=median(pm25$Arithmetic.Mean),lwd=3,col="red")
rug(pm25$Arithmetic.Mean)

boxplot(pm25$Arithmetic.Mean ~ pm25$Sample.Duration, col="blue")

# Plotting Systems

data("airquality")
with(airquality,{
    plot(Temp,Ozone)
    lines(loess.smooth(Temp,Ozone))
})

library(lattice)
state <- data.frame(state.x77, region = state.region)
xyplot(Life.Exp ~ Income | region, data = state, layout = c(4, 1))

library(ggplot2)
data(mpg)
qplot(displ,hwy,data=mpg)
