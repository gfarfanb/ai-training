
# GPU Offload comparison

| Setup | CPU | GPU | RAM | VRAM | Storage |
| --- | --- | ---  | --- | --- | --- |
| Without GPU Offloading* | Handles all computations | | Stores model and data | | Storage (SSD/HDD): Temporarily holds model before loading |
| With Partial GPU Offloading | Handles fewer computations | Specific computations | Partially relieved | Stores model and data | |
| Increased GPU Offloading | Lower workload | Higher workload | Further relieved | Higher memory requirement | |
| Maximum GPU Offloading** | Minimal workload | Handles almost all computations | Significantly relieved | Heavily used | |

> \* Without GPU Offloading impacts:
> * High CPU usage
> * Heat generation
> * Performance degradation
> * High RAM usage / Swap memory if needed
> * I/O operations

> \** Maximum GPU Offloading impacts:
> * Performance: Enhanced
> * Power consumption: Increases
> * Heat generation: Increases
> * Efficiency: Better workload distribution
