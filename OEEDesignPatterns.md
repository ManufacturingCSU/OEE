:warning: In progress

# OEE Solution Design Patterns

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
        - Asset grouping, Line level and Run level quality inputs
        - Update frequency (end of shift, end of day, ... ?)
        - NRT throughput, bandwidth, cost
        - Integration gateway, CDC, data pipelines
    - Parameters
        - Good units
        - Rejected units (Scrap)
        - Rework

### - Performance
    - Constraints
        - Ideal run rate, Cycle time for Process vs. Discrete
    - Parameters
        - Stoppages
        - Reduced speed reasons



