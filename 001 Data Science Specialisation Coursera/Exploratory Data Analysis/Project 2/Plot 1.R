library(dplyr)

# read in the data
NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

# convert to tbl class
data<-tbl_df(NEI)

# group by year
data<-group_by(data,year)

# total by year
total_by<-summarise(data,sum(Emissions))

# plot trend in base and to a png file
png(filename = "total_by_year.png")
plot(total_by$year,total_by$`sum(Emissions)`,type = 'b',main = "Total tons of PM2.5 by year")
dev.off()