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

# create new variable that holds hour in text format
sub$t<-strftime(sub$Time,format="%H:%M%:%S")

# create new variable with date as character
sub$d<-as.character(sub$Date)

# combine date and time into one string
sub$s<-paste(sub$d,sub$t)

# convert string into datetime
sub$dt<-ymd_hms(sub$s)

# create grpahics device
png(filename="plot4.png")

# set paramteres for a 2x2 plot
par(mfrow=c(2,2),mar = c(4, 4, 2, 1), oma = c(0, 0, 2, 0))

#plot top left plot (same as plot 2)
plot(sub$dt,sub$Global_active_power,type="l",ylab="Global Active Power (kilowatts)",xlab="")

# plot top left graph
plot(sub$dt,sub$Voltage,type="l",ylab="Voltage",xlab="datetime")

# plot bottom left graph (same as plot 3)
with(sub,plot(dt,Sub_metering_1,type="l",ylab = "Energy sub metering",xlab=" "))
lines(sub$dt,sub$Sub_metering_2,type="l",col="red",xlab=" ")
lines(sub$dt,sub$Sub_metering_3,type="l",col="blue",xlab=" ")
legend("topright",legend=c("Sub_metering_1","Sub_metering_2","Sub_metering_3"),
       lty=c(1,1,1),col=c("black","red","blue"))

#plot bottom right plot
plot(sub$dt,sub$Global_reactive_power,type="l",xlab="datetime")

# close graphic device
dev.off()