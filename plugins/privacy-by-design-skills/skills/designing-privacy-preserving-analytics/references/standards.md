# Privacy-Preserving Analytics Standards and References

## Academic Foundations

### Differential Privacy
- Dwork, C., McSherry, F., Nissim, K., & Smith, A. (2006). "Calibrating Noise to Sensitivity in Private Data Analysis." Theory of Cryptography Conference (TCC). Introduced the formal definition of (epsilon, delta)-differential privacy.

### k-Anonymity
- Sweeney, L. (2002). "k-Anonymity: A Model for Protecting Privacy." International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems, 10(5), 557-570. Established the k-anonymity model requiring each record be indistinguishable from at least k-1 others.

### l-Diversity
- Machanavajjhala, A., Kifer, D., Gehrke, J., & Venkitasubramaniam, M. (2007). "l-Diversity: Privacy Beyond k-Anonymity." ACM Transactions on Knowledge Discovery from Data, 1(1). Addressed attribute disclosure vulnerabilities in k-anonymity.

### t-Closeness
- Li, N., Li, T., & Venkatasubramanian, S. (2007). "t-Closeness: Privacy Beyond k-Anonymity and l-Diversity." IEEE International Conference on Data Engineering (ICDE). Introduced distributional privacy using Earth Mover's Distance.

## Regulatory Guidance

### GDPR Recital 26 — Anonymous Information
The principles of data protection should not apply to anonymous information, namely information which does not relate to an identified or identifiable natural person or to personal data rendered anonymous in such a manner that the data subject is not or no longer identifiable. This Regulation does not therefore concern the processing of such anonymous information, including for statistical or research purposes.

### Article 29 Working Party Opinion 05/2014 (WP216)
Evaluates anonymisation techniques against three criteria: singling out, linkability, and inference. Classifies techniques into randomization (noise addition, permutation, differential privacy) and generalization (k-anonymity, l-diversity, t-closeness). Concludes that no single technique is universally effective and recommends combining approaches.

### GDPR Article 89 — Statistical Processing Safeguards
Processing for statistical purposes shall be subject to appropriate safeguards for the rights and freedoms of the data subject. Those safeguards shall ensure that technical and organisational measures are in place in particular in order to ensure respect for the principle of data minimisation. Those measures may include pseudonymisation provided that those purposes can be fulfilled in that manner.

## Technical Standards

### NIST SP 800-188 — De-Identifying Government Datasets
Provides methodology for assessing re-identification risk and selecting de-identification techniques. Defines disclosure risk metrics and acceptable thresholds for statistical releases.

### ISO/IEC 20889:2018 — Privacy Enhancing Data De-identification
Classifies de-identification techniques and provides a framework for selecting appropriate methods based on data characteristics and privacy requirements.

## Tool Documentation

### Google Differential Privacy Library
Open-source library implementing differentially private algorithms. Supports bounded and unbounded DP for count, sum, mean, variance, and quantile computations. Includes partition selection for private set operations. Available at github.com/google/differential-privacy.

### OpenDP
Modular collection of statistical algorithms adhering to differential privacy. Built on a verified core in Rust with Python bindings. Supports composable transformations and measurements with automatic privacy accounting. Maintained by Harvard Institute for Quantitative Social Science and Microsoft. Available at github.com/opendp/opendp.

### IBM diffprivlib
Scikit-learn compatible library for machine learning with differential privacy. Implements DP versions of common ML algorithms: logistic regression, naive Bayes, k-means, PCA, and gradient descent. Available at github.com/IBM/differential-privacy-library.
