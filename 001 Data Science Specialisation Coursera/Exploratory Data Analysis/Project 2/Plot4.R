library(dplyr)
library(ggplot2)

# read in the data
NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

# convert to tbl class
data<-tbl_df(NEI)
scc<-tbl_df(SCC)

# filter rows where Short.Name includes 'Coal' and include only the name and code columns
f<-scc%>%filter(grepl('coal',scc$Short.Name,ignore.case = T))%>%select(SCC,Short.Name)

# only keep the rows from data with a matching SCC code in the filtered list
d<-filter(data,SCC %in% f$SCC)

# gruop d by year and find totals
ds<-d %>% group_by(year) %>% summarise(total_ems=sum(Emissions))

# plot in base
png('Total US coal based emissions in tons.png')
plot(ds$year,ds$total_ems,type = 'b',main="Total US coal based emissions in tons")
dev.off()

### alternative route is to attach the SCC name to data and then use grepl
### this approach takes A LOT longer because of the 6.5m rows to be matched
### but i get to use more dplyr functions which is fun

# select only name and code columns from scc and sort by code number
scccodes<-select(scc,SCC,Short.Name)%>%arrange(SCC)

#select only emissions, year and scc code columns and arrange by scc cdde
d<-select(data,SCC,Emissions,year)%>%arrange(SCC)

# merge SCC descriptions to data tbl
d<-merge(data,scccodes,by='SCC')

# filter only coal rows
dss<-filter(d,grepl('coal',d$Short.Name,ignore.case=T))

# group by year and calculate total emissions by year
dss<-group_by(dss,year)%>%summarise(total_ems=sum(Emissions))

# plot in base
png('Total US coal based emissions in tons.png')
plot(ds$year,ds$total_ems,type = 'b',main="Total US coal based emissions in tons")
dev.off()
