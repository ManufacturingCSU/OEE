:warning: In progress

# OEE Calculations

## Sample Excel

- See this [Excel with basic calculation](files/oee-basic.xlsx) along with losses


## Basic OEE

- Shift Length
- Break Time
- Planned Production Time === (Shift Length - Break Time)
- ----------------------
- Downtime
- Runtime === ( Planned Production Time - Downtime)
- ----------------------
- Total Units
- Rejected Units
- Good Units === (Total Units - Rejected Units)
- ----------------------
- A (Run Time / Planned Production Time)	
- P (Total Units / Run Time) / Ideal Run Rate)
- Q (Good Units / Total Units)
- ----------------------
- OEE === (A * P * Q)
- ----------------------

## OEE Losses

- Cycle time === (Time to product 1 Unit)
- ----------------------
- Availability Losses === (Downtime / Cycle time) / (Total time / Cycle time)	
- ----------------------
- Quality Losses === Rejected Units / (Total time / Cycle time)	
- ----------------------
- Speed Losses === 100 - Availability losses - Quality losses - OEE	
- ----------------------