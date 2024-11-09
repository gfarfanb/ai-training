
# What is Quantization?

Basically, Instead of storing and processing the numbers in a model with high precision (e.g., 32 bit), they are reduced to a lower precision (e.g., 8-bit or 4-bit). For example: A Number that is normally stored as a 32-bit floating point could be stored as an 8-bit or 4-bit integer.

Through quantization, even complex models can be run on less powerful hardware, making them more accessible and cost-effective.

**Advantages**
- Save Memory Space: Fewer bits means less memory is required.
- Faster Calculations: Smaller number formats can be processed more quickly, especially on specialized hardware.

## Q8 - 8-bit precision

The number in the model are reduced to 8-bit precision. This is a moderate reduction and offers a good compromise between memory space, computational performance, and model accuracy.

> It uses 8-bit precision, which represents a good compromise.

## Q4 - 4-bit precision

The number in the model are reduced to 4-bit precision. This saves even more memory space and computational power but can lead to a greater loss of accuracy.

> It uses 4-bit precision, which is even more efficient but at the cost of more accuracy.
