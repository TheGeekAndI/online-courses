# Compare emissions from motor vehicle sources in Baltimore City (fips==24510) with
# emissions from
# motor vehicle sources in Los Angeles County, California (fips == 06037). Which city
# has seen greater changes over time in motor vehicle emissions?

library(dplyr)
library(ggplot2)

# read in the data
NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

# convert to tbl_df
data<-tbl_df(NEI)
codes<-tbl_df(SCC)

# subset only BC and LA data
data<-filter(data,xor(fips=='24510',fips=='06037'))%>%select(SCC,fips,year,Emissions)

# filter vehicle emissions scc codes
vhcl<-filter(codes,grepl('vehicle',codes$SCC.Level.Two,ignore.case = T))%>%select(SCC)

# filter only vehicle emission rows from the data
data<-filter(data,data$SCC %in% vhcl$SCC)

# group by city then by year
data<-group_by(data,fips,year)

# summarise by year then by city
data<-summarise(data,total_ems=sum(Emissions))

# split by fips
s<-split(data,data$fips)
la<-tbl_df(data.frame(s[1]))
bc<-tbl_df(data.frame(s[2]))

# rename columns
la<-rename(la,fips=X06037.fips, year=X06037.year, total_ems=X06037.total_ems)
bc<-rename(bc,fips=X24510.fips, year=X24510.year, total_ems=X24510.total_ems)

# centre to base year
la<-mutate(la,centred=total_ems-total_ems[1])
bc<-mutate(bc,centred=total_ems-total_ems[1])


# join together
d<-rbind(la,bc)

# create city column to name fips
d$city[data$fips=='24510']<-'Baltimore'
d$city[data$fips=='06037']<-'Los Angeles'

# plot with ggplot2 each city a different colour
png('plot6.png')
ggplot(d,aes(x=as.factor(year),fill=city))+
    geom_bar(data=subset(d,d$fips=='06037'),aes(y=centred),stat='identity')+
    geom_bar(data=subset(d,d$fips=='24510'),aes(y=centred),stat='identity')+
    ggtitle("Change in total tons vehicle emissions from base year")+
    xlab("Year")+ylab('Change in emissions from base year - 1999 (tons)')
dev.off()
