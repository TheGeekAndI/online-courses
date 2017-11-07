library(dplyr)
library(ggplot2)

# read in the data
NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

# convert to tbl class
data<-tbl_df(NEI)

# subset data for Baltimore only
data<-filter(data,fips=='24510')

# group by year and type
data<-group_by(data,year,type)

# summarise by year and type
sums<-summarise(data,total_ems=sum(Emissions))

# convert to dataframe
sums<-as.data.frame(sums)

# make type a factor
sums$type<-as.factor(sums$type)

# plot in ggplot2 4 series by year (1 series per type)
png("emissions_by_type.png")
g<-ggplot(sums,aes(year,total_ems))
g+geom_line(aes(col=type))+ggtitle('Total PM2.5 emissions by type')
dev.off()