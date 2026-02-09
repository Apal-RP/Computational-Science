# Computational-Science

An exploration of numerical precision and the computational impact of rounding vs. truncation when calculating mathematical constants. This project uses the Gaussian (Normal) Distribution PDF to determine at what point higher-precision $\pi$ stops being physically relevant and becomes purely theoretical.

To determine if there is a tangible difference in results when using $\pi$ at different decimal precisions (4, 20, 40, 60, and 100 places) and whether Rounding to the nearest digit is significantly more accurate than Truncation (chopping off the decimals).

Normal Distribution (Gaussian), to calculate the peak height of the "Bell Curve" (where $\mu=0$ and $\sigma=1$)

Formula: $$f(0) = \frac{1}{\sqrt{2\pi}}$$


Result:
<img width="1002" height="712" alt="image" src="https://github.com/user-attachments/assets/05e6fbd2-325b-49e0-90e1-16abb2bfd134" />
<img width="486" height="128" alt="image" src="https://github.com/user-attachments/assets/51a407e4-bacd-4055-8138-776c278b22ca" />

Conclusion:

Rounding vs. Truncation: Rounding is almost always more accurate than just "cutting off" the numbers (truncation).

The "Wall": After about 15–20 decimal places, the error becomes so small that it is literally smaller than an atom.

The 100-Digit Flex: Using 100 digits of $\pi$ is cool for computers to calculate, but in the real world (like building bridges or landing rockets), it makes zero physical difference.

While Rounding is mathematically superior to Truncation at lower precisions (like the 3.1415 vs 3.1416 baseline), the difference becomes physically irrelevant once you surpass 20 decimal places. Using 100 digits of $\pi$ is a "computational flex", impressive for hardware testing, but unnecessary for landing a rocket.
