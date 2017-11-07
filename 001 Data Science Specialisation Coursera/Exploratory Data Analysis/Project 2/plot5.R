library(dplyr)

# read in the data
NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

# convert to tbl class
data<-tbl_df(NEI)
scc<-tbl_df(SCC)

# subset data to only contain Baltimore data and the relevant columns
data<-filter(data,fips==24510)%>%select(SCC,Emissions,year)

# find vehicle sources in scc data
vhcl<-filter(scc,grepl('vehicle',scc$SCC.Level.Two,ignore.case = T))%>%
        select(SCC)

# filter data in baltimore with matching SCC codes
data<-filter(data,SCC %in% vhcl$SCC)

# group by year and summarise total emissions
data<-group_by(data,year)%>%summarise(total_ems=sum(Emissions))

#plot in base
png('vehicle emissions in BC.png')
plot(data$year,data$total_ems,type='b',
     main='total tons of vehicle emissions in Baltimore City')
dev.off()