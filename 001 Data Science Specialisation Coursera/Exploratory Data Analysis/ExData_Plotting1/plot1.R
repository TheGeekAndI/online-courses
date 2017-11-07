#load libraries
library(dplyr)
library(lubridate)

# read in the data
ds<-read.table("household_power_consumption.txt",header=T,sep=";",na.strings = "?")

# convert data frame to dat table
data<-tbl_df(ds)

# remove original data frame to avoid confusion
rm(ds)

# convert factor variable 'Date' to actual date class
data<-mutate(data,Date=as.Date(dmy(Date)))

# select only date range in question
sub<-filter(data,Date>="2007-02-01",Date<="2007-02-02")

# convert data table to data frame as data frame does not allow POSIXlt results
sub<-as.data.frame(sub)

# convert time factor to POSIXlt class
sub$Time<-strptime(x=as.character(sub$Time),format="%H:%M:%S")

# plot histogram
png(filename = "plot1.png")
hist(sub$Global_active_power,col='red',xlab="Global Active Power (kilowatts)",
     main="Global Active Power")
dev.off()

#################################
play<-as.data.frame(sub)
play$nTime<-strptime(x=as.character(play$Time),format="%H:%M:%S")

filter(play,nDate>="2006-12-16",nDate<"2006-12-17")
