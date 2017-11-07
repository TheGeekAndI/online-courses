set.seed(13435)
X <- data.frame("var1"=sample(1:5),"var2"=sample(6:10),"var3"=sample(11:15))
X <- X[sample(1:5),]; X$var2[c(1,3)] = NA
X

library(plyr)
arrange(X,var1)
X$var4<-rnorm(5)

# quiz q1

fileURL<-"https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06hid.csv"
download.file(fileURL,destfile = './w3q1data.csv')
df<-read.csv('w3q1data.csv')


al<-ifelse(df$ACR==3&df$AGS==6,TRUE,FALSE)
which(al)

fileURL<-"https://d396qusza40orc.cloudfront.net/getdata%2Fjeff.jpg"
jp<-readJPEG(fileURL,native=T)

GDPURL<-"https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FGDP.csv"
download.file(GDPURL,destfile="./gdp.csv")
gdp<-read.csv("gdp.csv")
eduURL<-"https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FEDSTATS_Country.csv"
download.file(eduURL,destfile = "./edu.csv")
edu<-read.csv("edu.csv")
names(gdp)
names(edu)
head(gdp$X)
head(edu$CountryCode)
mergedData<-merge(edu,gdp,by.x = "CountryCode",by.y = "X")
mergedData<-rename(mergedData,gdp=X.3)
mergedData<-mutate(mergedData,gdpN=as.numeric(gdp))
md<-select(mergedData,Long.Name,gdp)
md<-mutate(md,as.numeric(gdp))
md<-arrange(md,desc(as.numeric(gdp)))
md[13,]
