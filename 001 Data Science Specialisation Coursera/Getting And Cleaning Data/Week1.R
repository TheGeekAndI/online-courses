# Question 1

fileURL<-"https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06hid.csv"
download.file(fileURL,destfile = "./q1data.csv")
q1<-read.csv("q1data.csv")
table(q1$VAL)

# Question 3
library("xlsx")
fileURL<-"https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FDATA.gov_NGAP.xlsx"
download.file(fileURL,destfile = "./q2data.xlsx",mode = 'wb')
colIndex<-7:15
rowIndex<-18:23
dat<-read.xlsx("./q2data.xlsx",sheetIndex = 1, header=T,colIndex=colIndex,rowIndex=rowIndex)
sum(dat$Zip*dat$Ext,na.rm=T)

# Question 4
library(XML)
fileURL<-"http://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Frestaurants.xml"
doc<-xmlTreeParse(fileURL,useInternal=TRUE)
rootNode<-xmlRoot(doc)
zipCodes<-xpathSApply(rootNode,"//zipcode",xmlValue)
table(zipCodes)
sum(zipCodes=="21231")