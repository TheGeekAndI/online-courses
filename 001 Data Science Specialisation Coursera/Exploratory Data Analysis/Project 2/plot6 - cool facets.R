# Compare emissions from motor vehicle sources in Baltimore City (fips==24510) with
# emissions from
# motor vehicle sources in Los Angeles County, California (fips == 06037). Which city
# has seen greater changes over time in motor vehicle emissions?

library(dplyr)
library(ggplot2)

# Assume zip file had been downloaded into the working directory

unzip("NEI_data.zip", files = NULL, list = FALSE, overwrite = TRUE,
      junkpaths = FALSE, exdir = "NEIdata", unzip = "internal",
      setTimes = FALSE)

# read the files

nei <- readRDS("NEIdata/summarySCC_PM25.rds")
scc <- readRDS("NEIdata/Source_Classification_Code.rds")
unlink("NEIdata",recursive=TRUE)  # done with the files. remove them

# Subset Motor Vehicle emissions from SCC table using Data.Category
sccVeh <- scc[grep("Onroad",scc$Data.Category),]

# Subset Baltimore data from NEI table
balt <- subset(nei,fips == "24510")

# Subset the Baltimore data to only include motor vehicle emissions
baltVeh <- merge(balt,sccVeh,key=SCC)

# add new column to identify the city
baltVeh$city <- "Baltimore"

# Subset Los Angeles data from NEI table
la <- subset(nei,fips == "06037")

# Subset the Los Angeles data to only include motor vehicle emissions
laVeh <- merge(la,sccVeh,key=SCC)

# add new column to identify the city
laVeh$city <- "Los Angeles"

# combine Baltimore and Los Angeles data into a single data frame
combo <- rbind(laVeh,baltVeh)

# Summarize emissions by year and city
byYearCity <- group_by(combo,year,city)
sumData <- summarize(byYearCity, sum(Emissions))

# Add a new column to sumData for cumulative % change
sumData$Change <- 0
names(sumData) <- c("Year","city","Emissions","Change")

# compute cumulative % change and add to the sumData table
for (i in seq(1,nrow(sumData),by=2)){
    sumData$Change[i] <- (sumData$Emissions[i]-sumData$Emissions[1]) /
        sumData$Emissions[1] * 100
    sumData$Change[i+1] <- (sumData$Emissions[i+1]-sumData$Emissions[2]) /
        sumData$Emissions[2] * 100
}

png(filename = "plot6.png", width = 480, height = 480, units = "px")

# Use ggplot2 to plot the emissions changes for each type
# Emissions changes are represented by cumulative % change
g<-ggplot(sumData,aes(x=Year,y=Change,city=city))
g + facet_grid(city~.)  + geom_line(aes(color=city)) +
    labs(title="Baltimore vs Los Angeles Motor Vehicle Emissions Change") +
    labs(y = "Cumulative % Change in Emissions")

dev.off()