# Privacy-Preserving Data Sharing — Workflows

## Workflow 1: Synthetic Data Generation

1. **Data Profiling**: Analyze source data distributions, correlations, constraints
2. **Metadata Creation**: Generate SDV metadata for the dataset
3. **Model Selection**: Choose synthesizer (GaussianCopula, CTGAN, TVAE)
4. **Training**: Train the model on source data
5. **Generation**: Generate synthetic dataset of desired size
6. **Quality Assessment**: Run SDV quality metrics and compare distributions
7. **Privacy Assessment**: Measure re-identification risk and membership inference
8. **Release Approval**: Privacy team approval if risk thresholds met

## Workflow 2: Data Clean Room Setup

1. **Partner Agreement**: Establish data sharing agreement with privacy terms
2. **Schema Alignment**: Map and normalize partner data schemas
3. **Policy Definition**: Configure query policies (allowed operations, min group size)
4. **Data Ingestion**: Encrypted upload of data from both parties
5. **Query Approval**: Pre-approve query templates
6. **Execution**: Run approved queries with output validation
7. **Output Review**: Verify output meets disclosure controls
8. **Audit**: Log all queries and outputs for compliance

## Workflow 3: Utility Measurement

1. **Define Use Case**: What analytical tasks the shared data must support
2. **Baseline Metrics**: Run analyses on original data for ground truth
3. **Run on Shared Data**: Execute same analyses on privacy-preserving version
4. **Compare Results**: Calculate statistical fidelity metrics
5. **Threshold Check**: Verify utility meets minimum acceptable level
6. **Iterate**: Adjust privacy parameters if utility is insufficient
