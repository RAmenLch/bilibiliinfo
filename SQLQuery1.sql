CREATE TABLE [dbo].[UserInfo](
	[UID] [nvarchar](15) NOT NULL,
	[Name] [nvarchar](50) NULL,
	[Sex] [nvarchar](2) NULL,
	[lvl] [smallint] NOT NULL,
	[VIPType] [nvarchar](10) NOT NULL,
	[fansNum] [int] NOT NULL,
	[geo] [nvarchar](10) NOT NULL,
 CONSTRAINT [PK_UserInfo] PRIMARY KEY(UID)
 )
GO
CREATE TABLE [dbo].[UserInfo2018](
	[UID] [nvarchar](15) NOT NULL,
	[Name] [nvarchar](50) NULL,
	[Sex] [nvarchar](2) NULL,
	[lvl] [smallint] NOT NULL,
	[VIPType] [nvarchar](10) NOT NULL,
	[fansNum] [int] NOT NULL,
	[geo] [nvarchar](10) NOT NULL,
 CONSTRAINT [PK_UserInfo2018] PRIMARY KEY(UID)
 )
GO