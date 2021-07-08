SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[AssetOEE](
	[AssetId] [nvarchar](100) NOT NULL,
	[ShiftTitle] [nvarchar](50) NULL,
	[ShiftStartTime] [datetime2](7) NOT NULL,
	[ShiftEndTime] [datetime2](7) NOT NULL,
	[IdealRunRate] [float] NOT NULL,
	[BreakInMinutes] [float] NOT NULL,
	[TotalUnits] [float] NOT NULL,
	[GoodUnits] [float] NOT NULL,
	[BadUnits] [float] NOT NULL,
	[PlannedProductionTime] [float] NOT NULL,
	[DownTime] [float] NOT NULL,
	[RunTime] [float] NOT NULL,
	[Availability] [float] NOT NULL,
	[Performance] [float] NOT NULL,
	[Quality] [float] NOT NULL,
	[OEE] [float] NOT NULL,
	[TimeStamp] [datetime2](7) NOT NULL
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[AssetOEE] ADD  DEFAULT (getdate()) FOR [TimeStamp]
GO

CREATE TABLE [dbo].[ShiftConfiguration](
	[Plant] [nvarchar](100) NOT NULL,
	[Product] [nvarchar](100) NOT NULL,
	[ShiftTitle] [nvarchar](50) NOT NULL,
	[ShiftStartTime] [time](7) NOT NULL,
	[ShiftEndTime] [time](7) NOT NULL,
	[BreakInMinutes] [int] NOT NULL,
	[IdealProductionUnitsPerMinute] [int] NOT NULL,
	[UtcOffsetInHours] [nvarchar](10) NOT NULL
) ON [PRIMARY]
GO
INSERT [dbo].[ShiftConfiguration] ([Plant], [Product], [ShiftTitle], [ShiftStartTime], [ShiftEndTime], [BreakInMinutes], [IdealProductionUnitsPerMinute], [UtcOffsetInHours]) VALUES (N'Plant-1', N'Product-1', N'Morning', CAST(N'00:00:00' AS Time), CAST(N'08:00:00' AS Time), 10, 1, N'-7h')
GO
INSERT [dbo].[ShiftConfiguration] ([Plant], [Product], [ShiftTitle], [ShiftStartTime], [ShiftEndTime], [BreakInMinutes], [IdealProductionUnitsPerMinute], [UtcOffsetInHours]) VALUES (N'Plant-1', N'Product-1', N'Evening', CAST(N'08:00:00' AS Time), CAST(N'16:00:00' AS Time), 10, 1, N'-7h')
GO



