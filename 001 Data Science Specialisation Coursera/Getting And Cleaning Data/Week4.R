# quiz q1

fileURL<-"https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06hid.csv "
download.file(fileURL,destfile = './americancommunityservice.csv')
ams<-read.csv('americancommunityservice.csv')

s<-strsplit(names(ams),"wgtp")
s[123]

# quiz q2
gdp<-gsub(",","",gdp$X.3)
head(gdp)
gdp<-gsub(" ","",gdp)
gdp2<-gdp[-c(1:4)]
gdp2<-as.numeric(gdp2)
mean(gdp2,na.rm=T)

#quiz q3
#rename

gdp<-rename(gdp,gdprank=Gross.domestic.product.2012,countrynames=X.2,gdp=X.3)
gdp<-gdp[-c(1:4),]
grep("^United",gdp$countrynames)

#quiz q4
edu<-read.csv("edu.csv")

m<-merge(gdp,edu,by.x = "countrycode",by.y = "CountryCode",all.y = T)

