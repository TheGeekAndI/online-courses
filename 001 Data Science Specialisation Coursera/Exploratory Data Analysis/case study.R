# unzip data
unzip('C:/Users/daniele.parenti/Downloads/RD_501_88101_2012.zip')
unzip('C:/Users/daniele.parenti/Downloads/RD_501_88101_2008.zip')

# have a look at the file

# read in 2008 data
pm0<-read.table('C:\\Users\\daniele.parenti\\Dropbox\\R\\R Specialisation\\datasciencecoursera\\Exploratory Data Analysis\\RD_501_88101_2008-0.txt',comment.char = '#',sep='|',header=F,na.strings = '')

# read in the column headers
cnames<-readLines('RD_501_88101_2008-0.txt',1)

# split the string
cnames<-strsplit(cnames,split = '|',fixed=T)

# attach column names to data. The make.names function makes valid R names e.g. without spaces
names(pm0)<-make.names(cnames[[1]])

# pull out sample column
x0<-pm0$Sample.Value
summary(x0)

# check proportion of missing data
mean(is.na(x0))

# read in 2012 data
pm1<-read.table('RD_501_88101_2012-0.txt',sep = '|',header=F,comment.char = '#',na.strings = '')
names(pm1)<-make.names(cnames[[1]])

# pull out sample column
x1<-pm1$Sample.Value
summary(x1)

# check proportion of missing data
mean(is.na(x1))

# create boxplot
boxplot(log10(x0),log10(x1))

# filter out negative values
neg<-x1<0
sum(neg,na.rm=T)

# look at dates
dates<-pm1$Date

#convert to date
dates<-ymd(pm1$Date)
dates<-as.Date(as.character(pm1$Date),"%y%m%d")

#histogram of dates
hist(dates,breaks='month')

# find a monitor that exists in 2008 and 2012
# create lists of measurement sites
site0<-unique(subset(pm0,State.Code==36,c('County.Code','Site.ID')))
site1<-unique(subset(pm1,State.Code==36,c('County.Code','Site.ID')))

# create variable to compare two years
site0<-paste(site0[,1],site0[,2],sep='.')
site1<-paste(site1[,1],site1[,2],sep='.')

# find which match
both<-intersect(site0,site1)

# find which of the common monitors has the most observations
pm0$County.site<-with(pm0,paste(County.Code,Site.ID,sep='.'))
pm1$County.site<-with(pm1,paste(County.Code,Site.ID,sep='.'))

# number of obs for monitors
cnt0<-subset(pm0,State.Code==36 & County.site %in% both)
cnt1<-subset(pm1,State.Code==36 & County.site %in% both)

# split data frame by site & count number of rows
sapply(split(cnt0,cnt0$County.site),nrow)
sapply(split(cnt1,cnt1$County.site),nrow)

# choose site 1.5
pm1sub<-subset(pm1,State.Code==36 & County.Code==1 & Site.ID==5)
pm0sub<-subset(pm0,State.Code==36 & County.Code==1 & Site.ID==5)

# plot values over time
dates1<-as.Date(as.character(pm1sub$Date),"%Y%m%d")
x1sub<-pm1sub$Sample.Value
plot(dates1,x1sub)

dates0<-as.Date(as.character(pm0sub$Date),"%Y%m%d")
x0sub<-pm0sub$Sample.Value
plot(dates0,x0sub)

rng<-range(x0sub,x1sub,na.rm=T)
par(mfrow=c(1,2),mar=c(4,4,2,1))
plot(dates0,x0sub,pch=20,ylim=rng)
abline(h=median(x0sub,na.rm = T))
plot(dates1,x1sub,pch=20,ylim=rng)
abline(h=median(x1sub, na.rm=T))

# calc average plloution at state level
mn0<-with(pm0,tapply(Sample.Value,State.Code,mean,na.rm=T))
mn1<-with(pm1,tapply(Sample.Value,State.Code,mean,na.rm=T))

d0<-data.frame(state=names(mn0),mean=mn0)
d1<-data.frame(state=names(mn1),mean=mn1)

# merge together on state
mrg<-merge(d0,d1,by='state')

par(mfrow=c(1,1))
with(mrg,plot(rep(1999,53),mrg[,2],xlim=c(1998,2013)))
with(mrg,points(rep(2012,53),mrg[,3]))
segments(rep(1999,53),mrg[,2],rep(2012,53),mrg[,3])
