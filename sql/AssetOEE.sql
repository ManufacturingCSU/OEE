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


