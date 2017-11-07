# Exploratory Data Analysis
setwd("C:/Users/daniele.parenti/Dropbox/R/R Specialisation/datasciencecoursera/Exploratory Data Analysis")
library(dplyr)
library(tidyr)
library(data.table)
library(readr)
library(lubridate)

# Quesiton:
# Which counties in the United States have the highest levels of ambient ozone pollution?

ozone<-read_csv("hourly_44201_2014.csv",col_types = "ccnccnnccccccncnnccccccc")
names(ozone)<-make.names(names(ozone))

dim(ozone)
str(ozone)
head(ozone[,c(6:7,10)])
tail(ozone[,c(6:7,10)])

table(ozone$Time.Local)

select(ozone,State.Name)%>%unique%>%nrow
unique(ozone$State.Name)
summary(ozone$Sample.Measurement)
quantile(ozone$Sample.Measurement,seq(0,1,0.1))

ranking<-tbl_df(ozone) %>% group_by(State.Name,County.Name) %>%
    summarize(ozonemean=mean(Sample.Measurement)) %>%
    as.data.frame %>% arrange(desc(ozonemean))

head(ranking,10)

filter(ozone,State.Name=="California" & County.Name == "Mariposa") %>% nrow

ozone<-mutate(ozone,Date.Local=ymd(Date.Local))

ozone<-tbl_df(ozone)

filter(ozone,State.Name=="California" & County.Name=="Mariposa") %>%
    mutate(month=factor(months(Date.Local),levels=month.name)) %>%
    group_by(month) %>%
    summarize(ozone=mean(Sample.Measurement))

filter(ozone,State.Name=="Oklahoma" & County.Name=="Caddo") %>%
    mutate(month=factor(months(Date.Local),levels=month.name)) %>%
    group_by(month) %>%
    summarize(ozone=mean(Sample.Measurement))

### Doing the actual course lectures

pollution<-read.csv("avgpm25.csv",colClasses = c("numeric","character","factor","character","character"))
summary(pollution$pm25)
boxplot(pollution$pm25)
abline(h=12)
hist(pollution$pm25,breaks=50)
rug(pollution$pm25)
abline(v=12)
abline(v=mean(pollution$pm25),col="red")

attach(pollution)
boxplot(pm25~region)
detach(pollution)

with(pollution,plot(latitude,pm25,col=region))
abline(h=12)

### base plotting system

