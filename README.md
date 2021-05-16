# Overall Equipment Effectiveness (OEE)

Overall Equipment Effectiveness is a measure of how well a manufacturing operation is utilized (facilities, time and material) compared to its full potential, during the periods when it is scheduled to run. It identifies the percentage of manufacturing time that is truly productive. An OEE of 100% means that only good parts are produced (100% quality), at the maximum speed (100% performance), and without interruption (100% availability).

Measuring OEE is a manufacturing best practice. By measuring OEE and the underlying losses, important insights can be gained on how to systematically improve the manufacturing process. OEE is an effective metric for identifying losses, bench-marking progress, and improving the productivity of manufacturing equipment (i.e., eliminating waste)

Total effective equipment performance (TEEP) is a closely related measure which quantifies OEE against calendar hours rather than only against scheduled operating hours. A TEEP of 100% means that the operations have run with an OEE of 100% 24 hours a day and 365 days a year (100% loading).

For more details and history of OEE, read [this](https://en.wikipedia.org/wiki/Overall_equipment_effectiveness)

## Calculating OEE

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

## Calculating OEE Losses

- Availability Losses === (Downtime / Cycle time) / (Total time / Cycle time)	
- ----------------------
- Quality Losses === Rejected Units / (Total time / Cycle time)	
- ----------------------
- Speed Losses === 100 - Availability losses - Quality losses - OEE	
- ----------------------

## Design Patterns

### - Availability
    - Connectivity
        - PLC --> Edge --> Cloud
    - Constraints
        - NRT throughput, bandwidth, cost
    - Parameters
        - Machine Status
        - Planned Downtime
        - Waiting/Changeover
        - Line restraint

### - Quality
    - Connectivity
        - MES --> Edge --> Cloud     (near real time)
        - MES --> Integration Gateway --> Cloud  (batch)
    - Constraints
        - NRT throughput, bandwidth, cost
        - Integration gateway, CDC, data pipelines
    - Parameters
        - Good parts
        - Bad parts (Scrap)
        - Rework

### - Performance
    - Connectivity
    - Constraints
    - Parameters
        - Stoppages
        - Reduced speed reasons

## Getting Started



